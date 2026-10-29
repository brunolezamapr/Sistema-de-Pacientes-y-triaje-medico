from descriptors import ValidarSignosVitales,ValidarFrecuenciaCardiaca
from medicamento import Medicamento
from exceptions import PacienteEgresadoError

class Paciente:

    temperatura = ValidarSignosVitales("temperatura")
    frecuencia_cardiaca = ValidarFrecuenciaCardiaca("frecuencia_cardiaca")
    def __init__(self,nombre:str,dni:str,temperatura:float,frecuencia_cardiaca:int):

        if not Paciente.es_dni_valido(dni):
            raise ValueError(
                f"El DNI '{dni}' no es valido.Debe contener exactamente 8 digitos númericos"
            )
        self.nombre = nombre.strip()
        self.dni = dni.strip()
        self.temperatura = temperatura
        self.frecuencia_cardiaca = frecuencia_cardiaca
        self._medicamentos = []
        self._dado_de_alta = False


    def administrar_medicamento(self,medicamento):
        if not isinstance(medicamento,Medicamento):
            raise TypeError("Debe ser una instancia de tipo medicamento")

        if self._dado_de_alta is True: 
            raise PacienteEgresadoError() 
        self._medicamentos.append(medicamento)

    def to_dict(self) -> dict:

        return {
            "nombre":self.nombre,
            "dni": self.dni,
            "temperatura": self.temperatura,
            "frecuencia_cardiaca": self.frecuencia_cardiaca,
            "dado_de_alta": self.dado_de_alta,
            "color_triaje": self.color_triaje,
            "medicamentos": [
                {
                    "nombre": med.nombre,
                    "dosis_mg": med.dosis_mg,
                    "hora_aplicacion": med.hora_aplicacion,
                }
                for med in self._medicamentos
            ]
        }


    @classmethod
    def desde_expediente(cls,texto_expediente:str) -> "Paciente":

        texto_partes = texto_expediente.split(",")
        if len(texto_partes) != 4:
            raise ValueError("El formato debe tener el siguiente: Nombre,DNI,Temperatura,FrecuenciaCardiaca")

        nombre = texto_partes[0]
        dni = texto_partes[1]
        temperatura = float(texto_partes[2])
        frecuencia_cardiaca = int(texto_partes[3])

        return cls(nombre,dni,temperatura,frecuencia_cardiaca)

    @classmethod
    def desde_lista_expedientes(cls,lista_cadenas:list[str]):
         lista_expedientes = []
         for texto  in lista_cadenas: 
             paciente_creado = cls.desde_expediente(texto)
             lista_expedientes.append(paciente_creado)

         return lista_expedientes
        
        
    @property
    def dado_de_alta(self):
        return self._dado_de_alta

    @dado_de_alta.setter
    def dado_de_alta(self,nuevo_estado): 
        if not isinstance(nuevo_estado,(bool)): 
            raise ValueError("El estado debe ser de tipo booleano")
        self._dado_de_alta = nuevo_estado
        if nuevo_estado:
            print("El paciente fue dado de alta") 
            


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
    