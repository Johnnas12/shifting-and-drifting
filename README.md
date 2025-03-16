# Shifting and Drifting Attention Models (Simple Python Expriment)
#### python version

This repository demonstrates the implementation of **shifting** and **drifting** attention models in Python. These models simulate how attention, as a finite cognitive resource, can be distributed across different concepts over time. The models are based on the concept of **Economic Attention Networks (ECAN)**, where attention is treated as a scarce resource allocated between agents or concepts.

## Table of Contents

- [Overview](#overview)
- [Shifting Attention](#shifting-attention)
- [Drifting Attention](#drifting-attention)
- [Usage](#usage)
- [Example](#example)
- [Installation](#installation)


## Overview

This project models attention allocation using two primary mechanisms:

1. **Shifting Attention**: Attention moves from one concept to another in response to external stimuli or sudden changes (e.g., a new event or piece of information).
2. **Drifting Attention**: Attention gradually shifts over time, reflecting slow-moving changes or long-term trends (e.g., gradual changes in focus or interest).

The project provides a Python-based simulation to demonstrate these concepts and visualize attention levels over time.

## Shifting Attention

Shifting attention represents sudden, large movements of attention from one concept to another based on an external stimulus or event.

### Example:
Imagine a group of investors who suddenly shift their focus to a new stock (e.g., after an important announcement in the tech industry).

In this model, we simulate the sudden shift in attention by updating the attention level of a specific concept.

## Drifting Attention

Drifting attention represents gradual changes in attention over time, where attention moves slowly due to long-term trends, fatigue, or changing preferences.

### Example:
Over time, consumers' attention gradually drifts from traditional retail to e-commerce due to shifting shopping habits.

This model simulates the gradual allocation of attention, changing the attention levels of concepts in a continuous manner.

## Usage

### Python Functions:
1. **shifting_attention(concept, shift_time, attention_change)**: 
   - Shifts the attention of a given concept by a specified value.
   
2. **drifting_attention(concept, drift_rate, start_time, end_time)**: 
   - Gradually drifts the attention of a given concept by a specified value over time.

### Example of Usage:

```python
from shifting_drifting import ShiftAttention, DriftAttention

# Initialize concepts and attention levels
concept1 = "Tech Stocks"
concept2 = "Retail Stocks"

# Initial attention levels
attention_tech = 0.5
attention_retail = 0.5

# Shift attention from Retail Stocks to Tech Stocks
attention_tech = ShiftAttention(concept1, 0.3)
attention_retail = ShiftAttention(concept2, -0.3)

# Drift attention towards Tech Stocks over time
for _ in range(10):
    attention_tech = DriftAttention(concept1, 0.05)

print(f"Tech Stocks Attention: {attention_tech}")
print(f"Retail Stocks Attention: {attention_retail}")
```
### Installation
```
  git clone https://github.com/johnnas12/shifting-and-drifting.git
  cd shifting-and-drifting
  pip install matplotlib numpy 


```
### Expremental outputs 
<img width="500" alt="image" src="https://github.com/user-attachments/assets/2966777f-f9f8-4a50-9517-46b595fade0e" />


