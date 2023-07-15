from re import M
import numpy as np
def comprobacion(a):
    i=2;
    t=2;
    r=0;
    print(a)
    for x in range(len(a)):
        if i == 7:
            if t == 4:
                resultado=int(r/11);
                resultado*11
                l=r-resultado
                u=11-l
                if u >= 0 and u <= 9:
                    k=int(dv_rut);
                    if u == k:
                        return print(f"El digito verificador de su rut coincide con el sistema:\t{rut} {dv_rut}\n");
                    else:
                        return print(f"El digito verificador de su rut no coincide con el sistema, ingreselo correctamente\n");
                elif u == 10:
                    if dv_rut == 'k' or dv_rut == 'K':
                        return print(f"El digito verificador de su rut coincide con el sistema:\t{rut} {dv_rut}\n");
                    else:
                        return print(f"El digito verificador de su rut no coincide con el sistema, ingreselo correctamente\n");
                elif u >= 11:
                    k=int(dv_rut);
                    if u == dv_rut:
                        return print(f"El digito verificador de su rut coincide con el sistema:\t{rut} {dv_rut}\n");
                    else:
                        return print(f"El digito verificador de su rut no coincide con el sistema, ingreselo correctamente\n");
                else:
                    return print(f"El rut ingresado y su digito verificador:\t{rut} {dv_rut} no es valido en el sistema, ingreselo correctamente\n");
            else:
                r=r+a[x]*t;
                t+=1;
        else:
            r=r+a[x]*i
            print(r)
            i+=1;
while True:
    try:
        rut=int(input("Ingrese su rut:\t"));
        dv_rut=input("Ingrese su digito verificador:\t");
        print();
        if rut >= 1000000 and rut <= 99999999:
            a=str(rut)
            tru=[];
            for x in range(len(a)):
                n=int(a);
                tru.append(n[x]);
            tru.reverse();
            print(comprobacion(tru));
        else:
            print(f"El rut ingresado:\t{rut} no es valido en el sistema, intentelo nuevamente\n");
    except ValueError:
        print("\nSolo digite números y caracteres\n");