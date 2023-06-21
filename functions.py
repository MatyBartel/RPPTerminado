import os
os.system("cls")
import json

def menu():
    os.system("cls")
    try:
        print("════════════════════════════════════════   MENU   ════════════════════════════════════════")
        print("")
        print("1-  Cargar datos del archivo (obligatorio)")
        print("2-  Mostrar marcas y insumos de cada una")
        print("3-  Mostrar para cada marca el nombre y el precio de los insumos")
        print("4-  Buscar por caracteristica")
        print("5-  Mostrar productos ordenados por marcas de forma ascendente")
        print("6-  Realizar Compras")
        print("7-  Guardar en JSON")
        print("8-  Leer desde JSON")
        print("9-  Actualizar Precios en 8.4%")
        print("10- Salir")
        print("════════════════════════════════════════ EXTRA ════════════════════════════════════════")
        print("11- Agregar producto")
        print("12- Generar archivo .csv o .json con los productos agregados")

        
        opcion=int(input("Ingrese una opcion:"))
        return opcion

    except ValueError:
        print("----------------OPCION INVALIDA--------------------")
        os.system("pause")
        os.system("cls")

def cargar_archivo(nombre_archivo)->list:
    """
    Function: 
        Ingresa direccion del archivo a cargar, por ejemplo: 'carpeta//ejemplo.csv'.

    Args:
        nombre_archivo (str): Archivo a cargar

    Returns:
        Se carga el archivo en formato de lista de diccionarios y los muestra.
    """
    os.system("cls")
    separador = ","


    with open(nombre_archivo, encoding="utf-8") as archivo:
        lista_diccionario = []
        for linea in archivo:
            linea = linea.strip("\n").replace("$", "")                                  # Saco el salto de linea y elimino $
            columnas = linea.split(separador)                                           # Separo con , los datos

            id, nombre, marca, precio, caracteristica = columnas                        # Asigno las columnas

            diccionarios = {
                "id": id,
                "nombre": nombre,
                "marca": marca,                                                         # Creo los diccionarios
                "precio": precio,
                "caracteristica": caracteristica
            }                                           

            lista_diccionario.append(diccionarios)                                      # Los agrego a la lista_diccionario

        print("═══════════════════════════════════════════════════════════════════════ DATOS DEL ARCHIVO ═══════════════════════════════════════════════════════════════════════")
        for diccionario in lista_diccionario:
            print(diccionario)                                                          # Muestro con un espacio entre cada diccionario
            print() 

        os.system("pause")
        os.system("cls")

        return lista_diccionario

def contar_en_lista(lista_dic:list,key:str)->dict:
    """
    Function: Recibe una lista de diccionarios y una clave, agrega esos valores de la clave a una lista y luego recorre la lista agregandolos a un diccionario, si ya estaban, cuenta.
    Por ultimo muestra de forma prolija los valores con su contador de veces que estan.

    Args:
        lista_dic (list): Lista que recibe
        key (str): Clave que usara sus valores para contarlos
    
    Returns:
        diccionario (dict): Diccionario con los valores sin repetir y contados.

    """
    lista_aux=[]
    diccionario = {}

    for clave in lista_dic:                    # Agrego a una lista las claves
        lista_aux.append(clave[key])
    for elemento in lista_aux:
        if elemento in diccionario:
            diccionario[elemento] += 1         # Si el elemento ya existe en el diccionario, los voy contando.
        else:
            diccionario[elemento] = 1
    print()
    print("MARCAS DISPONIBLES Y CANTIDAD DE INSUMOS:")
    for elemento in diccionario:               # Muestro de forma prolija
        cantidad = diccionario[elemento]
        print(f"{elemento}: {cantidad}")

    os.system("pause")
    os.system("cls")
    return diccionario

def mostrar_tres_claves(lista_dic:list,key:str,key_2:str,key_3:str)->list:
    """
    Function: Recibe una lista de diccionarios y tres claves,termina reduciendo la lista original agregando las claves con diccionarios a una nueva lista.

    Args:
        lista_dic (list): Lista de diccionarios que recibe
        key (_type_): Clave nro 1
        key_2 (_type_): Clave nro 2
        key_3 (_type_): Clave nro 3

    Returns:
        lista_reducida (list): Lista de diccionarios reducida a tres diccionarios
    """
    diccionario={}
    lista_reducida=[]
    for clave in lista_dic:
        diccionario = {
                "marca": clave[key],
                "nombre": clave[key_2],
                "precio": clave[key_3],                                            # Creo los diccionarios
            } 
        lista_reducida.append(diccionario)
    print("═══════════════════════════════════════════════════════════════════════ CLAVES - VALORES ═══════════════════════════════════════════════════════════════════════")
    for diccionario in lista_reducida:
        print(diccionario)                                             # Muestro con un espacio entre cada diccionario
        print() 

    os.system("pause")
    os.system("cls")
    return lista_reducida

def buscar_por_caracteristica(lista_diccionarios,caracteristica_ingresada)->list:
    """
    Function: Busca por la caracteristica ingresada y muestra los diccionarios que coincidan

    Args:
        lista_diccionarios (list): Lista que recibe
        caracteristica_ingresada (str): Caracteristica que buscara coincidencias
    
    Returns:
        lista_diccionarios (dict): Lista que tiene los diccionarios que coinciden con la caracteristica

    """
    lista_caracteristica = []
    for diccionario in lista_diccionarios:
        for valor in diccionario.values():
            if caracteristica_ingresada in valor:
                lista_caracteristica.append(diccionario)
    print("═══════════════════════════════════════════════════════════════════════ FILTRADO CARACTERISTICA ═══════════════════════════════════════════════════════════════════════")
    for diccionario in lista_caracteristica:
        print(diccionario)                                             # Muestro con un espacio entre cada diccionario
        print() 
    os.system("pause")
    os.system("cls")
    return lista_caracteristica

def ordenar_lista(lista_diccionarios: list, clave_principal: str, clave_auxiliar: str):
    """
    Function: Ordena la lista segun el abecedario de forma ascendente segun la clave que pongas.

    Args:
        lista_diccionarios (list): Lista que toma de base.
        clave (str): Clave que comparara y ordenara de forma ascendente.

    Returns:
        lista_diccionarios: Lista ordenada de forma ascendente.
    """

    tam = len(lista_diccionarios)
    
    for i in range(tam - 1):
        for j in range(0, tam): 
            if lista_diccionarios[i][clave_principal] < lista_diccionarios[j][clave_principal] or (lista_diccionarios[i][clave_principal] == lista_diccionarios[j][clave_principal] and lista_diccionarios[i][clave_auxiliar] > lista_diccionarios[j][clave_auxiliar]):
                aux=None
                aux=lista_diccionarios[i]
                lista_diccionarios[i]=lista_diccionarios[j]
                lista_diccionarios[j]= aux

    print("═══════════════════════════════════════════════════════════════════════ DATOS ORDENADOS ═══════════════════════════════════════════════════════════════════════")
    for diccionario in lista_diccionarios:
        print(diccionario)  # Muestro con un espacio entre cada diccionario
        print() 
    
    os.system("pause")
    os.system("cls")
    
    return lista_diccionarios

def seguir_salir():
    """
    Function: 
        Nos pregunta si deseamos continuar o finalizar un programa
    Returns:
        Nos retorna una respuesta, si es "S" continua, si no, finaliza el programa
    """
    continuar_salir=input("Desea continuar? s/n: ")
    while continuar_salir != "s" and continuar_salir != "n":
        continuar_salir=input("ERROR, desea continuar? s/n: ")
    if continuar_salir =="n":
        quit("----------------------------FIN DEL PROGRAMA-------------------------------")

def comprar(lista_diccionarios:list):
    lista_caracteristica = []
    while lista_caracteristica == []:
        marca_elegida = input("Ingrese marca:").lower()
        for diccionario in lista_diccionarios:
            diccionario["marca"] = diccionario["marca"].lower()
            if marca_elegida in diccionario.values():
                lista_caracteristica.append(diccionario)
        if lista_caracteristica == []:
            print("La marca \"",marca_elegida,"\" no esta disponible, reintente.")
            print()
        else:
            print("PRODUCTOS DISPONIBLES:")
            print()
            for diccionario_marca in lista_caracteristica:
                print(diccionario_marca)
                print()
            break
    
    carrito = []
    
    while True:
        producto_id = input("Ingrese el ID del producto que desea comprar (0 para finalizar): ")
        if producto_id == "0":
            if carrito == []: 
                print("El carrito está vacío. Por favor, seleccione al menos un producto.")
                continue
            else:
                break
        
        cantidad = int(input("Ingrese la cantidad: "))
        
        producto_seleccionado = None
        for diccionario in lista_caracteristica:
            if producto_id == diccionario['id']:
                producto_seleccionado = diccionario
                break
        
        if producto_seleccionado != None:
            producto_seleccionado['cantidad'] = cantidad
            carrito.append(producto_seleccionado)
            print("Producto agregado al carrito.")
        else:
            print("ID de producto inválido. Intente nuevamente.")
        print()
        respuesta = input("¿Desea elegir otro producto? (s/n): ")
        if respuesta.lower() != "s":
            break

    print("════════════ CARRITO:")
    for producto in carrito:
        print(producto)
    
    os.system("pause")
    os.system("cls")
    return carrito

def generar_archivo_txt(carrito, nombre_archivo:str):
    try:
        with open(nombre_archivo, 'w') as archivo:
            total = 0.0 
            
            for producto in carrito:
                archivo.write(str(producto) + '\n')
                precio = float(producto['precio'])
                cantidad = int(producto['cantidad'])
                total += precio * cantidad              # Calcular el total
                
            archivo.write(f"Total: ${total}\n")         # Escribir el total en el archivo
            
        print(f"El archivo {nombre_archivo} se ha generado correctamente.")
        os.system("pause")
        os.system("cls")
    except IOError:
        print("Se produjo un error al generar el archivo.")
        os.system("pause")
        os.system("cls")

def guardar_JSON(lista_de_productos,path):
    lista_filtrada=[]
    for producto in lista_de_productos:
        if ("Alimento" in producto['nombre']):
            lista_filtrada.append(producto)
    with open (path,"w") as file:
        json.dump(lista_filtrada,file,indent=4)

def leer_JSON(path):
    lista_leida=[]
    with open(path) as file:
        lista_leida=json.load(file)
    print("-ARCHIVO LEIDO-")
    for diccionario in lista_leida:
        print(diccionario)
        print()
    return lista_leida

def aplicar_aumento(diccionario):
    precio = float(diccionario["precio"]) 
    aumento = precio * 0.084
    precio_con_aumento = precio + aumento
    diccionario["precio"] = precio_con_aumento
    return diccionario

def guardar_csv(lista_aumentada,direccion_archivo_nuevo):
    with open(direccion_archivo_nuevo,"w",encoding="utf-8") as file:
        renglon = 0
        for i in lista_aumentada:
            linea= f'{i["id"]},{i["nombre"]},{i["marca"]},${i["precio"]},{i["caracteristica"]}'
            file.writelines("\n")
            file.writelines(linea)
            renglon+=1
        print("Datos guardados en el archivo CSV correctamente.")
    os.system("pause")
    os.system("cls")

def obtener_marcas():
    marcas = []
    with open("C:\\Users\\Matias\\Desktop\\TODO\\PARCIAL TP\\marcas.txt", "r") as archivo:
        for linea in archivo:
            marca = linea.strip()
            marcas.append(marca)
    
    return marcas

marcas_disponibles = obtener_marcas()

def agregar_producto(lista_diccionarios:list):
    """
    Function: Agregar un producto a la lista anterior, se valida id y caracteristica.

    Args:
        lista_diccionarios (list): Lista anterior

    Returns:
        lista_diccionarios: Nueva lista con el producto agregado o no, dependiendo de si el id se repite.
    """
    nuevo_diccionario = {}

    for diccionario in lista_diccionarios:
        ultimo_id = int(diccionario["id"])                          # ID
    id_nuevo_producto = ultimo_id+1

    nombre = input("Ingrese nombre del producto:")                     # NOMBRE

    print()
    print("-----Marcas disponibles----")
    for marca in marcas_disponibles:
        print("-", marca)
    while True:                                                        # MARCA
        marca = input("Ingrese la marca: ")
        if marca in marcas_disponibles:
            break
        else:
            print("Marca inválida. Intente nuevamente.")

    precio = input("Ingrese precio del producto:")                    # PRECIO

    caracteristica = "Característica predefinida"
    while caracteristica == "Caracteristica predefinida" or len(caracteristica) > 3:
        caracteristica = input("Ingrese las características (separadas por comas): ").split(",")
        
        if caracteristica == "Característica predefinida" or len(caracteristica) > 3:
            print("Debe ingresar entre 1 y 3 características.")       # CARACTERISTICA
        else:
            break

    for diccionario in lista_diccionarios:
        valores_diccionario = list(diccionario.values())
        if id_nuevo_producto in valores_diccionario :
            print("Al menos uno de los valores ya existe en los diccionarios anteriores.")
            return lista_diccionarios

    nuevo_diccionario['id'] = id_nuevo_producto
    nuevo_diccionario['nombre'] = nombre
    nuevo_diccionario['marca'] = marca
    nuevo_diccionario['precio'] = precio
    nuevo_diccionario['caracteristica'] = caracteristica
    

    lista_diccionarios.append(nuevo_diccionario)
    return lista_diccionarios

def guardar_json_csv(lista:list,direccion_archivo_nuevo,guardar_json_o_csv:str):
    """
    Function: Recibe una lista que la transformara en json o csv segun el usuario ingrese, guardara en el segundo parametro el archivo.

    Args:
        lista (list): Lista a transformar
        direccion_archivo_nuevo (path): Donde se guardara, Indicar .csv o .json al final
        guardar_json (True): JSON por defecto

    Returns:
        Archivo nuevo.
    """
    if guardar_json_o_csv == "json":
        lista_json=[]
        for producto in lista:
            lista_json.append(producto)
        with open (direccion_archivo_nuevo,"w") as file:
            json.dump(lista_json,file,indent=4)
    else:
        with open(direccion_archivo_nuevo,"w",encoding="utf-8") as file:
            renglon = 0
            for i in lista:
                linea= f'{i["id"]},{i["nombre"]},{i["marca"]},${i["precio"]},{i["caracteristica"]}'
                file.writelines("\n")
                file.writelines(linea)
                renglon+=1

    print("Datos guardados en el archivo correctamente.")
    os.system("pause")
    os.system("cls")

def mostrar_diccionarios(lista):
    for diccionario in lista:
        print (diccionario)
        print()