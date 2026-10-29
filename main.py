"""
main.py - Suite de pruebas integrales para el Sistema de Control de Pacientes y Triaje Médico.
Demuestra la integración de Descriptores, Dataclasses, @property, @classmethod, @staticmethod,
Excepciones Personalizadas, Búsquedas por DNI, Filtrados por Triaje y Exportación de Reportes.
"""

from exceptions import PacienteEgresadoError, SignoVitalInvalidoError
from medicamento import Medicamento
from paciente import Paciente
from sala_urgencias import SalaUrgencias

if __name__ == "__main__":
    print("=" * 70)
    print("1. VALIDACIÓN BIOLÓGICA Y CAPTURA DE EXCEPCIONES PERSONALIZADAS")
    print("=" * 70)

    # A) Instanciación válida de pacientes con DNI
    try:
        p1 = Paciente("Ana Gomez", "12345678", 38.5, 90)
        p2 = Paciente("Carlos Ruiz", "87654321", 36.6, 72)
        print(
            f"[OK] {p1.nombre} (DNI: {p1.dni}) | Temp: {p1.temperatura}°C | Triaje: {p1.color_triaje}"
        )
        print(
            f"[OK] {p2.nombre} (DNI: {p2.dni}) | Temp: {p2.temperatura}°C | Triaje: {p2.color_triaje}"
        )
    except SignoVitalInvalidoError as e:
        print(f"[ERROR SIGNO VITAL]: {e}")

    # B) Prueba de Captura de Excepción Personalizada (Signo Vital Fuera de Rango)
    try:
        p_error_temp = Paciente("Error Temp", "11223344", 50.0, 80)
    except SignoVitalInvalidoError as e:
        print(f"[CAPTURADO SignoVitalInvalidoError]: {e}")

    # C) Prueba de DNI Inválido
    try:
        p_error_dni = Paciente("Error DNI", "1234", 37.0, 80)
    except ValueError as e:
        print(f"[CAPTURADO ValueError DNI]: {e}")

    print("\n" + "=" * 70)
    print("2. CONSTRUCTORES EN LOTE (@classmethod) Y UTILITIES (@staticmethod)")
    print("=" * 70)

    # A) Carga masiva en lote usando @classmethod desde_lista_expedientes
    expedientes_raw = [
        "Bruno Lezama,45678912,40.0,130",
        "Laura Pausini,98765432,39.2,110",
        "Pedro Infante,55667788,36.5,70",
    ]
    pacientes_lote = Paciente.desde_lista_expedientes(expedientes_raw)
    print(
        f"[OK] {len(pacientes_lote)} pacientes cargados exitosamente desde expedientes."
    )

    # B) Validación estática con @staticmethod es_dni_valido
    dni_test = "87654321"
    print(
        f"[OK] ¿DNI '{dni_test}' es válido? (@staticmethod): {Paciente.es_dni_valido(dni_test)}"
    )

    print("\n" + "=" * 70)
    print("3. DATACLASSES INMUTABLES Y ALTA DE PACIENTES (SETTER)")
    print("=" * 70)

    # A) Suministro de Medicamentos Inmutables
    m1 = Medicamento("Ibuprofeno", 400.0, "08:00")
    m2 = Medicamento("Paracetamol", 500.0, "12:00")

    p_critico = pacientes_lote[0]  # Bruno Lezama
    p_critico.administrar_medicamento(m1)
    p_critico.administrar_medicamento(m2)
    print(f"Medicamentos aplicados a {p_critico.nombre}:")
    for med in p_critico.medicamentos_aplicados:
        print(
            f" - {med.nombre} ({med.dosis_mg}mg) asignado a las {med.hora_aplicacion}"
        )

    # B) Cambio de estado con @dado_de_alta.setter y captura de PacienteEgresadoError
    print("\n--- Proceso de Alta Médica ---")
    p2.dado_de_alta = True  # Dispara el setter y actualiza _dado_de_alta = True

    try:
        p2.administrar_medicamento(m1)
    except PacienteEgresadoError as e:
        print(f"[CAPTURADO PacienteEgresadoError]: {e}")

    print("\n" + "=" * 70)
    print("4. SALA DE URGENCIAS: BÚSQUEDAS, FILTRADO Y REPORTE DE EXPORTACIÓN")
    print("=" * 70)

    # A) Instanciación e ingreso mediante sobrecarga del operador '+'
    sala = SalaUrgencias("Urgencias Principales")
    sala = sala + p1
    sala = sala + p2
    for p in pacientes_lote:
        sala = sala + p

    print(f"Estado de la Sala: {sala}")
    print(f"Total de pacientes registrados (__len__): {len(sala)}")

    # B) Búsqueda por DNI
    dni_buscado = "45678912"
    paciente_encontrado = sala.buscar_por_dni(dni_buscado)
    if paciente_encontrado:
        print(
            f"\n[BÚSQUEDA ÉXITO] DNI {dni_buscado} pertenece a: {paciente_encontrado.nombre} (Triaje: {paciente_encontrado.color_triaje})"
        )

    paciente_inexistente = sala.buscar_por_dni("00000000")
    print(f"[BÚSQUEDA INEXISTENTE] Resultado: {paciente_inexistente}")

    # C) Filtrado por nivel de urgencia (Triaje)
    print("\n--- Pacientes Filtrados por Triaje 'ROJO' ---")
    rojos = sala.filtrar_por_triaje("ROJO")
    for p in rojos:
        print(
            f" 🚨 {p.nombre} (DNI: {p.dni}) | Temp: {p.temperatura}°C | FC: {p.frecuencia_cardiaca}bpm"
        )

    # D) Exportación del Reporte Consolidado
    print("\n--- Exportación de Reporte General (to_dict / exportar_reporte) ---")
    reporte = sala.exportar_reporte()
    print(f"Nombre Sala         : {reporte['Sala']}")
    print(f"Total Pacientes     : {reporte['Total_pacientes']}")
    print(f"Promedio Temperatura: {reporte['Promedio_temperatura']}°C")
    print(f"Resumen de Triaje   : {reporte['Resumen_triaje']}")
    print("\nEstructura del primer paciente en la lista del reporte:")
    print(reporte["pacientes"][0])

    print("\n" + "=" * 70)
    print("PRUEBAS COMPLETADAS CON ÉXITO")
    print("=" * 70)