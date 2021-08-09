#!/usr/bin/env python
import argparse
from os import path
from .SHATests import SHATests
from .AESTests import AESTests
from .SignVerifTests import SignVerifTests
from .RSAOAEPTest import RSAOAEPTest
import logging
logging.basicConfig(filename='./test_algoritmos_crypto.log', level=logging.DEBUG)

class Console(object):
  def __init__(self):
      self.parser = argparse.ArgumentParser()
      self.args = None
  
  def argumentParse(self):
      self.parser.add_argument('--out-folder',nargs='?',type=str, default="/results",help='ruta de salida de los resultados en formato xlsx o excel')
      self.parser.add_argument('--test-folder',nargs='?',type=str, default="/test_vectors",help='nombre de la carpeta donde estaran los vectores de prueba')
      self.parser.add_argument('--num-iteraciones',nargs='?',type=int, default=10,help='Numero de iteraciones para pruebas')
      self.args = self.parser.parse_args()
  
  def iniciar(self):
    logging.info('Inicio de pruebas criptograficas')
    print('Inicio de pruebas criptograficas')
    self.argumentParse()
    st = SHATests(self.args.test_folder, self.args.out_folder)
    st.correrPruebaTotal(self.args.num_iteraciones)
    at = AESTests(self.args.test_folder, self.args.out_folder)
    at.correrPruebaTotal(self.args.num_iteraciones)
    sv = SignVerifTests(self.args.test_folder, self.args.out_folder)
    sv.correrPruebaTotal(self.args.num_iteraciones)
    ro = RSAOAEPTest(self.args.test_folder, self.args.out_folder)
    ro.correrPruebaTotal(self.args.num_iteraciones)
    
