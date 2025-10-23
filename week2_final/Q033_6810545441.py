# Name: Krittitee Chaisang  # Student ID: 6810545441
while True:
    expression = input("Enter expression: ").strip()
    if expression == "EXIT":
        print("Goodbye!")
        break

    tokens = expression.split()

    if len(tokens) == 0:
        print("Error: Invalid expression format.")
        continue

    try:
        ans = float(tokens[0])
    except ValueError:
        print(f"Error: Invalid number '{tokens[0]}' in expression.")
        continue

    if len(tokens) == 1:
        print(f"Result: {ans:.1f}")
        continue

    if len(tokens) % 2 == 0:
        print("Error: Invalid expression format.")
        continue
    if tokens[-1] in ['+', '-', '*', '/']:
        print("Error: Invalid expression format.")
        continue
    bad = False
    for j in range(1, len(tokens) - 1):
        if tokens[j] in ['+', '-', '*', '/'] and tokens[j + 1] in ['+', '-', '*', '/']:
            print("Error: Invalid expression format.")
            bad = True
            break
    if bad:
        continue

    try:
        for i in range(1, len(tokens) - 1, 2):
            op = tokens[i]
            rhs_tok = tokens[i + 1]
            try:
                num = float(rhs_tok)
            except ValueError:
                print(f"Error: Invalid number '{rhs_tok}' in expression.")
                break

            if op not in ['+', '-', '*', '/']:
                print("Error: Invalid expression format.")
                break

            if op == '+':
                ans += num
            elif op == '-':
                ans -= num
            elif op == '*':
                ans *= num
            elif op == '/':
                if num == 0:
                    print("Error: Division by zero is not allowed.")
                    break
                ans /= num
        else:
            print(f"Result: {ans:.1f}")
    except Exception:
        print("Error: Invalid expression format.")
