import matplotlib.pyplot as plt
import numpy as np


class LIFNeuron:
    def __init__(self):

        self.t_max = 150e-3   # second
        self.dt = 1e-3        # second
        self.tau = 20e-3      # second
        self.el = -60e-3      # milivolt
        self.v_reset = -70e-3 # milivolt
        self.vth = -50e-3     # milivolt
        self.r = 100e6        # ohm
        self.i_mean = 25e-11  # ampere
        self.random_seed = 1999 

        # self.t_max = t_max   # second
        # self.dt = dt        # second
        # self.tau = tau      # second
        # self.el = el     # milivolt
        # self.v_reset = v_reset # milivolt
        # self.vth = vth    # milivolt
        # self.r = r    # ohm
        # self.i_mean = i_mean  # ampere
        # self.random_seed = random_seed 


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

        # self.properties = [['Membrane Potential',0,130,25], 
        #                     ['Resting Potential',10,50,14], 
        #                     ['Membrane Time Constant', 0,130,25],
        #                     ['Membrane Resistance',10,50,14],
        #                     ['Input Current Mean (25e-11)',15,35,25],
        #                     ['Membrane Treshold (-50e-3)',-60,-40,-50]
        #                     ]

        self.properties = [
                            ['Input Current Mean (25e-11)',15,35,25],
                            ['Membrane Treshold (-50e-3)',-60,-40,-50]
                            ]

    

    # Set random number generator
    random_seed = np.random.seed(3)


# neuron = LIFNeuron(t_max, dt, tau, el, v_reset,vth, r, i_mean, random_seed)

    # def setDefaultParameters(self):
    #     t_max = self.t_max = 150e-3   # second
    #     dt = self.dt = 1e-3        # second
    #     tau = self.tau = 20e-3      # second
    #     el = self.el = -60e-3      # milivolt
    #     v_reset = self.v_reset = -70e-3 # milivolt
    #     vth = self.vth = -50e-3     # milivolt
    #     r = self.r = 100e6        # ohm
    #     i_mean = self.i_mean = 25e-11  # ampere
    #     random_seed = self.random_seed = 1999 

    #     return t_max, dt, tau, el, v_reset,vth, r, i_mean, random_seed


    def GenerateInputCurrent(self,step_end):
        """
        Full Equation Below:
            input_current = i_mean * (1 + 0.1 * (t_max/dt) ** (0.5) * (2 * np.random.random(step_end) - 1)))   

        Args:
            None

        Returns:
            An Array with input simulated over time

        """

        
        # Step 1: Create a scale factor by calculating the standard deviation or square root of t_max divided by dt 
        temp = (self.t_max/self.dt) ** (0.5)

        # Step 2: Generate an array of random values 
        rand_array = np.random.random(step_end)

        # Step 3: Scale the random values to have a range of -1:1
        scaled_rand = 2 * rand_array - 1

        # Step 4: Calculate the noise component
        noise = 0.1 * temp * scaled_rand

        # Step 5: Multiple my the input mean and add 1 to the noise component
        input_current = self.i_mean * (1 + noise)

        return input_current

    def modelNeuron(self):
        # Initialize step_end, t_range, v
        step_end = int(self.t_max / self.dt) - 1
        t_range = np.linspace(0, self.t_max, num=step_end, endpoint=False)
        v = self.el * np.ones(step_end)


        # Simulate current over time
        # Step 1: Create a scale factor by calculating the standard deviation or square root of t_max divided by dt 
        temp = (self.t_max/self.dt) ** (0.5)

        # Step 2: Generate an array of random values 
        rand_array = np.random.random(step_end)

        # Step 3: Scale the random values to have a range of -1:1
        scaled_rand = 2 * rand_array - 1

        # Step 4: Calculate the noise component
        noise = 0.1 * temp * scaled_rand

        # Step 5: Multiple my the input mean and add 1 to the noise component
        input_current = self.i_mean * (1 + noise)


        # Loop for step_end steps
        for step in range(1, step_end):

            # Compute v as function of i
            v[step] = v[step - 1] + (self.dt / self.tau) * (self.el - v[step - 1] + self.r * input_current[step])

            if (v[step]> self.vth):
                v[step] = self.v_reset


        # PLOT VM
        VmFig = plt.figure()
        plt.title('$V_m$ with random I(t)')
        plt.xlabel('time (s)')
        plt.ylabel('$V_m$ (V)')


        plt.axhline(y=self.vth, color ='r', label='V Threshold')
        plt.axhline(y=self.v_reset, color='k', label="V Reset")
        plt.legend(loc="upper right")
        plt.plot(t_range, v, 'k')

        # Plot Input Current
        IFig = plt.figure()
        plt.title('Random Input $(I)$ ')
        plt.xlabel('time (s)')
        plt.ylabel('$(I)$')

        plt.plot(t_range, input_current,'k')
            

        return VmFig, IFig



    # PLOTTING FUNCTIONS
    def plotVm(self,t_range, v):
        fig = plt.figure()
        plt.title('$V_m$ with random I(t)')
        plt.xlabel('time (s)')
        plt.ylabel('$V_m$ (V)')


        plt.axhline(y=self.vth, color ='r', label='V Threshold')
        plt.axhline(y=self.v_reset, color='k', label="V Reset")
        plt.legend(loc="upper right")
        plt.plot(t_range, v, 'k')


        return fig

    # PLOTTING FUNCTIONS
    def plotInputCurrent(t_range, input_current):
        fig = plt.figure()
        plt.title('Random Input $(I)$ ')
        plt.xlabel('time (s)')
        plt.ylabel('$(I)$')

        plt.plot(t_range, input_current,'k')
        return fig


    # GETTERS AND SETTERS
    def getT_max(self):
        return self.t_max
    def setT_max(self,t_max):
        self.t_max = t_max


    def getDt(self):
        return self.dt
    def setDt(self, dt):
        self.dt = dt

    
    def getTau(self):
        return self.tau
    def setTau(self, tau):
        self.tau = tau
    

    def getEl(self):
        return self.el
    def setEl(self, el):
        self.el = el

        
    def getV_Reset(self):
        return self.v_reset
    def setV_Reset(self, v_reset):
        self.v_reset = v_reset        


    def getVth(self):
        return self.vth
    def setVth(self, vth):
        self.vth = vth       


    def getR(self):
        return self.r
    def setR(self, r):
        self.r = r   


    def getI_mean(self):
        return self.i_mean
    def setR(self, i_mean):
        self.i_mean = i_mean 


    def getRandom_seed(self):
        return self.random_seed
    def setR(self, random_seed):
        self.random_seed = random_seed 


    def getDescription(self):
        return self.description


    def getEquation(self):
        return self.equation
    

    def getEquationDescription(self):
        return self.equationDescription
    
    def getProperties(self):
        return self.properties


    def printProperties(self):
        print("Properties: ", self.properties)
        return self.getProperties
    