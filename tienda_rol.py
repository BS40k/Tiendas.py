
op=0
c=0
d=0
e=0
nombre=0
precioCF=0
precioDF=0
precioEF=0
opm=0
while opm==0:
    print("Seleccione que juego comprara")
    print("1.Catan             $29.990")
    print("2.Dixit             $19.990")
    print("3.Explodint kitens  $19.990")
    print("4.finalizar compra")
    print("5.Salir")
    op=int(input("ingrese su opcion"))
    if op==1:
        c=c+1
        precioC=29990
        precioCF=precioC*d
        print(f"Usted compro {c} catan")
    if op==2:
        d=d+1
        precioD=19990
        precioDF=precioD*d
        print(f"usted compro {d} dixit")
    if op==3:
        e=e+1
        precioE=19990
        precioEF=precioE*e
        print(f"usted compro {e} Explodint kittens")
    if op==4:
        nombre=str(input("ingrese su nombre"))
        print(f"{nombre}")
        print(f"{c} Catan               ${precioCF}")
        print(f"{d} Dixit               ${precioDF}")
        print(f"{e} Explodint kittens   ${precioEF}")
    else:
        opm=1
        c=0
        d=0
        e=0
        op=0
        nombre=0
        precioCF=0
        precioDF=0
        precioEF=0
        print("Gracias por comprar con nosotros")