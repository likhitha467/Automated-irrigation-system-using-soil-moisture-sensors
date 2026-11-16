**Automated Irrigation System Using Soil Moisture Sensors**

 **Description**
An Arduino UNO-based automated irrigation system that monitors soil moisture levels and controls water pumping automatically. A 10kΩ potentiometer simulates the soil moisture sensor, while a DC motor represents the water pump.
** Components Used**
- Arduino UNO
- 10kΩ Potentiometer
- DC Motor
- NPN BJT Transistor
- 1N4007 Diode
- 1kΩ Resistor
- 220Ω Resistors (2)
- Red LED
- Green LED

** Software Tools**
- Python
- Arduino IDE
- SimulIDE

**Working**

The potentiometer provides analog readings between 0 and 1023 to Arduino UNO through pin A0.

- Red LED indicates dry soil.
- Green LED indicates wet soil.
- DC motor simulates the water pump.

Implementation Steps
1. Develop irrigation logic using Python.
2. Test different moisture input values.
3. Design the circuit in SimulIDE.
4. Write and compile Arduino code.
5. Load the HEX file into SimulIDE.
6. Test motor and LED responses.
**Outcome**
The system automatically activates the simulated water pump when soil moisture is low and switches it OFF when the soil reaches medium or wet conditions.

