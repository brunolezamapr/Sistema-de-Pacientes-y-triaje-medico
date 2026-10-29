
class TriajeMedicoError(Exception):

    """Excepción base para errores del sistema de triaje"""
    pass

class SignoVitalInvalidoError(Exception):
    """Temperatura o Frecuencia Cardiaca fuera del rango"""

    pass

class PacienteEgresadoError(Exception):

    """Paciente fue dado de alta"""
    pass    

