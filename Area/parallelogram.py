

class Parallelogram:
  #formula for area of Trapezoid is product of sum of bases (a+b) and height (h) divided by 2.
  
  def ParallelogramArea(a,b):
    return a*b
  
  try:
    a=float(input("Length of First Base: "))
    b=float(input("Length of Second Base: "))
    print(ParallelogramArea(a,b))
  except:
    print("Error in Input value")
