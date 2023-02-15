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

    # LIF Neuron
    if(selected_neuron_type == neuron_type[1]):
        st.caption(lif.neuron.description)
        st.latex(lif.neuron.equation)
        st.markdown(lif.neuron.equationDescription)
        
        
        with st.expander("Edit Properties"):
            for property in lif.neuron.properties:
                property = st.slider(property, 0, 130, 25)

        st.text("Model")

        t_range, input_current,v = lif.modelNeuron()

        st.pyplot(lif.plotVm(t_range,v))

        st.pyplot(lif.plotInputCurrent(t_range, input_current))


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