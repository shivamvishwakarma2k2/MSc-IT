from simpleai.search import CspProblem, backtrack

# Define the constraint function
def different_colors_constraint(names, values):
    return values[0] != values[1]

def main():
    variables = ['A', 'B', 'C'] # Define variables
    
    # Define domains (color choices)
    domains = {
        'A': ['red', 'green', 'blue'],
        'B': ['red', 'green', 'blue'],
        'C': ['red', 'green', 'blue']
    }
    
    # Define constraints
    constraints = [
        (('A', 'B'), different_colors_constraint),
        (('A', 'C'), different_colors_constraint),
        (('B', 'C'), different_colors_constraint)
    ]
    
    # Create CSP problem
    problem = CspProblem(variables, domains, constraints)
    
    # Solve the problem
    solution = backtrack(problem)
    print("Solution:", solution)

if __name__ == "__main__":
    main()