import rebound
from math import pi

sim = rebound.Simulation()
sim.integrator = "whfast"
sim.dt = 0.001 

# set parameters
m_alc_a = 3.6      # As a fraction of the mass of the sun
m_alc_b =  0.1       
m_alc_c =  1.8
m_planet = 3e-6


a_alc_b =  0.16  # AU      
a_alc_c =  5   
a_planet = 50

e_alc_b = 0.01
e_alc_c =  0.01   
e_planet = 0.01

# add objects to system
sim.add(m=m_alc_a)
sim.add(m=m_alc_b, a=a_alc_b, e=e_alc_b)
sim.add(m=m_alc_c, a=a_alc_c, e=e_alc_c)
sim.add(m=m_planet, a=a_planet, e=e_planet)

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

# iterate through n integrations. 
# rebound represents an Earth year as 2pi for m = m_sol, a = 1 AU

for i in range(0, 10000000, 1000):
        sim.move_to_com()
        sim.integrate(i*2*pi)
       
        alc_b_dist = ps[1].calculate_orbit().d    
        alc_c_dist = ps[2].calculate_orbit().d     
        plan_dist = ps[3].calculate_orbit().d     
    
        print(i, alc_b_dist, alc_c_dist, plan_dist)
    
        # 200 AU means you are headed to deep space
        if any([x > 200 for x in [alc_b_dist, alc_c_dist, plan_dist]]):
            break
            
            
        

