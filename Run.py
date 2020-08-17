import numpy as np
import matplotlib.pyplot as plt

# here we load the shared library created using the Makefile
from ROOT import gSystem
gSystem.Load("BJ_loglike.so")

# now we can create instance of the class in python using its syntax
from ROOT import BJ_loglike
bja = BJ_loglike()

# just a test to call a function
# print(bja.f(2.))

# now plot the data 
n_points = bja.BJ_LL_NOBS
x_range  = []
y_vals   = []
y_func   = []
for x_ind in np.arange(0,n_points,1):
    x_range.append(bja.getXBin(int(x_ind)))
    y_vals.append(bja.getOb(int(x_ind)))
    y_func.append(bja.f(bja.getXBin(int(x_ind))))
#plt.figure(1)
#plt.plot(x_range, y_vals)
#plt.show()
#plt.close()

# now set parameters and test ll
print("ll=",bja.ll())
bja.setPar(0,0.3)
bja.setPar(1,0.7)
print("ll=",bja.ll())

# test a random generation
bja.generateRandom(19780126)
for x_ind in np.arange(0,n_points,1):
    x_range[x_ind]= bja.getXBin(int(x_ind))
    y_vals[x_ind] = bja.getOb(int(x_ind))
    y_func[x_ind] = bja.f(bja.getXBin(int(x_ind)))

#plt.figure(1)
#plt. errorbar(x_range, y_vals, yerr = bja.BJ_LL_SIGMA, fmt='o', label='Data')  
#plt.plot(x_range,y_func, label='Theory')
#plt.legend()
#plt.show()
#plt.close()

# First Maximum Likelihood!
from scipy.optimize import minimize

def log_likelihood(theta):
    for i in range(len(theta)):
        bja.setPar(i,theta[i])
    return bja.ll()

np.random.seed(20200813)
nll = lambda *args: -log_likelihood(*args)
initial = np.array([0.5, 0.5])
soln = minimize(nll, initial)
p0_ml, p1_ml = soln.x
print("Maximum likelihood estimates:")
print("p0 = {0:.3f}".format(p0_ml))
print("p1 = {0:.3f}".format(p1_ml))

# Now Bayesian
import emcee

def log_prior(theta):
    p0 , p1 = theta
    if 0 < p0 < 1 and 0 < p1 < 1 :
        return 0.0
    return -np.inf

def log_probability(theta):
    lp = log_prior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp + log_likelihood(theta)

pos = soln.x + 1e-4 * np.random.randn(32, 2)
nwalkers, ndim = pos.shape
sampler = emcee.EnsembleSampler(nwalkers, ndim, log_probability)
sampler.run_mcmc(pos, 50000, progress=True);


# Now plot time series
#plt.figure(1)
fig, axes = plt.subplots(2, figsize=(10, 7), sharex=True)
samples = sampler.get_chain()
labels = ["p0", "p1"]
axes[0].plot(samples[:, :, 0], "k", alpha=0.3)
axes[0].set_xlim(0, len(samples))
axes[0].set_ylabel(labels[0])
axes[0].yaxis.set_label_coords(-0.1, 0.5)
axes[1].plot(samples[:, :, 1], "k", alpha=0.3)
axes[1].set_xlim(0, len(samples))
axes[1].set_ylabel(labels[1])
axes[1].yaxis.set_label_coords(-0.1, 0.5)



axes[-1].set_xlabel("step number");
plt.show()
plt.close()

import corner

flat_samples = sampler.get_chain(discard=100, thin=15, flat=True)
fig = corner.corner( flat_samples, labels=labels )
plt.show()

#def log_prior(theta):
#    p0, p1, log_f = theta
#    if -5.0 < m < 0.5 and 0.0 < b < 10.0 and -10.0 < log_f < 1.0:
#        return 0.0
#    return -np.inf


