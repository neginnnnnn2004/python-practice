lst = [1,3,5,7,9,11,13,15,17,19]
x = int(input('Please enter a number: '))
res = -1
left = 0
right = len(lst) - 1

while left <= right:
    mid = (left + right) // 2
    if x == lst[mid]:
        res = mid
        break
    elif x > lst[mid]:
        left = mid + 1
    else:  # x < lst[mid]
        right = mid - 1

if res != -1:
    print(f'Found at index {res}')
else:
    print('Not found')