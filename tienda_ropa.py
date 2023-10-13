
op=0
opm=0
ope=0
opei=0
nombre=0
total=0
while op==0:
    print("Bienvenido a nuestra tienda")
    print("1.Agregar prenda/prendas")
    print("2.Finalizar compra")
    print("3.Salir")
    opm=int(input("Seleccione una opcion"))
    if opm==1:
        print("1.Camiseta  $ 2500")
        print("2.Pantalon  $ 5000")
        print("3.Chaqueta  $ 8000")
        print("4.Salir")
        ope=int(input("Ingrese que va a comprar"))
        while opei==0:
            if ope==1:
                c=int(input("¿Cuantas camisetas llevara?"))
                precioC=2500
                precioCF=precioC*c
                print(f"Usted lleva {c} camisetas")
            if ope==2:
                p=int(input("¿Cuantos pantalones llevara?"))
                precioP=5000
                precioPF=precioP*p
                print(f"Usted lleva {p} pantalones")
            if ope==3:
                ch=int(input("¿Cuantas chaquetas llevara?"))
                precioCH=8000
                precioCHF=precioCH*ch
                print(f"Usted lleva {ch} chaquetas")
            else:
                opei=1
                opm=0
                total=precioCF+precioCHF+precioPF
    if opm==2:
        nombre=str(input("Ingrese su nombre"))
        print("======= Factura Tienda de Ropa =======")
        print(f"{c}  Camisetas  x {precioC}  = {precioCF} ")
        print(f"{p}  Pantalones x {precioP}  = {precioPF} ")
        print(f"{ch} Chaquetas  x {precioCH} = {precioCHF}")
        print("---------------------------------------")
        print(f"Total: ${total}")
        print(f"Gracias por su compra {nombre}")
    if opm==3:
        op=1
        print("Hasta pronto")
    else:
        op=0
        print("Seleccione una opcion valida")