import matplotlib.pyplot as plt
import numpy as np
import brian2 as b2

class LIFNeuron:
    def __init__(self, tau_m, v_rest, v_threshold, v_reset, delta_t):
        self.tau_m = tau_m
        self.v_rest = v_rest
        self.v_threshold = v_threshold
        self.v_reset = v_reset
        self.delta_t = delta_t
        self.v = v_rest
        self.spike = False
        self.i_mean = 25e-11
        

        self.description = "The LIF model consists of a membrane potential that integrates incoming signals (from synapses) until it reaches a certain threshold. Once the threshold is reached, the membrane potential fires (emits a spike) and is reset to a resting potential. The membrane potential decays (leaks) back to the resting potential at a slower rate between spikes."
        self.equation = "\\tau_m \\frac{dV}{dt} = E_L - V + R_m I_e"
        self.equationDescription = """
                                    \\tau_m = Time Constant  \n
                                    \\frac{dV}{dt} = Membrane Potential \n
                                    E_L = Resting Potential \n
                                    V = Voltage \n
                                    R_m = Total Membrane Resistance \n
                                    I_e = Input \n
                                    """

        self.equation2 = "\\frac{dV}{dt} = \\frac{v_{rest} - v + i_{input}}{\\tau_m}"
        self.properties = ['Membrane Potential', 'Resting Potential', 'Membrane Time Constant', 'Membrane Resistance', 'Input Current', 'Membrane Treshold']

    def update(self, i_input):
        # Update membrane potential
        dv = (self.v_rest - self.v + i_input * self.delta_t) / self.tau_m
        self.v += dv * self.delta_t

        # Check if the treshold is reached
        if self.v >= self.v_threshold:
            self.spike = True
            self.v = self.v_reset
        else:
            self.spike = False

    def fire(self,maxTime):
        tau_m = 10.0
        Vth = -55 # Threshold Value, Units: mV , range is -55 to -50 mV
        Vrest = -70 # Units: mV
        E_L = 0



        
t_max = 150e-3   # second
dt = 1e-3        # second
tau = 20e-3      # second
el = -60e-3      # milivolt
vr = -70e-3      # milivolt
vth = -50e-3     # milivolt
r = 100e6        # ohm
i_mean = 25e-11  # ampere

print(t_max, dt, tau, el, vr, vth, r, i_mean)







neuron = LIFNeuron(tau_m=10.0, v_rest=-70.0, v_threshold=-55.0, v_reset=-75.0, delta_t=0.1)



np.random.random(1999)



plt.figure()
plt.xlabel("")


t_max = 100 
dt = 10

steps = int(t_max / dt)
v = .1
v_rest = .75
tau_m = 1
treshhold = 10

spikes = np.zeros(steps)

print(spikes)

for step in range(steps):

    t = step * dt

    random_num = 2 * np.random.random() - 1 

    i = neuron.i_mean * (1 + 0.1 * (t_max / dt ) ** 0.5 * random_num)
    
    v = (v_rest - v + i) / tau_m


    if (v >= treshhold):
        print('True')
        v = 0
    
    spikes[step] = v

plt.plot(t, v)



t_max = 150e-3   # second
dt = 1e-3        # second
tau = 20e-3      # second
el = -60e-3      # milivolt
vr = -70e-3      # milivolt
vth = -50e-3     # milivolt
r = 100e6        # ohm
i_mean = 25e-11  # ampere


vRest = -70
vThreshold = -55












# Set random number generator
np.random.seed(200 )

# Initialize step_end and v
step_end = int(t_max / dt)
v = el


  # Initialize the figure
plt.figure()
plt.title('$V_m$ with random I(t)')
plt.xlabel('time (s)')
plt.ylabel('$V_m$ (V)')


leakPotential = -70




  # loop for step_end steps
for step in range(step_end):

    # Compute value of t
    t = step * dt

    # Get random number in correct range of -1 to 1 (will need to adjust output of np.random.random)
    random_num = 2 * np.random.random() - 1

    # Compute value of i at this time step
    i =  i_mean * (1 + 0.1 * (t_max / dt)**(0.5) * random_num)

    # Compute v
    #v = v + dt/tau * (el - v + r*i)
    v = .5 

    # Plot v (using 'k.' to get even smaller markers)
    plt.ylim(0,1)
    plt.plot(t, v, 'k.')





EL = -70 # mV
RI = 10e6 # MΩ
τm = 33.3 # ms
I = 1 # nA
Vrest = -70 # mV
Vthreshold = 2 # mV
Vm = Vrest
dt = 0.1 # ms
t = 0 # ms
step_end = 100



t_max = 150e-3   # second
dt = 1e-3        # second
tau = 20e-3      # second
el = -60e-3      # milivolt
vr = -70e-3      # milivolt
vth = -50e-3     # milivolt
r = 100e6        # ohm
i_mean = 25e-11  # ampere

print(t_max, dt, tau, el, vr, vth, r, i_mean)

step_end = 25

  # Initialize the figure
plt.figure()
plt.title('Synaptic Input $I(t)$')
plt.xlabel('time (s)')
plt.ylabel('$I$ (A)')

  # Loop for step_end steps
for step in range(step_end):

    # Compute value of t
    t = step * dt

    # Compute value of i at this time step
    i = np.random.uniform(low=.1, high =1)

    dVm = (el - Vm + r  * i) * dt / τm
    Vm = Vm + dVm
    
    # if Vm >= Vthreshold:
    #     Vm = Vrest
    # t = t + dt



    # Plot i (use 'ko' to get small black dots (short for color='k' and marker = 'o'))
    plt.plot(t, Vm, 'ko')

  # Display the plot
plt.show()



EL = -70 # mV
RI = 10e6 # MΩ
τm = 33.3 # ms
I = 1 # nA
Vrest = -70 # mV
Vthreshold = -55 # mV 
Vm = Vrest
dt = 0.1 # ms
t = 0 # ms
step_end = 100

arra = np.zeros(step_end)

for step in range(step_end): # ms
    I = np.random.uniform(low=-0.1, high=0.1)
    dVm = (EL - Vm + RI * I) * dt / τm
    Vm = Vm + dVm
    
    if Vm >= Vthreshold:
        Vm = Vrest
    t = t + dt
    arra[step] = Vm
    plt.plot(step,Vm)
 


print(len(arra))

plt.show()


count=0
for step in range(10):
    count += 1
    I = np.random.uniform(low=1,high =10)
    
    if(I > 5):
        I = 0

    plt.plot(count,I)

plt.show()









V_REST = -70*b2.mV
V_RESET = -65*b2.mV
FIRING_THRESHOLD = -50*b2.mV
MEMBRANE_RESISTANCE = 10. * b2.Mohm
MEMBRANE_TIME_SCALE = 8. * b2.ms
ABSOLUTE_REFRACTORY_PERIOD = 2.0 * b2.ms

from neurodynex3.leaky_integrate_and_fire import LIF
from neurodynex3.tools import input_factory

# create a step current with amplitude = I_min
step_current = input_factory.get_step_current(
    t_start=5, t_end=100, unit_time=b2.ms,
    amplitude=I_min)  # set I_min to your value

# run the LIF model.
# Note: As we do not specify any model parameters, the simulation runs with the default values
(state_monitor,spike_monitor) = LIF.simulate_LIF_neuron(input_current=step_current, simulation_time = 100 * b2.ms)

# plot I and vm
plot_tools.plot_voltage_and_current_traces(
state_monitor, step_current, title="min input", firing_threshold=LIF.FIRING_THRESHOLD)
print("nr of spikes: {}".format(spike_monitor.count[0]))  # should be 0