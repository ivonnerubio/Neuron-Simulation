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

col_neuron, col_network = st.columns(2)



with col_neuron:
    st.subheader("Neuron")
    selected_neuron_type = st.selectbox("Choose a neuron:", neuron_type)
    st.text("Description")
    neuron = lif.LIFNeuron()
    vMFig, IFig = lif.LIFNeuron.modelNeuron(neuron)

    neuron = lif.LIFNeuron()
    st.text(lif.LIFNeuron.getProperties(neuron)[1][0])
    # LIF Neuron
    if(selected_neuron_type == neuron_type[1]):
        st.caption(lif.LIFNeuron.getDescription(neuron))
        st.latex(lif.LIFNeuron.getEquation(neuron))
        st.markdown(lif.LIFNeuron.getEquationDescription(neuron))
        # st.text(lif.LIFNeuron.getProperties)
        
        with st.expander("Edit Properties"):
            for property in lif.LIFNeuron.getProperties(neuron):
              label = property[0]
              min_val = property[1]
              max_val = property[2]
              default_val = property[3]
              property = st.slider(label, min_val, max_val, default_val)

              def myFunkyFunc(property):
                if property == "Membrane Treshold":
                    neuron.setVth(property)
                #neuron.setDt(property)
                vMFig, IFig = lif.LIFNeuron.modelNeuron(neuron)
                
                return neuron.getVth
              
              st.write('Output:', myFunkyFunc(property))
        



       

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
    # Define the slider
    x = st.slider('Select a value', 0, 10, 5)

    # Define a function that takes in the slider value and returns the output
    def my_function(x):
        return x**2

    # Use st.write to display the output
    st.write('Output:', my_function(x))

    # Wrap the slider and function call in a while loop to update the output in real-time
    while True:
        new_x = st.slider('Select a value', 0, 10, 5)
        st.write('Output:', my_function(new_x))