
class ValidarSignosVitales:

    def __init__(self,nombre_atributo):
        self.nombre_atributo = nombre_atributo

    def __get__(self, instance, owner):

        if instance is None:
            return self

        return instance.__dict__.get(self.nombre_atributo)

    def __set__(self, instance, value):

        if not isinstance(value,(int,float)):
            raise TypeError("La temperatura debe ser de tipo entero o flotante")

        if not (30.0 < value < 45.0):
            raise ValueError("La temperatura esta fuera del rango biológico")

        instance.__dict__[self.nombre_atributo] = float(value)


class ValidarFrecuenciaCardiaca:

    def __init__(self,nombre_atributo):
        self.nombre_atributo = nombre_atributo


    def __get__(self, instance, owner):
        if instance is None:
            return self

        return instance.__dict__.get(self.nombre_atributo)

    def __set__(self, instance, value):

        if not isinstance(value,(int,float)):

            raise TypeError("La presión arterial debe ser un entero o float")

        if not (30 < value < 220):
            raise ValueError("La frecuencia cardiaca esta fuera del rango biologico")

        instance.__dict__[self.nombre_atributo] = value
        


        

    