#! python3
import os, sys

#cmd = "pip uninstall -y lightpipes"
#cmd = "pip install lightpipes"
#returned_value = os.system(cmd)  # return the exit code in unix
#print('returned value:', returned_value)
import time
import matplotlib.pyplot as plt


from LightPipes import *
#help(LPdemo)
#LPdemo()
print('Executed with python version: ' + sys.version)
print('using LightPipes version: ' + LPversion)
#LPtest()

wavelength=20*um
size=30.0*mm
N=2000

#LPhelp()
F=Begin(size,wavelength,N)
#F=GaussBeam(size,wavelength,N,size/40,0.04,0)
#F1=PointSource(size,wavelength,N,-0.6*mm,0)
#F2=PointSource(size,wavelength,N, 0.6*mm,0)
#F.field[1][1]=2.0+1j*10
#F=GaussScreen(5,5*mm,-5*mm,0.6,F)

#F=CircAperture(10*mm, 0,0, F)
# F1=CircAperture(0.15*mm, -0.6*mm,0, F)
# F2=CircAperture(0.15*mm, 0.6*mm,0, F)    
# F=BeamMix(F1,F2)
# print(Strehl(F))
#F=GaussHermite(3,0,1,2*mm,F)
F=GaussLaguerre(3,0,1,2*mm,F) 
# start_time = time.time()
F=Fresnel(200*cm,F)
# print("Execution time: --- %4.2f seconds ---" % (time.time() - start_time)) 
# print(Strehl(F))

#print(F.field[1000][1000])
#(0.7745966692414834+0j) Py  GaussAperture
#(0.7745966692414834+0j) C++ GaussAperture
#(0.7745971856385743+0j) C++ GaussScreen
#(0.7745971856385743+0j) Py  GaussScreen
#(0.006281897522507002-0.014192976297891407j) C++ Fresnel
#(0.006281839301893334-0.014193002066545864j) Py  Fresnel
#(0.0231791443628783 - 0.006580876619145629j) C++ Forvard
#(0.023181814976935982-0.006571462915263024j) Py  Forvard
#(-1.8207623436959382e-36+0j) Py  GaussHermite
#(-1.8207623436959376e-36+0j) C++ Gausshermite
#(7.920909571258688e-30+0j)  Py GaussLaguerre
#(1.9802911769117567e-30+0j) C++ GaussLaguerre

I=Intensity(1,F)

  
plt.imshow(I,cmap='rainbow');plt.axis('off')
# #plt.contourf(I,50); plt.axis('equal')
plt.show()

