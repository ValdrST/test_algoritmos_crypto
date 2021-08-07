import pandas as pd
import math
from os import path

class TestVector(object):
    def __init__(self, tipo='sha', archivoVectores='vectores.txt', dirVectores='./'):
        self.tipo = tipo
        self.datos = []
        self.file = archivoVectores
        self.dir = dirVectores
    
    def leerArchivo(self, archivo):
        with open(path.join(self.dir,archivo), 'rb') as f:
            return f.read()


    def parseVectores(self):
        vectores_texto = pd.read_csv(self.file,dtype=object)
        if self.tipo == 'sha' or self.tipo == 'aes':
            for index, row in vectores_texto.iterrows():
                try:
                    if math.isnan(float(row['archivo'])):
                        self.datos.append({'nombre':str(row['texto']),'vector':str(row['texto']).encode()})
                    else:
                        self.datos.append({'nombre':row['texto'],'vector':self.leerArchivo(row['archivo']).encode()})
                except:
                    self.datos.append({'nombre':row['texto'],'vector':self.leerArchivo(row['archivo'])})
        elif self.tipo == 'rsa_sign' or self.tipo == 'rsa_padding':
            c = 1
            for index, row in vectores_texto.iterrows():
                vector = {'nombre':"vector#{}".format(c),
                'modulo':row['modulo'],
                'exponente_publico':row['exponente_publico'],
                'exponente_privado':row['exponente_privado'],
                'vector':bytes.fromhex(row['datos']),
                }
                self.datos.append(vector)
                c += 1
        else:
            print("Formato de vector no reconocido")

if __name__ == '__main__':
    tv = TestVector(archivoVectores = '../../test_vectors/sha_2_3_384_512_vectors.csv', dirVectores = '../../test_vectors/')
    tv.parseVectores()
    print(tv.datos)
    