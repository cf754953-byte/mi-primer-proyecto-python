# Practica 5: Asistente de Evaluacion Fisica
# Introducir los decimales con punto, por ejemplo: 62.5.

print("ASISTENTE DE EVALUACIÓN FÍSICA")

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
peso = float(input("Ingresa tu peso en kg: "))
horas_ejercicio = float(input("Horas de ejercicio a la semana: "))

calorias_semanales = horas_ejercicio * 350

if edad < 18:
    categoria = "Categoría: Juvenil"
else:
    categoria = "Categoría: Adulto"

if horas_ejercicio >= 3:
    estado = "Estado: Físicamente Activo"
else:
    estado = "Estado: Requiere mayor actividad física"

print("\nRESUMEN DE LA EVALUACIÓN")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Peso: {peso:.2f} kg")
print(f"Ejercicio semanal: {horas_ejercicio:.2f} horas")
print(f"Calorías quemadas estimadas por semana: {calorias_semanales:.2f} kcal")
print(f"{categoria}")
print(f"{estado}")
