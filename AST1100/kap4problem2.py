from scitools.std import *

class galaxy:
    def __init__(self, name, gal_dist, gal_vel):
        self.name = name
        self.filename = name + '.txt'
        self.gal_dist = gal_dist
        self.gal_vel = gal_vel
        self.wavelength = []
        self.ang_dist = []

        self.read_file()
        self.dist_observation()
        self.rel_velocity()
        self.rot_curve()
        self.density_profile()
      

    def read_file(self):
        self.infile = open(self.filename, 'r')
        for line in self.infile:
            numbers = line.split()
            self.ang_dist.append(float(numbers[0]))
            self.wavelength.append(float(numbers[1]))
        
        self.infile.close()

        self.ang_dist = array(self.ang_dist)
        self.wavelength = array(self.wavelength)

        return self.ang_dist, self.wavelength

    def dist_observation(self):
        radians = self.ang_dist*(1/3600.)*(2*pi/360.)
        self.dist = self.gal_dist*radians

        return self.dist

    def rel_velocity(self):
        lambda0 = 21.2/100.
        c = 299792458

        self.rad_vel = c*((self.wavelength-lambda0)/lambda0)
	self.rad_vel = self.rad_vel/1000.
        self.rel_vel = self.rad_vel - self.gal_vel

        return self.rad_vel, self.rel_vel

    def rot_curve(self):
        kpc = 3.26*9.4605284*10**15*1000
        self.dist = self.dist/(kpc)
        self.rel_vel = self.rel_vel/1000.

        plot(self.dist, self.rel_vel, 
        xlabel='Distance [kpc]', ylabel='Relative velocity [km/s]',
        title='Plot of relative velocity vs distance from the center of galaxy')
        
        figure()

    def density_profile(self):
        G = 6.673*10**-11
        kpc = 3.26*9.4605284*10**15*1000
        solar_mass = 1.9891*10**30

        self.density = self.rel_vel**2/(4*pi*G*self.dist**2)
        self.dist = self.dist/kpc
        self.density = self.density/(solar_mass/(3.26*9.4605284*10**15))
       
        plot(self.dist, self.density,
        xlabel='Distance [kpc]', ylabel='Density [solar mass/pc**3]',
        title='Plot of density profile of galaxy vs distance')
'''
    def constants(self):
        rho0 = float(raw_input('rho_0 = ')
        R_min = float(raw_input('Type in minimum value of R: '))
        R_max = float(raw_input('Type in maximum value of R: '))
        

        R_best = R_min
        best_delta = sum((...)**2)
        R = linspace(0.01, 20, 100)

        for i in range(len(R)):
            mod_density = ...
            delta = sum((...)**2)

            if delta < best_delta:
                delta_best = delta
                R_best = R[i]
'''

galaxy0 = galaxy('galaxy0', 32.0*10**3, 120)
galaxy1 = galaxy('galaxy1', 4.0*10**3, -75)
galaxy2 = galaxy('galaxy2', 12.0*10**3, 442)

raw_input('Press Enter: ')
