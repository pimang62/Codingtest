n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

# array = sorted(array, reverse=True)
array.sort(reverse=True)

for num in array:
    print(num, end=' ')