class LIFNeuron:
    def __init__(self, tau_m, v_rest, v_threshold, v_reset, delta_t):
        self.tau_m = tau_m
        self.v_rest = v_rest
        self.v_threshold = v_threshold
        self.v_reset = v_reset
        self.delta_t = delta_t
        self.v = v_rest
        self.spike = False

        self.description = "The LIF model consists of a membrane potential that integrates incoming signals (from synapses) until it reaches a certain threshold. Once the threshold is reached, the membrane potential fires (emits a spike) and is reset to a resting potential. The membrane potential decays (leaks) back to the resting potential at a slower rate between spikes."
        self.equation = "\\frac{dV}{dt} = \\frac{v_{rest} - v + i_{input}}{\\tau_m}"
        self.properties = ['Membrane Potential', 'Resting Potential', 'Membrane Time Constant', 'Membrane Resistance', 'Input Current', 'Membrane Treshold']

    def update(self, i_input):
        # Update membrane potential
        dv = (self.v_reset - self.v + i_input * self.delta_t) / self.tau_m
        self.v += dv * self.delta_t

        # Check if the treshold is reached
        if self.v >= self.v_threshold:
            self.spike = True
            self.v = self.v_reset
        else:
            self.spike = False


neuron = LIFNeuron(tau_m=10.0, v_rest=-70.0, v_threshold=-55.0, v_reset=-75.0, delta_t=0.1)

i_input = 5.0
neuron.update(i_input)


print(neuron.description)