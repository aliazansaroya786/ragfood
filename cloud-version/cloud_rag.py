import json
import os
from dotenv import load_dotenv
from upstash_vector import Index
from groq import Groq

# Load environment variables
from pathlib import Path
load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")

# Constants
JSON_FILE = "data/foods.json"

# Setup Upstash Vector
index = Index(
    url=os.environ.get("UPSTASH_VECTOR_REST_URL"),
    token=os.environ.get("UPSTASH_VECTOR_REST_TOKEN")
)

# Setup Groq
groq_client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

# Load food data
with open(JSON_FILE, "r", encoding="utf-8") as f:
    food_data = json.load(f)

# Check existing items
print("🔍 Checking existing records in Upstash Vector...")
info = index.info()
existing_count = info.vector_count
print(f"📊 Found {existing_count} existing records")

# Add only new items
if existing_count == 0:
    print(f"\n🆕 Adding {len(food_data)} documents to Upstash Vector...")
    
    batch = []
    for item in food_data:
        # Enhance text with region/type
        enriched_text = item["text"]
        if "region" in item:
            enriched_text += f" This food is popular in {item['region']}."
        if "type" in item:
            enriched_text += f" It is a type of {item['type']}."

        batch.append({
            "id": str(item["id"]),
            "data": enriched_text,  # Upstash handles embedding automatically!
            "metadata": {
                "text": item["text"],
                "region": item.get("region", ""),
                "type": item.get("type", "")
            }
        })

    # Upsert in batches of 10
    batch_size = 10
    for i in range(0, len(batch), batch_size):
        chunk = batch[i:i+batch_size]
        index.upsert(vectors=chunk)
        print(f"  ✅ Uploaded {min(i+batch_size, len(batch))}/{len(batch)} items")

    print(f"\n✅ All {len(food_data)} documents uploaded to Upstash Vector!")
else:
    print(f"✅ Database already has {existing_count} records. Skipping upload.")


# RAG query function
def rag_query(question):
    # Step 1: Query Upstash Vector (embedding handled automatically!)
    print("\n🧠 Retrieving relevant information...\n")
    
    results = index.query(
        data=question,       # Upstash embeds this automatically
        top_k=3,
        include_metadata=True
    )

    # Step 2: Extract documents
    top_docs = []
    for i, result in enumerate(results):
        doc_text = result.metadata.get("text", "") if result.metadata else ""
        doc_id = result.id
        score = round(result.score, 4)
        top_docs.append(doc_text)
        print(f"🔹 Source {i+1} (ID: {doc_id}, Score: {score}):")
        print(f"    \"{doc_text}\"\n")

    print("📚 These are the most relevant pieces of information.\n")

    # Step 3: Build prompt
    context = "\n".join(top_docs)
    prompt = f"""Use the following context to answer the question accurately.

Context:
{context}

Question: {question}
Answer:"""

    # Step 4: Generate answer with Groq (super fast!)
    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=500
    )

    return response.choices[0].message.content.strip()


# Interactive loop
print("\n☁️  Cloud RAG is ready! Ask a question (type 'exit' to quit):\n")
while True:
    question = input("You: ")
    if question.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break
    answer = rag_query(question)
    print("🤖:", answer)