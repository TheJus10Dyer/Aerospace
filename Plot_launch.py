# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 12:22:51 2022

@author: Justin

LAUNCH DATA 
"""

import numpy as np
import matplotlib.pyplot as plt

#Load Data
data = np.loadtxt('Launch_t_gxyz_mxyz_eaxyz_iaxyz_T.txt')
data2 = np.loadtxt('Launch_t_axyz_p_rH_Te_T.txt')

#Assign variables to data
#First txt
time = data[:,0]
gx = data[:,1]
gy = data[:,2]
gz = data[:,3]
mx = data[:,4]
my = data[:,5]
mz = data[:,6]
eax = data[:,7]
eay = data[:,8]
eaz = data[:,9]
iax = data[:,10]
iay = data[:,11]
iaz = data[:,12]
T = data[:,13]

#Second txt
time2 = data2[:,0]
ax = data2[:,1]
ay = data2[:,2]
az = data2[:,3]
p = data2[:,4]
rH = data2[:,5]
Te = data2[:,6]
T2 = data2[:,7]


#Set launch time
tlaunch = 1350
tlaunch2 = 1294

#Adjust data to launch time
gx = gx[time>tlaunch]
gy = gy[time>tlaunch]
gz = gz[time>tlaunch]
mx = mx[time>tlaunch]
my = my[time>tlaunch]
mz = mz[time>tlaunch]
eax = eax[time>tlaunch]
eay = eay[time>tlaunch]
eaz = eaz[time>tlaunch]
iax = iax[time>tlaunch]
iay = iay[time>tlaunch]
iaz = iaz[time>tlaunch]
T = T[time>tlaunch]
ax = ax[time2>tlaunch2]
ay = ay[time2>tlaunch2]
az = az[time2>tlaunch2]
p = p[time2>tlaunch2]
rH = rH[time2>tlaunch2]
Te = Te[time2>tlaunch2]
T2 = T2[time2>tlaunch2]
time = time[time>tlaunch]
time2 = time2[time2>tlaunch2]

## Set launch land time
tland = 1550
tland2 = 1494

#Adjust data to land time
gx = gx[time<tland]
gy = gy[time<tland]
gz = gz[time<tland]
mx = mx[time<tland]
my = my[time<tland]
mz = mz[time<tland]
eax = eax[time<tland]
eay = eay[time<tland]
eaz = eaz[time<tland]
iax = iax[time<tland]
iay = iay[time<tland]
iaz = iaz[time<tland]
T = T[time<tland]
ax = ax[time2<tland2]
ay = ay[time2<tland2]
az = az[time2<tland2]
p = p[time2<tland2]
rH = rH[time2<tland2]
Te = Te[time2<tland2]
T2 = T2[time2<tland2]
time = time[time<tland]
time2 = time2[time2<tland2]
time -= time[0]
time2 -= time2[0]


####PLOT RAW DATA

###PLOT RAW External ACCEL
plt.figure()
plt.plot(time,eax, 'b-', label = 'X Axis')
plt.plot(time,-eay, 'r-', label = 'Y Axis')
plt.plot(time,eaz, 'g-', label = 'Z Axis')
plt.xlabel('Time (seconds)')
plt.ylabel('Acceleration (m/s^2)')
plt.title('Raw External Acceleration (DO NOT TRUST)')
plt.grid()
plt.legend()


#Set gravity
g = 9.81

##get magnitude of external accel
eaxyz = np.sqrt(eax**2+eay**2+eaz**2)-g

#Plot magnitude of external accel
plt.figure()
plt.plot(time,eaxyz, 'b-')
plt.xlabel('Time (seconds)')
plt.ylabel('Acceleration (m/s^2)')
plt.title('External Acceleration Magnetude (DO NOT TRUST)')
plt.grid()

#Integrate accel to get velo
evelo = eaxyz*0
for i in range(0,len(eaxyz)-1):
    evelo[i+1] = evelo[i]+(eaxyz[i]*(time[i+1]-time[i]))

#Plot external velo
plt.figure()
plt.plot(time,evelo, 'b-')
plt.xlabel('Time (seconds)')
plt.ylabel('Velocity (m/s)')
plt.title('External Velocity (DO NOT TRUST)')
plt.grid()

#Integrate velo to get position
epos = evelo*0
for i in range(0,len(evelo)-1):
    epos[i+1] = epos[i]+(evelo[i]*(time[i+1]-time[i]))
    
    
#Plot external position
plt.figure()
plt.plot(time,epos, 'b-')
plt.xlabel('Time (seconds)')
plt.ylabel('Altitude (m)')
plt.title('External Position (DO NOT TRUST)')
plt.grid()
    

###PLOT RAW Internal ACCEL1
plt.figure()
plt.plot(time,iax, 'b-', label = 'X Axis')
plt.plot(time,-iay, 'r-', label = 'Y Axis')
plt.plot(time,iaz, 'g-', label = 'Z Axis')
plt.xlabel('Time (seconds)')
plt.ylabel('Acceleration (m/s^2)')
plt.title('Raw Internal Acceleration1 (DO NOT TRUST)')
plt.grid()
plt.legend()


##get magnitude of external accel
iaxyz = np.sqrt(iax**2+iay**2+iaz**2)

#Plot magnitude of external accel
plt.figure()
plt.plot(time,iaxyz, 'b-')
plt.xlabel('Time (seconds)')
plt.ylabel('Acceleration (m/s^2)')
plt.title('Internal Acceleration Magnetude (DO NOT TRUST)')
plt.grid()

#Integrate accel to get velo
ivelo = iaxyz*0
for i in range(0,len(iaxyz)-1):
    ivelo[i+1] = ivelo[i]+(iaxyz[i]*(time[i+1]-time[i]))

#Plot external velo
plt.figure()
plt.plot(time,ivelo, 'b-')
plt.xlabel('Time (seconds)')
plt.ylabel('Velocity (m/s)')
plt.title('Internal Velocity (DO NOT TRUST)')
plt.grid()

#Integrate velo to get position
ipos = ivelo*0
for i in range(0,len(ivelo)-1):
    ipos[i+1] = ipos[i]+(ivelo[i]*(time[i+1]-time[i]))
    
    
#Plot internal position
plt.figure()
plt.plot(time,ipos, 'b-')
plt.xlabel('Time (seconds)')
plt.ylabel('Altitude (m)')
plt.title('Internal Position (DO NOT TRUST)')
plt.grid()


###PLOT RAW External GYRO
plt.figure()
plt.plot(time,gx, 'b-', label = 'X Axis')
plt.plot(time,gy, 'r-', label = 'Y Axis')
plt.plot(time,gz, 'g-', label = 'Z Axis')
plt.xlabel('Time (seconds)')
plt.ylabel('Angular Acceleration (rad/s^2)')
plt.title('Raw angular Acceleration')
plt.grid()
plt.legend()

###PLOT RAW Magnetometer
plt.figure()
plt.plot(time,mx, 'b-', label = 'X Axis')
plt.plot(time,my, 'r-', label = 'Y Axis')
plt.plot(time,mz, 'g-', label = 'Z Axis')
plt.xlabel('Time (seconds)')
plt.ylabel('Magenetic Field Strength (uT)')
plt.title('Raw Magnetometer')
plt.grid()
plt.legend()


###PLOT RAW Temperature1
plt.figure()
plt.plot(time,T, 'b-')
plt.xlabel('Time (seconds)')
plt.ylabel('Temperature (Celcius)')
plt.title('Raw Temperature 1')
plt.grid()

###PLOT RAW Temperature2
plt.figure()
plt.plot(time2,T2, 'b-')
plt.xlabel('Time (seconds)')
plt.ylabel('Temperature (Celcius)')
plt.title('Raw Temperature 2')
plt.grid()

###PLOT RAW External Temperature
plt.figure()
plt.plot(time2,Te, 'b-')
plt.xlabel('Time (seconds)')
plt.ylabel('Temperature (Celcius)')
plt.title('Raw External Temperature')
plt.grid()

###PLOT RAW Internal ACCEL2
plt.figure()
plt.plot(time2,ax, 'b-', label = 'X Axis')
plt.plot(time2,ay, 'r-', label = 'Y Axis')
plt.plot(time2,az, 'g-', label = 'Z Axis')
plt.xlabel('Time (seconds)')
plt.ylabel('Acceleration (m/s^2)')
plt.title('Raw Internal Acceleration2')
plt.grid()
plt.legend()

###PLOT RAW Pressure
plt.figure()
plt.plot(time2,p, 'b-')
plt.xlabel('Time (seconds)')
plt.ylabel('Pressure (hPa)')
plt.title('Raw Pressure')
plt.grid()

###PLOT RAW Relative Humidity
plt.figure()
plt.plot(time2,rH, 'b-')
plt.xlabel('Time (seconds)')
plt.ylabel('Relative Humidity (%)')
plt.title('Raw Relative Humidity')
plt.grid()

## Apply international barometric formula to get altitude
alt = (44330*(1-(p/1013.25)**(1/5.255)))#*3.28084 #for ft

###PLOT altitude from pressure
plt.figure()
plt.plot(time2,alt,'b-')
plt.xlabel('Time (seconds)')
plt.ylabel('Altitude (m)')
plt.title('Altitude from Pressure Data')
plt.grid()

### Take the derivative of Altitude to get vertiacal velocity
velo = 0*alt
for i in range(0,len(alt)-1):
    velo[i+1] = ((alt[i+1]-alt[i])/(time2[i+1]-time2[i]))


### Plot vertical velocity
plt.figure()
plt.plot(time2,velo,'b-')
plt.xlabel('Time (seconds)')
plt.ylabel('Velocity (m/s)')
plt.title('Vertical Velocity from Pressure Data')
plt.grid()

### Take the derivative of vertiacal velocity to get vertiacal 
##acceleration
accel = 0*velo
for i in range(0,len(velo)-1):
    accel[i+1] = ((velo[i+1]-velo[i])/(time2[i+1]-time2[i]))

##Plot vertical acceleration
plt.figure()
plt.plot(time2,accel,'b-')
plt.xlabel('Time (seconds)')
plt.ylabel('Acceleration (m/s^2)')
plt.title('Vertical Acceleration from Pressure Data')
plt.grid()

