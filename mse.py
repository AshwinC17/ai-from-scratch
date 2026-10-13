# Mean Squared Error from Scratch

def mean_squared_error(actual, predicted):
    squared_errors = [
        (a - p) ** 2
        for a, p in zip(actual, predicted)
    ]

    return sum(squared_errors) / len(squared_errors)


actual = [10, 20, 30]
predicted = [7, 18, 25]

loss = mean_squared_error(actual, predicted)

print("MSE:", loss)