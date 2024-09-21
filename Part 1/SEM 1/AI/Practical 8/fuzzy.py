import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Create input and output variables
temperature = ctrl.Antecedent(np.arange(0, 101, 1), 'temperature')
fan_speed = ctrl.Consequent(np.arange(0, 101, 1), 'fan_speed')

# Define fuzzy sets for temperature
temperature['cold'] = fuzz.trimf(temperature.universe, [0, 0, 50])
temperature['warm'] = fuzz.trimf(temperature.universe, [0, 50, 100])
temperature['hot'] = fuzz.trimf(temperature.universe, [50, 100, 100])

# Define fuzzy sets for fan_speed
fan_speed['low'] = fuzz.trimf(fan_speed.universe, [0, 0, 50])
fan_speed['medium'] = fuzz.trimf(fan_speed.universe, [0, 50, 100])
fan_speed['high'] = fuzz.trimf(fan_speed.universe, [50, 100, 100])

# Define rules
rule1 = ctrl.Rule(temperature['cold'], fan_speed['low'])
rule2 = ctrl.Rule(temperature['warm'], fan_speed['medium'])
rule3 = ctrl.Rule(temperature['hot'], fan_speed['high'])

# Create the control system
fan_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

# Create a simulation
fan_sim = ctrl.ControlSystemSimulation(fan_ctrl)

# Input temperature value
temperature_input = 20

# Set the input temperature
fan_sim.input['temperature'] = temperature_input

# Compute the fan speed
fan_sim.compute()

# Get the fan speed value
fan_speed_output = fan_sim.output['fan_speed']

print(f"For a temperature of {temperature_input} degrees")
print(f"Fan Speed: {fan_speed_output:.2f}%")
