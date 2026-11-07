# Gradient Descent Simulator

An interactive web application built with Python and Streamlit to demonstrate how Gradient Descent works. The application allows users to experiment with different starting values, learning rates, iteration limits, and tolerance levels while visualising the optimisation process.

## Project Overview

Gradient Descent is an optimisation algorithm commonly used in Machine Learning to minimise a function by iteratively moving towards a point where its gradient is close to zero.

This project implements the Gradient Descent algorithm from scratch and provides an interactive interface for exploring how its parameters affect optimisation.

Users can define their own quadratic functions in the form:

\[
f(x) = ax^2 + bx + c
\]

The application calculates the derivative automatically:

\[
f'(x) = 2ax + b
\]

It then applies the Gradient Descent update rule:

\[
x_{\text{new}} = x - \alpha f'(x)
\]

Where:
- \(x\) is the current value.
- \(\alpha\) is the learning rate.
- \(f'(x)\) is the gradient of the function.

## Features

- **Custom Quadratic Functions:** Define functions using coefficients a, b, and c.
- **Adjustable Starting Value:** Choose the initial point from which optimisation begins.
- **Configurable Learning Rate:** Experiment with different learning rates and observe their effects.
- **Maximum Iterations:** Set the maximum number of updates the algorithm can perform.
- **Tolerance-Based Early Stopping:** Stop the algorithm when the absolute gradient falls below the specified tolerance.
- **Convergence Reporting:** See whether the algorithm converged or reached its iteration limit.
- **Interactive Visualisation:** View the function curve, starting point, optimisation path, and final point.

## Technologies Used

- Python
- NumPy
- Matplotlib
- Streamlit

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Tobi454/gradient-descent-project.git
```

Replace the repository URL with your actual GitHub repository URL if you use a different repository name.

### 2. Navigate into the project directory

```bash
cd gradient-descent-project
```

### 3. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
```

Activate it:

**Linux/macOS:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## How to Use

1. Enter your desired starting value.
2. Adjust the learning rate.
3. Set the maximum number of iterations.
4. Specify the tolerance level.
5. Enter the coefficients a, b, and c to define your quadratic function.
6. Click **Run Gradient Descent**.
7. Examine the resulting metrics and visualisation.

Experiment with different parameter values to understand how they influence the optimisation process.

## Project Structure

```text
gradient-descent-project/
│
├── app.py
├── gradient_descent.ipynb
├── requirements.txt
└── README.md
```

## Limitations

The current implementation supports quadratic functions of the form \(f(x)=ax^2+bx+c\), with a positive coefficient a.

The learning rate also affects whether the algorithm converges. An unsuitable learning rate can cause slow convergence or divergence.

## Future Improvements

- Support for additional mathematical functions.
- More advanced optimisation algorithms.
- Improved visualisation of individual optimisation steps.
- Support for multivariable Gradient Descent.
