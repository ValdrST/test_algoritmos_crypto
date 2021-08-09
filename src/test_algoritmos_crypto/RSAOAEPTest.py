from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
import time
from os import path
from .TestVector import TestVector
from .Results import Results
import logging

class RSAOAEPTest(object):
    def __init__(self,test_folder='/tests_vectors/', out_folder='./'):
        self.tiempos = {
            'rsa-oaep-encrypt':[],
            'rsa-oaep-decrypt':[]
        }
        self.nombre = "prueba Cifrado y descifrado RSA-OAEP"
        tv = TestVector(dirVectores=test_folder,archivoVectores= path.join(test_folder,'rsa_oaep_test_vectors.csv'),tipo='rsa_padding')
        tv.parseVectores()
        self.vectores = tv.datos
        self.resultados = Results(dirResultados=out_folder, nombre='rsa_oaep_res.csv')
        self.res = { }
    
    def armarResultado(self, tiempo, nombre, tipo):
      self.res[tipo] = tiempo

    def rsa_oaep_encrypt(self, data, n, e, d):
      privateKey = RSA.construct((n, e, d))
      publicKey = privateKey.publickey()

      cipher = PKCS1_OAEP.new(publicKey)
      start = time.process_time()
      ct = cipher.encrypt(data)    
      end = time.process_time()
      tiempo = end - start
      return ct, privateKey, tiempo
    
    def rsa_oaep_decrypt(self, ct, privateKey):
      decipher = PKCS1_OAEP.new(privateKey)
      start = time.process_time()
      pt = decipher.decrypt(ct)
      end = time.process_time()
      tiempo = end - start
      return tiempo

    def correrPruebaTotal(self, tiempos=1000):
      for i in range(tiempos):
        logging.info("Iteracion {} de la {}".format(i+1, self.nombre))
        print("Iteracion {} de la {}".format(i+1, self.nombre))
        self.correrPrueba()
      self.resultados.escribirResultados()


    def correrPrueba(self):
      for vector in self.vectores:
        n = int(vector['modulo'], 16)
        e = int(vector['exponente_publico'], 16)
        d = int(vector['exponente_privado'], 16)
        self.res['nombre'] = vector['nombre']
        ct, key, tiempo = self.rsa_oaep_encrypt(vector['vector'], n, e, d)
        self.armarResultado(tiempo, vector['nombre'],'rsa-oaep-encrypt')
        
        tiempo = self.rsa_oaep_decrypt(ct, key)
        self.armarResultado(tiempo, vector['nombre'],'rsa-oaep-decrypt')
        self.resultados.añadirResultado(self.res)
      



if __name__ == '__main__':
  at = RSAOAEPTest('../../test_vectors/')
  at.correrPrueba()
    