def Q_learning(Q, S, R, A, next_S, gamma, alpha):
    # bellman equation
    Q_estimated = R[S][next_S] +  alpha * max(Q[next_S])

    Q[S, A] = Q[S, A] + gamma * (Q_estimated - Q[S, A])

    return Q

path = [(0, 1), (1, 1), (2, 1), (3, 0), (2, 2), (3, 2), (3, 2), (0, 4), (2, 5), (0, 2), (0, 4), (3, 2), (3, 2), (3, 4), (2, 5), (1, 0), (0, 2), (2, 4), (0, 4), (1, 4), (3, 4), (1, 2), (0, 4), (2, 4), (2, 5), (0, 2), (2, 3), (0, 5), (3, 0), (0, 0), (0, 2), (0, 4), (3, 4), (1, 2), (0, 4), (0, 4), (0, 4), (1, 2), (0, 2), (3, 2), (2, 3), (0, 5)]

# 4 5
# 2 3
# 0 1

import numpy as np

# reward
R = np.full((6, 6), -1)

# hitting the wall
R[0, 0] = -10
R[1, 1] = -10
R[2, 2] = -10
R[3, 3] = -10
R[4, 4] = -10
R[5, 5] = 10

# going to the terminal state
R[:, 5] = 10

# initial Q
Q = np.zeros((6, 4))

#parameters
alpha = 0.5
gamma = 1

S = 0

# updating Q
for action, next_S in path:
    Q = Q_learning(Q, S, R, action, next_S, gamma, alpha)
    S = next_S

# building policy
actions = {0: "UP", 1: "DW", 2: "RG", 3: "LF"}
policy = []
for S in Q:
    # choosing the better action at each state
    policy.append(actions[np.argmax(S)])

# output
show_policy = f"{policy[4]} 10\n{policy[2]} {policy[3]}\n{policy[0]} {policy[1]}"
print(f"- Trajetória\n{Q}\n\n{show_policy}\n")