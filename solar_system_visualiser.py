import numpy as np
from vpython import sphere, vector, rate, canvas, color, vec, label

# Load positions from the saved numpy arrays

AU = 1.496e11

class planet:
    def __init__(self, name, radius, color):
        self.name = name
        self.r = np.load(f'planet_data/{name}_trag.npy')
        self.radius = radius
        self.color = color
        self.x = self.r[:, 0]
        self.y = self.r[:, 1]
        self.z = self.r[:, 2]
    
    def load_data(self):
        self.planet = sphere(pos=vector(self.x[0], self.y[0], self.z[0]), radius=self.radius , color=self.color, make_trail=True)
        self.label = label(pos=vector(self.x[0], self.y[0], self.z[0]), text=self.name, xoffset=20, yoffset=50,space=30, height=16, border=4, box = False)

    def update_pos(self,index):
        index = index % len(self.x) #keeps it looped
        if self.name != 'Sun':
            self.label.text = f'{self.name}, distance from sun = {np.round(np.linalg.norm(self.r[index]) /AU, 2)} AU'
        self.planet.pos = vector(self.x[index], self.y[index], self.z[index])
        self.label.pos = vector(self.x[index], self.y[index], self.z[index])
        
    
    


# Create a VPython canvas
scene = canvas(title='Planetary Motion',
               color = vector(1, 0, 0),
               width=1200, height=900,
               center=vector(0, 0, 0),
               background=color.black)

# Create sphere objects for the two planets
sun = planet('Sun',1e10, color.yellow)
earth = planet('Earth',5e9, color.blue)
mars = planet('Mars', 5e9, color.red)
jupiter = planet('Jupiter', 7e9, color.orange)
neptune = planet('Neptune', 5e9, color.blue)
uranus = planet('Uranus', 5e9, color.cyan)
saturn = planet('Saturn', 7e9,  vec(1,0.7,0.2))
venus = planet('Venus', 5e9, color.yellow)
mercury = planet('Mercury', 5e9, color.black)



sun.load_data()
earth.load_data()
mars.load_data()
jupiter.load_data()
neptune.load_data()
uranus.load_data()
saturn.load_data()
venus.load_data()
mercury.load_data()

# Animation loop
i = 0
while True:
    i += 1
    rate(5)  # Adjust the rate to control the speed of the animation
    sun.update_pos(i)
    earth.update_pos(i)
    mars.update_pos(i)
    jupiter.update_pos(i)
    neptune.update_pos(i)
    uranus.update_pos(i)
    saturn.update_pos(i)
    venus.update_pos(i)
    mercury.update_pos(i)
