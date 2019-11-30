#Python Projects for beginners
#Generating sine and cosine curve
#https://www.codementor.io/ilyaas97/6-python-projects-for-beginners-yn3va03fs#generating-a-sine-vs-cosine-curve

import numpy as np
import matplotlib.pylab as plt
plt.show()
x=np.linspace(-360,360,180)
x=np.deg2rad(x)
y1=np.sin(x)
y2=np.cos(x)

#Drawing sin and cos functions
plt.plot(x,y1,color='blue',linewidth=1.5, label="Sin(x)")
plt.scatter([-np.deg2rad(180),-np.deg2rad(90),np.deg2rad(0),np.deg2rad(90),np.deg2rad(180)],[0,-1,0,1,0],c='green')
plt.plot(x,y2,color='orange', label="Cos(x)")
plt.scatter([-np.deg2rad(180),-np.deg2rad(90),np.deg2rad(0),np.deg2rad(90),np.deg2rad(180)],[-1,0,1,0,-1],c='red',marker='+')
plt.xlabel('Angle [rad]')
plt.ylabel('sin(x):blue \n cos(x):orange')
plt.legend()
#plt.axis('tight')
plt.show()


