def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    positives = {}
    negatives = {}

    for item in a:
        if (item > 0):
            if (item in positives):
                positives[item] += 1
            else:
                positives[(item)] = 1
        if (item < 0):
            if (item in negatives):
                negatives[abs(item)] += 1
            else:
                negatives[abs(item)] = 1

    for key in positives:
        if key in negatives:
            result.append(key)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
