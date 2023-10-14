
# a er quantity--1 mole/vol
# b er quantity--0.5 mole/vol
# rate constant: k1,k2--.05
#
# step 500
#
# time 100 sec
# 0---100 || 500
#_____________________________________________________

import matplotlib.pyplot as plt
time = 100
N = 500
t = 0.2
a = 1.0
b = 0.5
c = 0.0
k = 0.05

A=[]
B=[]
C=[]

print("Time\t\t\tA(i)\t\t\tB(i)\t\t\tC(i)")
print(0.00,a,b,c,sep="\t\t\t")

dt = t
while dt<=N:
    a = a + k*(c-a*b)*dt
    b = b + k*(c-a*b)*dt
    c = c + 2*k*(a*b-c)*dt
    print(f"{dt:.2f}",f"{a:.2f}",f"{b:.2f}",f"{c:.2f}",sep="\t\t\t")
    A.append(a)
    B.append(b)
    C.append(c)
    dt += t

plt.plot(A,label = "a")
plt.plot(B,label = "b")
plt.plot(C,label = "c")

plt.legend(title = "title")
plt.show()