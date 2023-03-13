from PIL import Image


class HHNeuron:
    def __init__(self):
        self.description = "The model describes the membrane potential of a neuron as the result of ionic currents flowing across its membrane, specifically sodium (Na) and potassium (K) ions. The model uses four equations to describe the time-varying changes in the ionic currents and in the membrane potential."
        self.equation1 = "\\frac{dV}{dt} = \\frac{(I_ion - I_Na - I_K - I_L)}{C_m}"
        self.equation2 = "\\frac{dh}{dt} = \\frac{(h_∞(V) - h)}{τ_h(V)}"
        self.equation3 = "\\frac{dn}{dt}  = \\frac{(n_∞(V) - n)}{τ_n(V)}"
        self.equation4 = "\\frac{dm}{dt}  = \\frac{(m_∞(V) - m)}{τ_m(V)}"
        self.equation5 = "Cm \\frac{dV}{dt} = -g_Nam^3h(V-ENa) - g_K*n^4(V-EK) - g_L(V-EL) + I"
        self.equation6 = "Cm \\frac{dV}{dt} = \overline{g}_L (V-E_L) + \overline{g}_K n^4(V-E_K) + \overline{g}_{Na} m^3h(V-E_{Na})"         
        self.properties = ['Membrane Potential']

        self.propertiesDescriptions = ["im","total"]

        self.circuit = Image.open('Neuron/Circuit Models/HH Circuit.jpg')

        #https://www.bonaccorso.eu/2017/08/19/hodgkin-huxley-spiking-neuron-model-python/
        self.gL = 3e-6          # ms/mm^2
        # Average potassium channel conductance per unit area (mS/cm^2)
        self.gK = 3.6e-4        # ms/mm^2
        self.gNa = 1.2e-3       # ms/mm^2
        self.eL = -5.4387e-2    # Voltage
        self.eK = -7.7e-2       # Voltage
        self.eNa = 5e-2         # Voltage


neuron = HHNeuron()
