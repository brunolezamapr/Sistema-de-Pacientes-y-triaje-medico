from descriptors import ValidarSignosVitales,ValidarFrecuenciaCardiaca
from medicamento import Medicamento
class Paciente:

    temperatura = ValidarSignosVitales("temperatura")
    frecuencia_cardiaca = ValidarFrecuenciaCardiaca("frecuencia_cardiaca")
    def __init__(self,nombre:str,temperatura:float,frecuencia_cardiaca:int):
        self.nombre = nombre.strip()
        self.temperatura = temperatura
        self.frecuencia_cardiaca = frecuencia_cardiaca
        self._medicamentos = []

    def administrar_medicamento(self,medicamento):
        if not isinstance(medicamento,Medicamento):
            raise TypeError("Debe ser una instancia de tipo medicamento")
        self._medicamentos.append(medicamento)


    @classmethod
    def desde_expediente(cls,texto_expediente:str) -> "Paciente":

        texto_partes = texto_expediente.split(",")
        if len(texto_partes) != 3:
            raise ValueError("El formato debe tener el siguiente: Nombre,Temperatura,FrecuenciaCardiaca")

        nombre = texto_partes[0]
        temperatura = float(texto_partes[1])
        frecuencia_cardiaca = int(texto_partes[2])

        return cls(nombre,temperatura,frecuencia_cardiaca)

    @property
    def tiene_fiebre(self) -> bool:
    
        return self.temperatura >= 37.5 

    @property
    def medicamentos_aplicados(self):
        return tuple(self._medicamentos)

    @property
    def color_triaje(self) -> str:
        if self.temperatura > 39.0 or self.frecuencia_cardiaca > 120:
            return "ROJO"
        elif self.tiene_fiebre or (100 < self.frecuencia_cardiaca < 120):
            return "AMARILLO"
        else:
            return "VERDE"

    @staticmethod 
    def es_dni_valido(dni:str) -> bool:
        if not isinstance(dni,str):
            return False
        
        return len(dni.strip()) == 8 and dni.strip().isdigit()

    def __eq__(self, other) -> bool:
        if not isinstance(other,Paciente):
            return NotImplemented
        return self.temperatura == other.temperatura and self.frecuencia_cardiaca == other.frecuencia_cardiaca

    def __lt__(self, other) -> bool:
        if not isinstance(other,Paciente):
            return NotImplemented
        return self.temperatura < other.temperatura

    def __repr__(self): 
        return f"Paciente(nombre='{self.nombre}',temp={self.temperatura}°C,fc={self.frecuencia_cardiaca}bpm)"
    