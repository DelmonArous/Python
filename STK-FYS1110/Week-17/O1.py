import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

def standard_deviation(obs, dof=0):
    x_avg           = np.mean(obs)
    x_diff_squared  = np.array([(x_i - x_avg)**2 for x_i in obs])
    variance        = np.sum(x_diff_squared) / (len(x_diff_squared) - dof)
    stddev          = np.sqrt(variance)
    return stddev

# Open and read txt. file
path = 'C:\\Users\\delmo\\PycharmProjects\\pythonFiles_STK-FYS1110\\Week-17\\motstand.txt'
df = pd.read_csv(path, names=['Motstand'])

# Define new column representing time
df['Tid'] = np.arange(1,len(df)+1)

# Scatter plot
plt.figure(1)
plt.plot(df['Tid'], df['Motstand'], 'o', mfc='none')
plt.xlabel('Målenummer', fontsize=14)
plt.ylabel('Motstand ($m\Omega$)', fontsize=14)
plt.title('Motstand i en 10 m lang koppertråd med tverrsnitt 1 mm$^2$')
# plt.ylim([160., 180.])
plt.show()

# Define parameters
N       = len(df)
k       = np.sqrt(N)
x_min   = np.amin(df['Motstand'])
x_max   = np.amax(df['Motstand'])
deltax  = (x_max - x_min)/k

# Compute bins and middle point of each bin
bins  = np.array([x_min+(j-1)*deltax for j in np.arange(1,int(k)+2)])
x_mid = np.array([x_min+(j-0.5)*deltax for j in np.arange(1,int(k)+1)])

# Add bin as column to the dataframe
df['Bin'] = pd.cut(df['Motstand'], bins=bins, include_lowest=True)
N_j = np.array(df['Bin'].value_counts().sort_index())
# N_j = N_j/(np.sum(N_j)*deltax) # estimer frekvenstetthet
S_j = x_mid

#
hist, bins = np.histogram(df['Motstand'], bins=10)

# Compute mean, variance and standard deviation
x_mean  = np.mean(df['Motstand'])
x_std   = standard_deviation(np.array(df['Motstand']), 1)
x_var   = x_std**2
x       = np.linspace(x_min, x_max, 100, endpoint=True)
pdf_fit = stats.norm.pdf(x, x_mean, x_std)

#

# Plot histogram
width = 0.05 # deltax
plt.figure()
plt.bar(S_j, N_j, width, color='red', edgecolor='black', label='Tilpasset histogram')
plt.bar(bins[:-1], hist, width, color='blue', edgecolor='black', alpha = 0.6, label='numpy.histogram')
plt.plot(x, pdf_fit*17, color='r', label='Fitted pdf')
plt.xlabel('Motstand ($m\Omega$)', fontsize = 14)
plt.ylabel('Frekvens', fontsize = 14)
plt.legend()
plt.show()
