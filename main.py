import openpyxl

# PARTE 1: Crear diccionario y entrada de datos
# Crea un diccionario vacío llamado 'estudiantes'
estudiantes = {}

# Usa un ciclo for para pedir 3 nombres y notas (convierte la nota a float)
for i in range(3):  
    nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")
    try:
        # Convertimos la nota a float 
        nota = float(input(f"Ingrese la nota de {nombre}: "))
        estudiantes[nombre] = nota  # Guardamos el par nombre-nota en el diccionario
    except ValueError:
        print("Error: Por favor ingrese una nota válida (número).")
        break  
# PARTE 2: Crear archivo Excel
# Crea un nuevo libro de trabajo
libro = openpyxl.Workbook()
# Obtén la hoja activa
hoja = libro.active

# PARTE 3: Escribir encabezados
# Escribe "Estudiante" en A1 y "Clasificación" en B1
hoja["A1"] = "Estudiante"
hoja["B1"] = "Clasificación"

# PARTE 4: Escribir datos con ciclo y condicional
fila = 2  
for estudiante, nota in estudiantes.items():
    if nota > 70:  # Si la nota es mayor a 70
        clasificacion = "Bueno"
    else:
        clasificacion = "Regular"
    
    # Escribimos el nombre en la columna A y la clasificación en la columna B
    hoja[f"A{fila}"] = estudiante
    hoja[f"B{fila}"] = clasificacion
    fila += 1  # Incrementamos la fila para el siguiente estudiante

# PARTE 5: Guardar archivo
# Guarda el archivo como "ejercicio3.xlsx"
libro.save("ejercicio3.xlsx")

print("!Texto agregado¡")
