from numpy import *

n = int(input("Enter number of proccessers: "))
m = int(input("Enter number of sources: "))

source = [x for x in map(int,input("Enter samples of sources by space: ").split())]

allocation = zeros((n,m))
max_ = zeros((n,m))
available = zeros((1,m))

for i in range(5):
    for j in range(3):
        a = int(input("Enter allocation in [{},{}]: ".format(i,j)))
        m = int(input("Enter max in [{},{}]: ".format(i,j)))

        allocation[i,j] = a
        max_[i,j] = m
    print()

for j in range(m):
    a = int(input("Enter available in [{},{}]: ".format(0,j)))
    available[0,j] = a
print()

need = zeros((n,m))

for i in range(5):
    for j in range(3):
        need[i,j] = max_[i,j] - allocation[i,j]

work = available
finish = ['false'] * n

for i in range(5):
    if all(need[i] <= work):
        work += allocation[i]
        finish[i] = 'true'

for i in finish:
    if i == 'false':
        j = finish.index(i)
        if all(need[j] <= work):
            work += allocation[j]
            finish[j] = 'true'

count = finish.count('true')

if count == n:
    print("It is safe.")
else:
    print("It is unsafe.")
print()

request = zeros((1,m))

for i in range(m):
    r = int(input("Enter request in [{},{}]: ".format(0,i)))
    request[0,i] = r
print()

if all(request <= available):
    print("Yes.")
else:
    print("No.")
print()

quit = input("Press Enter to Exit.")
