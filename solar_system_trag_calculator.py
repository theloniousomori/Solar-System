import numpy as np


class planet:
    def __init__(self, name, m, r0, v0, period):
        self.name = name
        self.period = int(period * 24 * 60 * 60)
        self.n_days = period
        self.t_steps = np.linspace(0, int(self.period), int(1e7))
        self.dt = self.t_steps[1] - self.t_steps[0]
        self.step = int((60*60*24)/self.dt)
        self.a = np.zeros((len(self.t_steps),3))
        self.v = np.zeros((len(self.t_steps),3))
        self.r = np.zeros((len(self.t_steps),3))
        self.m = m
        self.v[0] = v0
        self.r[0] = r0
        self.trag = np.zeros((self.n_days, 3))
    
    def calculate_trag(self):
        if self.step > 1:
            r_sun = np.zeros((len(self.t_steps),3))
            for i in range(0, len(self.t_steps) - 1):
                r_hat = self.r[i] / np.linalg.norm(self.r[i])
                self.a[i + 1] = - r_hat * G * m_sun / (np.linalg.norm(self.r[i]) ** 2)
                self.v[i + 1] = self.v[i] + self.a[i] * self.dt
                self.r[i + 1] = self.r[i] + self.v[i] * self.dt

                if i % 1000 == 0:  
                    print(f"{self.name} Progress: {i / len(self.t_steps) * 100}%")
            sun_trag = np.zeros((self.n_days,3))
            for i in range(0, self.n_days):
                self.trag[i] = self.r[i * self.step]
                sun_trag[i] = r_sun[i * self.step]
                print(i/len(self.trag) * 100)
            np.save(f'planet_data/{self.name}_trag', self.trag)
            np.save('planet_data/Sun_trag', sun_trag)
            print('Tragectories Calculated!')
        else:
            print('error skip is too small')



#assume sun to be fixed in place
m_sun = 1.989e30
G = 6.674e-11
AU = 1.496e11
    
Earth = planet('Earth',5.972e24, np.array([AU,0,0]), np.array([0, 29.75e3, 0]), 365) 
Mars = planet('Mars',0.642e24, np.array([1.5 * AU,0,0]), np.array([0, 24.1e3, 0]), 687)
Jupiter = planet('Jupiter', 1898.13e24, np.array([5.2* AU,0,0]), np.array([0, 13.06e3,0]), 4331)
Neptune = planet('Neptune', 102e24, np.array([30* AU,0,0]), np.array([0, 5.45e3,0]), 59800)
Uranus = planet('Uranus', 87e24, np.array([19* AU,0,0]), np.array([0, 6.79e3,0]), 30589)
Saturn = planet('Saturn', 568e24, np.array([9.54 * AU,0,0]), np.array([0, 9.67e3,0]), 10747)
Venus = planet('Venus', 4.87e24, np.array([0.72 * AU,0,0]), np.array([0, 35e3,0]), 225)
Mercury = planet('Mercury', 0.33e24, np.array([0.38 * AU,0,0]), np.array([0, 47.36e3,0]), 88)

Mercury.calculate_trag()
Earth.calculate_trag()
Mars.calculate_trag()
Jupiter.calculate_trag()
Neptune.calculate_trag()
Uranus.calculate_trag()
Saturn.calculate_trag()
Venus.calculate_trag()

