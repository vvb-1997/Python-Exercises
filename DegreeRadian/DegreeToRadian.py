"""
The radian is the standard unit of angular measure, used in many areas of mathematics
An angle's measurement in radians is numerically equal to the length of a corresponding arc of a unit circle
"""

class Method:
  import math
  
  """
  The formula for Degree to Radians is multiply π/180 with degree value to get equivalent radian  
  """
  
  def DegreeToRadian(degree):
    return degree*(math.pi/180)
  
  try:
    degree = float(input("Input degrees: "))
    DegreeToRadian(degree)
  except IOError:
    print("Provide a Numerical value")
    
  #for example 1 degree is approximately 0.0174533 Radian
  DegreeToRadian(1) # output is 0.01745329251..
