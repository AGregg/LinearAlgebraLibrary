from vector import *

x = Vector([8.218,-9.341])
y = Vector([-1.129,2.111])
print(x.add(y).coordinates)

x = Vector([7.119,8.215])
y = Vector([-8.223,0.878])
print(x.subtract(y).coordinates)

x = Vector([1.671,-1.012,-0.318])
y = 7.41
print(x.scalar_multiply(y).coordinates)
