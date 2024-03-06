#compound interest
#A = p(1+r/100)**t
#compound interest = A - p
A = int(input("enter the value of A"))
p = int(input("enter the value of p"))
r = int(input("enter the value of r"))
t = int(input("enter the value of t"))
interest =  A - p * (1 + r / 100) ** t
print(interest)





