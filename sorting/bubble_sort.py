import random

n1 =10000
unorder_list = [random.randint(1,10000) for i in range(n1)]
n = len(unorder_list)
i = n-1

print(unorder_list)
while i>0:
    swapped = False
    j=0
    while j<i:
        if unorder_list[j]>unorder_list[j+1]:
            unorder_list[j], unorder_list[j+1]=unorder_list[j+1], unorder_list[j]
            swapped = True
        j = j+1
    if not swapped:
        break
    i = i-1
print("sorted_lisr: ",unorder_list)