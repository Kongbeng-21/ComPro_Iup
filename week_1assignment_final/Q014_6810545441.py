# Name: Krittitee Chaisang # Student ID: 6810545441
import math

shapes = []

while True:
    shape = input("Enter shape type ( circle/rectangle/triangle ) or 'done' to finish: ")
    if shape == "done":
        break

    if shape == "circle":
        r = input("Enter radius: ")
        r_float = float(r)
        area = math.pi * (r_float ** 2)
        print(f"Circle area: {area:.2f}")
        shapes.append({"type": "circle", "dimensions": {"radius": r}, "area": area})

    elif shape == "rectangle":
        w = input("Enter width: ")
        h = input("Enter height: ")
        area = float(w) * float(h)
        print(f"Rectangle area: {area:.2f}")
        shapes.append({"type": "rectangle", "dimensions": {"width": w, "height": h}, "area": area})

    elif shape == "triangle":
        b = input("Enter base: ")
        h = input("Enter height: ")
        area = 0.5 * float(b) * float(h)
        print(f"Triangle area: {area:.2f}")
        shapes.append({"type": "triangle", "dimensions": {"base": b, "height": h}, "area": area})

print("\n--- SHAPE AREA REPORT ---")
total = sum(s["area"] for s in shapes) if shapes else 0.0
print(f"Total area: {total:.2f}")

if shapes:
    largest = max(shapes, key=lambda s: s["area"])
    smallest = min(shapes, key=lambda s: s["area"])

    def show(label, s):
        t, d, a = s["type"], s["dimensions"], s["area"]
        if t == "circle":
            print(f"{label} shape: Circle with radius {d['radius']}, area: {a:.2f}")
        elif t == "rectangle":
            print(f"{label} shape: Rectangle with width {d['width']}, height {d['height']}, area: {a:.2f}")
        else:
            print(f"{label} shape: Triangle with base {d['base']}, height {d['height']}, area: {a:.2f}")

    show("Largest", largest)
    show("Smallest", smallest)

print("\n-----------------------------")
