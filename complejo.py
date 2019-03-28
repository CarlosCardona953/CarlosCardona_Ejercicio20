import numpy as np


class Complejo  ():
    
    def __init__(self,r,i):
        
        self.complejo = (r + i*1j)
        self.imaginario = self.complejo.imag
        self.real= self.complejo.real
        self.norma = np.sqrt(self.imaginario**2 + self.real**2 )
        
        
    def conjugado(self):
        self.real= -self.real
        self.imaginario= -self.imaginario
    
    def calcula_norma(self):
        self.norma
    
    def pow(self,n):
        
        i= self.imaginario**n
        r= self.real**n
        return  (r+i*1j)