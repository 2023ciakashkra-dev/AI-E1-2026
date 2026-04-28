#program to calculate the probability of an event using its probability notation

# Function to calculate probability
def calculate_probability(favorable_outcomes, total_outcomes):
    if total_outcomes == 0:
        return "Total outcomes cannot be zero."
    
    probability = favorable_outcomes / total_outcomes
    return probability

# Taking input from user
favorable = int(input("Enter number of favorable outcomes: "))
total = int(input("Enter total number of outcomes: "))

# Calculate probability
result = calculate_probability(favorable, total)

# Display result
print(f"Probability P(A) = {result}")