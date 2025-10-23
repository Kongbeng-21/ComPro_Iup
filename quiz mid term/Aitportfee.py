weight = float(input("Input maximum takeoff weight: "))
days = float(input("Input number of parking days: "))
type = input("Input flight type (inter/dom): ")

FLF = 1000
if weight < 40:
    FLF + 120
elif 40 < weight < 90:
    FLF + 150
else: 
    FLF + 200
    
if type == "dom":
        FLF / 2
    
RLF = 1

PF = 0
if days > 50:
    PF = 15 * days
elif > 100:
    PF = 20 * days
TAF = FLF + RLF + PF

print(f"Flat-rate Landing Fee = {FLF:.2f}")
print(f"Remaining Landing Fee = {RLF:.2f}")
print(f"Parking Fee = {PF:.2f}")
print(f"Total Airport Fee = {TAF:.2f}")