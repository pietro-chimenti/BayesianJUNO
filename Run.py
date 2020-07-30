import numpy as np

# here we load the shared library created using the Makefile
from ROOT import gSystem
gSystem.Load("BJ_loglike.so")

# now we can create instance of the class in python using its syntax
from ROOT import BJ_loglike
bj_ana = BJ_loglike()
print(bj_ana.f(2.))
#i = np.arange(10)
#s = "A string"
#print(hw.EchoNumbers(i.size,i.astype(np.intc)))
#hw.EchoString(s)
#print(type(hw.EchoNumbers))
## we can also call the function runMe
#from ROOT import runMe
#runMe()
