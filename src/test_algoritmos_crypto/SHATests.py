import hashlib
import time
from os import path
from .TestVector import TestVector
from .Results import Results

class SHATests(object):
    def __init__(self,test_folder='/tests_vectors/', out_folder='./'):
        self.tiempos = {
            'sha2-384':[],
            'sha2-512':[],
            'sha3-384':[],
            'sha2-512':[],
        }
        tv = TestVector(dirVectores=test_folder,archivoVectores= path.join(test_folder,'sha_2_3_384_512_vectors.csv'),tipo='sha')
        tv.parseVectores()
        self.vectores = tv.datos
        self.resultados = Results(dirResultados=out_folder,nombre='sha_res.csv')
    
    def armarResultado(self, tiempo, nombre, tipo):
        res = {
            'nombre': nombre,
            'tiempo':tiempo,
            'tipo':tipo
        }
        self.resultados.añadirResultado(res)
        return res


    def correrPrueba(self):
        for vector in self.vectores:
            start = time.process_time()
            SHA2 = hashlib.sha384(vector['vector']).hexdigest()
            end = time.process_time()
            tiempo = end - start
            self.armarResultado(tiempo, vector['nombre'],'sha2_384')
            start = time.process_time()
            SHA2 = hashlib.sha512(vector['vector']).hexdigest()
            end = time.process_time()
            tiempo = end - start
            self.armarResultado(tiempo, vector['nombre'],'sha2_512')
            start = time.process_time()
            SHA2 = hashlib.sha3_384(vector['vector']).hexdigest()
            end = time.process_time()
            tiempo = end - start
            self.armarResultado(tiempo, vector['nombre'],'sha3_384')
            start = time.process_time()
            SHA2 = hashlib.sha3_512(vector['vector']).hexdigest()
            end = time.process_time()
            tiempo = end - start
            self.armarResultado(tiempo, vector['nombre'],'sha3_512')
        self.resultados.escribirResultados()



if __name__ == '__main__':
    st = SHATests('../../test_vectors/')
    st.correrPrueba()
    