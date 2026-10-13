def relu(x):
    return max(0, x)

def neuron(inputs, weights, bias):
    weighted_sum = sum(xi*wi for xi, wi in zip(inputs, weights)) + bias
    return relu(weighted_sum)

def layer(inputs, weights, biases):
    outputs = []
    for neuron_weights, bias in zip(weights, biases):
        output = neuron(inputs, neuron_weights, bias)
        outputs.append(output)

    return outputs

def forward_propagation(inputs, network):
    for weights, biases in network:
        inputs = layer(inputs, weights, biases)

    return inputs

inputs = [1, 5, 2]

network = [
    (
        [
            [0.5, 0.2, 0.1],
            [0.1, 0.4, 0.3],
            [0.7, 0.2, 0.5]
        ],
        [1, 0.5, -1]
    ),
    (
        [
            [0.2, 0.3, 0.4],
            [0.5, 0.1, 0.2]
        ],
        [0.1, -0.5]
    )
]

result = forward_propagation(inputs, network)
print("Final output:", result)