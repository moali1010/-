def calculator(n, m, ls):
    num_arr = n // m
    counter = 0
    output = {}
    for i in range(num_arr + 1):
        arr = {}
        for j in range(m):
            if counter < n:
                arr[j] = ls[counter]
            counter += 1
        s_arr = sum(arr.values())
        if i % 2 == 0:
            output[i] = s_arr
        else:
            output[i] = (-1) * s_arr
    return sum(output.values())


# Local Tests
print(calculator(8, 3, [1, 2, 3, 4, 5, 6, 7, 8]))
print(calculator(8, 1, [1, 2, 3, 4, 5, 6, 7, 8]))
