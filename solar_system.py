import numpy as np
from vpython import sphere, vector, rate, canvas, color, vec, label

class planet:
    def __init__(self, name, m, r0, v0, radius, color):
        self.name = name
        self.a = np.zeros((1,3))
        self.m = m
        self.v = v0
        self.r = r0
        self.radius = radius
        self.color = color
        self.x = r0[0]
        self.y = r0[1]
        self.z = r0[2]
        print(self.x)

    def load_data(self):
        self.planet = sphere(pos=vector(self.x, self.y, self.z), radius=self.radius , color=self.color, make_trail=True)
        self.label = label(pos=vector(self.x, self.y, self.z), text=self.name, xoffset=20, yoffset=50,space=30, height=16, border=4, box = False)
    
    def iterate_pos(self, i):
        r_hat = self.r / np.linalg.norm(self.r)
        v = self.v
        r = self.r
        self.a = - r_hat * G * m_sun / (np.linalg.norm(self.r) ** 2)
        self.v = v + self.a * dt
        self.r = r + v * dt
        self.x = self.r[0] 
        self.y = self.r[1]
        self.z = self.r[2]
        self.label.text = f'{self.name}, distance from sun = {np.round(np.linalg.norm(self.r) /AU, 2)} AU'
        self.planet.pos = vector(self.x, self.y, self.z)
        self.label.pos = vector(self.x, self.y, self.z)
    




#assume sun to be fixed in place
dt = 60
m_sun = 1.989e30
r_sun = np.zeros((1,3))
G = 6.674e-11
AU = 1.496e11

scene = canvas(title='Planetary Motion',
               color = vector(1, 0, 0),
               width=1200, height=900,
               center=vector(0, 0, 0),
               background=color.black)
    
Earth = planet('Earth',5.972e24, np.array([AU,0,0]), np.array([0, 29.75e3, 0]),5e9, color.blue) 
Mars = planet('Mars',0.642e24, np.array([1.5 * AU,0,0]), np.array([0, 24.1e3, 0]), 5e9, color.red)
Jupiter = planet('Jupiter', 1898.13e24, np.array([5.2* AU,0,0]), np.array([0, 13.06e3,0]), 7e9, color.orange)
Neptune = planet('Neptune', 102e24, np.array([30* AU,0,0]), np.array([0, 5.45e3,0]), 5e9, color.blue)
Uranus = planet('Uranus', 87e24, np.array([19* AU,0,0]), np.array([0, 6.79e3,0]), 5e9, color.cyan)
Saturn = planet('Saturn', 568e24, np.array([9.54 * AU,0,0]), np.array([0, 9.67e3,0]), 7e9,  vec(1,0.7,0.2))
Venus = planet('Venus', 4.87e24, np.array([0.72 * AU,0,0]), np.array([0, 35e3,0]), 5e9, color.yellow)
Mercury = planet('Mercury', 0.33e24, np.array([0.38 * AU,0,0]), np.array([0, 47.36e3,0]), 5e9, color.white)
black_hole = planet('Blackhole', 0.33e24, np.array([0.38 * AU,0,0]), np.array([0, 47.36e3,0]), 5e9, color.white)

Mercury.load_data()
Earth.load_data()
Mars.load_data()
Jupiter.load_data()
Neptune.load_data()
Uranus.load_data()
Saturn.load_data()
Venus.load_data()
black_hole.load_data()

sun = sphere(pos=vector(0, 0, 0), radius=3e10 , color=color.yellow)

i = 0
while True:
    i += 1
    rate(1e10)
    Mercury.iterate_pos(i)
    Earth.iterate_pos(i)
    Mars.iterate_pos(i)
    Jupiter.iterate_pos(i)
    Neptune.iterate_pos(i)
    Uranus.iterate_pos(i)
    Saturn.iterate_pos(i)
    Venus.iterate_pos(i)
    black_hole.iterate_pos