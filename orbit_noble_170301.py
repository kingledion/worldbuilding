import rebound
from math import pi, sqrt

sim = rebound.Simulation()
sim.integrator = "whfast"
sim.dt = 0.01


m_star = 0.24119      #4.797e29 kg
m_paveiha = 9.4218e-7 #1.874e24 kg 
m_     #4.921e21 kg

a_paveiha = 0.07 # AU
a_jeah = 0.000122 # AU;relative to paveiha

e_paveiha = 0.011
e_jeah = 0.30 

sim.add(m=m_star)
sim.add(m=m_paveiha, a=a_paveiha, e=e_paveiha)
paveiha = sim.particles[-1]
sim.add(primary = paveiha, m=m_jeah, a=a_jeah, e=e_jeah)

ps = sim.particles

for i in range(100):
        sim.move_to_com()
        sim.integrate(i*1000*2*pi)
        d = sqrt((ps[1].x-ps[2].x)**2 + (ps[1].y-ps[2].y)**2)
        print(i, d)
        if d > 100:
            break
        
print(ps[1].calculate_orbit())
print(ps[2].calculate_orbit())
