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

neuron_type = ['Select Neuron','Leaky Fire-and-Integrate (LIF)','Hodgkin-Huxley (HH)', 'FitzHugh-Nagumo Model (FHN)','Morris-Lecar Model (ML)','AdEx Model (Adaptive Exponential Integrate-and-Fire)']

selected_neuron_type = st.selectbox("Choose a neuron:", neuron_type)
col_neuron, col_network = st.columns(2)



with col_neuron:
    st.subheader("Neuron")
    st.markdown("**Description**")
    neuron = lif.LIFNeuron()
    vMFig, IFig = lif.LIFNeuron.modelNeuron(neuron)
    

    #neuron = lif.LIFNeuron(-70e-3,-50e-3,1999)
   
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
            
            def updateValues(x, y,z):
                return x, y, z
            
            LIFProperties = neuron.getProperties()

            value_i_mean = st.slider(LIFProperties[0][0], LIFProperties[0][1],LIFProperties[0][2],LIFProperties[0][3],key="slider_i_mean")
            value_vth = st.slider(LIFProperties[1][0], LIFProperties[1][1],LIFProperties[1][2],LIFProperties[1][3],key="slider_vth")
            value_v_reset = st.slider(LIFProperties[2][0], LIFProperties[2][1],LIFProperties[2][2],LIFProperties[2][3],key="slider_v_reset")

            # Call the function with the selected values and display the result
            result = updateValues(value_i_mean, value_vth, value_v_reset)
            #st.write("The product of", value_i_mean, "and", value_vth, "and", value_v_reset, "is", result)

        
        # st.text(result)
        x,y,z = result
        neuron.setVth(y)
        neuron.setV_Reset(z)



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

          #st.latex(neuron_hh.equation1)
          #st.latex(neuron_hh.equation2)
          #st.latex(neuron_hh.equation3)
          #st.latex(neuron_hh.equation4)
          #st.latex(neuron_hh.equation5)
          st.latex(neuron_hh.equation6)
          

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
    
