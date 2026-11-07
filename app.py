import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Gradient Descent Simulator")

st.write(
    "An interactive application for understanding and experimenting with gradient descent."
)

starting_value = st.sidebar.number_input( "Starting value (x)",value=4.0 )
learning_rate = st.sidebar.number_input("Learning rate",value=0.1,min_value=0.001,max_value=1.0)
maximum_iterations = st.sidebar.number_input("Maximum iterations",value=10,min_value=1,max_value=1000,step=1)
tolerance = st.sidebar.number_input("Tolerance",value=0.001,min_value=0.000001,format="%.6f")

st.sidebar.caption("Enter the coefficients a, b, and c to define your quadratic function.")
a = st.sidebar.number_input("Coefficient a",value=1.0)
b = st.sidebar.number_input("Coefficient b",value=0.0)
c = st.sidebar.number_input("Coefficient c",value=0.0)


run = st.button("Run Gradient Descent")

def f(x):
    return a*x**2 + b*x + c

def df(x):
    return 2*a*x + b

if run:
    x_history = []
    y_history = []

    converged = False

    x = starting_value
    
    i = 0
    while(i<maximum_iterations):
        x_new = x - learning_rate * df(x)
            
        x_history.append(x)
        y_history.append(f(x))
            
        x = x_new
        i = i + 1

        if abs(df(x)) < tolerance:
            converged = True
            break

    #append final x to x_history and append final f(x) to y_history
    x_history.append(x)
    y_history.append(f(x))

    st.metric("Final x-value",x)
    st.metric("Final function value",f(x))
    st.metric("Iterations performed",i)
    st.metric("Converged",converged)


    x_axis = np.linspace(-10,10)
    y_axis = f(x_axis)


    fig, ax = plt.subplots()


    ax.plot(x_axis, y_axis, label="f(x) = x²")


    ax.plot(x_history,y_history,marker="o",color="orange",label="Optimization path")


    ax.scatter(x_history[0],y_history[0],color="green",s=70,label="Starting point",zorder=5)

   
    ax.scatter(x_history[-1],y_history[-1],color="red",s=70,label="Final point",zorder=5)

    ax.set_title("Gradient Descent on f(x) = x²")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.legend()

    st.pyplot(fig)


    

            
    