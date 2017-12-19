import rebound, numpy as np
from math import pi
from matplotlib import pyplot as plt

sim = rebound.Simulation()
sim.integrator = "whfast"
sim.dt = 0.01

# set parameters
m_star = 0.907      # As a fraction of the mass of the sun
m_labita =  3e-6       
m_vir =  3e-6
m_mena = 3e-6
m_kaldreer = 3e-6

a_labita =  0.53  # AU      
a_vir =  0.88   
a_mena = 1.24
a_kaldreer = 1.59

e_labita = 0.01
e_vir =  0.01   
e_mena = 0.01
e_kaldreer = 0.01

# add objects to system
sim.add(m=m_star)
sim.add(m=m_labita, a=a_labita, e=e_labita)
sim.add(m=m_vir, a=a_vir, e=e_vir)
sim.add(m=m_mena, a=a_mena, e=e_mena)
sim.add(m=m_kaldreer, a=a_kaldreer, e=e_kaldreer)

# handler for accessing planets
# index is in order of addition:
#   1 = sun
#   2 = labita
#   etc
ps = sim.particles

# lists to store plottable features
lab = []
vir = []
men = []
kal = []

# iterate through n integrations. Each integration is 100 years
# rebound represents an Earth year as 2pi

for i in range(10000):
        sim.move_to_com()
        sim.integrate(i*2*pi)
        
 
        
        if i % 100 == 0:
       
            #sun_dist = ps[0].calculate_orbit().d
            lab_dist = ps[1].calculate_orbit().d    
            vir_dist = ps[2].calculate_orbit().d     
            men_dist = ps[3].calculate_orbit().d     
            kal_dist = ps[4].calculate_orbit().d 
        
            print(i, lab_dist, vir_dist, men_dist, kal_dist)
        
#            lab.append(lab_dist)
#            vir.append(vir_dist)
#            men.append(men_dist)
#            kal.append(kal_dist)

            # 100 AU means you are headed to deep space
            if any([x > 100 for x in [lab_dist, vir_dist, men_dist, kal_dist]]):
                break
        

#ty = range(1000)       
        
#print("Labita", min(lab), max(lab))
#print("Vir", min(vir), max(vir))
#print("Mena", min(men), max(men))
#print("Kaldreer", min(kal), max(kal))
        
# adjust ty units to thousands of years
#ty = np.array(ty)

# make single plot
#plt.plot(ty, lab, 'r-', ty, vir, 'b-', ty, men, 'k-', ty, kal, 'g-')
#plt.show()


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
        

