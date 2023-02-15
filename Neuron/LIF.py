import matplotlib.pyplot as plt
import numpy as np


class LIFNeuron:
    def __init__(self, t_max, dt, tau, el, v_reset,vth, r, i_mean, random_seed):

        self.t_max = 150e-3   # second
        self.dt = 1e-3        # second
        self.tau = 20e-3      # second
        self.el = -60e-3      # milivolt
        self.v_reset = -70e-3 # milivolt
        self.vth = -50e-3     # milivolt
        self.r = 100e6        # ohm
        self.i_mean = 25e-11  # ampere
        self.random_seed = 1999 



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
  



t_max = 150e-3   # second
dt = 1e-3        # second
tau = 20e-3      # second
el = -60e-3      # milivolt
v_reset = -70e-3      # milivolt
vth = -50e-3     # milivolt
r = 100e6        # ohm
i_mean = 25e-11  # ampere



# Set random number generator
random_seed = np.random.seed(3)


neuron = LIFNeuron(t_max, dt, tau, el, v_reset,vth, r, i_mean, random_seed)


def GenerateInputCurrent(step_end):
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

def modelNeuron():
    # Initialize step_end, t_range, v
    step_end = int(t_max / dt) - 1
    t_range = np.linspace(0, t_max, num=step_end, endpoint=False)
    v = el * np.ones(step_end)


    # Simulate current over time
    input_current = GenerateInputCurrent(step_end)



    # Loop for step_end steps
    for step in range(1, step_end):

        # Compute v as function of i
        v[step] = v[step - 1] + (dt / tau) * (el - v[step - 1] + r * input_current[step])

        if (v[step]> vth):
            v[step] = v_reset
        

    return t_range, input_current, v




def plotVm(t_range, v):
    fig = plt.figure()
    plt.title('$V_m$ with random I(t)')
    plt.xlabel('time (s)')
    plt.ylabel('$V_m$ (V)')


    plt.axhline(y=vth, color ='r', label='V Threshold')
    plt.axhline(y=v_reset, color='k', label="V Reset")
    plt.legend(loc="upper right")
    plt.plot(t_range, v, 'k')


    return fig


def plotInputCurrent(t_range, input_current):
    fig = plt.figure()
    plt.title('Random Input $(I)$ ')
    plt.xlabel('time (s)')
    plt.ylabel('$(I)$')

    plt.plot(t_range, input_current,'k')
    return fig
    


    # def GenerateInputCurrent(self):
    #     """
    #     Full Equation Below:
    #         input_current = i_mean * (1 + 0.1 * (t_max/dt) ** (0.5) * (2 * np.random.random(step_end) - 1)))   

    #     Args:
    #         None

    #     Returns:
    #         An Array with input simulated over time

    #     """

    #     # Set random number generator
    #     np.random.seed(self.random_seed)

        
    #     # Step 1: Create a scale factor by calculating the standard deviation or square root of t_max divided by dt 
    #     temp = (self.t_max/self.dt) ** (0.5)

    #     # Step 2: Generate an array of random values 
    #     rand_array = np.random.random(self.step_end)

    #     # Step 3: Scale the random values to have a range of -1:1
    #     scaled_rand = 2 * rand_array - 1

    #     # Step 4: Calculate the noise component
    #     noise = 0.1 * temp * scaled_rand

    #     # Step 5: Multiple my the input mean and add 1 to the noise component
    #     input_current = self.i_mean * (1 + noise)

    #     return input_current


    # def Fire():

    #     # Simulate current over time
    #     input_current = GenerateInputCurrent(neuron)



    #     # Loop for step_end steps
    #     for step in range(1, step_end):

    #     # Compute v as function of i
    #         v[step] = v[step - 1] + (dt / tau) * (el - v[step - 1] + r * input_current[step])

    #         if (v[step]> vth):
    #             v[step] = v_reset
                
            

    #     # Plot membrane potential

    #     plt.figure()
    #     plt.title('$V_m$ with random I(t)')
    #     plt.xlabel('time (s)')
    #     plt.ylabel('$V_m$ (V)')


    #     plt.axhline(y=vth, color ='r', label='V Threshold')
    #     plt.axhline(y=v_reset, color='k', label="V Reset")
    #     plt.legend(loc="upper right")
    #     plt.plot(t_range, v, 'k')
    #     plt.show()

    #     plt.figure()
    #     plt.title('Random Input $(I)$ ')
    #     plt.plot(t_range, input_current,'k')










