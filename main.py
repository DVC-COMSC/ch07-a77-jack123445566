num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
num3 = []
smaller = len(num2)
if len(num1) < len(num2):
    smaller = len(num1)

for i in range(smaller):
    num3.append(num1[0])
    num1.pop(0)
    num3.append(num2[0])
    num2.pop(0)
num3.append(num1 + num2)
print (num3) 
