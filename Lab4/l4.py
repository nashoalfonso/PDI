from SimpleCV import Image, Camera, Display, Image, Color
import time
import matplotlib.pyplot as plt
import numpy as np


imagen=Image('/home/pi/lunar_con_pelos.png')
#imagen.show()

#se prueba distintos metodos para ver si detecta los bellos en la piel
ed=imagen.edges()
edg=imagen+ed
edg.save('bordes_edge.png')

grad = imagen.morphGradient()
grd = imagen+grad
grd.save('bordes_gradiente.png')

lineas=imagen.findLines()
lineas.draw(Color.RED,width=3)
#imagen.show()
imagen.save("linbeas.png")

resu = imagen.resize(320,240) #se redefine la imagen para que tenga un menor tiempo 
                             #de procesamiento
gray=resu.grayscale()
inv=gray.invert()
sumimg=resu+inv
res=(resu*1.5)-(gray/2)
res.save('muestras/imagen_tratada.png')

[red, green, blue]=res.splitChannels(False)

def Rho(A,B): # A es el color del lunar y B es el color de la piel
   Ar=A[0]; Ag=A[1]; Ab=A[2]
   Br=B[0]; Bg=B[1]; Bb=B[2]
   r=np.array([Ar/Br,Ar/Bg,Ar/Bb,Ag/Br,Ag/Bg,Ag/Bb,Ab/Br,Ab/Bg,Ab/Bb])

   return r

A=np.array([30,50,65],dtype='float64')
B=np.array([220,210,150],dtype='float64')

rho=Rho(A,B)

matrix= res.getNumpy().astype(dtype='float64') 
filas = 320 
columnas = 240
bordesHs=np.zeros((filas,columnas,3))
bordesHi=np.zeros((filas,columnas,3))
bordesVd=np.zeros((filas,columnas,3))
bordesVi=np.zeros((filas,columnas,3))
borde_rojo=np.array([220,0,0],dtype='float64')
brdsHs=np.zeros((filas,columnas,3))
brdsHi=np.zeros((filas,columnas,3))
brdsVd=np.zeros((filas,columnas,3))
brdsVi=np.zeros((filas,columnas,3))
eps=2.1 #se configura epsilon

eps2=2.2

# borde horizontal
for i in range(0,filas-2):
    for j in range(0,columnas-2):  
        At=matrix[i][j+1] # pixel del lunar
        Bt=matrix[i+2][j+1] # pixel de la piel
        rhot=Rho(At,Bt)  
        rhot2=Rho(Bt,At) 
        if (np.linalg.norm(rho-rhot)<eps): #recorre la matriz en busca de bordes 
            bordesHs[i+1][j+1]=borde_rojo   #superior e inferior
        elif(np.linalg.norm(rho-rhot2)<eps): 
            bordesHi[i+1][j+1]=borde_rojo 

#borde vertical
for i in range(0,filas-2): 
    for j in range(0,columnas-2):
        At=matrix[i+1][j]
        Bt=matrix[i+1][j+2]
        rhot=Rho(At,Bt)
        rhot2=Rho(Bt,At)        
        if (np.linalg.norm(rho-rhot)<eps):
            bordesVd[i+1][j+1]=borde_rojo
        elif (np.linalg.norm(rho-rhot2)<eps):    
            bordesVi[i+1][j+1]=borde_rojo



imborHs=Image(bordesHs)
imborHi=Image(bordesHi)
imborVd=Image(bordesVd)
imborVi=Image(bordesVi)
imbor=imborHs+imborHi+imborVd+imborVi
imbor.save('muestras/bordes.png')
imdet=imbor+res
imdet.sideBySide(imbor)
imdt = imdet.resize(640,480)
imnd=imagen.sideBySide(imdt)
imnd.show() 
imnd.save('muestras/lunar_con_bordes.png')

###

matrix2= resu.getNumpy().astype(dtype='float64')             
   
# borde horizontal
for i in range(0,filas-2):
    for j in range(0,columnas-2):  
        At=matrix2[i][j+1] # pixel del lunar
        Bt=matrix2[i+2][j+1] # pixel de la piel
        rhot=Rho(At,Bt)  
        rhot2=Rho(Bt,At) 
        if (np.linalg.norm(rho-rhot)<eps2): #recorre la matriz en busca de bordes 
            brdsHs[i+1][j+1]=borde_rojo   #superior e inferior
        elif(np.linalg.norm(rho-rhot2)<eps2): 
            brdsHi[i+1][j+1]=borde_rojo 

#borde vertical
for i in range(0,filas-2): 
    for j in range(0,columnas-2):
        At=matrix2[i+1][j]
        Bt=matrix2[i+1][j+2]
        rhot=Rho(At,Bt)
        rhot2=Rho(Bt,At)        
        if (np.linalg.norm(rho-rhot)<eps2):
            brdsVd[i+1][j+1]=borde_rojo
        elif (np.linalg.norm(rho-rhot2)<eps2):    
            brdsVi[i+1][j+1]=borde_rojo


imbHs=Image(brdsHs)
imbHi=Image(brdsHi)
imbVd=Image(brdsVd)
imbVi=Image(brdsVi)
imbr=imbHs+imbHi+imbVd+imbVi
imbr.save('muestras/bordes_final.png')
imdt=imbr+res
imdt.sideBySide(imbr)
imnd = imdt.resize(640,480)
imnd=imagen.sideBySide(imdt)
imnd.show() 
imnd.save('muestras/lunar_con_bordes_final.png')



