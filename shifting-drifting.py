import matplotlib.pyplot as plt
import numpy as np

# Define the concepts (e.g., economic sectors or agents)
concepts = ["Tech", "Retail", "Finance", "Healthcare", "Energy"]

# Initial attention levels (Percentage) for each concept
initial_attention = {
    "Tech": 50,
    "Retail": 30,
    "Finance": 10,
    "Healthcare": 5,
    "Energy": 5
}

# Time-related parameters
time_steps = 100  # Total time steps for the simulation
time_interval = 0.1  # Time interval (seconds)

# Initialize a dictionary to store the attention over time for each concept
attention_over_time = {concept: [] for concept in concepts}

# Function to simulate shifting attention (sudden change)
def shifting_attention(concept, shift_time, attention_change):
    # At shift_time, change the attention by a sudden amount
    if shift_time < time_steps:
        initial_attention[concept] += attention_change
        initial_attention[concept] = max(0, min(initial_attention[concept], 100))  # Ensure it stays between 0 and 100

# Function to simulate drifting attention (gradual change)
def drifting_attention(concept, drift_rate, start_time, end_time):
    # Gradually drift the attention over time
    for t in range(start_time, end_time):
        initial_attention[concept] += drift_rate
        initial_attention[concept] = max(0, min(initial_attention[concept], 100))  # Ensure it stays between 0 and 100

# Simulate the attention changes over time
for t in range(time_steps):
    # Drift attention over time for each concept (for example, a gradual increase)
    drifting_attention("Tech", 0.1, t, time_steps)
    drifting_attention("Retail", -0.05, t, time_steps)
    drifting_attention("Finance", 0.05, t, time_steps)
    drifting_attention("Healthcare", -0.02, t, time_steps)
    drifting_attention("Energy", 0.02, t, time_steps)
    
    # Record attention at each time step
    for concept in concepts:
        attention_over_time[concept].append(initial_attention[concept])

    # Simulate a sudden shift in attention at specific times
    if t == 50:  # Example: Shift attention at time step 50
        shifting_attention("Tech", t, 20)  # Sudden shift in Tech's attention
        shifting_attention("Retail", t, -10)  # Sudden shift in Retail's attention

# Plot the results
plt.figure(figsize=(10, 6))

# Plot each concept's attention level over time
for concept in concepts:
    plt.plot(np.arange(0, time_steps * time_interval, time_interval), attention_over_time[concept], label=concept)

# Labels and title
plt.xlabel("Time (seconds)")
plt.ylabel("Attention Level (%)")
plt.title("Attention Allocation Over Time (Shifting & Drifting Attention)")
plt.legend()

# Show plot
plt.grid(True)
plt.show()