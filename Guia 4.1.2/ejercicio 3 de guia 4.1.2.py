import random


a=[];
b=[];
sum_a=0;
sum_b=0;
for n in range(10):
    a.append(random.randrange(0,300));
    b.append(random.randrange(0,300));
    sum_a=sum_a+a[n]
    sum_b=sum_b+b[n]
print(f"La suma del arreglo 'a' es: {sum(a)}\n\n");
print(f"La suma del arreglo 'b' es: {sum(b)}\n\n");
print(f"La suma entre el arreglo 'a' y el arreglo 'b' es: {sum_a+sum_b}\n\n");
for x in range(len(b)):
    if b[x] % 2 == 0:
        continue
    else:
        print(f"La tabla de {b[x]}\n");
        for n in range(1,11):
            print(f"La tabla de multiplicacion de {b[x]} del 1 al 10 es: {b[x]*n}");
        print();