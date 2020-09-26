# arr = [1, n]

arr = [1, 3, 2, 3, 4, 7, 5, 6]


def help(arr):
    max_value = len(arr) - 1
    y = max_value * (max_value + 1) / 2
    z = sum(arr) - y
    return z


h = help(arr)
print(h)
