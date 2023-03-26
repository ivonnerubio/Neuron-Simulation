import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
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

neuron_type = ['Select Neuron','Leaky Fire-and-Integrate (LIF)','Hodgkin-Huxley (HH)']
#neuron_type = ['Select Neuron','Leaky Fire-and-Integrate (LIF)','Hodgkin-Huxley (HH)', 'FitzHugh-Nagumo Model (FHN)','Morris-Lecar Model (ML)','AdEx Model (Adaptive Exponential Integrate-and-Fire)']

selected_neuron_type = st.selectbox("Choose a neuron:", neuron_type)
col_neuron, col_network = st.columns(2)



with col_neuron:
    st.subheader("Neuron")
    st.markdown("**Description**")
    neuron = lif.LIFNeuron()
    vMFig, IFig = lif.LIFNeuron.modelNeuron(neuron)
    


   
    # LIF Neuron
    if(selected_neuron_type == neuron_type[1]):
        st.caption(lif.LIFNeuron.getDescription(neuron))
        st.markdown("**Equation**")
        st.latex(lif.LIFNeuron.getEquation(neuron))

        #st.markdown(lif.LIFNeuron.getEquationDescription(neuron))
        # st.text(lif.LIFNeuron.getProperties)
        


              # Define a function that takes two values as input and returns their product











        st.markdown("**Adjust Model**")
        with st.expander("Edit Properties"):
            
            def updateValues(x, y):
                return x, y
            
            LIFProperties = neuron.getProperties()
            #value_i_mean = st.slider(LIFProperties[0][0], LIFProperties[0][1],LIFProperties[0][2],LIFProperties[0][3],key="slider_i_mean")
            value_vth = st.slider(LIFProperties[0][0], LIFProperties[0][1],LIFProperties[0][2],LIFProperties[0][3],key="slider_i_mean")
            value_v_reset = st.slider(LIFProperties[1][0], LIFProperties[1][1],LIFProperties[1][2],LIFProperties[1][3],key="slider_vth")
            #value_v_reset = st.slider(LIFProperties[2][0], LIFProperties[2][1],LIFProperties[2][2],LIFProperties[2][3],key="slider_v_reset")

            # Call the function with the selected values and display the result
            result = updateValues(value_vth, value_v_reset)
            #st.write("The product of", value_i_mean, "and", value_vth, "and", value_v_reset, "is", result)

        
        # st.text(result)
        x,y = result
        neuron.setVth(x)
        neuron.setV_Reset(y)



        # mynym = updateLIFNeuronProperties(property)   
        # st.text("NUMER" + str(mynym))


        #neuron.setV_Reset(mynym)
        #neuron.getV_Reset()

        #st.text("Model")

        vMFig, IFig = lif.LIFNeuron.modelNeuron(neuron)
        st.markdown("**Circuit**")
        st.image(neuron.circuit, width=500, use_column_width=True)

        # st.pyplot(vMFig)
        # st.pyplot(IFig)
        # st.pyplot(lif.LIFNeuron.plotVm(t_range,v))

        # st.pyplot(lif.LIFNeuron.plotInputCurrent(t_range, input_current))


        #specifying the figure to plot 
      #  fig, x = plt.subplots()
      #  x.hist(a, bins=10)

        #plotting the figure
      #  st.pyplot(fig)



    # HH Neuron
    elif(selected_neuron_type == neuron_type[2]):
          neuron_hh = hh.HHNeuron()
          st.caption(neuron_hh.description)

          st.latex(neuron_hh.equationIm)

          col1, col2, col3 = st.columns([1, 1, 1])
          with col1:
              st.latex(neuron_hh.equationNa)
              st.caption("The sodium conductance is time-dependent and voltage-dependent")
          with col2:
              st.latex(neuron_hh.equationK)
              st.caption("The potassium conductance is time-dependent and voltage-dependent")
          with col3:
              st.latex(neuron_hh.equationL)
              st.caption("The leak conductance is neither time-dependent nor voltage-dependent")


          
          
          
          

          

          with st.expander("Edit Properties"):
              for property in hh.neuron.properties:
                  property = st.slider(property, 0, 130, 25)


          st.image(neuron_hh.circuit)




          

with col_network:
      st.subheader("Model")
      if(selected_neuron_type == neuron_type[1]):
        st.pyplot(vMFig)
        st.pyplot(IFig)
      #value_123 = st.slider("ivonne",float(5e-10),float(15e-10),float(10e-10),key="sliderdope")
    






def getLIFNeuronData():
    LIFCaption = neuron.getDescription
    LIFEquation = neuron.getEquation
    LIFCircuit = neuron.getCircuit
    return LIFCaption,LIFEquation,LIFCircuit