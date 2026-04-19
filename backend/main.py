
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from backend.solver import solve_equation
from backend.ocr import extract_text
from backend.ai_engine import generate_steps
from backend.verifier import verify


app = FastAPI()

# Enable CORS (for frontend connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ------------------- ROOT -------------------
@app.get("/")
def home():
    return {"message": "MathMind API is running 🚀"}


# ------------------- TEXT SOLVER -------------------
@app.get("/solve")
def solve(q: str):
    try:
        answer = solve_equation(q)
        explanation = generate_steps(q)

        # Verification loop
        if not verify(q, explanation):
            explanation = generate_steps(q + " verify carefully and correct mistakes")

        return {
            "question": q,
            "answer": str(answer),
            "explanation": explanation
        }

    except Exception as e:
        return {"error": str(e)}


# ------------------- IMAGE SOLVER -------------------
@app.post("/solve-image")
async def solve_image(file: UploadFile = File(...)):
    try:
        # OCR extraction
        extracted_text = await extract_text(file)

        # Solve
        answer = solve_equation(extracted_text)
        explanation = generate_steps(extracted_text)

        # Verification
        if not verify(extracted_text, explanation):
            explanation = generate_steps(
                extracted_text + " verify carefully and correct mistakes"
            )

        return {
            "detected_text": extracted_text,
            "answer": str(answer),
            "explanation": explanation
        }

    except Exception as e:
        return {"error": str(e)}