
# 🏥 Sistema de Control de Pacientes y Triaje Médico (POO en Python)

Un sistema modular desarrollado en Python enfocado en la gestión de urgencias médicas, triaje en tiempo real y administración protegida de fármacos. El proyecto combina patrones avanzados de **Programación Orientada a Objetos (POO)** para asegurar la integridad de los datos biológicos y la inmutabilidad en el registro de medicamentos.

---

## 📌 Conceptos Clave de POO Aplicados

### 1. Descriptores de Validación Biológica (`ValidarSignosVitales` y `ValidarFrecuenciaCardiaca`)
* **El Problema:** Interceptar y validar asignaciones de signos vitales para evitar registrar temperaturas fuera de rango biológico ($30.0$ °C a $45.0$ °C) o frecuencias cardíacas anormales ($30$ a $220$ bpm).
* **La Solución:** Implementación del protocolo descriptor (`__get__` y `__set__`) a nivel de clase para actuar como guardián reutilizable de los atributos sin repetir validaciones en setters.

### 2. Dataclasses Inmutables (`Medicamento`)
* Uso del decorador `@dataclass(frozen=True)` para representar prescripciones médicas. Garantiza que una vez registrado un fármaco (nombre, dosis y hora), no pueda ser modificado ni alterado.

### 3. Propiedades Calculadas y Nivel de Triaje (`@property`)
* Evaluación en tiempo real del estado académico del paciente (`tiene_fiebre`) y del nivel de riesgo médico (`color_triaje`: ROJO, AMARILLO, VERDE) en función de la combinación de la temperatura y los latidos por minuto.

### 4. Constructores Alternativos (`@classmethod`)
* Implementación de `desde_expediente` (*Factory Method*) para parsear cadenas de texto o expedientes médicos tipo `"Nombre,Temperatura,FrecuenciaCardiaca"` e instanciar la clase limpiamente.

### 5. Contenedor e Iterabilidad con Métodos Dunder (`SalaUrgencias`)
* Uso de agregación para gestionar pacientes en sala de urgencias:
  - **`__len__`**: Consulta el número de pacientes en espera (`len(sala)`).
  - **`__getitem__`**: Habilita la indexación (`sala[0]`) y la iteración directa en bucles `for`.
  - **`__add__`**: Sobrecarga del operador `+` para ingresar un paciente a la sala (`sala + paciente`).
  - **`obtener_prioridad_atencion()`**: Aprovecha el método dunder `__lt__` de `Paciente` para ordenar a los pacientes por prioridad de gravedad.

---

## 📁 Arquitectura del Proyecto

```text
TriajeMedico/
│
├── descriptors.py      # Descriptores de validación para signos vitales
├── medicamento.py      # Dataclass inmutable Medicamento
├── paciente.py         # Entidad del modelo de dominio Paciente con @property y @classmethod
├── sala_urgencias.py   # Contenedor SalaUrgencias con sobrecarga de operadores
├── main.py             # Script de ejecución con instancias reales
└── README.md           # Documentación técnica explicativa
```

---

## 🚀 Guía de Ejecución

```bash
python3 main.py
```
```
