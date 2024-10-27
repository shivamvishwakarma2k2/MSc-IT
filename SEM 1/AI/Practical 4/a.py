from simpleai.search import CspProblem, backtrack

# Define the constraint function
def different_colors_constraint(names, values):
    return values[0] != values[1]

# Define the problem
def main():
    # Define variables
    variables = ['WA', 'NT','SA', 'QL','Vict', 'Tasmania']
    
    # Define domains (color choices)
    domains = {
        'WA': ['red', 'green', 'blue'],
        'NT': ['red', 'green', 'blue'],
        'QL': ['red', 'green', 'blue'],
        'Vict': ['red', 'green', 'blue'],
        'Tasmania': ['red', 'green', 'blue'],
        'SA': ['red', 'green', 'blue']
    }
    
    # Define constraints
    constraints = [
        (('WA', 'NT'), different_colors_constraint),
        (('WA', 'SA'), different_colors_constraint),
        (('SA', 'QL'), different_colors_constraint),
        (('SA', 'NT'), different_colors_constraint),
        (('SA', 'Vict'), different_colors_constraint),
        (('QL', 'NT'), different_colors_constraint),
        (('QL', 'Vict'), different_colors_constraint),
        (('Tasmania'), different_colors_constraint)
    ]
    
    # Create CSP problem
    problem = CspProblem(variables, domains, constraints)
    
    # Solve the problem
    solution = backtrack(problem)
    
    print("Solution:\n", solution)

if __name__ == "__main__":
    main()