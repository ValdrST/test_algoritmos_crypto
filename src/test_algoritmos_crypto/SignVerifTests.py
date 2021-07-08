import time
import csv
from Crypto.Signature import pss
from Crypto.PublicKey import ECC, DSA, RSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA512, SHA256
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.exceptions import InvalidSignature
import time
from os import path
from .TestVector import TestVector
from .Results import Results

class SignVerifTests(object):
  def __init__(self,test_folder='/tests_vectors/', out_folder='./'):
      self.tiempos = {
          'dsa-signing':[],
          'ecdsa-signing':[],
          'rsa-pss-signing':[],
          'dsa-verifing':[],
          'ecdsa-verifing':[],
          'rsa-pss-verifing':[]
      }
      tv = TestVector(dirVectores=test_folder,archivoVectores= path.join(test_folder,'rsa_pss_dsa_ecdsa_test_vectors.csv'),tipo='rsa_sign')
      tv.parseVectores()
      self.vectores = tv.datos
      self.resultados = Results(dirResultados=out_folder, nombre='rsa_sign_verif_res.csv')
    
  def armarResultado(self, tiempo, nombre, tipo):
      res = {
          'nombre': nombre,
          'tiempo':tiempo,
          'tipo':tipo
      }
      self.resultados.añadirResultado(res)
      return res

  def rsa_pss_sign(self, data, n, e, d):
    privateKeyRSA = RSA.construct((n, e, d))
    publicKeyRSA = privateKeyRSA.publickey()
    hashValue = SHA256.new(data)
    signFunction = pss.new(privateKeyRSA)
    start = time.process_time()
    firma = signFunction.sign(hashValue)
    end = time.process_time()
    tiempo = end - start
    return firma, publicKeyRSA, hashValue, tiempo
  
  def rsa_pss_verif(self, firma, publicKeyRSA, hashValue):
    verifier = pss.new(publicKeyRSA)
    verifier.verify(hashValue, firma)
    start = time.process_time()
    verifier.verify(hashValue, firma)
    end = time.process_time()
    tiempo = end - start
    return tiempo


  def dsa_sign(self, data):
    key = DSA.generate(1024)
    hashValue = SHA512.new(data)
    controler = DSS.new(key, 'fips-186-3')
    start = time.process_time()
    firma = controler.sign(hashValue)
    end = time.process_time()
    tiempo = end - start
    return firma, hashValue, controler, tiempo

  def dsa_verif(self, firma, hashValue, controler):
    start = time.process_time()
    try:
      controler.verify(hashValue, firma)
    except ValueError:
      print("El mensaje no es autentico")
    end = time.process_time()
    tiempo = end - start
    return tiempo
  
  def ecdsa_binary_sign(self, data):
    private_key = ec.generate_private_key(ec.SECT571K1())
    start = time.process_time()
    firma = private_key.sign(data,ec.ECDSA(hashes.SHA256()))
    end = time.process_time()
    tiempo = end - start
    return firma, private_key.public_key(), tiempo
  
  def ecdsa_binary_verif(self, firma, data, public_key):
    start = time.process_time()
    try:
      public_key.verify(firma, data, ec.ECDSA(hashes.SHA256()))
    except InvalidSignature:
      print("El mensaje no es autentico")
    end = time.process_time()
    tiempo = end - start
    return tiempo

  def ecdsa_prime_sign(self, data):
    private_key = ec.generate_private_key(ec.SECP521R1())
    start = time.process_time()
    firma = private_key.sign(data,ec.ECDSA(hashes.SHA256()))
    end = time.process_time()
    tiempo = end - start
    return firma, private_key.public_key(), tiempo
  
  def ecdsa_prime_verif(self, firma, data, public_key):
    start = time.process_time()
    try:
      public_key.verify(firma, data, ec.ECDSA(hashes.SHA256()))
    except InvalidSignature:
      print("El mensaje no es autentico")
    end = time.process_time()
    tiempo = end - start
    return tiempo



  def correrPrueba(self):
    for vector in self.vectores:
      n = int(vector['modulo'], 16)
      e = int(vector['exponente_publico'], 16)
      d = int(vector['exponente_privado'], 16)
      firma, public_key, tiempo = self.ecdsa_binary_sign(vector['vector'])
      self.armarResultado(tiempo, vector['nombre'],'ecdsa-binary-signing')

      tiempo = self.ecdsa_binary_verif(firma, vector['vector'], public_key)
      self.armarResultado(tiempo, vector['nombre'],'ecdsa-binary-verif')

      firma, public_key, tiempo = self.ecdsa_prime_sign(vector['vector'])
      self.armarResultado(tiempo, vector['nombre'],'ecdsa-prime-signing')

      tiempo = self.ecdsa_prime_verif(firma, vector['vector'], public_key)
      self.armarResultado(tiempo, vector['nombre'],'ecdsa-prime-verif')

      firma, hashValue, controler, tiempo = self.dsa_sign(vector['vector'])
      self.armarResultado(tiempo, vector['nombre'],'dsa-signing')

      tiempo = self.dsa_verif(firma, hashValue, controler)
      self.armarResultado(tiempo, vector['nombre'],'dsa-verif')

      firma, hashValue, controler, tiempo = self.rsa_pss_sign(vector['vector'], n, e, d)
      self.armarResultado(tiempo, vector['nombre'],'rsa-pss-signing')

      tiempo = self.rsa_pss_verif(firma, hashValue, controler)
      self.armarResultado(tiempo, vector['nombre'],'rsa-pss-verif')
    self.resultados.escribirResultados()



if __name__ == '__main__':
  sv = SignVerifTests('../../test_vectors/')
  sv.correrPrueba()
    