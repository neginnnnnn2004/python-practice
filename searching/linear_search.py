list1 = [14,94,36,81,43,9,58,26,7,87,35,19,10,23,45,70,11,15]
x = int(input('Please enter a number: '))
res = -1
for i in range(len(list1)):
    if list1[i] == x:
        res = i
        break
if res != -1:
    print("index number: ",res)
    print("chosen number: ",list1[res])
else:
    print('Not Found')
