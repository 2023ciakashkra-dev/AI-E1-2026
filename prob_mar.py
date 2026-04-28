# program to calculate marginal probability from a joint distribution

# Function to calculate marginal probabilities from joint distribution

def marginal_probability(joint_dist):
    """
    joint_dist: 2D list (matrix) representing P(X, Y)
    rows -> X values
    columns -> Y values
    """

    # Marginal P(X)
    marginal_X = [sum(row) for row in joint_dist]

    # Marginal P(Y)
    marginal_Y = [sum(col) for col in zip(*joint_dist)]

    return marginal_X, marginal_Y


# Example joint distribution
# P(X, Y)
joint_distribution = [
    [0.1, 0.2, 0.1],
    [0.05, 0.25, 0.3]
]

# Calculate marginals
px, py = marginal_probability(joint_distribution)

# Display results
print("Joint Distribution:")
for row in joint_distribution:
    print(row)

print("\nMarginal Probability P(X):", px)
print("Marginal Probability P(Y):", py)