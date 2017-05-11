import rebound
from math import pi, sqrt

sim = rebound.Simulation()
sim.integrator = "whfast"
sim.dt = 0.01

m_magnus = 1.1          #2.19e30 kg
m_ignis =  0.26         #5.17e29 kg 
m_enkei =  2.83e-6      #5.63e24 kg

a_ignis = 0.2     # AU
a_enkei = 1.74    # AU

e_ignis = 0.01
e_enkei = 0.01 

sim.add(m=m_magnus)
sim.add(m=m_ignis, a=a_ignis, e=e_ignis)
sim.add(m=m_enkei, a=a_enkei, e=e_enkei)

ps = sim.particles

for i in range(100):
        sim.move_to_com()
        sim.integrate(i*1000*2*pi)
        d = sqrt((ps[1].x-ps[2].x)**2 + (ps[1].y-ps[2].y)**2)
        if i % 10 == 0:
            print(i, d)
            print(ps[1].calculate_orbit())
            print(ps[2].calculate_orbit())
            print()
                   
        if d > 100:
            break
        

