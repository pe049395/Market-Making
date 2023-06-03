import math
import numpy as np

n_timesteps = 200
n_simulations = 1000

T = 1
dt = T / n_timesteps

sigma = 2
k = 1.5
A = 140
gamma = 0.1

profit = []
final_q = []

for _ in range(n_simulations):
    s = 100
    x = 0
    q = 0

    for timesteps in range(1, n_timesteps + 1):
        z = np.random.standard_normal()
        s += sigma * math.sqrt(dt) * z
        t = timesteps / n_timesteps

        r = s - q * gamma * sigma**2 * (T - t)
        delta = gamma * sigma**2 * (T - t) + 2 / gamma * math.log(1 + gamma / k)

        bid = r - delta / 2
        ask = r + delta / 2

        delta_b = s - bid
        delta_a = ask - s

        lambda_b = A * math.exp(-k * delta_b)
        prob_b = lambda_b * dt
        rand_b = np.random.uniform()

        lambda_a = A * math.exp(-k * delta_a)
        prob_a = lambda_a * dt
        rand_a = np.random.uniform()

        if prob_b >= rand_b:
            x -= bid
            q += 1

        if prob_a >= rand_a:
            x += ask
            q -= 1

    profit.append(x + q * s)
    final_q.append(q)

print("Simulation Result:")
print("Profit:", np.mean(profit))
print("Final q:", np.mean(final_q))
