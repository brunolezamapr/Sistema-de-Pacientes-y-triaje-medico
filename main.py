"""
main.py - Script de Pruebas Integrales y Demostración del Sistema de Triaje Médico.
Demuestra la integración entre Descriptores, Dataclasses, @property, @classmethod, 
@staticmethod, Composición de Colecciones y Sobrecarga de Operadores.
"""



if __name__ == "__main__":
    from medicamento import Medicamento
    from paciente import Paciente
    from sala_urgencias import SalaUrgencias
    print("=" * 65)
    print("1. CREACIÓN DE PACIENTES Y VALIDACIÓN CON DESCRIPTORES")
    print("=" * 65)

    # A) Instanciación individual limpia
    p1 = Paciente("Ana Gomez", 38.5, 90)
    p2 = Paciente("Carlos Ruiz", 36.6, 72)
    print(
        f"[OK] {p1.nombre} | Temp: {p1.temperatura}°C | FC: {p1.frecuencia_cardiaca}bpm | Triaje: {p1.color_triaje}"
    )
    print(
        f"[OK] {p2.nombre} | Temp: {p2.temperatura}°C | FC: {p2.frecuencia_cardiaca}bpm | Triaje: {p2.color_triaje}"
    )

    # B) Prueba de Captura de Errores en Descriptores
    print("\n--- Pruebas de Captura de Errores en Descriptores ---")
    try:
        p_error_temp = Paciente("Error Temp", 50.0, 80)
    except ValueError as e:
        print(f"[CAPTURADO] Error esperado en temperatura: {e}")

    try:
        p_error_fc = Paciente("Error FC", 37.0, 300)
    except ValueError as e:
        print(f"[CAPTURADO] Error esperado en frecuencia cardíaca: {e}")

    print("\n" + "=" * 65)
    print("2. CONSTRUCTORES EN LOTE (@classmethod) Y UTILITIES (@staticmethod)")
    print("=" * 65)

    # A) Carga masiva usando @classmethod desde_lista_expedientes
    expedientes_raw = [
        "Bruno Lezama,40.0,130",
        "Laura Pausini,39.2,110",
        "Pedro Infante,36.5,70",
    ]
    pacientes_lote = Paciente.desde_lista_expedientes(expedientes_raw)
    print(
        f"[OK] Se cargaron {len(pacientes_lote)} pacientes en lote exitosamente."
    )

    # B) Validación estática con @staticmethod
    dni_test = "12345678"
    print(
        f"[OK] ¿DNI '{dni_test}' es válido? (@staticmethod): {Paciente.es_dni_valido(dni_test)}"
    )

    print("\n" + "=" * 65)
    print("3. DATACLASSES INMUTABLES Y ESTADO DE ALTA MÉDICA")
    print("=" * 65)

    # A) Asignación de Medicamento (Dataclass frozen)
    p_critico = pacientes_lote[0]  # Bruno Lezama (40.0°C, 130bpm)
    m1 = Medicamento("Ibuprofeno", 400.0, "08:00")
    m2 = Medicamento("Paracetamol", 500.0, "12:00")

    p_critico.administrar_medicamento(m1)
    p_critico.administrar_medicamento(m2)
    print(f"Medicamentos aplicados a {p_critico.nombre}:")
    for med in p_critico.medicamentos_aplicados:
        print(f" - {med.nombre} ({med.dosis_mg}mg) a las {med.hora_aplicacion}")

    # B) Prueba de Alta Médica con @property.setter
    print("\n--- Cambio de Estado (Alta Médica) ---")
    p2.dado_de_alta = True  # Dispara el setter

    try:
        p2.administrar_medicamento(m1)
    except ValueError as e:
        print(
            f"[CAPTURADO] Error esperado al medicar paciente egresado: {e}"
        )

    print("\n" + "=" * 65)
    print("4. COMPOSICIÓN, SOBRECARGA (+) Y ESTADÍSTICAS EN SALA DE URGENCIAS")
    print("=" * 65)

    # A) Instanciación de la Sala de Urgencias
    sala = SalaUrgencias("Urgencias Pediátricas")

    # B) Inserción mediante sobrecarga del operador '+'
    sala = sala + p1
    sala = sala + p2
    for p in pacientes_lote:
        sala = sala + p

    print(f"Estado de la Sala: {sala}")
    print(f"Cantidad total de pacientes en espera (__len__): {len(sala)}")

    # C) Propiedades Estadísticas Calculadas
    print(f"Temperatura promedio en sala: {sala.promedio_temperatura:.2f}°C")
    print(f"Desglose de Triaje en Sala: {sala.resumen_triaje}")
    print(
        f"Pacientes actualmente con fiebre: {len(sala.pacientes_con_fiebre)}"
    )

    # D) Ordenamiento por Prioridad utilizando __lt__
    print("\n--- Prioridad de Atención (Ordenados por Gravedad/Temperatura) ---")
    for pos, paciente in enumerate(sala.obtener_prioridad_atencion(), start=1):
        print(
            f" [{pos}] {paciente.nombre:<15} | Temp: {paciente.temperatura}°C | FC: {paciente.frecuencia_cardiaca}bpm | Triaje: {paciente.color_triaje}"
        )

    print("=" * 65)