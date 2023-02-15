import brian2 as b2
import random
import matplotlib.pyplot as plt
import numpy as np


class LIFNeuron:

    def __init__(self, 
                t_max,
                dt,
                tau,
                el,
                v_reset,
                vth,
                r,
                i_mean,):
        self.t_max = t_max
        self.dt = dt
        self.tau = tau
        self.el = el
        self.v_reset = v_reset
        self.vth = vth
        self.r = r
        self.i_mean = i_mean


    def GenerateInputCurrent(t_max, dt, step_end, i_mean):
        """
        Full Equation Below:
            input_current = i_mean * (1 + 0.1 * (t_max/dt) ** (0.5) * (2 * np.random.random(step_end) - 1)))   

        Args:
            None

        Returns:
            An Array with input simulated over time

        """

     
        # Step 1: Create a scale factor by calculating the standard deviation or square root of t_max divided by dt 
        temp = (t_max/dt) ** (0.5)

        # Step 2: Generate an array of random values 
        rand_array = np.random.random(step_end)

        # Step 3: Scale the random values to have a range of -1:1
        scaled_rand = 2 * rand_array - 1

        # Step 4: Calculate the noise component
        noise = 0.1 * temp * scaled_rand

        # Step 5: Multiple my the input mean and add 1 to the noise component
        input_current = i_mean * (1 + noise)

        return input_current


