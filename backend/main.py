from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from ocr import extract_text
from solver import solve_equation
from ai_engine import generate_steps
from verifier import verify

# Initialize FastAPI app
app = FastAPI()

# Enable CORS so frontend can talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint (health check)
@app.get("/")
def home():
    return {"message": "MathMind API is running 🚀"}


# TEXT INPUT ENDPOINT
@app.get("/solve")
def solve(q: str):
    """
    This endpoint takes a math problem as a string
    Example: /solve?q=2*x+5=15
    """

    # Step 1: Solve using symbolic math
    answer = solve_equation(q)

    # Step 2: Generate AI explanation
    explanation = generate_steps(q)

    # Step 3: Verification loop
    # If AI output doesn't match actual answer, regenerate
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
    """
    This endpoint takes an uploaded image,
    extracts text using OCR, then solves it
    """

    # Step 1: OCR → extract math problem
    extracted_text = extract_text(file)

    # Step 2: Solve equation
    answer = solve_equation(extracted_text)

    # Step 3: Generate explanation
    explanation = generate_steps(extracted_text)

    # Step 4: Verification loop
    if not verify(extracted_text, explanation):
        explanation = generate_steps(extracted_text + " verify carefully and correct mistakes")

    return {
        "detected_text": extracted_text,
        "answer": str(answer),
        "explanation": explanation
    }