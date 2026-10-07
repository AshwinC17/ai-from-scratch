# ReLU Activation Function


def relu(x):
    return max(0, x)


print("ReLU(5):", relu(5))

print("ReLU(-3):", relu(-3))

print("ReLU(0):", relu(0))