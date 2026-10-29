
from paciente import Paciente


class SalaUrgencias:

    def __init__(self,nombre_sala:str):
        self.nombre_sala = nombre_sala
        self._pacientes = []

    def ingresar_paciente(self,paciente:Paciente):
        if not isinstance(paciente,Paciente):
            raise TypeError("no es una instancia de la clase Paciente")
        self._pacientes.append(paciente)

    def __len__(self):
        return len(self._pacientes)

    def __getitem__(self, index):
        return self._pacientes[index]

    def __add__(self, otro):

        if not isinstance(otro,Paciente):
            return NotImplemented
        
        self.ingresar_paciente(otro)
        return self

    @property
    def pacientes_con_fiebre(self):
        tienen_fiebre = [paciente for paciente in self._pacientes if paciente.tiene_fiebre]
        return tienen_fiebre

    @property
    def promedio_temperatura(self): 
        if not self._pacientes:
            return 0.0
        return sum(paciente.temperatura for paciente in self._pacientes) / len(self._pacientes)

    @property
    def resumen_triaje(self):
        conteo = {"ROJO":0,"AMARILLO":0,"VERDE": 0}
        for paciente in self._pacientes:
            color = paciente.color_triaje
            if color in conteo: 
                conteo[color] += 1

        return conteo
        
    def obtener_prioridad_atencion(self):

        return sorted(self._pacientes,reverse=True)

    def exportar_reporte(self) -> dict:

        return {
            "Sala": self.nombre_sala,
            "Total_pacientes": len(self),
            "Resumen_triaje": self.resumen_triaje,
            "Promedio_temperatura": round(self.promedio_temperatura,2),
            "pacientes": [paciente.to_dict() for paciente in self._pacientes]
        }

    def buscar_por_dni(self,dni:str) -> Paciente | None:

        if not Paciente.es_dni_valido(dni):
            return None

        for paciente in self._pacientes:
            if paciente.dni == dni.strip():
                return paciente

        return None          


    
    def filtrar_por_triaje(self,color:str) -> list[Paciente]:

        color_mayusculas = color.upper()
        return [p for p in self._pacientes if p.color_triaje == color_mayusculas] 
    