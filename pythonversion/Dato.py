class Dato:
    def __init__(self, notadelcurso, pesodelasnotas):
        self.notadelcurso = notadelcurso
        self.pesodelasnotas = pesodelasnotas

    @staticmethod
    def calcular_promedio_final(datos):
        if not datos:
            return 0
        total_peso = sum(dato.pesodelasnotas for dato in datos)
        if total_peso == 0:
            return 0
        promedio = sum(dato.notadelcurso * dato.pesodelasnotas for dato in datos) / total_peso
        return promedio
