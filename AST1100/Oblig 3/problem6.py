from scitools.std import *

class spectrum:
    def __init__(self, filename):
        self.filename = filename
        self.wavelength, self.flux = [], []

        self.read_data()
        self.plot_spectrum()
        self.star_velocity()
        self.model()

    def read_data(self):
        self.infile = open(self.filename, 'r')
        for line in self.infile:
            numbers = line.split()
            self.wavelength.append(float(numbers[0]))
            self.flux.append(float(numbers[1]))

        self.infile.close()

        self.wavelength = array(self.wavelength)
        self.flux = array(self.flux)

        return self.wavelength, self.flux

    def plot_spectrum(self):
        
        plot(self.wavelength, self.flux,
             xlabel='Observed wavelength [nm]', ylabel='Flux',
             title='Plot of observed wavelength vs flux')

    def star_velocity(self, c=299792458, lambda0=656.3):
        self.c, self.lambda0 = c, lambda0
        lambda_min = float(raw_input('Minimum wavelength of the flux: '))
        
        self.vel_rad = c*(self.wavelength-lambda0)/lambda0
        
        return self.vel_rad
    
    def model(self, c=299792458, lambda0 = 656.3):
        
        self.lambda0 = lambda0

        F_min = float(raw_input('Type in the minimum value of the flux: '))
        F_max = float(raw_input('Type in the maximum value of the flux: '))
        sigma_min =\
            float(raw_input('Type in the minimum value of the width: ')) 
        sigma_max =\
            float(raw_input('Type in the maximum value of the width: '))
        lambdacenter_min =\
            float(raw_input('Type in the minimum value of the central wavelength: '))
        lambdacenter_max =\
            float(raw_input('Type in the maximum value of the central wavelength: '))

        Fmin = linspace(F_min, F_max, 50)
        sigma = linspace(sigma_min, sigma_max, 50)
        lambdacenter = linspace(lambdacenter_min, lambdacenter_max, 50)
        
        Fmin_best = F_min
        sigma_best = sigma_min
        lambdacenter_best = lambdacenter_min
        delta_best = sum(self.flux**2)

        for i in range(len(Fmin)):
            for j in range(len(sigma)):
                for k in range(len(lambdacenter)):
                    F_model = 1 + (Fmin[i] - 1)*\
                        exp(-((self.wavelength-lambdacenter[k])**2)/2*sigma[j]**2)
                    delta = sum((self.flux - F_model)**2)

                    if delta < delta_best:
                        delta_best = delta
                        Fmin_best = Fmin[i]
                        sigma_best = sigma[j]
                        lambdacenter_best = lambdacenter[k]

        vr = c*(lambdacenter_best-lambda0)/lambda0
        print 'The velocity of the star is %.2f m/s' % vr


        return Fmin_best, sigma_best, lambdacenter_best
        
day0 = spectrum('spectrum_day0.txt')
'''
day67 = day('day67.txt')
day133 = day('day133.txt')
day200 = day('day200.txt')
day267 = day('day267.txt')
day333 = day('day333.txt')
day400 = day('day400.txt')
day467 = day('day467.txt')
day533 = day('day533.txt')
day600 = day('day600.txt')
'''
        


