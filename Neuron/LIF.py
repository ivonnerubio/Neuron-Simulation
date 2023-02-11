import matplotlib.pyplot as plt
import numpy as np


class LIFNeuron:
    def __init__(self, t_max, dt, tau, el, v_reset,vth, r, i_mean):

        self.t_max = 150e-3   # second
        self.dt = 1e-3        # second
        self.tau = 20e-3      # second
        self.el = -60e-3      # milivolt
        self.v_reset = -70e-3 # milivolt
        self.vth = -50e-3     # milivolt
        self.r = 100e6        # ohm
        self.i_mean = 25e-11  # ampere



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

    def GenerateInputCurrent(self,RandomSeed):
        """
        Full Equation Below:
            input_current = i_mean * (1 + 0.1 * (t_max/dt) ** (0.5) * (2 * np.random.random(step_end) - 1)))   

        Args:
            None

        Returns:
            An Array with input simulated over time

        """

        # Set random number generator
        np.random.seed(RandomSeed)

        
        # Step 1: Create a scale factor by calculating the standard deviation or square root of t_max divided by dt 
        temp = (self.t_max/self.dt) ** (0.5)

        # Step 2: Generate an array of random values 
        rand_array = np.random.random(self.step_end)

        # Step 3: Scale the random values to have a range of -1:1
        scaled_rand = 2 * rand_array - 1

        # Step 4: Calculate the noise component
        noise = 0.1 * temp * scaled_rand

        # Step 5: Multiple my the input mean and add 1 to the noise component
        input_current = self.i_mean * (1 + noise)

        return input_current









neuron = LIFNeuron(tau_m=10.0, v_rest=-70.0, v_threshold=-55.0, v_reset=-75.0, delta_t=0.1)

