from backend.solver import solve_equation

def verify(problem, ai_output):
    correct_answer = solve_equation(problem)

    if correct_answer and str(correct_answer) in ai_output:
        return True
    
    return False