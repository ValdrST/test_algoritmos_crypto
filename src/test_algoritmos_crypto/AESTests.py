from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes
import time
from os import path
from .TestVector import TestVector
from .Results import Results

class AESTests(object):
    def __init__(self,test_folder='/tests_vectors/', out_folder='./'):
        self.tiempos = {
            'aes-ecb-encrypt':[],
            'aes-cbc-encrypt':[],
            'aes-ecb-decrypt':[],
            'aes-cbc-decrypt':[],
        }
        tv = TestVector(dirVectores=test_folder,archivoVectores= path.join(test_folder,'aes_256_ebc-cbc_vectors.csv'),tipo='aes')
        tv.parseVectores()
        self.vectores = tv.datos
        self.resultados = Results(dirResultados=out_folder, nombre='aes_res.csv')
        self.res = { }
    
    def armarResultado(self, tiempo, nombre, tipo):
      self.res[tipo] = tiempo

    def aes_cbd_encrypt(self, key, data):
      cipher = AES.new(key, AES.MODE_CBC)
      ct = cipher.encrypt(pad(data, AES.block_size))
      return (ct,cipher.iv)
    
    def aes_cbd_decrypt(self, key, ct, iv):
      decipher = AES.new(key, AES.MODE_CBC, iv)
      return unpad(decipher.decrypt(ct), AES.block_size)

    def aes_ecb_encrypt(self, key, data):
      cipher = AES.new(key, AES.MODE_ECB)
      ct = cipher.encrypt(pad(data, AES.block_size))
      return ct
    
    def aes_ecb_decrypt(self, key, ct):
      decipher = AES.new(key, AES.MODE_ECB)
      return unpad(decipher.decrypt(ct), AES.block_size)

    def correrPruebaTotal(self, tiempos=1000):
      for i in range(tiempos):
        self.correrPrueba()

    def correrPrueba(self):
      for vector in self.vectores:
        self.res['nombre'] = vector['nombre']
        key = get_random_bytes(32)
        start = time.process_time()
        AES_CBD_E, iv = self.aes_cbd_encrypt(key,vector['vector'])
        end = time.process_time()
        tiempo = end - start
        self.armarResultado(tiempo, vector['nombre'],'aes-cbc-encrypt')
        
        start = time.process_time()
        AES_CBD_D = self.aes_cbd_decrypt(key, AES_CBD_E, iv)
        end = time.process_time()
        tiempo = end - start
        self.armarResultado(tiempo, vector['nombre'],'aes-cbc-decrypt')

        start = time.process_time()
        AES_ECB_E = self.aes_ecb_encrypt(key, vector['vector'])
        end = time.process_time()
        tiempo = end - start
        self.armarResultado(tiempo, vector['nombre'],'aes-ecb-encrypt')
        
        start = time.process_time()
        AES_ECB_D = self.aes_ecb_decrypt(key, AES_ECB_E)
        end = time.process_time()
        tiempo = end - start
        self.armarResultado(tiempo, vector['nombre'],'aes-ecb-decrypt')
        self.resultados.añadirResultado(self.res)
      self.resultados.escribirResultados()



if __name__ == '__main__':
  at = AESTests('../../test_vectors/')
  at.correrPrueba()
    