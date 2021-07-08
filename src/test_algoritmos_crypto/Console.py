#!/usr/bin/env python
import argparse
from os import path
from .SHATests import SHATests
from .AESTests import AESTests
from .SignVerifTests import SignVerifTests
from .RSAOAEPTest import RSAOAEPTest

class Console(object):
  def __init__(self):
      self.parser = argparse.ArgumentParser()
      self.args = None
  
  def argumentParse(self):
      self.parser.add_argument('--out-folder',nargs='?',type=str, default="/results",help='ruta de salida de los resultados en formato xlsx o excel')
      self.parser.add_argument('--test-folder',nargs='?',type=str, default="/test_vectors",help='nombre de la carpeta donde estaran los vectores de prueba')
      self.args = self.parser.parse_args()
  
  def iniciar(self):
    self.argumentParse()
    st = SHATests(self.args.test_folder, self.args.out_folder)
    st.correrPrueba()
    at = AESTests(self.args.test_folder, self.args.out_folder)
    at.correrPrueba()
    sv = SignVerifTests(self.args.test_folder, self.args.out_folder)
    sv.correrPrueba()
    ro = RSAOAEPTest(self.args.test_folder, self.args.out_folder)
    ro.correrPrueba()
    
