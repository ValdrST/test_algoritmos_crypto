from pandas import DataFrame
import pandas as pd
from os import path

class Results(object):
    def __init__(self, dirResultados='/results/', nombre='resultados.csv'):
        self.dir = dirResultados
        self.ruta_resultados = path.join(self.dir,nombre)
        self.datos = DataFrame()
    
    def añadirResultado(self, datos:dict):
        self.datos = self.datos.append(datos, ignore_index=True)
        
    def escribirResultados(self):
        self.datos.to_csv(self.ruta_resultados, index=False)
    