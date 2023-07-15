import random


a=[];
for i in range(10):
    a.append(random.randrange(0,100));
print(max(a));
print(min(a));
print(sum(a));
print(sum(a)/10);
print(a);