import math

#8. Calculate the slope, x-intercept and y-intercept of y = 2x -2

# m = (y2-y1) / (x1-x2)

# Python program for slope of line 
def slope(x1, y1, x2, y2): 
    return (float)(y2-y1)/(x2-x1)  
  
# driver code     
x1 = 4
y1 = 2 
x2 = 2 
y2 = 5 
print "Slope is :", slope(x1, y1, x2, y2) 
