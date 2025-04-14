# ⚖️ Legal Document Analyzer

A multi-functional system— **Legal Document Analyzer**—that integrates judgment retrieval, IPC section mapping,summarization, and question answering.

---

## Introduction

Legal documents are often lengthy, complex, and written in jargon-heavy language. This project aims to provide the following functionality:

- **IPC Section Retrieval**: Instantly fetch relevant Indian Penal Code (IPC) sections based on the legal query or keywords provided.
- **Similar Judgement Finder**: Retrieve case judgments similar to a given legal scenario using semantic matching.
- **Summarizer**: Generate brief and coherent summaries of lengthy legal documents or case texts.
- **Chatbot**: Interact with a legal chatbot to ask questions and receive responses based on legal context and trained models.
- Provide an intuitive web interface for seamless user interaction.

This can be extremely useful for:

- Law students
- Legal researchers
- Common users trying to understand their contracts, agreements, or policies

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/Serendipity-scribe-dev/Legal-Document-Analyzer.git
cd LegalDoc_Analyzer
```

### 2. Set up Python Environment

```bash
python -m venv venv
venv/Scripts/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create .env File

```
API_KEY =your_api_key
```

### 5. Run the Sever

```bash
uvicorn main:app --reload
Then visit http://127.0.0.1:8000/
```

---

## Models Used

### 1. `all-mpnet-base-v2` (IPC Section Retrieval)

- 12 layers, 768 hidden units, 12 heads (~110M parameters)
- Based on MPNet with relative position embeddings
- Fine-tuned using contrastive learning on over 1B sentence pairs
- Optimized for semantic search & legal provision retrieval

### 2. `TheBloke/Mistral-7B-Instruct-v0.2-GPTQ` (Chatbot)

- 32 layers, 4096 hidden size, 7.3B parameters
- Uses grouped-query attention, RoPE, and sliding window attention
- 4-bit quantized (GPTQ) for efficient inference
- SFT + DPO tuned on legal Q&A data

### 3. `all-MiniLM-L6-v2` (Similar Judgment Finder)

- 6 transformer layers, 384 hidden size (~22M parameters)
- Distilled from BERT-base for high-speed inference
- Fine-tuned on NLI and STS for semantic similarity
- Best for real-time judgment matching

### 4. `bert-base-uncased` (Case Summarization)

- 12 layers, 768 hidden size, 12 heads (~110M parameters)
- Pre-trained with MLM + NSP
- Fine-tuned on legal case summaries
- Effective for extractive summarization of long texts

---

## File Descriptions

| File / Folder                     | Description                                          |
| --------------------------------- | ---------------------------------------------------- |
| `ipynb_files`                     | Contains all the primary ipynb files                 |
| `app/main.py`                     | Main FastAPI entry point for the application         |
| `app/routes/chatbot_routes.py`    | Routes and logic for handling chatbot requests       |
| `app/routes/ipc_routes.py`        | IPC classifier and retrieval APIs                    |
| `app/routes/judgement_routes.py`  | Endpoint to fetch similar legal cases                |
| `app/routes/summarizer_routes.py` | Text summarization logic using BERT                  |
| `models/`                         | Folder to store trained models and embeddings        |
| `templates/`                      | Frontend HTML files including chatbot interface      |
| `.env`                            | Environment variables for API keys and model configs |
| `requirements.txt`                | List of all the required Dependencies                |

---

## Demo Video

[Watch the demo](https://www.loom.com/share/e3e113300a634ccd8ebabdefe9b2084b)

---

## Conclusion

The Legal Document Analyzer empowers legal professionals and students by automating key tasks using cutting-edge NLP. It bridges the gap between raw legal data and actionable insights using different ML models and FastAPI.

---
