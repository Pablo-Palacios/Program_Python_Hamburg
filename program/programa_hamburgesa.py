import sys

import os

import time

import sqlite3

conn = sqlite3.connect("comercio_hambur.sqlite3")
cursor = conn.cursor()



# BASE DE DATOS Y TABLAS 



# TABLA DE VENTAS 
"""""
try:
    cursor.execute("CREATE TABLE ventas (ID  PRIMARY KEY INT, ENCARGADO TEXT, fechas FECHA, ComboS INT, ComboD INT, ComboT INT, ComboMC INT, TOTAL REAL)") 
    conn.commit()
    conn.close()
except sqlite3.OperationalError:
    print("tabla de ventas ya creada")

# TABLA DE REGISTROS 
try:
    cursor.execute("CREATE TABLE registros (ID PRIMARY KEY INT, ENCARGADO TEXT, fechas FECHA, EVENTOS TEXT, CAJA REAL)")
    conn.commit()
    conn.close()
except sqlite3.OperationalError:
    print("tabla de registro ya creada")
"""


#FUNCIONES
fecha = time.asctime


def contador():
    global suma_a
    suma_a=id+1

def nombre_encargados(nombre):
    nombre = sys.argv 


def sumar_precios(a, b, c, d):
    total = a + b + c + d 
    total = int(total)

    return total


def resto_vuelto(abono, total):
    vuelto = abono - total
    vuelto = int(vuelto)

    return vuelto


def cantidad_total(cantidad, precio):
    total = cantidad * precio
    total = int(total)

    return total


def tabla_ventas(cliente,fecha,comboS,comboD,comboT,comboMC,total):


    import sqlite3

    conn = sqlite3.connect("comercio_hambur.sqlite3")
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO ventas VALUES(null,?,?,?,?,?,?,?)", (cliente,fecha,comboS,comboD,comboT,comboMC,total))
       
    except sqlite3.OperationalError:
        cursor.execute("""CREATE TABLE ventas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente TEXT,
            fecha TEXT,
            ComboS INT,
            ComboD INT,
            ComboT INT,
            Flurby INT,
            tota REAL)""") 
            

        cursor.execute("INSERT INTO ventas VALUES(null,?,?,?,?,?,?,?)", (cliente,fecha,comboS,comboD,comboT,comboMC,total))

    print("se cargaron las ventas")
    
        
    conn.commit()
    conn.close()



def tabla_registros(data):
    datosIN = (data["nombre"], data["ingreso"], "IN", 0)
    datosOUT = (data["nombre"], data["egreso"], "OUT", data["facturado"])

    import sqlite3

    conn = sqlite3.connect("comercio_hambur.sqlite3")
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO registros VALUES(null,?,?,?,?)", datosIN)
        cursor.execute("INSERT INTO registros VALUES(null,?,?,?,?)", datosOUT)
    except sqlite3.OperationalError:
        cursor.execute("""CREATE TABLE registros (id INTEGER PRIMARY KEY AUTOINCREMENT,
            encargado TEXT,
            fecha TEXT,
            evento TEXT,
            caja REAL)""")
        
        cursor.execute("INSERT INTO registros VALUES(null,?,?,?,?)", datosIN)
        cursor.execute("INSERT INTO registros VALUES(null,?,?,?,?)", datosOUT)

    print("se cargaron los registros")

    conn.commit()
    conn.close()






##########################################################################

#SISTEMA PARA BORRAR EL PROGRAMA 
if os.name == "nt":
    borrar = "cls"

os.system(borrar)

#########################################################################



#INGRESO 


while True:
    datosEncargado = {"nombre":"","ingreso":"","egreso":"","facturado":0}

    print("Bienvenido a Hamburguesas IT")
    encargado = input("Ingrese su nombre encargad@: ")

    datosEncargado["nombre"] = encargado

    datosEncargado["ingreso"] = time.asctime()

    tabla_registros(datosEncargado)


   
    break
os.system(borrar)

###########################################################################

#MENU DE COMPRA Y VENTA 


        
while True:


    caja = 0


    print("Hamburguesas IT")

    print("Encargad@ -> ",(encargado))

    print(" ")

    print("Recuerda, siempre hay que recibir al")
    print("cliente con una sonrisa :)")

    print(" ")

    print("1. Ingreso nuevo pedido")

    print("2. Cambio de turno")

    print("3. Apagar sistema")

    print(" ")
    


    opcion = input(">>>")

    if opcion == "1":
        cliente = input("Ingrese nombre del cliente: ")
        print("")
        combo_s = int(input("Ingrese cantidad Combo S: "))
        print("")
        combo_d = int(input("Ingrese cantidad Combo D: "))
        print("")
        combo_t = int(input("Ingrese cantidad Combo T: "))
        print("")
        combo_mc = int(input("Ingrese cantidad Combo MC: "))

#PRECIO DE LOS COMBOS
        precio_S = 5 
        precio_d = 6
        precio_t = 7
        precio_mc = 2

#SUMA DE LA CANTIDAD DEL CLIENTE CON EL PRECIO DEL COMBO

        cantidad_S = cantidad_total(combo_s, precio_S)

        cantidad_D = cantidad_total(combo_d, precio_d)

        cantidad_T = cantidad_total(combo_t, precio_t)

        cantidad_MC = cantidad_total(combo_mc, precio_mc)


#CAJA 

        total_real = sumar_precios(cantidad_S, cantidad_D, cantidad_T, cantidad_MC)
        print(" ")
       
        print("TOTAL: $",total_real)
        print(" ")

        abona = int(input("Con cuanto abona el cliente: "))
        print(" ")
        vuelto = resto_vuelto(abona, total_real)
        
        print("TOTAL: $",total_real)
        print("usted abono con: ",abona)
        print("Su vuelto: ",vuelto)
        print(" ")


        confirma = input("¿Confirma pedido? si / no : ")

        caja_total = caja + total_real
        fecha = time.asctime()

        if confirma == "si":
           caja += total_real
     
           tabla_ventas(cliente,fecha,combo_s,combo_d,combo_t,combo_mc,total_real)
        else:
            print("no se han cargado")

        print("\n\n")
        input("Toque ENTER para continuar...")

        

#cambio de encargado / turno

    elif opcion == "2":

        datosEncargado["egreso"] = time.asctime()
        datosEncargado["facturado"] = total_real

        tabla_registros(datosEncargado)
        
        
        import os
        while True:
            print("Bienvenido a Hamburguesas IT")
            encargado = input("Ingrese su nombre encargad@: ")

            

            break
        os.system(borrar)
        encargado = encargado

#salir del programa

    else:
        datosEncargado["egreso"] = time.asctime()
        datosEncargado["facturado"] = caja_total
        tabla_registros(datosEncargado)
        print("gracias por usar el programa!!")

        break 
    























