nom=input("Ingrese su nombre: ");
print("");
nom_list=[nom];
x=range(2);
cont_a_vocal=0;
cont_a_consonante=0;
cont_b_vocal=0;
cont_b_consonante=0;
cont_c_vocal=0;
cont_c_consonante=0;
for n in x:
    no1=input("Ingrese su nombre: ");
    print("");
    nom_list.append(no1);
print(nom_list);
a=nom_list.pop(0);
c=nom_list.pop(1);
b=nom_list.pop(-1);
print(a);
for caracter in a:
    if caracter == 'A' or caracter == 'a' or caracter == 'E' or caracter == 'e' or caracter == 'I' or caracter == 'i' or caracter == 'O' or caracter == 'o' or caracter == 'U' or caracter == 'u':
        cont_a_vocal=cont_a_vocal+1;
    else:
        cont_a_consonante=cont_a_consonante+1
sum_a=cont_a_vocal+cont_a_consonante;
print(sum_a)
print(b);
for caracter in b:
    if caracter == 'A' or caracter == 'a' or caracter == 'E' or caracter == 'e' or caracter == 'I' or caracter == 'i' or caracter == 'O' or caracter == 'o' or caracter == 'U' or caracter == 'u':
        cont_b_vocal=cont_b_vocal+1;
    else:
        cont_b_consonante=cont_b_consonante+1
sum_b=cont_b_vocal+cont_b_consonante;
print(sum_b)
print(c);
for caracter in c:
    if caracter == 'A' or caracter == 'a' or caracter == 'E' or caracter == 'e' or caracter == 'I' or caracter == 'i' or caracter == 'O' or caracter == 'o' or caracter == 'U' or caracter == 'u':
        cont_c_vocal=cont_c_vocal+1;
    else:
        cont_c_consonante=cont_c_consonante+1
sum_c=cont_c_vocal+cont_c_consonante;
print(sum_c)
if sum_a > sum_b and sum_a > sum_c:
    print(f"El nombre {a} tiene la mayor cantidad de caracteres de los 3 nombres ingresados.");
elif sum_b > sum_a and sum_b > sum_c:
    print(f"El nombre {b} tiene la mayor cantidad de caracteres de los 3 nombres ingresados.");
elif sum_c > sum_a and sum_c > sum_b:
    print(f"El nombre {c} tiene la mayor cantidad de caracteres de los 3 nombres ingresados.");