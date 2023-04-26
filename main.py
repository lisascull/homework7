N = int(input('enter width triangle'))

#triangle #1
print('triangle #1')
for i in range(N, 0, -1):
    for j in range(i):
        print('*', end='')
    print()

#triangle #2
print('triangle #2')
for i in range(1, N+1):
   for j in range(i):
       print('*', end='')
   print()

#triangle #3
print('triangle #3')
for i in range(N):
    for j in range(i):
        print(" ", end="")
    for j in range(N-i):
        print("*", end="")
    print()
#triangle #4
print('triangle #4')
for i in range(N):
    for j in range(N-i):
        print(" ", end="")
    for k in range(i+1):
        print("*", end="")
    print()
