# 🌟 LangGraph AI Agent  

This project is a **FastAPI-based AI chatbot** that leverages **LangChain, LangGraph, and Groq's Llama-3.3-70B** to provide intelligent, real-time responses. It integrates a **retrieval-augmented generation (RAG) pipeline** with the **Tavily search tool** for enhanced information retrieval.

---

## 🚀 Features  
- ⚡ **FastAPI backend** for easy integration  
- 🤖 **Llama-3.3-70B (Groq)** for natural language processing  
- 🌍 **Tavily search API** for retrieving up-to-date web results  
- 🧠 **LangGraph-powered AI agent** with memory support  
- 🎭 **Customizable behavior prompts** (e.g., "act like Harry Potter")  

---

## 🔧 Installation  

### **1. Clone the repository**  
```bash
git clone https://github.com/yourusername/langgraph-ai-agent.git
cd langgraph-ai-agent
```

### **2. Install dependencies**  
```bash
pip install -r requirements.txt
```

### **3. Create a `.env` file** and add your API keys:  
```plaintext
TAVILY_API_KEY=your_tavily_api_key
GROQ_API_KEY=your_groq_api_key
```

### **4. Run the FastAPI server**  
```bash
python main.py
```

---

## 🛠 API Endpoints  

| Method | Endpoint             | Description |
|--------|----------------------|-------------|
| **POST**  | `/get_ans/invoke`    | Get AI response based on chat history |
| **GET**   | `/meta-llama`        | Access the Llama-3.3-70B model |

---

## 📌 Example Usage  

### **POST /get_ans/invoke**  
#### **Request:**  
```json
{
  "messages": [
    {"role": "user", "content": "Tell me about Hogwarts."}
  ]
}
```

#### **Response:**  
```json
{
  "content": "Hogwarts is a magical school where young witches and wizards learn spells, potions, and more!"
}
```

---

