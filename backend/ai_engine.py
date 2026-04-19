# backend/ai_engine.py

def generate_steps(question: str) -> str:
    """
    Generate step-by-step explanation without using paid APIs
    Works best for algebra-type equations
    """

    try:
        # Basic explanation template
        explanation = f"""
Step-by-step solution:

1. Given equation:
   {question}

2. Simplify both sides if needed.

3. Move variables to one side and constants to the other.

4. Solve for the variable.

5. Final Answer is obtained after simplification.

(This is an auto-generated explanation. For advanced steps, AI model can be integrated.)
"""
        return explanation.strip()

    except Exception as e:
        return f"Error generating steps: {str(e)}"