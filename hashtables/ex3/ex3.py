def intersection(arrays):
    """
    YOUR CODE HERE
    """

    result = []
    dir = {}

    for array in arrays:
        for item in array:
            if item in dir:
                dir[item] += 1
            else:
                dir[item] = 1


    for key, value in dir.items():
        if value == len(arrays):
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
