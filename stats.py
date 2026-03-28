def calcular():
    print("Selecciona operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = input("Opción: ")

    num1 = float(input("Número 1: "))
    num2 = float(input("Número 2: "))

    if opcion == "1":
        resultado = int(num1 + num2)
        operacion = "Suma"
    elif opcion == "2":
        resultado = int(num1 - num2)
        operacion = "Resta"
    elif opcion == "3":
        resultado = int(num1 * num2)
        operacion = "Multiplicación"
    elif opcion == "4":
        resultado = int(num1 / num2)
        operacion = "División"
    else:
        print("Opción inválida")
        return

    print ("Resultado:", resultado)
    return operacion, num1, num2, resultado

import pyodbc

def conectar_db():
    conexion = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"   # o tu servidor
        "DATABASE=pinga;"
        "Trusted_Connection=yes;"
    )
    return conexion

def guardar_en_db(operacion, num1, num2, resultado):
    conexion = conectar_db()
    cursor = conexion.cursor()

    query = """
    INSERT INTO Historial (operacion, num1, num2, resultado)
    VALUES (?, ?, ?, ?)
    """

    cursor.execute(query, (operacion, num1, num2, resultado))
    conexion.commit()

    cursor.close()
    conexion.close()

while True:
    datos = calcular()
    
    if datos:
        operacion, num1, num2, resultado = datos
        guardar_en_db(operacion, num1, num2, resultado)

    salir = input("¿Deseas continuar? (s/n): ")
    if salir.lower() != "s":
        break