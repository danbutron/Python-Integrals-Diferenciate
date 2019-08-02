import os,glob,subprocess
from sympy import *

init_printing(use_unicode=True)
x = Symbol('x')
nombre = input("Nombre de el pdf ")
nombretex = nombre+'.tex'
nombreaux=nombre+'.aux'
nombrelog=nombre+'.log'

salto='$\\\\$'

header = r'''\documentclass[a4paper]{article}
   \begin{document}
   '''


footer = r'''\end{document}'''

content = header

def derivacion():
   Sign = '$'
   func = input("funcion a derivar en terminos de x ")
   mas= '+'
   C='\\\\'
   equal='='
   equal= equal
   n=C
   a =latex(Derivative(func,x))
   b= latex(diff(func,x))
   a = a
   b= b 
   contenido =Sign+a  +equal+ b + C+Sign+salto
   return contenido

def integracion():
   Sign = '$'
   func = input("funcion a integrar en terminos de x ")
   mas= '+'
   C='+C\\\\'
   equal='='
   equal= equal
   n=C
   a =latex(Integral(func,x))
   b= latex(integrate(func,x))
   a = a
   b= b 
   contenido =Sign+a  +equal+ b + C+Sign+salto
   return contenido

i=int(input("1 para ingresar otra derivada,2 para integral y 3 para salir : "))

while i !=3:
	if i==1:
		content=content + derivacion()
	elif i==2:
		content=content + integracion()
	print('1 para  derivar')
	print('2 para integral')
	i=int(input("2 para integral y 3 para salir : "))
	print(content)
  
	   

content = content + footer

print(content)
with open(nombretex,'w') as f:
        f.write(content)

commandLine = subprocess.Popen(['pdflatex', nombretex])
commandLine.communicate()
os.unlink(nombreaux)
os.unlink(nombrelog)
os.unkink(nombretex)
