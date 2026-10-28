from dataclasses import dataclass

@dataclass(frozen=True)
class Medicamento:

    nombre: str
    dosis_mg: float
    hora_aplicacion: str

    