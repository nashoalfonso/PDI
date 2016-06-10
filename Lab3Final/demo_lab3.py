from SimpleCV import Image, Camera, Display, Color
import time
import matplotlib.pyplot as plt
import numpy as np

cam=Camera()
imagen=cam.getImage()
imagen.save('muestras/lunar.png')
time.sleep(3)

#imagen=Image("muestras/lunar01.png")
#imagen.show()

res = imagen.resize(320,240)
#res.show()
[red, green, blue]=res.splitChannels(False)

def Rho(A,B): # A es el color del lunar y B es el color de la piel
   Ar=A[0]; Ag=A[1]; Ab=A[2]
   Br=B[0]; Bg=B[1]; Bb=B[2]
   r=np.array([Ar/Br,Ar/Bg,Ar/Bb,Ag/Br,Ag/Bg,Ag/Bb,Ab/Br,Ab/Bg,Ab/Bb])

   return r

A=np.array([30,50,65],dtype='float64')
B=np.array([230,220,150],dtype='float64')

rho=Rho(A,B)

matrix= res.getNumpy().astype(dtype='float64') 
filas = 320 
columnas = 240
bordesHs=np.zeros((filas,columnas,3))
bordesHi=np.zeros((filas,columnas,3))
bordesVd=np.zeros((filas,columnas,3))
bordesVi=np.zeros((filas,columnas,3))
borde_rojo=np.array([220,0,0],dtype='float64')
eps=2.1 #se configura epsilon

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


imnd=res.sideBySide(imdet)
imnd.show() 
imnd.save('muestras/lunar_con_bordes.png')

   
