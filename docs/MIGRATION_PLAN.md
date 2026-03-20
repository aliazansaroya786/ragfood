# 🔄 Migration Plan: Local RAG → Cloud RAG

**Author:** Ali Azan  
**University:** Victoria University  
**Subject:** AI Data Analyst Industry Project — Week 3  
**AI Tool Used:** Claude (Anthropic) for migration planning and code generation

---

## 📋 Overview

This document describes the migration of the Week 2 local RAG Food System to a production-ready cloud infrastructure using Upstash Vector Database and Groq Cloud API.

---

## 🏗️ Architecture Changes

### Week 2 — Local Architecture
```
foods.json
    ↓
Ollama (mxbai-embed-large) → Generate Embeddings locally
    ↓
ChromaDB (local folder)    → Store vectors on disk
    ↓
Ollama (llama3.2)          → Generate answers locally
    ↓
Terminal output
```

### Week 3 — Cloud Architecture
```
foods.json
    ↓
Upstash Vector             → Handles embeddings automatically (bge-large-en-v1.5)
    ↓
Upstash Vector DB (cloud)  → Stores vectors in cloud (AWS us-east-1)
    ↓
Groq Cloud API (llama3-8b) → Generates answers in cloud (super fast!)
    ↓
Terminal output
```

---

## 🔄 Component Migration Table

| Component | Week 2 (Local) | Week 3 (Cloud) | Reason |
|-----------|---------------|----------------|--------|
| **Embedding** | Ollama mxbai-embed-large | Upstash built-in bge-large-en-v1.5 | No local GPU needed |
| **Vector DB** | ChromaDB (local folder) | Upstash Vector (AWS cloud) | Persistent, scalable |
| **LLM** | Ollama llama3.2 | Groq llama3-8b-8192 | 10x faster responses |
| **Storage** | Local disk | Cloud (1GB free) | Accessible anywhere |
| **Setup** | Install Ollama + models | API keys only | Much simpler |

---

## 📊 Embedding Strategy Changes

### Before (Week 2):
- Manually called Ollama API to generate embeddings
- Had to manage embedding dimensions ourselves
- Required local GPU/CPU for embedding generation
- Slow: ~2-5 seconds per embedding

### After (Week 3):
- Upstash automatically generates embeddings when we upsert text
- No manual embedding code needed
- Runs on Upstash cloud servers
- Fast: embeddings generated server-side instantly

---

## ⚡ LLM Changes

### Before (Week 2) — Ollama llama3.2:
```
Response time: 15-60 seconds
Runs on: Local laptop CPU
Internet needed: No
Cost: Free
Quality: Good
```

### After (Week 3) — Groq llama3-8b-8192:
```
Response time: 1-3 seconds
Runs on: Groq cloud servers
Internet needed: Yes
Cost: Free tier available
Quality: Excellent (same model, faster hardware)
```

---

## 🔧 Code Changes Summary

### Removed:
- `requests` library calls to Ollama
- Manual embedding generation function
- ChromaDB client setup
- Local model management

### Added:
- `upstash-vector` SDK
- `groq` SDK
- `python-dotenv` for environment variables
- `.env` file for secure credential storage

### Simplified:
- Embedding: 15 lines of code → 1 line (Upstash handles it)
- LLM call: 10 lines → 5 lines (Groq SDK)
- Setup: Install Ollama + pull 2 models → Just API keys

---

## 🌐 Environment Variables Required

```dotenv
UPSTASH_VECTOR_REST_URL=     # Upstash Vector endpoint URL
UPSTASH_VECTOR_REST_TOKEN=   # Upstash Vector auth token
GROQ_API_KEY=                # Groq Cloud API key
```

---

## ✅ Benefits of Migration

1. **Speed** — Groq responses in 1-3 seconds vs 15-60 seconds locally
2. **No GPU needed** — Works on any laptop, no powerful hardware required
3. **Persistent storage** — Data stays in cloud, no local chroma_db folder
4. **Scalable** — Can handle thousands of food items easily
5. **Accessible** — Works from any computer with internet
6. **Professional** — Production-ready cloud infrastructure

---

## ⚠️ Trade-offs

1. **Internet required** — Cannot run offline like local version
2. **API limits** — Free tier has usage limits
3. **Privacy** — Data sent to cloud servers
4. **Dependency** — Relies on third-party services

---

## 📈 Performance Comparison

| Metric | Local (Week 2) | Cloud (Week 3) |
|--------|---------------|----------------|
| Response time | 15-60 seconds | 1-3 seconds |
| Setup time | 30+ minutes | 10 minutes |
| Storage | Local disk | Cloud (free 1GB) |
| Cost | Free | Free tier |
| Portability | One machine | Any machine |
| Internet needed | No | Yes |
