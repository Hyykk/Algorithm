import random
from timeit import default_timer as timer

def shell_sort(arr, len):
    h = len // 2
    while h > 0:
        for i in range(h, len):
            temp = arr[i]
            j = i - h
            while j >= 0 and arr[j] > temp:
                arr[j + h] = arr[j]
                j -= h
            arr[j + h] = temp
        h //= 2
    return arr

def test(A):
    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            return False
    return True

x = random.choices(range(10000), k = 100)
start = timer()
print(x)
x = shell_sort(x, 100)
print(timer() - start)
print(x)
print(test(x))