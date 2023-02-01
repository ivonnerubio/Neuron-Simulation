import matplotlib.pyplot as plt
import numpy as np

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
        self.equation = "\\frac{dV}{dt} = \\frac{v_{rest} - v + i_{input}}{\\tau_m}"
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
# Set random number generator
np.random.seed(199)

# Initialize step_end and v
step_end = int(t_max / dt)
v = el


  # Initialize the figure
plt.figure()
plt.title('$V_m$ with random I(t)')
plt.xlabel('time (s)')
plt.ylabel('$V_m$ (V)')

  # loop for step_end steps
for step in range(step_end):

    # Compute value of t
    t = step * dt

    # Get random number in correct range of -1 to 1 (will need to adjust output of np.random.random)
    random_num = 2 * np.random.random() - 1

    # Compute value of i at this time step
    i =  i_mean * (1 + 0.1 * (t_max / dt)**(0.5) * random_num)

    # Compute v
    v = v + dt/tau * (el - v + r*i)

    # Plot v (using 'k.' to get even smaller markers)
    plt.plot(t, v, 'k.')





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
    i = i_mean * (1 + np.sin((t * 2 * np.pi) / 0.01))

    # Plot i (use 'ko' to get small black dots (short for color='k' and marker = 'o'))
    plt.plot(t, i, 'ko')

  # Display the plot
plt.show()