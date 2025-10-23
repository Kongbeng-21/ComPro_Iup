import math

def read_inputs():
    R = int(input('Input R: '))
    r = int(input('Input r: '))
    d = int(input('Input d: '))
    return (R,r,d)


def compute_and_display_coordinate(R, r, d):
    x0 = (R - r) * (math.cos(0)) + d * (math.cos((R - r) / r * (math.radians(0))))
    y0 = (R - r) * (math.sin(0)) + d * (math.sin((R - r) / r * (math.radians(0))))
    x90 = (R - r) * (math.cos(90)) + d * (math.cos((R - r) / r * (math.radians(90))))
    y90 = (R - r) * (math.sin(90)) + d * (math.sin((R - r) / r * (math.radians(90))))
    x180 = (R - r) * (math.cos(180)) + d * (math.cos((R - r) / r * (math.radians(180))))
    y180 = (R - r) * (math.sin(180)) + d * (math.sin((R - r) / r * (math.radians(180))))
    return (x0,y0,x90,y90,x180,y180)
    
def display_coordinate(x0,y0,x90,y90,x180,y180):
    xy0 = (f"Coordinate is ({x0:.3f}, {y0:.3f}) is at 0-degree angle.")
    xy90 = (f"Coordinate is ({x90:.3f}, {y90:.3f}) is at 90-degree angle.")
    xy180 = (f"Coordinate is ({x180:.3f}, {y180:.3f}) is at 180-degree angle.")
    
    
def compute_eccentricity(r, d):
    return (2 * math.sqrt((d / r))) / 1 + (d / r)

R,r,d = read_inputs()
cadc = compute_and_display_coordinate(R, r, d)



