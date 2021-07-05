#!/usr/bin/env python
import argparse

class Console(object):
  def __init__(self):
      self.parser = argparse.ArgumentParser()
      self.args = None
  
  def argumentParse(self):
      self.parser.add_argument('--out-file',nargs='?',type=str, default="/results",help='ruta de salida de los resultados en formato xlsx o excel')
      self.parser.add_argument('--test-folder',nargs='?',type=str, default="/test_vectors",help='nombre de la carpeta donde estaran los vectores de prueba')
      self.args = self.parser.parse_args()
  
  def iniciar(self):
    self.argumentParse()
    
