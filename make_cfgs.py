# 1DQM

# This script generates path configurations which will be used to evaluate the
# Monte Carlo. The configurations satisfy the periodic boundary confition
# x(0) = x(N), and configurations are distributed in the set by e^-S.

# import modules
import numpy as np
#from whrandom import uniform
from math import *

# Lattice variables
N = 20 # Recall that x(0) = x(N)
N_cor = 1000 # Updates between saved configurations
N_init = 100 # Thermalization steps.
N_cf = 10 # Size of the set of configurations
a = 0.5 # Lattice spacing
eps = 1.4 # Sets how much we vary x on each step.

MCset = []

def update(x): # Runs through the vector x, some of the x[j] may change
        z = np.zeros(len(x))
        for j in range(0,N):
                old_x = x[j] # save original value
                old_Sj = S(j,x)
                z[j] = x[j] + 2*eps*(np.random.rand(1,1)[0,0] - 0.5) # update x[j]
                dS = S(j,x) - old_Sj # change in action
                #print(dS)
                if dS>0 and np.exp(-dS)<np.random.rand(1,1)[0,0]:
                        z[j] = old_x # restore old value
        return z

def S(j,x): # single piece of the harmonic oscillator action S
        jp = (j+1)%N # next site
        jm = (j-1)%N # previous site
        return a*x[j]**2/2 + x[j]*(x[j]-x[jp]-x[jm])/a

def thermalize(n1,n2):
        x = np.zeros(n1)
        for i in range(n2):
                x = update(x)
        MCset.append(x)
        return x

y = thermalize(N,N_init)

counter = 0 # counts how many updates completed before a cfg is saved.
while len(MCset)< N_cf:
        counter = counter + 1
        y = update(y)
        if counter == N_cor:
                MCset.append(y)
                counter = 0

for i in range(len(MCset)):
        print(MCset[i])
        
#print(5*4)
#print(2*eps*(np.random.rand(1,1)[0,0]) - eps)
#print(2*eps*(np.random.rand(1,1)[0,0]) - eps)
#print(2*eps*(np.random.rand(1,1)[0,0]) - eps)
#print(2*eps*(np.random.rand(1,1)[0,0]) - eps)
#print(2*eps*(np.random.rand(1,1)[0,0]) - eps)
