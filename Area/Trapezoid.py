"""
A trapezoid is a quadrilateral with two sides parallel. The trapezoid is equivalent to the British definition of the trapezium.
An isosceles trapezoid is a trapezoid in which the base angles are equal so.
Trapezoid contains 2 sides which are parallel with length 'a' and 'b'.
And Height between those 2 lines is denoted by 'h'
"""

class Trapezoid:
  #formula for area of Trapezoid is product of sum of bases (a+b) and height (h) divided by 2.
  
  def TrapezoidArea(a,b,h):
    sum=(a+b)*h
    return sum/2
  
  try:
    a=float(input("Length of First Base: "))
    b=float(input("Length of Second Base: "))
    height=float(input("Height of Trapezoid: "))
    print(TrapezoidArea(a,b,height))
  except:
    print("Error in Input value")
    
  
  
