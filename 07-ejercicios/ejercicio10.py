"""
Ejercicio 10. El programa tiene que pedir la nota de 15 alumnos 
y sacar por pantalla cuantos han aporbado y cuantos han reprobado.
"""
alumno = 1
aprobados = 0
reprobados = 0
while alumno <= 15:
    nota = int(input("que nota sacó el alumno " + str(alumno) + ":"))
    if nota >= 6:
        print("Este alumno pasó")
        aprobados +=1
    elif nota <= 5:
        print("Este alumno no pasó")
        reprobados +=1

    alumno += 1

print(f"\nAprobados: {aprobados}")
print(f"\nReprobados: {reprobados}")