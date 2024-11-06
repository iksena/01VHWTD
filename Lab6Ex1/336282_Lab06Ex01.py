import math

# Calculate diameter (d) from wire gauge (n)
# @param {number} n - wire gauge
# @returns {number} diameter of the wire
def diameter(n):
    return 0.127 * (92 ** ((36 - n) / 39))

# Calculate resistance (R) from resistivity(ro), wire length(L), and wire gauge(n)
# @param {number} resistivity - conductor resistiviy
# @param {number} length - wire length
# @param {number} n - wire gauge
# @returns {number} resistance of wire
def resistance(resistivity, length, n):
    diameterInMeter = diameter(n) / 1000

    return (4 * resistivity * length) / (math.pi * (diameterInMeter ** 2))

# Calculate resistance of copper wire
# @param {number} length - copper wire length
# @param {number} n - wire gauge
# @returns {number} resistance of copper wire
def copper_wire_resistance(length, n):
    COPPER_RESISTIVITY = 1.678 * (10 ** (-8))
    
    return resistance(COPPER_RESISTIVITY, length, n)

# Calculate resistance of aluminum wire
# @param {number} length - aluminum wire length
# @param {number} n - wire gauge
# @returns {number} resistance of aluminum wire
def aluminum_wire_resistance(length, n):
    ALUMINUM_RESISTIVITY = 2.82 * (10 ** (-8))

    return resistance(ALUMINUM_RESISTIVITY, length, n)

# Main function to test the program
# @returns {void}
def main():
    wireGauge = input("Input wire gauge: ")
    if(not wireGauge.isnumeric()):
        print('Input only numeric value')
        return
    wireGauge = int(wireGauge)
    if(wireGauge >= 0 and wireGauge <= 36):
        print(f'Diameter = {diameter(wireGauge)} mm')
    else:
        print('Input wire gauge only in between 0 and 36')
        return

    wireLength = input("Input wire length (m): ")
    if(not wireLength.isnumeric()):
        print('Input only numeric value')
        return
    wireLength = int(wireLength)
    if(wireLength > 0):
        print(f'Length = {wireLength} m')
    else:
        print('Input wire length only greater than 0')
        return
    
    wireType = input("Input wire type Copper (c) or Aluminum (a): ")
    if(wireType != 'c' and wireType != 'a'):
        print('Choose only c or a')
        return
    
    if(wireType == 'c'):
        resistance = copper_wire_resistance(wireLength, wireGauge)
        print(f'Copper Resistance = {resistance} ohm')

    if(wireType == 'a'):
        resistance = aluminum_wire_resistance(wireLength, wireGauge)
        print(f'Aluminum Resistance = {resistance} ohm')

main()