def whiileloop(n):
    a = 0
    while (a < n * n * n):
        a = a + n * n
        print(a) 
whiileloop(10)

def sum(n):
    sum = 0
    for i in range(n): #O(n)
      j = 1
      while j < n: #O(1)
        j *= 2     #O(1)
        sum += 1  #O(1)
        print(sum)
sum(6)
