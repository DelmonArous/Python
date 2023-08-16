from scitools.std import *

def minmax(t, y):

    minima = []; maxima = []
   
    if y[0] > y[1]:
        maxima.append((t[0], y[0]))
    else:
        minima.append((t[0], y[0]))

    for k in range(1, len(y)-1):
        if y[k-1] < y[k] > y[k+1]:
            maxima.append((t[k], y[k]))
        elif y[k-1] > y[k] < y[k+1]:
            minima.append((t[k], y[k]))
            
    if y[-1] > y[-2]:
        maxima.append((t[-1], y[-1]))
    else:
        minima.append((t[-1], y[-1]))

    return array(minima), array(maxima)

def wavelength(peaks):
    peak_distance = []
    for k in range(1, len(peaks)):
        peak_distance.append(peaks[k][0]-peaks[k-1][0])

    return array(peak_distance)

t = linspace(0, 4*pi, 101)

def test1():

    y = exp(t/4.)*cos(2*t)
    peaks_min, peaks_max = minmax(t, y)
    wavelength_max = wavelength(peaks_max)

    plot(t, y, peaks_min[:,0], peaks_min[:,1],'bo',
         peaks_max[:,0], peaks_max[:,1], 'sm',
         xlabel='t', ylabel='y', 
         legend=('y = exp(t/4)*cos(2*t)',
                 'Local minimum','Local maximum'),
         title='Plot of the function y and its local minimum and maximum')
    figure()
    plot(range(len(wavelength_max)), wavelength_max, 'o',
         xlabel='indices', ylabel='wavelength',
         legend='Distance between local maximum',
         title='Plot of distances between local maximum for the function y=exp(t/4)*cos(2*t)')

def test2():

    y = exp(-t/4.)*cos(t**2/5.)
    peaks_min, peaks_max = minmax(t, y)
    wavelength_max = wavelength(peaks_max)
    
    plot(t, y, peaks_min[:,0], peaks_min[:,1],'bo',
         peaks_max[:,0], peaks_max[:,1], 'sm',
         xlabel='t', ylabel='y',
         legend=('y = exp(-t/4)*cos(t**2/5)',
                 'Local minimum','Local maximum'),
         title='Plot of the function y and its local minimum and maximum')
    figure()
    plot(range(len(wavelength_max)), wavelength_max, 'o',
         xlabel='indices', ylabel='wavelength',
         legend='Distance between local maximum',
         title='Plot of distances between local maximum for the function y=exp(-t/4)*cos(t**2/5)')

if __name__ == '__main__':
    test2()
    figure()
    test1()
