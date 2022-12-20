from itertools import*
s = input().split()
list1 = []
for i in permutations(s):
    if list(i) not in list1:
        list1.append(list(i))
print(list1)