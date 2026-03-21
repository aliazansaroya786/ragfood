"use server";

import { Index } from "@upstash/vector";
import Groq from "groq-sdk";
import type { FoodSource, RAGResponse } from "@/lib/types";

// Initialize Upstash Vector client
const index = new Index({
  url: process.env.UPSTASH_VECTOR_REST_URL!,
  token: process.env.UPSTASH_VECTOR_REST_TOKEN!,
});

// Initialize Groq client
const groq = new Groq({
  apiKey: process.env.GROQ_API_KEY,
});

export async function ragQuery(question: string): Promise<RAGResponse> {
  if (!question.trim()) {
    throw new Error("Please enter a question");
  }

  // Step 1: Query Upstash Vector (embedding handled automatically with data parameter)
  const results = await index.query({
    data: question,
    topK: 3,
    includeMetadata: true,
  });

  // Step 2: Extract documents and build sources
  const sources: FoodSource[] = results.map((result) => ({
    id: result.id as string,
    text: (result.metadata?.text as string) || "",
    region: (result.metadata?.region as string) || "",
    type: (result.metadata?.type as string) || "",
    score: Math.round((result.score || 0) * 10000) / 10000,
  }));

  // Step 3: Build context from top documents
  const context = sources.map((s) => s.text).join("\n");

  // Step 4: Generate answer with Groq (same model as Python code)
  const prompt = `Use the following context to answer the question accurately.

Context:
${context}

Question: ${question}
Answer:`;

  const completion = await groq.chat.completions.create({
    model: "llama-3.3-70b-versatile",
    messages: [
      {
        role: "user",
        content: prompt,
      },
    ],
    max_tokens: 500,
  });

  const answer = completion.choices[0]?.message?.content?.trim() || "";

  return {
    sources,
    answer,
  };
}
