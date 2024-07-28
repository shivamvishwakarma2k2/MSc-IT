from collections import deque

class Solution:

    def solve(self, board):
        # Renamed dict to state_dict and initialize with the flattened initial board
        state_dict = {}
        flatten = []
        for i in range(len(board)):
            flatten += board[i]
        flatten = tuple(flatten)
        
        print("flatten : ", flatten) 
        state_dict[flatten] = 0  # Initial state with depth 0

        print("state_dict", state_dict)
        
        goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
        if flatten == goal_state:
            return 0

        return self.get_paths(state_dict, goal_state)

    def get_paths(self, state_dict, goal_state):
        cnt = 0
        queue = deque([x for x in state_dict if state_dict[x] == cnt])
        
        while queue:
            current_node = queue.popleft()

            if current_node == goal_state:
                return state_dict[current_node]

            next_moves = self.find_next(current_node)
            for move in next_moves:
                if move not in state_dict:
                    state_dict[move] = state_dict[current_node] + 1
                    queue.append(move)
                    if move == goal_state:
                        return state_dict[move]

        return -1  # No solution found

    def find_next(self, node):
        moves = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4, 6],
            4: [1, 3, 5, 7],
            5: [2, 4, 8],
            6: [3, 7],
            7: [4, 6, 8],
            8: [5, 7],
        }

        results = []
        pos_0 = node.index(0)
        for move in moves[pos_0]:
            new_node = list(node)
            new_node[move], new_node[pos_0] = new_node[pos_0], new_node[move]
            results.append(tuple(new_node))
        
        return results

# Example usage
ob = Solution()
matrix = [
    [3, 1, 2],
    [4, 7, 5],
    [6, 8, 0]
]
print(ob.solve(matrix))  # Output the number of moves required to solve the puzzle