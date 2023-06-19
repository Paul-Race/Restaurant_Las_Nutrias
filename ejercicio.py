import numpy
import time
import msvcrt
def mostrarArreglo(p_array):
    for x in range(3):
        print(f"Esta fila es para {2 * x+2} personas, fila{x+1}: ", end=" ")
        for y in range(3):
            print(p_array[x][y], end=" ")
        print(" ")
    print("\t\t\t    Columna:  1 2 3")
    time.sleep(3)

def validarCantidad(p_producto, p_stock):
    while True:
        try:
            cantidad = int(input(f"Ingrese la cantidad de {p_producto} que desea: "))
            if cantidad > 0 and cantidad <= p_stock:
                p_stock -= cantidad
                return cantidad
            else:
                print(f"ERROR! debe ingresar una cantidad de {p_producto}")
        except:
            print(f"ERROR! debe ingresar una cantidad de {p_producto}")

def calcularSubTotal(p_cantidad, p_producto):
        subtotal = p_cantidad * p_producto
        return subtotal

def validarAsiento(p_str):
    while True:
        try:
            p_str = int(input(f"Ingrese la {p_str} de la reserva: "))
            if p_str > 0 and p_str <= 3:
                return p_str
            else:
                print(f"ERROR! debe ingresar un numero de {p_str}")
        except:
            print(f"ERROR! debe ingresar un numero de {p_str}")


def MostrarMenuCarta(p_producto, p_alim1, p_alim2, p_alim3, p_lista1, p_lista2, p_lista3):
    print(f"""Menu Carta {p_producto}
            Que {p_producto} desea:
            1. {p_alim1} ${p_lista1}
            2. {p_alim2} ${p_lista2}
            3. {p_alim3} ${p_lista3}
            4. Volver al menu principal
            """)

def validarRut():
    while True:
            try:
                rut = int(input("Ingrese su rut (sin puntos ni digito verificador): "))
                if rut >= 1000000 and rut <= 99999999:
                    return rut
                else:
                    print("ERROR! Debe ingresar un rut valido(sin puntos ni digito verificador)")
            except:
                print("ERROR! Debe ingresar un rut valido(sin puntos ni digito verificador)")
array = numpy.zeros((3,3), int)
lista_ruts = []
lista_nombres = []
lista_correos = []
lista_filas = []
lista_columnas = []
lista_subtotales = []
lista_bebidas = [1200, 1500, 2000]
lista_platos = [5000, 8000, 12000]
lista_postres = [1500, 2000, 2500]
stock_bebida = 100
stock_platos = 100
stock_postre = 100

while True:
    registro_cant_beb = 0
    registro_cant_pl = 0
    registro_cant_pos = 0
    subtotal = 0
    print("""Bienvenido al Reastaurant "Las Nutrias"
1. Ver mesas disponibles
2. Reservar mesa
3. Carta (Hacer pedido)
4. Pagar
5. Cancelar Reserva
6. Salir
    """)
    while True:
        try:
            userOption = int(input("Seleccione una opcion: "))
            if userOption in(1,2,3,4,5,6):
                break
            else:
                print("ERROR! dbe ingresar una opcion valida")
        except:
            print("ERROR! debe ingresar un numero valido")
    if userOption == 1:
        mostrarArreglo(array)
    elif userOption == 2:
        if 0 not in array:
            print("Estan todas las mesas ocupadas, intentelo mas tarde")
            continue
        rut = validarRut()
        if rut in lista_ruts:
            print("Rut ya registrado")
            continue
        while True:
            nombre = input("Ingrese su nombre: ")
            if len(nombre.strip()) >= 3 and nombre.isalpha:
                break
            else:
                print("ERROR! Ingrese un nombre valido")
        while True:
            correo = input("Ingrese su correo: ")
            if "@" in(correo):
                break
            else:
                print("ERROR! Debe ingresar una opcion valida")
        while True:
            try:
                cantPersonas = int(input("¿Cuantas personas estan en la mesa?: "))
                if cantPersonas >= 1 and cantPersonas <= 6:
                    break
                else:
                    print("ERROR! Debe ingresar una cantidad de personas valida(1 a 6")
            except:
                print("ERROR! Debe ingresar una cantidad de personas valida(1 a 6")
        if cantPersonas in(5,6):
            mostrarArreglo(array)
            while True:
                try:
                    fila = validarAsiento("fila")
                    colmuna = validarAsiento("columna")
                    if fila == 3 and colmuna in(1,2,3):
                        break
                    else:
                        print("ERROR! Solo pueden sentarse en la 3ra fila")
                except:
                    print("ERROR! Solo pueden sentarse en la 3ra fila")
            array[fila-1][colmuna-1] = 1
        elif cantPersonas >= 4:
            mostrarArreglo(array)
            while True:
                try:
                    fila = validarAsiento("fila")
                    colmuna = validarAsiento("columna")
                    if fila in(2,3) and colmuna in(1,2,3):
                        break
                    else:
                        print("ERROR! Solo pueden sentarse en la 2da o 3ra fila")
                except:
                    print("ERROR! Solo pueden sentarse en la 2da o 3ra fila")
            array[fila-1][colmuna-1] = 1
        else:
            mostrarArreglo(array)
            fila = validarAsiento("fila")
            colmuna = validarAsiento("columna")
            array[fila-1][colmuna-1] = 1
        lista_filas.append(fila-1)
        lista_columnas.append(colmuna-1)
        lista_ruts.append(rut)
        lista_nombres.append(nombre)
        lista_correos.append(correo)
        lista_subtotales.append(0)
    elif userOption == 3:
        print("Primero debe registrarse")
        rut = validarRut()
        if rut not in lista_ruts:
            print("Primero debe reservar una mesa")
            continue
        posicion = lista_ruts.index(rut)
        while True:
            print("""La Carta:
            1. Bebidas (Soda, Jugo o Cerveza)
            2. Platos (Pasta Bolognesa, Lomo vetado con pure o Chorrillana)
            3. Postres (Torta tres leches, Suspiro limeño o Flan)
            4. Confirmar compra
            5. Cancelar compra
            """)
            while True:
                try:
                    userOption = int(input("Seleccione una opcion: "))
                    if userOption in(1,2,3,4,5):
                        break
                    else:
                        print("ERROR! dbe ingresar una opcion valida")
                except:
                    print("ERROR! debe ingresar un numero valido")

            if userOption == 1:
                MostrarMenuCarta("Bebidas", "Soda", "Jugos", "Cerveza", lista_bebidas[0], lista_bebidas[1], lista_bebidas[2])
                while True:
                    try:
                        userOption = int(input("Seleccione una opcion: "))
                        if userOption in(1,2,3,4):
                            break
                        else:
                            print("ERROR! dbe ingresar una opcion valida")
                    except:
                        print("ERROR! debe ingresar un numero valido")
                if userOption == 1:
                    cantidad = validarCantidad("Soda/s", stock_bebida)
                    subtotal += calcularSubTotal(cantidad, lista_bebidas[0])
                elif userOption == 2:
                    cantidad = validarCantidad("Jugo/s", stock_bebida)
                    subtotal += calcularSubTotal(cantidad, lista_bebidas[1])
                elif userOption == 3:
                    cantidad = validarCantidad("Cerveza/s", stock_bebida)
                    subtotal += calcularSubTotal(cantidad, lista_bebidas[2])
                else:
                    print("Usted volvera al menu principal")
                    print("Pulse cualquier tecla para continuar")
                    msvcrt.getch()
                    continue
                registro_cant_beb += cantidad
            elif userOption == 2:
                MostrarMenuCarta("Platos", "Pasta Bolognesa", "Lomo vetado con papas", "Chorrillana", lista_platos[0], lista_platos[1], lista_platos[2])
                while True:
                    try:
                        userOption = int(input("Seleccione una opcion: "))
                        if userOption in(1,2,3,4):
                            break
                        else:
                            print("ERROR! dbe ingresar una opcion valida")
                    except:
                        print("ERROR! debe ingresar un numero valido")
                if userOption == 1:
                    cantidad = validarCantidad("Platos", stock_platos)
                    subtotal += calcularSubTotal(cantidad, lista_platos[0])
                elif userOption == 2:
                    cantidad = validarCantidad("Platos", stock_platos)
                    subtotal += calcularSubTotal(cantidad, lista_platos[1])
                elif userOption == 3:
                    cantidad = validarCantidad("Platos", stock_platos)
                    subtotal += calcularSubTotal(cantidad, lista_platos[2])
                else:
                    print("Usted volvera al menu principal")
                    print("Pulse cualquier tecla para continuar")
                    msvcrt.getch()
                    continue
                registro_cant_pl += cantidad
            elif userOption == 3:
                MostrarMenuCarta("Postres", "Torta tres leches", "Suspiro limeño", "Flan", lista_postres[0], lista_postres[1], lista_postres[2])
                while True:
                    try:
                        userOption = int(input("Seleccione una opcion: "))
                        if userOption in(1,2,3,4):
                            break
                        else:
                            print("ERROR! dbe ingresar una opcion valida")
                    except:
                        print("ERROR! debe ingresar un numero valido")
                if userOption == 1:
                    cantidad = validarCantidad("trozos de torta", stock_postre)
                    subtotal += calcularSubTotal(cantidad, lista_postres[0])
                elif userOption == 2:
                    cantidad = validarCantidad("porciones de suspiro limeño", stock_postre)
                    subtotal += calcularSubTotal(cantidad, lista_postres[1])
                elif userOption == 3:
                    cantidad = validarCantidad("porciones de flan", stock_postre)
                    subtotal += calcularSubTotal(cantidad, lista_postres[2])
                else:
                    print("Usted volvera al menu principal")
                    print("Pulse cualquier tecla para continuar")
                    msvcrt.getch()
                    continue
                registro_cant_pos += cantidad
            elif userOption == 4:
                if lista_subtotales[posicion] == 0:
                    print("Usted aun no compra nada, volvera al menu principal")
                    continue
                else:
                    print(f"Su total a pagar es {subtotal}")
                    time.sleep(3)
                    break
            else:
                if lista_subtotales[posicion] == 0:
                    print("Usted aun no compra nada, volvera al menu principal")
                    time.sleep(3)
                    break
                else:
                    lista_subtotales[posicion] = 0
                    stock_bebida += registro_cant_beb
                    stock_platos += registro_cant_pl
                    stock_postre += registro_cant_pos
                    print("Su compra se a cancelado con exito")
                    print("Usted volvera al menu principal")
                    print("Pulse cualquier tecla para continuar")
                    msvcrt.getch()
                    break
            lista_subtotales[posicion] = subtotal
    elif userOption == 4:
        print("Primero debe registrarse")
        rut = validarRut()
        if rut not in lista_ruts:
            print("Primero debe reservar una mesa")
            continue
        posicion = lista_ruts.index(rut)
        print(f"""Su boleta 
            Subtotal   ${lista_subtotales[posicion]}
            IVA        ${lista_subtotales[posicion] * 0.19}
            Descuento  $ No tiene
            _________________________________
            Total a pagar ${lista_subtotales[posicion]}
              """)
        time.sleep(5)
        array[lista_filas[posicion]][lista_columnas[posicion]] = 0
        lista_ruts.pop(posicion)
        lista_nombres.pop(posicion)
        lista_correos.pop(posicion)
        lista_filas.pop(posicion)
        lista_columnas.pop(posicion)
        lista_subtotales.pop(posicion)
    elif userOption == 5:
        print("Primero debe registrarse")
        rut = validarRut()
        if rut not in lista_ruts:
            print("Primero debe reservar una mesa")
            continue
        posicion = lista_ruts.index(rut)
        array[lista_filas[posicion]][lista_columnas[posicion]] = 0
        lista_ruts.pop(posicion)
        lista_nombres.pop(posicion)
        lista_correos.pop(posicion)
        lista_filas.pop(posicion)
        lista_columnas.pop(posicion)
        lista_subtotales.pop(posicion)
        print("Usted a cancelado su reserva con exito")
        print("Vuelva al menú principal pulsando cualquiera de las teclas del teclado")
        msvcrt.getch()
    else:
        print("Usted saldra del programa")
        print("Pulse cualquier tecla para continuar")
        msvcrt.getch()
        break
print("Gracias, Adios")
        

