import os


CARGOS = {
    "CEO": {"salud": 0.07, "AFP": 0.12},
    "Desarrollador": {"salud": 0.07, "AFP": 0.12},
    "Analista de datos": {"salud": 0.07, "AFP": 0.12}
}


trabajadores = []

def registrar_trabajador():
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    cargo = input("Ingrese el cargo (CEO, Desarrollado, Analista de datos): ")
    sueldo_bruto = float(input("Ingrese el sueldo bruto: "))
    
    if cargo in CARGOS:
        descuento_salud = sueldo_bruto * CARGOS[cargo]["salud"]
        desc_afp = sueldo_bruto * CARGOS[cargo]["AFP"]
        liquido_pagar = sueldo_bruto - (descuento_salud + desc_afp)
        
        trabajador = {
            "nombre": nombre,
            "apellido": apellido,
            "cargo": cargo,
            "sueldo_bruto": sueldo_bruto,
            "desc_salud": descuento_salud,
            "desc_afp": desc_afp,
            "liquido_pagar": liquido_pagar
        }
        
        trabajadores.append(trabajador)
        print(f"Trabajador {nombre} {apellido} registrado exitosamente.\n")
    else:
        print("Cargo no válido.\n")

def listar_trabajadores():
    if trabajadores:
        for trabajador in trabajadores:
            print(f"{trabajador['nombre']} {trabajador['apellido']} - {trabajador['cargo']}, Sueldo Bruto: {trabajador['sueldo_bruto']}, Descuento Salud: {trabajador['desc_salud']}, Descuento AFP: {trabajador['desc_afp']}, Líquido a Pagar: {trabajador['liquido_pagar']}\n")
    else:
        print("No hay trabajadores registrados.\n")

def imprimir_planilla():
    cargo = input("Ingrese el cargo para generar la planilla (o 'todos' para todos los cargos): ")
    archivo = "planilla_sueldos.txt"
    
    with open(archivo, 'w') as f:
        if cargo == "todos":
            for trabajador in trabajadores:
                f.write(f"{trabajador['nombre']} {trabajador['apellido']} - {trabajador['cargo']}, Sueldo Bruto: {trabajador['sueldo_bruto']}, Descuento Salud: {trabajador['desc_salud']}, Descuento AFP: {trabajador['desc_afp']}, Líquido a Pagar: {trabajador['liquido_pagar']}\n")
        else:
            for trabajador in trabajadores:
                if trabajador['cargo'] == cargo:
                    f.write(f"{trabajador['nombre']} {trabajador['apellido']} - {trabajador['cargo']}, Sueldo Bruto: {trabajador['sueldo_bruto']}, Descuento Salud: {trabajador['desc_salud']}, Descuento AFP: {trabajador['desc_afp']}, Líquido a Pagar: {trabajador['liquido_pagar']}\n")
    
    print(f"Planilla generada en {archivo}\n")

def menu_principal():
    while True:
        print("-"*20)
        print("1. Registrar trabajador")
        print("2. Listar todos los trabajadores")
        print("3. Imprimir planilla de sueldos")
        print("4. Salir del Programa")
        print("-"*20)
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            registrar_trabajador()
        elif opcion == '2':
            listar_trabajadores()
        elif opcion == '3':
            imprimir_planilla()
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")
            


if __name__ == "__main__":
    menu_principal()
