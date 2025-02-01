# 🧠 AI-Powered PostgreSQL Coding Tutor

This project is an **AI-powered SQL tutor** that:
- 🏎 **Optimizes PostgreSQL queries** using `sqlglot`
- 📈 **Suggests best practices** using `LLaMA 2`
- ⚡ **Runs `EXPLAIN ANALYZE`** to evaluate query performance
- 🖥 **Provides a Streamlit UI** for interactive learning

---

## 📌 Features
✅ **AI-powered query optimization**  
✅ **Best practice recommendations**  
✅ **Real-time `EXPLAIN ANALYZE` query analysis**  
✅ **Streamlit-based UI** for interactive SQL tutoring  

---

## 🚀 **Setup & Installation**
### **1️⃣ Install Dependencies**
Ensure **Python 3.11+** and **Poetry** are installed.

```sh
# Clone the repo
git clone https://github.com/yourusername/sql-coding-tutor.git
cd sql-coding-tutor

# Initialize Poetry environment
poetry install

### **2️⃣ Install Dependencies**
Ensure **Python 3.11+** and **Poetry** are installed.

```sh
# Clone llama.cpp
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
make

# Download LLaMA 2 model
mkdir -p models
cd models
wget https://huggingface.co/TheBloke/Llama-2-7B-GGUF/resolve/main/llama-2-7b.Q4_0.gguf


### **3️⃣ Download LLaMA 2 Model**
Ensure **Python 3.11+** and **Poetry** are installed.

```sh
# Start the LLaMA Model
./llama.cpp/main -m models/llama-2-7b.Q4_0.gguf

# Start Streamlit UI
poetry run streamlit run app.py

