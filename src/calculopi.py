#!/usr/bin/python

import modulo
n=0.0
m=0.0
l=[]
import sys
n = int(sys.argv[1])          #guarda el primer valor de los argumentos que hemos escrito desde la consola
m = int(sys.argv[2])          #guarda el segundo valor de los argumentos que hemos escrito desde la consola
s=modulo.calculo(n)
p=modulo.calculo(m)
l=l+[s]
l=l+[p]
print s
print p
print l