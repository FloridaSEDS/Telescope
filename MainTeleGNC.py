import time
import serial


# Telescope guidance, navigation, and control algorithm main program

# Assumptions:
#	Telescope is situated in Northern Hemisphere 
# 	User has some knowledge of inputs and astrometry (can determine which guide stars are available) 

# Use magnetometer and gravity vector to determine orientation
#	Attach IMU to shaft of telescope and align x-axis along major telescope axis 

# Import time 

# Write main function for pointing 
#	Use time to compute star position
#	Solve Kepler's Equation for sun's mean anomaly via numerical integration 
# 	Solve Kepler's Equation for Earth's mean anomaly 
# 	Rotate ECEF from ECI based on reference time 
#	Find Euler angles or quaternions to rotate from telescope to ECEF to star (multiply 2 rotation matrices) 

# Calibration 1: point to Polaris 

# Calibration 2: point to Sirius (if calculated to be 15 degrees above horizon) 

# Calibration 3: point to Rigel (if calculated to be 15 degrees above horizon) 