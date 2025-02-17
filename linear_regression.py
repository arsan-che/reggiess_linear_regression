#Calculating error
def get_y(m, b, x):
  y = m*x + b
  return y

get_y(1, 0, 7) == 7
get_y(5, 10, 3) == 25

#calculating error and distance between the points
def calculate_error(m, b, point):
  x_point, y_point = point
  y = m*x_point + b
  distance = abs(y - y_point)
  return distance

#testing the function
print(calculate_error(1, 0, (3, 3)))
print(calculate_error(1, 0, (3, 4)))
print(calculate_error(1, -1, (3, 3)))
print(calculate_error(-1, 1, (3, 3)))

#added some datapoints
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]