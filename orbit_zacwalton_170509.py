import rebound, numpy as np
from math import pi
from matplotlib import pyplot as plt

sim = rebound.Simulation()
sim.integrator = "whfast"
sim.dt = 0.01

# set parameters
m_magnus = 1.1          #2.19e30 kg
m_ignis =  0.26         #5.17e29 kg 
m_enkei =  2.83e-6      #5.63e24 kg

a_ignis = 0.2     # AU
a_enkei = 1.74    # AU

e_ignis = 0.01
e_enkei = 0.01 

# add objects to system
sim.add(m=m_magnus)
sim.add(m=m_ignis, a=a_ignis, e=e_ignis)
sim.add(m=m_enkei, a=a_enkei, e=e_enkei)

# handler for accessing planets
# index is in order of addition:
#   1 = magnus
#   2 = ignis
#   3 = enkei
ps = sim.particles

# lists to store plottable features
ecc = []
sma = []
ty = []

# iterate through n integrations. Each integration is 100 years
# rebound represents an Earth year as 2pi
for i in range(200):
        sim.move_to_com()
        sim.integrate(i*2*pi)
        
        enkei_orbit = ps[2].calculate_orbit()     
        
        if i % 10 == 0:
            print(i, enkei_orbit.a)
        
        ty.append(i)
        ecc.append(enkei_orbit.e)
        sma.append(enkei_orbit.a)

        # 100 AU means you are headed to deep space
        if enkei_orbit.a > 100:
            break
        
# adjust ty units to thousands of years
ty = np.array(ty)

# make single plot
plt.plot(ty, sma, 'r-')


'''
# make dual plot     
fig, ax1 = plt.subplots()
ax1.plot(ty, ecc, 'b-')
ax1.set_xlabel("Time (years)")
ax1.set_ylabel('Eccentricity', color='b')
ax2 = ax1.twinx()
ax2.plot(ty, sma, 'r-')  
ax2.set_ylabel('Semi-major axis (AU)', color='r')    
'''
        

