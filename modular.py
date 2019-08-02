import os,glob,subprocess
from sympy import *

init_printing(use_unicode=True)
x = Symbol('x')
name = input("Name of the pdf file ")
nametex = name+'.tex'
nameaux=name+'.aux'
namelog=name+'.log'

jump='$\\\\$'

header = r'''\documentclass[a4paper]{article}
   \begin{document}
   '''


footer = r'''\end{document}'''

content = header

def derivacion():
   Sign = '$'
   func = input("function to derive in terms x")
   mas= '+'
   C='\\\\'
   equal='='
   equal= equal
   n=C
   a =latex(Derivative(func,x))
   b= latex(diff(func,x))
   a = a
   b= b 
   contenido =Sign+a  +equal+ b + C+Sign+jump
   return contenido

def integracion():
   Sign = '$'
   func = input("function to integrate in terms x ")
   mas= '+'
   C='+C\\\\'
   equal='='
   equal= equal
   n=C
   a =latex(Integral(func,x))
   b= latex(integrate(func,x))
   a = a
   b= b 
   contenido =Sign+a  +equal+ b + C+Sign+jump
   return contenido

i=int(input("1 add a derivative,2 add an integral y 3 EXIT : "))

while i !=3:
	if i==1:
		content=content + derivacion()
	elif i==2:
		content=content + integracion()
	print('1 add a derivative')
	print('2 add an integral')
	i=int(input("3 EXIT : "))
	print(content)
  
	   

content = content + footer

#print(content)
with open(nametex,'w') as f:
        f.write(content)

commandLine = subprocess.Popen(['pdflatex', nametex])
commandLine.communicate()
os.unlink(nameaux)
os.unlink(namelog)
os.unkink(nametex)
