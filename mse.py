def mean_squared_error(actual, predicted):
    if len(actual) != len(predicted):
        raise ValueError("Lists must have equal lengths")

    if len(actual) == 0:
        raise ValueError("Lists cannot be empty")

    squared_errors = [
        (a - p) ** 2
        for a, p in zip(actual, predicted)
    ]

    return sum(squared_errors) / len(squared_errors)


actual = [5, 10, 15]
predicted = [4, 12, 10]

loss = mean_squared_error(actual, predicted)

print("MSE:", loss)