# Name: Krittitee Chaisang  # Student ID: 6810545441
from pathlib import Path
from math import pi

def has_file(name):
    p = Path(name)
    if not p.exists():
        print(f"Error: {name} not found.\n")
        return False
    return True

def show_summary(cir, rect, sq, total_n, total_a, fname=""):
    title = f"Report for {fname}" if fname else "Grand Total"
    label = "Shapes:" if fname else "Total shapes:"
    overall = "" if fname else "overall "
    print(f"--- {title} ---")
    print(label)
    print(f"  circle: {cir}")
    print(f"  rectangle: {rect}")
    print(f"  square: {sq}")
    print(f"Total {overall}shapes: {total_n}")
    print(f"Total {overall}area: {total_a:.2f}")
    print("-------------------")

def valid_tokens(tokens):
    if not tokens:
        return False
    shape = tokens[0]
    if shape not in ("circle", "rectangle", "square"):
        return False
    try:
        if shape == "circle" and len(tokens) == 2:
            float(tokens[1]); return True
        if shape == "rectangle" and len(tokens) == 3:
            float(tokens[1]); float(tokens[2]); return True
        if shape == "square" and len(tokens) == 2:
            float(tokens[1]); return True
    except (ValueError, IndexError):
        return False
    return False

def unpack(tokens):
    try:
        kind = tokens[0]
        a = float(tokens[1])
        b = float(tokens[2]) if len(tokens) > 2 else None
        return kind, a, b
    except (ValueError, IndexError):
        return None, None, None

def bump(kind, area, file_acc, all_acc):
    if kind == "circle":
        file_acc["cir"] += 1; all_acc["cir"] += 1
    elif kind == "rectangle":
        file_acc["rect"] += 1; all_acc["rect"] += 1
    else:
        file_acc["sq"] += 1; all_acc["sq"] += 1
    file_acc["n"] += 1;  all_acc["n"] += 1
    file_acc["area"] += area; all_acc["area"] += area

totals = {"cir": 0, "rect": 0, "sq": 0, "n": 0, "area": 0.0}

if has_file("index.txt"):
    with open("index.txt", "r", encoding="utf-8") as fh:
        index_lines = fh.readlines()

    for name_line in index_lines:
        data_name = name_line.strip()
        if not data_name:
            continue
        if not has_file(data_name):
            continue

        print(f"Processing file: {data_name}")
        with open(Path(data_name), "r", encoding="utf-8") as fh:
            rows = fh.readlines()

        per_file = {"cir": 0, "rect": 0, "sq": 0, "n": 0, "area": 0.0}

        for raw in rows:
            parts = raw.split()
            if not parts:
                continue

            if valid_tokens(parts):
                kind, x, y = unpack(parts)
                if kind is None:
                    print(f"Error on line: {raw}", end="")
                    continue
                if kind == "circle":
                    area = pi * (x ** 2) 
                elif kind == "rectangle":
                    area = x * y 
                else:
                    area = x ** 2 
                bump(kind, area, per_file, totals)
            else:
                print(f"Error on line: {raw}", end="")

        show_summary(per_file["cir"], per_file["rect"], per_file["sq"],
                     per_file["n"], per_file["area"], data_name)
        print()

    show_summary(totals["cir"], totals["rect"], totals["sq"],
                 totals["n"], totals["area"])
