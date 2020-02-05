import random

n = int(input('n: '))
array = []

for i in range(0, n):
    arr0 = list(range(n))

    random.shuffle(arr0)
    array.append(arr0)

print(array)


k = int(input('k: '))
result = []

for arr1 in array:
    for elem in arr1:
        if elem % k == 0 and elem != 0:
            result.append(elem)


print(result)
print(len(result))


"""
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
    l_nums = [n for n in nums if n < q]

    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    return quicksort(l_nums) + e_nums + quicksort(b_nums)

"""
