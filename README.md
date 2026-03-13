# 🍽️ RAG Food System — Enhanced Edition

> An AI-powered food knowledge base using Retrieval-Augmented Generation (RAG), local LLMs via Ollama, and ChromaDB vector search.

---

## 👤 About This Fork

This is a personalized and enhanced fork of the original [RAG Food repository](https://github.com/gocallum/ragfood).  
**Enhanced by:** Ali Azan  
**University:** Victoria University  
**Subject:** AI Data Analyst Industry Project — Week 2 Assessment  

---

## 🆕 15 New Food Items Added

### 🇵🇰 5 Pakistani Cultural Foods
| ID | Food | Description |
|----|------|-------------|
| 76 | **Halwa Puri** | Traditional Pakistani breakfast with fried puri, sweet semolina halwa, and spiced chickpeas |
| 77 | **Sajji** | Slow-roasted whole lamb or chicken from Balochistan, cooked over open wood fire |
| 78 | **Chapli Kebab** | Peshawari minced meat patties with pomegranate seeds and spices, shallow fried |
| 79 | **Dum Pukht Biryani** | Royal Mughal-style biryani slow-cooked in a sealed pot with saffron and whole spices |
| 80 | **Sheer Khurma** | Creamy Eid dessert made from vermicelli, milk, dates, and dried fruits |

### 🥗 5 Healthy Foods with Nutritional Details
| ID | Food | Key Benefit |
|----|------|-------------|
| 81 | **Salmon** | 25g protein per 100g, rich in omega-3 fatty acids for heart and brain health |
| 82 | **Quinoa** | Complete protein with all 9 essential amino acids, gluten-free ancient grain |
| 83 | **Avocado** | Heart-healthy monounsaturated fats, high potassium, vegan and paleo-friendly |
| 84 | **Greek Yogurt** | Up to 20g protein per cup, rich in probiotics for gut health |
| 85 | **Lentil Soup** | 18g protein and 16g fiber per cup, vegan, gluten-free, diabetic-friendly |

### 🌍 5 Popular International Dishes
| ID | Food | Origin |
|----|------|--------|
| 86 | **Margherita Pizza** | Naples, Italy — UNESCO protected authentic pizza |
| 87 | **Tacos al Pastor** | Mexico City — Lebanese-Mexican fusion street food |
| 88 | **Croissant** | France — Laminated pastry with hundreds of buttery layers |
| 89 | **Jollof Rice** | West Africa — Smoky one-pot rice dish cooked in tomato base |
| 90 | **Paella** | Valencia, Spain — Saffron rice with crispy socarrat bottom layer |

---

## 🛠️ Installation & Setup

### Prerequisites
Make sure you have these installed:
- Python 3.9+
- [Ollama](https://ollama.com) — for running local AI models
- Git

### Step 1: Clone Your Forked Repository
```bash
git clone https://github.com/aliazansaroya786/ragfood.git
cd ragfood
```

### Step 2: Create Virtual Environment
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

### Step 3: Install Python Dependencies
```bash
pip install chromadb requests
```

### Step 4: Download AI Models via Ollama
```bash
# Start Ollama (if not already running)
ollama serve

# In a new terminal, pull required models
ollama pull mxbai-embed-large
ollama pull llama3.2
```

### Step 5: Run the Application
```bash
python rag_run.py
```

---

## 💬 Sample Queries & Expected Responses

### Query 1: Pakistani Cuisine
```
You: What is Chapli Kebab?
🤖: Chapli Kebab is a signature Pakistani minced meat patty from Peshawar,
    made with beef or mutton, pomegranate seeds, and spices, shallow fried
    in beef tallow. Served with naan and coriander chutney.
```

### Query 2: Healthy Food
```
You: Which foods are high in protein?
🤖: Several foods in our database are high in protein:
    - Salmon provides 25g per 100g serving
    - Greek Yogurt offers up to 20g per cup
    - Lentil Soup contains 18g per cup
    - Quinoa is a complete protein source
```

### Query 3: Vegan Options
```
You: What vegan foods are available?
🤖: Vegan options include Quinoa, Avocado, Lentil Soup,
    Jollof Rice, Tabbouleh, and Hummus among others.
```

### Query 4: Cultural Cuisine
```
You: Tell me about Pakistani breakfast foods
🤖: Pakistani breakfast culture is rich and hearty.
    Halwa Puri is one of the most beloved breakfast dishes,
    especially in Lahore, featuring fried puri with sweet halwa
    and spiced chickpeas.
```

### Query 5: Cooking Methods
```
You: What foods can be grilled?
🤖: Several foods in the database can be grilled including
    Sajji (whole lamb/chicken), Chapli Kebab, Salmon,
    Tacos al Pastor, and Paella traditionally cooked over fire.
```

---

## 🖼️ Screenshots

Screenshots of successful RAG system operation are available in the `screenshots/` folder of this repository, showing all 10 test queries and their responses.

---

## 🧠 Personal Reflection on RAG Learning Experience

Building this RAG Food System has been one of the most eye-opening experiences in my journey as an AI builder. Before this project, I had a general understanding of artificial intelligence as something abstract and distant, but working hands-on with this system made everything concrete and real.

The most fascinating concept I learned was the idea of embeddings. Before this project, I had no idea that text could be converted into hundreds of numbers that capture the actual meaning and context of words. The fact that "spicy Pakistani food" and "Chapli Kebab" would be numerically close in a vector space, while "French Croissant" would be mathematically far away, genuinely amazed me. This is fundamentally different from how traditional databases work, and it opened my mind to why AI search feels so much more natural than keyword-based search.

ChromaDB was another revelation. I expected a database to require complex setup like MySQL or SQL Server, but ChromaDB simply installed with pip and created a folder on my computer. Understanding that it was storing vector embeddings — essentially a mathematical map of meaning — made me appreciate how much engineering goes into making complex things simple for developers.

Working with Ollama and running LLaMA 3.2 entirely on my own laptop was also surprising. I always assumed large language models required massive cloud servers, but having a capable AI model running locally felt empowering. It also taught me about the difference between using a pre-trained model versus training one from scratch, which are completely different activities requiring completely different resources.

The RAG architecture itself — Retrieve, then Generate — is an elegant solution to a real problem: how do you make an AI answer questions about specific data it was never trained on? By first finding relevant context through vector similarity search, then feeding that context to the language model, the system can answer highly specific questions accurately. This pattern is used in real production AI applications at major companies, and understanding it at this level gives me a strong foundation for building more sophisticated AI systems in the future.

---

## 📁 Project Structure

```
ragfood/
├── rag_run.py          # Main RAG application
├── foods.json          # Enhanced food database (90 items)
├── chroma_db/          # Vector database (auto-generated)
├── screenshots/        # Testing screenshots
└── README.md           # This file
```

---

## 🔗 Original Repository

[https://github.com/gocallum/ragfood](https://github.com/gocallum/ragfood)