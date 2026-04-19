from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from ocr import extract_text
from solver import solve_equation
from ai_engine import generate_steps
from verifier import verify

# Initialize FastAPI app
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
def home():
    return {"message": "MathMind API is running 🚀"}


# TEXT INPUT ENDPOINT
@app.get("/solve")
def solve(q: str):
    answer = solve_equation(q)
    explanation = generate_steps(q)

    if not verify(q, explanation):
        explanation = generate_steps(q + " verify carefully and correct mistakes")

    return {
        "question": q,
        "answer": str(answer),
        "explanation": explanation
    }


# IMAGE INPUT ENDPOINT
@app.post("/solve-image")
async def solve_image(file: UploadFile = File(...)):
    extracted_text = await extract_text(file)  # ⚠️ async fix

    answer = solve_equation(extracted_text)
    explanation = generate_steps(extracted_text)

    if not verify(extracted_text, explanation):
        explanation = generate_steps(extracted_text + " verify carefully and correct mistakes")

    return {
        "detected_text": extracted_text,
        "answer": str(answer),
        "explanation": explanation
    }