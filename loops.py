num = int(input("insert non negative numbers"))
factorial = 1
for i in range(1,num+1):
    factorial *= i
print(f"{i};{factorial}")
