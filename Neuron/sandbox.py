import matplotlib.pyplot as plt
import numpy as np



# Define simulation parameters
dt = 0.01 # time step
T = .1 # total simulation time
t = np.arange(0, T, dt) # time array
t_max = 150e-3   # second
dt = 1e-3        # second
tau = 20e-3      # second
el = -60e-3      # milivolt
vr = -70e-3      # milivolt
vth = -50e-3     # milivolt
r = 100e6        # ohm
i_mean = 25e-11  # ampere

I = i_mean * (1 + 0.1 * (t_max / dt ) ** 0.5 * np.random.random() -1 )
print(I)

plt.figure()
plt.xlabel("LIF Neuron with random I")

np.random.seed(2023)
for step in range(len(t)):
   # I = np.random.uniform(low=-0.1, high=0.1)'
    #I = np.random.random()
    print('I ==',I)
    dVm = (el - vr + r * I ) / tau
    if(dVm >= vth):
        dVm = 0
   # print(dVm)
    #t[step] = dVm
    plt.plot(t[step],dVm,'ro')
   # print(t[step])

    

plt.show()