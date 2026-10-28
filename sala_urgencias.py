
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
        
    def obtener_prioridad_atencion(self):

        return sorted(self._pacientes,reverse=True)

    
    
    

        

        
    