from sympy.parsing.sympy_parser import parse_expr

def parse_equation(eq):
    try:
        return parse_expr(eq)
    except:
        return None