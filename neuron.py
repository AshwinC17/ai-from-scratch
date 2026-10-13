# Artificial Neuron from Scratch


def relu(x):
    return max(0, x)


def neuron(inputs, weights, bias):

    weighted_sum = sum(
        input_value * weight
        for input_value, weight in zip(inputs, weights)
    )

    weighted_sum += bias

    output = relu(weighted_sum)

    return output


# Inputs
inputs = [2, 3, 4]


# Weights
weights = [0.5, 0.2, 0.1]


# Bias
bias = 1


# Calculate neuron output
output = neuron(
    inputs,
    weights,
    bias
)


print("Neuron output:", output)