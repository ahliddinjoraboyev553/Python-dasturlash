from math import *
x=float(input("x ni kiriting x="))
y=float(input("y ni kiriting y="))
z=float(input("z ni 0<=z<=1 oraliqda kiriting z="))
f=(pow((y+pow((x-1),1/3)),1/4))/(fabs(x-y)*(pow(sin(z),2)+tan(z)))
print(f"f={f}")