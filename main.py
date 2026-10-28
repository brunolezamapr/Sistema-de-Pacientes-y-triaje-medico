if __name__ == "__main__":

    from medicamento import Medicamento
    from paciente import Paciente
    from sala_urgencias import SalaUrgencias

    print("=" * 60)
    print("PRUEBA COMPLETA: PACIENTE Y TRIAJE MÉDICO")
    print("=" * 60)

    # 1. Constructor alternativo (@classmethod)
    p1 = Paciente.desde_expediente("Ana Gomez,38.5,90")
    p2 = Paciente.desde_expediente("Carlos Ruiz,36.6,72")
    p3 = Paciente.desde_expediente("Bruno Lezama,40.0,130")

    print(f"Paciente 1: {p1.nombre} | Temp: {p1.temperatura}°C | Triaje: {p1.color_triaje}")
    print(f"Paciente 2: {p2.nombre} | Temp: {p2.temperatura}°C | Triaje: {p2.color_triaje}")
    print(f"Paciente 3: {p3.nombre} | Temp: {p3.temperatura}°C | Triaje: {p3.color_triaje}")

    # 2. Uso de Medicamentos
    print("\n--- Suministro de Medicamentos ---")
    m1 = Medicamento("ibuprofeno", 4.5, "8 hrs")
    m2 = Medicamento("paracetamol", 6.5, "4 hrs")

    p3.administrar_medicamento(m1)
    p3.administrar_medicamento(m2)
    print(f"Medicamentos de {p3.nombre}: {p3.medicamentos_aplicados}")

    # 3. Administración de la Sala
    print("\n--- Sala de Urgencias ---")
    sala = SalaUrgencias("Urgencias Generales")
    sala = sala + p1
    sala = sala + p2
    sala = sala + p3

    print(f"Total en sala: {len(sala)} pacientes.")
    print(f"Pacientes con fiebre: {len(sala.pacientes_con_fiebre)}")

    print("\nPrioridad de Atención (Ordenados de mayor a menor gravedad):")
    for paciente in sala.obtener_prioridad_atencion():
        print(f" 🚨 {paciente.nombre} - {paciente.temperatura}°C - Triaje: {paciente.color_triaje}")