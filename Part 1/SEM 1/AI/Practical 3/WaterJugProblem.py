from collections import defaultdict

visited = defaultdict(lambda: False)

def waterJugSolver(amt1, amt2):
    # Check if we've reached the target amount in either jug with the other empty
    if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
        print(amt1, amt2)
        return True

    # If this state has not been visited yet
    if not visited[(amt1, amt2)]:
        print(amt1, amt2)  # Print the current state
        visited[(amt1, amt2)] = True
        
        # Recursively try all possible actions
        return (
            waterJugSolver(0, amt2) or   # Empty jug1
            waterJugSolver(amt1, 0) or   # Empty jug2
            waterJugSolver(jug1, amt2) or # Fill jug1
            waterJugSolver(amt1, jug2) or # Fill jug2
            waterJugSolver(amt1 + min(amt2, jug1 - amt1), 
                           amt2 - min(amt2, jug1 - amt1)) or # Pour from jug2 to jug1 
            waterJugSolver(amt1 - min(amt1, jug2 - amt2), 
                           amt2 + min(amt1, jug2 - amt2)) # Pour from jug1 to jug2 
        )
    else:
        return False


# Jug capacities
jug1, jug2 = 7, 4

# target amount
aim = 5

print("Steps: ")
waterJugSolver(0, 0)