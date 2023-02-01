class HHNeuron:
    def __init__(self):
        self.description = "The model describes the membrane potential of a neuron as the result of ionic currents flowing across its membrane, specifically sodium (Na) and potassium (K) ions. The model uses four equations to describe the time-varying changes in the ionic currents and in the membrane potential."
        self.equation1 = "\\frac{dV}{dt} = \\frac{(I_ion - I_Na - I_K - I_L)}{C_m}"
        self.equation2 = "\\frac{dh}{dt} = \\frac{(h_∞(V) - h)}{τ_h(V)}"
        self.equation3 = "\\frac{dn}{dt}  = \\frac{(n_∞(V) - n)}{τ_n(V)}"
        self.equation4 = "\\frac{dm}{dt}  = \\frac{(m_∞(V) - m)}{τ_m(V)}"
         
        self.properties = ['Membrane Potential']

neuron = HHNeuron()
