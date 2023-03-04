import streamlit as st
import numpy as np

from Neuron import LIF as lif
from Neuron import HH as hh


st.set_page_config(layout="wide")
hide_st_style = """
            <style>
            #MainMenu {visibility: visible;}
            footer {visibility: hidden;}
            header {visibility: visible;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


st.title("Neuron Simulation")

neuron_type = ['Select Neuron','Leaky Fire-and-Integrate (LIF)','Hodgkin-Huxley (HH)', 'FitzHugh-Nagumo Model (FHN)','Morris-Lecar Model (ML)','AdEx Model (Adaptive Exponential Integrate-and-Fire)']

col_neuron, col_network = st.columns(2)



with col_neuron:
    st.subheader("Neuron")
    selected_neuron_type = st.selectbox("Choose a neuron:", neuron_type)
    st.text("Description")
    neuron = lif.LIFNeuron()
    vMFig, IFig = lif.LIFNeuron.modelNeuron(neuron)

    #neuron = lif.LIFNeuron(-70e-3,-50e-3,1999)
   
    # LIF Neuron
    if(selected_neuron_type == neuron_type[1]):
        st.caption(lif.LIFNeuron.getDescription(neuron))
        st.latex(lif.LIFNeuron.getEquation(neuron))
        #st.markdown(lif.LIFNeuron.getEquationDescription(neuron))
        # st.text(lif.LIFNeuron.getProperties)
        
        with st.expander("Edit Properties"):
            for property in lif.LIFNeuron.getProperties(neuron):
              label = property[0]
              min_val = property[1]
              max_val = property[2]
              default_val = property[3]

              propertySlider = st.slider(label, min_val, max_val, default_val)
    
              def updateLIFNeuronProperties(property):
                valReturn = 0
                propertyName = str(property[0])
                #st.text("property:" + str(property[0]))
                propertyValue = propertySlider

                if propertyName == "Input Current Mean (25e-11)":
                    lif.LIFNeuron.GenerateInputCurrent(neuron,10)
                elif propertyName == "Membrane Treshold (-50e-3)":
                    lif.LIFNeuron.setVth = propertyValue
                    valReturn = lif.LIFNeuron.getVth(neuron)
                
                
                return valReturn
              
              st.write('Output:', updateLIFNeuronProperties(property))
        



       

        st.text("Model")

        # vMFig, IFig = lif.LIFNeuron.modelNeuron(neuron)

        st.pyplot(vMFig)
        st.pyplot(IFig)
        # st.pyplot(lif.LIFNeuron.plotVm(t_range,v))

        # st.pyplot(lif.LIFNeuron.plotInputCurrent(t_range, input_current))


        #specifying the figure to plot 
      #  fig, x = plt.subplots()
      #  x.hist(a, bins=10)

        #plotting the figure
      #  st.pyplot(fig)



    # HH Neuron
    elif(selected_neuron_type == neuron_type[2]):
          st.caption(hh.neuron.description)

          st.latex(hh.neuron.equation1)
          st.latex(hh.neuron.equation2)
          st.latex(hh.neuron.equation3)
          st.latex(hh.neuron.equation4)

          with st.expander("Edit Properties"):
              for property in hh.neuron.properties:
                  property = st.slider(property, 0, 130, 25)




          

with col_network:
      st.subheader("Network")
      # st.pyplot(lif.LIFNeuron.clickableFig())
      