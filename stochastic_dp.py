# --------------
# USER INSTRUCTIONS
#
# Write a function called stochastic_value that
# takes no input and RETURNS two grids. The
# first grid, value, should contain the computed
# value of each cell as shown in the video. The
# second grid, policy, should contain the optimum
# policy for each cell.
#
# Stay tuned for a homework help video! This should
# be available by Thursday and will be visible
# in the course content tab.
#
# Good luck! Keep learning!
#
# --------------
# GRADING NOTES
#
# We will be calling your stochastic_value function
# with several different grids and different values
# of success_prob, collision_cost, and cost_step.
# In order to be marked correct, your function must
# RETURN (it does not have to print) two grids,
# value and policy.
#
# When grading your value grid, we will compare the
# value of each cell with the true value according
# to this model. If your answer for each cell
# is sufficiently close to the correct answer
# (within 0.001), you will be marked as correct.
#
# NOTE: Please do not modify the values of grid,
# success_prob, collision_cost, or cost_step inside
# your function. Doing so could result in your
# submission being inappropriately marked as incorrect.

# -------------
# GLOBAL VARIABLES
#
# You may modify these variables for testing
# purposes, but you should only modify them here.
# Do NOT modify them inside your stochastic_value
# function.

grid = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]]

#grid = [[0, 0, 0],
#        [0, 0, 0]]

goal = [0, len(grid[0])-1] # Goal is in top right corner


delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>'] # Use these when creating your policy grid.

success_prob = 0.5
failure_prob = (1.0 - success_prob)/2.0 # Probability(stepping left) = prob(stepping right) = failure_prob
collision_cost = 100
cost_step = 1


############## INSERT/MODIFY YOUR CODE BELOW ##################
#
# You may modify the code below if you want, but remember that
# your function must...
#
# 1) ...be called stochastic_value().
# 2) ...NOT take any arguments.
# 3) ...return two grids: FIRST value and THEN policy.

import copy, math

def stochastic_value():
    value = [[1000 for row in range(len(grid[0]))] for col in range(len(grid))]
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    lock = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]

    next = [(goal[1], goal[0])]

    value[goal[0]][goal[1]] = 0
    policy[goal[0]][goal[1]]= '*'

    def wall(pos):
        x, y = pos
        try:
            if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid) or grid[y][x] == 1:
                return True
            else:
                return False
        except IndexError:
            return True

    def _val(pos):
        return collision_cost if wall(pos) else value[pos[1]][pos[0]]

    def step(pos):
        x, y = pos

        vals = []

        for i in xrange(len(delta)):
            dy, dx = delta[i]

            val = cost_step+success_prob*_val((x+dx, y+dy))
            if dy != 0:
                # up/down's left/right
                val += failure_prob*_val((x-1, y))
                val += failure_prob*_val((x+1, y))
            else:
                # left/right's left/right
                val += failure_prob*_val((x, y-1))
                val += failure_prob*_val((x, y+1))

            vals.append((val, delta_name[i]))

            if not wall([x+dx, y+dy]) and lock[y+dy][x+dx] < 1000:
                next.append((x+dx, y+dy))

        val = min(vals, key=lambda v: v[0])

        if [y,x] == goal:
            return (0, '*')
        else:
            return val

    while len(next) > 0:
        pos = next.pop(0)
        val, pol = step(pos)

        if value[pos[1]][pos[0]] == val:
            lock[pos[1]][pos[0]] += 1

        value[pos[1]][pos[0]] = val
        policy[pos[1]][pos[0]] = pol

    print value
    print policy


    return value, policy

stochastic_value()
