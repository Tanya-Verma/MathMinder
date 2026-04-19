from sympy import symbols, Eq, solve

def solve_equation(eq_str):
    try:
        x = symbols('x')

        left, right = eq_str.split("=")
        equation = Eq(eval(left), eval(right))

        solution = solve(equation, x)
        return solution
    except:
        return None