import json
import os
import sys

db = "datos_estudiantes.txt"

'''
guarda los datos del estudiante en un archivo simulando una base de datos
'''
def registrar_estudiante(dato_estudiante):
	f = open(db,"a")
	f.write(dato_estudiante + "\n")
	f.close()

'''
verifica si el rango de nota esta entre el rango mínimo y máximo, si se encuentra en 
el rango retorna la nota del estudiante, caso contrario vuelve a solicitar la nota
'''
def get_nota(minimo = 1, maximo = 10):
    while True:
        try:
            nota = float(input("Nota : "))
            if nota >= minimo and nota <= maximo :
                return nota
            print("Error :")
            print("Nota debe estar entre " + str(minimo) + " y " + str(maximo))
            print("Ingresaste ", nota)
            linea_separador("+")
        except :
            print("Error :")
            print("Ingresar Numero entre " + str(minimo) + " y " + str(maximo))
            linea_separador("+")

def print_start():
    linea_separador(c=2)
    print("\t\tBienvenido")
    print("\tCarga de Datos de Estudiantes")
    linea_separador(c=2)
    print("Elija una opción : ")
    print("1 - Insertar")
    print("2 - Consultar")
    print("3 - Nuevo Registro")
    print("4 - Mostrar Promedio de Notas Cargadas")
    print("5 - Mostrar Cantidad de Estudiantes con Notas Superiores-Inferiores al Promedio")
    print("6 - Estudiante con Mayor Nota")
    print("0 - Cerrar el Programa")
    linea_separador()
    menu_principal()

def print_end():
    linea_separador(c=2)
    print("\tPrograma Finalizado")
    linea_separador(c=2)
    exit()

def linea_separador(tl = "-", c = 1):
    if tl == "-":
        print("-----------------------------------\n" * c)
    elif tl == "=":
        print("==================================\n" * c)
    elif tl == "+":
        print("+++++++++++++++++++++++++++++\n" * c)

def pause():
    input("Enter para continuar...")

def print_menu_consultar():
    clear()
    print("Consulta de Datos de los Estudiantes")
    print("Elija una opción : ")
    print("1 - Todos")

def get_registro_estudiantes():
    datos_estudiantes = []
    f = open(db, "r")
    while True:            
        line = f.readline()
        if not line:
            break
        datos_estudiantes.append(json.loads(line))
    f.close()
    return datos_estudiantes

def clear():
    os_current = sys.platform
    if os_current=='win32':
        os.system('cls')
    elif os_current=='linux' or os_current=='linux2':
        os.system('clear')

def ingresar_datos_estudiante():
    while True:
        clear()
        print("Ingrese los Datos del Estudiante...")
        nombre = input("Nombre : ")
        apellido = input("Apellido : ")
        nota = get_nota()
        redondeo_nota = 7 if nota>=6.5 and nota<7 else int(nota)
        dato_estudiante = {
            "nombre":nombre,
            "apellido":apellido,
            "nota real": nota,
            "redondeo de nota": redondeo_nota,
            "condicion": "Aprobado" if redondeo_nota>=7 else "Reprobado" 
            }
        linea_separador("=")
        print("Estudiante : " + dato_estudiante['nombre'], dato_estudiante['apellido'])
        print("Nota Real : " + str(dato_estudiante['nota real']))
        print("Redondeo de Nota : " + str(dato_estudiante['redondeo de nota']))
        print("Materia : Ciencias de la Computación")
        print("Condición : " + dato_estudiante['condicion'])
        linea_separador("=")
        registrar_estudiante(str(json.dumps(dato_estudiante)))
        print("Finalizar Si, S, s")
        token_close = input("Finalizar programa (Si|S|s) ")
        if token_close == 'Si' or token_close == 'S' or token_close == 's':
            break
        linea_separador("=")

def mostrar_datos_estudiante(datos_estudiantes):
    for estudiante in datos_estudiantes:
        print("Nombre : ", estudiante['nombre'])
        print("Apellido : ", estudiante['apellido'])
        print("Nota Real : ", estudiante['nota real'])
        print("Redondeo de Nota : ", estudiante['redondeo de nota'])
        print("Condición : ", estudiante['condicion'])
        linea_separador()
    datos_estudiantes.clear()
    linea_separador("=", 2)
    pause()

def do_new_register():
    f = open(db, "w")
    f.write("")
    f.close()

def new_register():
    clear()
    print("Se eliminara el registro actual")
    print("Elija una opción :")
    print("1 - Nuevo Registro")
    print("0 - Cancelar")
    token_opcion = get_opcion_number(1,1)
    if token_opcion == 1:
        do_new_register()
    elif token_opcion == 0:
        pass

def get_promedio_notas():
    datos_estudiantes = get_registro_estudiantes()
    promedio_nota_real = 0
    total_estudiantes = len(datos_estudiantes)
    for estudiante in datos_estudiantes:
        promedio_nota_real = promedio_nota_real + estudiante['nota real']
    return promedio_nota_real/total_estudiantes

def print_promedio_notas():
    clear()
    print("Promedio de Notas:")
    linea_separador()
    print("Promedio Nota Real : ", (round(get_promedio_notas(),2)))
    linea_separador("=", 2)
    pause()

def get_estudiantes_promedio_mayor_menor():
    datos_estudiantes = get_registro_estudiantes()
    promedio_mayor = 0
    promedio_menor = 0
    promedio = get_promedio_notas()
    for estudiante in datos_estudiantes:
        if promedio > estudiante['nota real']:
            promedio_mayor = promedio_mayor + 1
        elif promedio < estudiante['nota real']:
            promedio_menor = promedio_menor + 1
    return {'promedio mayor':promedio_mayor,'promedio menor':promedio_menor}
    
def print_estudiantes_promedio_mayor_menor():
    clear()
    print("Cantidad de Estudiantes con Notas Mayores y Menores al Promedio:")
    linea_separador()
    promedio_mayor_menor = get_estudiantes_promedio_mayor_menor()
    print("Superiores al Promedio :", promedio_mayor_menor['promedio mayor'])
    print("Inferiores al Promedio :", promedio_mayor_menor['promedio menor'])
    linea_separador("=", 2)
    pause()

def get_estudiante_con_mayor_nota():
    datos_estudiantes = get_registro_estudiantes()
    nota_mayor = 0
    estudiante_nota_mayor = {}
    is_array_objcet = False
    for estudiante in datos_estudiantes:
        if nota_mayor<estudiante['nota real']:
            nota_mayor = estudiante['nota real']
            estudiante_nota_mayor = estudiante
            is_array_objcet = False
        elif nota_mayor==estudiante['nota real']:
            if is_array_objcet:
                estudiante_nota_mayor.append(estudiante)
            else:
                aux_estudiante_nota_mayor = estudiante_nota_mayor
                estudiante_nota_mayor = []
                estudiante_nota_mayor.append(aux_estudiante_nota_mayor)
                estudiante_nota_mayor.append(estudiante)
                del aux_estudiante_nota_mayor
            is_array_objcet = True
    type_data =  0 if is_array_objcet else 1
    return {"type":type_data, "data":estudiante_nota_mayor}

def print_estudiante_con_mayor_nota():
    print("Estudiante con Mayor Nota :")
    linea_separador()
    estudiante = get_estudiante_con_mayor_nota()
    if estudiante['type']==0:
        print("Los Estudiantes con mejores notas son :")
        for data in estudiante['data']:
            print_estudiante_mayor_nota(data['nombre'] + " " + data['apellido'], data['nota real'], True)
    else:
        data = estudiante['data']
        print_estudiante_mayor_nota(data['nombre'] + " " + data['apellido'], data['nota real'])
    linea_separador("=", 2)
    pause()

def print_estudiante_mayor_nota(nombre, nota, mas_de_uno = False):
    if mas_de_uno:
        print(nombre + " con nota : " + str(nota))
    else:
        print(nombre + " es el/la mejor estudiante que consiguió la nota más alta : " + str(nota))

def menu_principal():    
    token_opcion = get_opcion_number(1, 6)
    if token_opcion == 1:
        clear()
        ingresar_datos_estudiante()
    elif token_opcion == 2:
        menu_consultar()
    elif token_opcion == 3:
        new_register()
    elif token_opcion == 4:
        print_promedio_notas()
    elif token_opcion == 5:
        print_estudiantes_promedio_mayor_menor()
    elif token_opcion == 6:
        print_estudiante_con_mayor_nota()
    elif token_opcion == 0:
        clear()
        print_end()

def menu_consultar():
    while True:
        clear()
        print_menu_consultar()
        token_opcion = get_opcion_number(1,1)
        if token_opcion == 1:
            todos_datos_estudiantes()
            break
        elif token_opcion == 0:
            break

def todos_datos_estudiantes():
    clear()
    print("Datos de Estudiantes")
    linea_separador()
    datos_estudiantes = get_registro_estudiantes()
    mostrar_datos_estudiante(datos_estudiantes)

def get_opcion_number(minimo, maximo, close = 0):
    while True:
        try:
            token_opcion = int(input("Ingrese una opción : "))
            if token_opcion>=minimo and token_opcion<=maximo or token_opcion==close:
                return token_opcion 
        except:
            print("Debes ingresar un numero entre " + str(minimo) + " y " + str(maximo))

def init():
    while True:
        clear()
        print_start()


if "__main__"==__name__:
    init()