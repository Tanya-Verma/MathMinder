# 🧠 MathMind AI Math Assistant

**It works on Understanding math,then solving it.**

*MathMind is an AI-powered math problem solver that accepts **typed equations and images**, processes them through a **vision + symbolic + reasoning pipeline**, and returns **step-by-step explanations** in a your writting.*

## 🚀 Features

* ✏️ `Solve typed math problems`
* 📷 `Solve problems from images (OCR)`
* 🧮 `Symbolic computation using SymPy`
* 🧠 `Step-by-step explanations`
* ⚡ `Fast API backend`
* 🌐 `Deployable full-stack web app`

## 🧠 How It Works

MathMind follows a pipeline architecture:

1. **Input Layer**

   * User enters equation OR uploads image

2. **OCR (for images)**

   * Extracts text using Tesseract OCR

3. **Parsing & Solving**

   * Converts expression into symbolic form
   * Solves using SymPy

4. **Explanation Engine**

   * Generates step-by-step reasoning

5. **Verification Loop**

   * Ensures solution correctness

---

## 🗂️ Project Structure

```
mathmind/<br>
│
├── backend/<br>
│   ├── main.py<br>        
│   ├── solver.py<br>      
│   ├── ai_engine.py<br>    
│   ├── ocr.py<br>          
│   ├── verifier.py<br>     
│   └── requirements.txt<br>
│
├── frontend/<br>
│   ├── index.html<br>
│   ├── style.css<br>
│   └── script.js<br>
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/mathmind.git
cd mathmind
```

---

### 2. Setup Backend

```bash
cd backend
pip install -r requirements.txt
```

---

### 3. Run Backend Server

```bash
uvicorn main:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

---

### 4. Run Frontend

Open:

```
frontend/index.html
```

---

## 🌐 Deployment

### Backend:

Deploy using Render

### Frontend:

Deploy using Vercel


## 🔮

* 📊 `User progress tracking`
* 🔐 `Authentication system`
* ✍️ `Handwritten-style rendering`
* 🤖 `Advanced LLM integration`
* 📷 `Real-time camera solving`


## 💡 Tech Stack

* `Backend: FastAPI (Python)`
* `Math Engine: SymPy`
* `OCR: Tesseract`
* `Frontend: HTML, CSS, JavaScript`


## 👩‍💻 Author

*Tanya Verma*
*Computer Science (AI) Student*


