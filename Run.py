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
x_range = []
y_vals   = []
for x_ind in np.arange(0,n_points,1):
    x_range.append(bja.getXBin(int(x_ind)))
    y_vals.append(bja.getOb(int(x_ind)))
plt.plot(x_range, y_vals)
plt.show()

# now test ll
print("ll=",bja.ll())
bja.setPar(0,1.)
print("ll=",bja.ll())
