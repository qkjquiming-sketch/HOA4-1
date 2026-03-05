from truthtablegen import generate_truthtable

def evaluate_propositional_logic(c_list):
    expression = input("Enter the propositional logic expression: ")
    
    num_vars = len(c_list[0])
    
    if num_vars == 2:
        print("A B f")
        for A, B in c_list:
            evaluated_expression = eval(expression)
            print(A, B, evaluated_expression)
    
    elif num_vars == 3:
        print("A B C f")
        for A, B, C in c_list:
            evaluated_expression = eval(expression)
            print(A, B, C, evaluated_expression)


# MAIN PROGRAM (only this at the bottom)
print("Propositional logic evaluator for discrete math")
variables = int(input("How many variables? "))

evaluate_propositional_logic(generate_truthtable(variables))