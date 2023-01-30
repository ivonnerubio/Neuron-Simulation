class IFARP:
    def __init__(self):
        self.description = "The Integrate-and-Fire with Absolute Refractory Period (IF-ARP) is a mathematical model of a spiking neuron. It mimics the behavior of a real neuron by integrating incoming signals and generating an output spike when a threshold is reached. After the spike, the neuron enters a fixed period during which it cannot respond to incoming signals, called the absolute refractory period. The model is used to study the behavior and interactions of neurons in a network."
        self.equation = "dv/dt = \\frac{v_{rest} - v + i_{input}}{\\tau_m}"
  
