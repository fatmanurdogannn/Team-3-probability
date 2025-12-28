import numpy as np
import matplotlib.pyplot as plt

# Number of observations
n = 10000  # recommended n ≥ 10,000

# Generate U(0,1) random variables
X = np.random.uniform(0, 1, n)

# Compute cumulative mean
S_n = np.cumsum(X) / np.arange(1, n + 1)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(S_n, label='Cumulative Mean $S_n$')
plt.axhline(y=0.5, color='red', linestyle='--', label='μ = 0.5')

plt.xlabel('Number of Observations (n)')
plt.ylabel('Cumulative Mean')
plt.title('SLLN Simulation for U(0,1)')
plt.legend()
plt.grid(True)
plt.show()
