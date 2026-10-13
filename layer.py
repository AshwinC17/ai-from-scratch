# Neural Network Layer from Scratch

# -------------------------
# ReLU Activation
# -------------------------
def relu(x):
    return max(0, x)

# -------------------------
# Single Neuron
# -------------------------
def neuron(inputs, weights, bias):
    weighted_sum = sum(xi*wi for xi, wi in zip(inputs, weights)) + bias
    return relu(weighted_sum)

# -------------------------
# Neural Network Layer
# -------------------------
def layer(inputs, weights, biases):
    outputs = []
    for w,b in zip(weights, biases):
        output = neuron(inputs, w, b)
        outputs.append(output)

    return outputs

# Input
inputs = [1, 5, 2]


# Weights for three neurons
weights = [
    [0.5, 0.2, 0.1],
    [0.1, 0.4, 0.3],
    [0.7, 0.2, 0.5]
]


# Bias for each neuron
biases = [
    1,
    0.5,
    -1
]


# Forward through layer
outputs = layer(
    inputs,
    weights,
    biases
)


print("Layer output:", outputs)