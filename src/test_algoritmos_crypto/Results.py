from pandas import DataFrame
import pandas as pd
from os import path

class Results(object):
    def __init__(self, dirResultados='/results/', nombre='resultados.csv'):
        self.dir = dirResultados
        self.ruta_resultados = path.join(self.dir,nombre)
        self.datos = DataFrame()
        self.promedios = DataFrame()
    
    def añadirResultado(self, datos:dict):
        self.datos = self.datos.append(datos, ignore_index=True)
        
    def escribirResultados(self):
        self.calcularPromedio()
        self.promedios.to_csv(self.ruta_resultados, index=False)
    
    def calcularPromedio(self):
        for d in self.datos:
            if d != 'nombre':
                res = {
                    'Algoritmo':d,
                    'Promedio':self.datos[d].mean(), 
                    'Pruebas' : self.datos[d].size
                    }
                self.promedios = self.promedios.append(res, ignore_index=True)
        return self.promedios