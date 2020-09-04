def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """

    dict = {}

    for x in range(0, length):
        minuend = limit - weights[x]
        if minuend in dict:
            return [x, dict[minuend]]
        else:
            dict[weights[x]] = x
    return None