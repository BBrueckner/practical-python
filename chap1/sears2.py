import math

bill_thickness = 0.11 * 0.001 # meters (0.11 mm)
sears_height = 442 # meters

t = math.log(sears_height / bill_thickness, 2) + 1
print(f'It takes {math.ceil(t)} days to surpass Sears Tower.')


# Explanation:
# 2^(t - 1) * bill_thickness > sears_height
# 2^(t - 1) > sears_height / bill_thickness # use log2
# t - 1 > log2(sears_height / bill_thickness)
# t > log2(sears_height / bill_thickness) + 1
# math.ceil(t) # round up because t is measured in full days
# To use log2 [log(x, base = 2)] and ceil the math module needs
# to be imported first.