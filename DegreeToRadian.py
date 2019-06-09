"""
The radian is the standard unit of angular measure, used in many areas of mathematics
An angle's measurement in radians is numerically equal to the length of a corresponding arc of a unit circle
"""

class Method1:
  #Method 1
  """
  1 radian is just under 57.3 degrees
  Hence the ratio between degree and radian is (57.3)^-1 
  """

  def DegreeToRadian(degree,ratioDegreeRadian):
    return degree*ratioDegreeRadian

  #for example 1 degree is approximately 0.01745200698 Radian
  DegreeToRadian(1,1/57.3) # output is 0.017452..  

class Method2:
  import math
  #Method2
  """
  The formula for Degree to Radians is multiply π/180 with degree value to get equivalent radian  
  """
  def DegreeToRadian(degree):
    return degree*math.pi/180
  
  #for example 1 degree is approximately 0.0174533 Radian
  DegreeToRadian(1,1/57.3) # output is 0.01745329251..
