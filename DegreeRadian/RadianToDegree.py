"""
The radian is the standard unit of angular measure, used in many areas of mathematics
An angle's measurement in radians is numerically equal to the length of a corresponding arc of a unit circle
"""

class Method:
  import math
  
  """
  The formula for Degree to Radians is multiply π/180 with degree value to get equivalent radian  
  """
  
  def RadianToDegree(radian):
    return radian*(180/math.pi)
    
  try:
    radian = float(input("Input degrees: "))
    print(RadianToDegree(radian))
  except IOError:
    print("Provide a Numerical value")
    
  #for example 1 degree is approximately 0.0174533 Radian
  print(RadianToDegree(1)) # output is 0.01745329251..
