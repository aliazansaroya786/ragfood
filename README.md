# 🍽️ RAG Food System — Cloud Migration Edition

> An AI-powered food knowledge base using Retrieval-Augmented Generation (RAG), migrated from local infrastructure to production-ready cloud services.

---

## 👤 About This Project

**Author:** Ali Azan  
**University:** Victoria University  
**Subject:** AI Data Analyst Industry Project  
**Week 2:** Local RAG (ChromaDB + Ollama)  
**Week 3:** Cloud RAG (Upstash Vector + Groq)

---

## ☁️ Cloud Migration Overview

```
WEEK 2 (Local)                    WEEK 3 (Cloud)
──────────────                    ──────────────
ChromaDB (local folder)    →      Upstash Vector (AWS cloud)
Ollama mxbai-embed-large   →      Upstash built-in embeddings
Ollama llama3.2 (local)    →      Groq llama-3.3-70b (cloud)
15-60 second responses     →      1-3 second responses
One machine only           →      Works from anywhere
```

---

## 📁 Repository Structure

```
ragfood/
├── local-version/          # Week 2 - ChromaDB + Ollama
│   └── rag_run.py
├── cloud-version/          # Week 3 - Upstash + Groq
│   └── cloud_rag.py
├── data/
│   └── foods.json          # Enhanced database (110 items)
├── docs/
│   ├── MIGRATION_PLAN.md
│   └── PERFORMANCE_COMPARISON.md
├── screenshots/
│   ├── local/              # Week 2 screenshots
│   └── cloud/              # Week 3 screenshots
├── .env                    # Credentials (not committed)
└── README.md
```

---

## 🛠️ Setup Instructions

### Local Version (Week 2)
```bash
# Install dependencies
pip install chromadb requests

# Pull Ollama models
ollama pull mxbai-embed-large
ollama pull llama3.2

# Run
python local-version/rag_run.py
```

### Cloud Version (Week 3)
```bash
# Install dependencies
pip install upstash-vector groq python-dotenv

# Create .env file
UPSTASH_VECTOR_REST_URL=your_url
UPSTASH_VECTOR_REST_TOKEN=your_token
GROQ_API_KEY=your_key

# Run
python cloud-version/cloud_rag.py
```

---

## 🔑 Environment Variables

| Variable | Description |
|----------|-------------|
| `UPSTASH_VECTOR_REST_URL` | Upstash Vector database endpoint |
| `UPSTASH_VECTOR_REST_TOKEN` | Upstash authentication token |
| `GROQ_API_KEY` | Groq Cloud API key |

---

## ⚡ Local vs Cloud Comparison

| Feature | Local (Week 2) | Cloud (Week 3) |
|---------|---------------|----------------|
| Vector DB | ChromaDB | Upstash Vector |
| Embeddings | Ollama mxbai | Upstash bge-large |
| LLM | llama3.2 (3B) | llama-3.3-70b |
| Response Time | 15-60 seconds | 1-3 seconds |
| Internet | Not required | Required |
| Storage | Local disk | Cloud (free 1GB) |
| Cost | Free | Free tier |
| Portability | One machine | Anywhere |

---

## 🍽️ Food Database (110 Items)

### Original 75 Items
Diverse foods from Asia, Pacific, Middle East, and more

### Week 2 Additions (15 items)
- 🇵🇰 5 Pakistani cultural foods (Halwa Puri, Sajji, Chapli Kebab, Dum Pukht Biryani, Sheer Khurma)
- 🥗 5 healthy foods (Salmon, Quinoa, Avocado, Greek Yogurt, Lentil Soup)
- 🌍 5 international dishes (Margherita Pizza, Tacos al Pastor, Croissant, Jollof Rice, Paella)

### Week 3 Additions (20 items)
- 🌏 8 world cuisines (Thai, Mediterranean, Egyptian, Moroccan, Ethiopian, Peruvian, Polish, Russian)
- 🥦 6 health-conscious options (Broccoli, Sweet Potato, Chia Seeds, Edamame, Kale, Greek Salad)
- 🍲 6 comfort foods (Mac and Cheese, Ramen, Poutine, Pierogi, Beef Stroganoff, Butter Mochi)

---

## 💬 Advanced Query Examples

```
You: What healthy Mediterranean options are available?
You: What spicy vegetarian Asian dishes are there?
You: Which foods are high in protein and low in carbs?
You: Tell me about traditional comfort foods
You: What foods can be grilled?
You: What is Chapli Kebab?
You: Tell me about Pakistani breakfast foods
```

---

## 🔧 Troubleshooting

| Error | Solution |
|-------|----------|
| `GROQ_API_KEY not set` | Set env variables in terminal: `$env:GROQ_API_KEY="your_key"` |
| `Could not resolve host` | Check internet connection |
| `Model decommissioned` | Change model to `llama-3.3-70b-versatile` in cloud_rag.py |
| `FileNotFoundError foods.json` | Change JSON_FILE path to `data/foods.json` |

---

## 🔗 Links

- **Original Repository:** https://github.com/gocallum/ragfood
- **Upstash Vector:** https://upstash.com
- **Groq Cloud:** https://console.groq.com
- **Migration Plan:** docs/MIGRATION_PLAN.md
- **Performance Report:** docs/PERFORMANCE_COMPARISON.md