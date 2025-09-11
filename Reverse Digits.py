n = int(input("Enter number to reverse :"))
r = 0
while (n > 0):
     r = r*10 + n % 10
     n = n//10
print(r)


# Enter number to reverse :989456
# 654989
