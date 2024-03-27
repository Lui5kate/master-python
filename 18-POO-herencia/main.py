import clases

persona = clases.Persona()
persona.setNombre("Luis")
persona.setApellidos("Lira")
persona.setAltura("190cm")
persona.setEdad("800 años")

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())

print("----------")

informatico = clases.Informatico()
informatico.setNombre("Carlos")
informatico.setApellidos("Martinez")

print(f"El informatico es: {informatico.getNombre()} {informatico.getApellidos()}")
print(informatico.getLenguajes())
print(informatico.caminar())
print(informatico.experiencia)

print("----------")

tecnico = clases.TecnicoRedes()
tecnico.setNombre("Luis")
print(tecnico.auditarRedes, tecnico.getNombre(), tecnico.getLenguajes())