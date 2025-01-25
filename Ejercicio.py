# Realice un programa que pueda gestionar tickets de buses
# las clases a usar seran buses  , conductores
# 1. Un menu iteractivo con las siguiente opciones: agregar bus , agregar ruta a bus 
# registrar horario a bus, agregar conductor , agregar horario a conductor(*) y asignar bus a conductor(**)
# * consideremos que el horario de los conductores solo es a nivel de horas mas no dias ni fechas
# **validar que no haya conductores en ese horario ya asignados

class Conductor:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
        self.horarios = []  

    def agregar_horario(self, hora):
        if hora not in self.horarios:
            self.horarios.append(hora)
        else:
            print("Horario ya asignado al conductor.")

class Bus:
    def __init__(self, placa):
        self.placa = placa
        self.ruta = None  
        self.horarios = [] 
        self.conductores_asignados = {}  

    def agregar_ruta(self, ruta):
        self.ruta = ruta

    def registrar_horario(self, hora):
        if hora not in self.horarios:
            self.horarios.append(hora)
        else:
            print("Horario ya registrado para el bus.")

    def asignar_conductor(self, hora, conductor):
        if hora in self.conductores_asignados:
            print(f"El horario {hora} ya tiene un conductor asignado.")
        elif hora not in self.horarios:
            print("El horario no está registrado para este bus.")
        elif hora in conductor.horarios:
            print("El conductor ya tiene asignado este horario en otro bus.")
        else:
            self.conductores_asignados[hora] = conductor
            conductor.agregar_horario(hora)

class Admin:
    def __init__(self):
        self.buses = []
        self.conductores = []

    def agregar_bus(self, placa):
        bus = Bus(placa)
        self.buses.append(bus)
        print(f"Bus con placa {placa} agregado correctamente.")

    def agregar_conductor(self, nombre, dni):
        conductor = Conductor(nombre, dni)
        self.conductores.append(conductor)
        print(f"Conductor {nombre} agregado correctamente.")

    def buscar_bus(self, placa):
        for bus in self.buses:
            if bus.placa == placa:
                return bus
        print("Bus no encontrado.")
        return None

    def buscar_conductor(self, dni):
        for conductor in self.conductores:
            if conductor.dni == dni:
                return conductor
        print("Conductor no encontrado.")
        return None

    def menu(self):
        while True:
            print("\n--- Menú ---")
            print("1. Agregar bus")
            print("2. Agregar ruta a bus")
            print("3. Registrar horario a bus")
            print("4. Agregar conductor")
            print("5. Agregar horario a conductor")
            print("6. Asignar bus a conductor")
            print("7. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                placa = input("Ingrese la placa del bus: ")
                self.agregar_bus(placa)

            elif opcion == "2":
                placa = input("Ingrese la placa del bus: ")
                bus = self.buscar_bus(placa)
                if bus:
                    ruta = input("Ingrese la ruta para el bus: ")
                    bus.agregar_ruta(ruta)
                    print(f"Ruta {ruta} asignada al bus {placa}.")

            elif opcion == "3":
                placa = input("Ingrese la placa del bus: ")
                bus = self.buscar_bus(placa)
                if bus:
                    hora = input("Ingrese el horario (hh:mm): ")
                    bus.registrar_horario(hora)

            elif opcion == "4":
                nombre = input("Ingrese el nombre del conductor: ")
                dni = input("Ingrese el DNI del conductor: ")
                self.agregar_conductor(nombre, dni)

            elif opcion == "5":
                dni = input("Ingrese el DNI del conductor: ")
                conductor = self.buscar_conductor(dni)
                if conductor:
                    hora = input("Ingrese el horario (hh:mm): ")
                    conductor.agregar_horario(hora)

            elif opcion == "6":
                placa = input("Ingrese la placa del bus: ")
                bus = self.buscar_bus(placa)
                if bus:
                    dni = input("Ingrese el DNI del conductor: ")
                    conductor = self.buscar_conductor(dni)
                    if conductor:
                        hora = input("Ingrese el horario (hh:mm): ")
                        bus.asignar_conductor(hora, conductor)

            elif opcion == "7":
                print("Saliendo del programa...")
                break

            else:
                print("Opción no válida. Intente nuevamente.")

admin = Admin()
admin.menu()