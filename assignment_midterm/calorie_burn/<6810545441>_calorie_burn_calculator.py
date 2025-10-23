FOOD_DATA = {
    'entrees': {
        'porridge': 200,
            'grilled pork': 320,
            'pork bun': 200,
            'cereal': 250,
            'egg and sausage': 550,
            'basil pork': 580,
            'chicken rice': 590,
            'bbq pork rice': 540,
            'garlic pork rice': 520,
            'rice and curry': 480,
            'noodle soup': 270,
            'suki': 345,
            'rat na noodle': 400,
            'fried noodle': 620,
            'fried rice': 550,
            'somtam': 110,
            'yam woon sen': 170,
            'chicken salad': 120,
        'instant noodle': 250,
            'spaghetti': 430,
            'ham sandwich': 290,
        'burger and fries': 620,
            'pizza': 700,
            'pork steak': 540,
            'fried chicken': 710,
    },
    'desserts': {
        'fruit': 80,
            'mango sticky rice': 170,
            'potato chips': 180,
            'ice cream': 260,
        'cookies': 240,
            'brownie': 160,
            'donut': 180,
            'croissant': 270,
            'cake': 370,
        'none': 0,
    },
    'drinks': {
        'milk': 160,
            'soy_milk': 100,
            'juice': 110,
            'soda': 130,
            'black coffee': 15,
        'iced capucino': 150,
            'matcha': 5,
            'matcha latte': 130,
            'smoothie': 115,
        'water': 0,
    }
}
EXERCISE_DATA = {
    'aerobics': 600,
    'badminton': 315,
    'cycling': 560,
    'housework': 215,
    'running': 550,
    'swimming': 420,
    'walking': 230,
}
print("--- Setting up your profile ---")
while True:
    name = input(f"Enter your name: ").strip()
    if name:
        break
    print("Invalid input.")
    
while True:
    gender = input("Enter your gender (M/F): ").strip().upper()
    if gender in ("M", "F"):
        break
    print("Invalid input.")
    
while True:
    age = int(input("Enter your age: "))
    if age > 0:
        break
    print("Invalid input.")

while True:
    weight = float(input("Enter your weight (kg): "))
    if weight > 0:
        break
    print("Weight must be positive.")
    
while True:
    height = float(input("Enter your height (cm): "))
    if height > 0:
        break
    print("Height must be positive.")
    
    
print("--- Activity Level ---")
print("1. Sedentary (little or no exercise)")
print("2. Lightly active (1-3 workouts/week)")
print("3. Moderately active (4-5 workouts/week)")
print("4. Very active (6-7 workouts/week)")
print("5. Extremely active (physical job or training)")

while True:
    x = input("Choose your activity level (1-5): ").strip()
    if x.isdigit() and 1 <= int(x) <= 5:
        act_lev = int(x)
        break
    print("Invalid choice.")


def cal_BMR(name, gender, age, weight, height):
    if gender == ("M"):
        return (88.362 + (13.397 * (weight))) + ((4.799 * height) - (5.677 *age))
    else:
        return (447.593 + (9.247 * (weight))) + ((3.098 * height) - (4.330 *age))                


def cal_TDEE(BMR, act_lev):
    factors = {1: 1.2,2: 1.375,3: 1.55,4: 1.725,5 :1.9}
    return int(BMR * factors[act_lev])


BMR = cal_BMR(name, gender, age, weight, height)
tdee = cal_TDEE(BMR, act_lev)
print(f'Profile created for Eaty {name}. Your TDEE is {tdee} kcal.')
tdee_goal = tdee
history = {}


def list_options(options_dict):
    return sorted(options_dict.keys())

def choose_from_list(title, items, cols=5, col_w=22):
    print(f"\n{title}:")
    line = "┌" + "┬".join(["─"*col_w]*cols) + "┐"
    print(line)
    for r in range(0, len(items), cols):
        row_items = items[r:r+cols]
        cells = []
        for i, name in enumerate(row_items, start=r+1):
            cells.append(f" {i:>2}. {name:<{col_w-6}} ")
        # เติมช่องว่างให้ครบคอลัมน์
        while len(cells) < cols:
            cells.append(" " * col_w)
        print("│" + "│".join(cells) + "│")
    print("└" + "┴".join(["─"*col_w]*cols) + "┘")

    while True:
        s = input(f"Choose a {title[:-1]} by number (1-{len(items)}): ").strip()
        if s.isdigit():
            k = int(s)
            if 1 <= k <= len(items):
                return items[k-1]
            else:
                print("Invalid number.")
        else:
            print("Invalid input. Please enter a number.")

        
def get_or_create_day(date_str):
    if date_str not in history:
        history[date_str] = {"meals": [], "exercises": []}
    return history[date_str]

def add_meals():
    print("--- Adding Your Meals ---")
    date_str = input("Enter the date (YYYY-MM-DD): ").strip()
    day = get_or_create_day(date_str)
    
    while True:
        n = input("How many more meals to add? ").strip()
        if n.isdigit() and int(n) > 0:
            n = int(n)
            break
        print("Invalid number.")
        
    entree_list  = list_options(FOOD_DATA['entrees'])
    dessert_list = list_options(FOOD_DATA['desserts'])
    drink_list   = list_options(FOOD_DATA['drinks'])   

    for i in range(1, n+1):
        print(f"\n--- Meal #{i} ---")
        entree = choose_from_list("Entree Choices",  entree_list)
        dessert = choose_from_list("Dessert Choices", dessert_list)
        drink   = choose_from_list("Drink Choices",   drink_list)
        
        
        meal_kcal = (
            FOOD_DATA['entrees'][entree] +
            FOOD_DATA['desserts'][dessert] +
            FOOD_DATA['drinks'][drink]
        )
        day["meals"].append({
            "entree": entree,
            "dessert": dessert,
            "drink": drink,
            "kcal": meal_kcal
        })
    print("\nMeals added successfully!")
    
    
def add_exercise():
    print("--- Adding Your Exercise ---")
    date_str = input("Enter the date (YYYY-MM-DD): ").strip()
    day = get_or_create_day(date_str)

    ex_list = list_options(EXERCISE_DATA)
    exercise = choose_from_list("Exercise Choices", ex_list)

    while True:
        mins = input(f"Enter duration for {exercise} in minutes: ").strip()
        try:
            mins = float(mins)
            if mins > 0:
                break
        except:
            pass
        print("Invalid input.")    
    per_hour = EXERCISE_DATA[exercise]
    burned = int(round((per_hour/60.0) * mins))
    day["exercises"].append({"name": exercise, "mins": mins, "kcal": burned})

    print(f"\nLogged {exercise} for {mins:.1f} minutes, burning {burned} kcal.")

def remove_entry():
    print("--- Remove an Entry ---")
    date_str = input("Enter the date (YYYY-MM-DD): ").strip()
    if date_str not in history:
        print("No data for that date.")
        return
    kind = input("Remove a 'meal' or an 'exercise'? ").strip().lower()
    if kind not in ("meal", "exercise"):
        print("Invalid type.")
        return

    day = history[date_str]
    if kind == "meal":
        items = day["meals"]
        if not items:
            print("No meals to remove.")
            return
        print("\n--- Select Meal to Remove ---")
        for i, m in enumerate(items, start=1):
            print(f"{i}. Entree: {m['entree']}, Dessert: {m['dessert']}, Drink: {m['drink']}")
        s = input("Enter the number of the meal to remove: ").strip()
        if s.isdigit() and 1 <= int(s) <= len(items):
            idx = int(s)-1
            items.pop(idx)
            print(f"Meal #{int(s)} has been removed.")
        else:
            print("Invalid number.")
    else:
        items = day["exercises"]
        if not items:
            print("No exercises to remove.")
            return
        print("\n--- Select Exercise to Remove ---")
        for i, e in enumerate(items, start=1):
            print(f"{i}. {e['name']} ({e['kcal']} kcal burned)")
        s = input("Enter the number of the exercise to remove: ").strip()
        if s.isdigit() and 1 <= int(s) <= len(items):
            idx = int(s)-1
            items.pop(idx)
            print(f"Exercise #{int(s)} has been removed.")
        else:
            print("Invalid number.")

def show_summary_of_the_day():
    print("--- Daily Summary ---")
    date_str = input("Enter the date (YYYY-MM-DD): ").strip()
    if date_str not in history:
        print("No data found for that date.")
        return

    day = history[date_str]
    meals = day["meals"]
    exs   = day["exercises"]

    consumed = sum(m["kcal"] for m in meals)
    burned   = sum(e["kcal"] for e in exs)
    net = consumed - burned - tdee_goal
    print_daily_table(date_str, meals, exs, consumed, burned, tdee_goal, net)

def _draw_line(left, mid, right, widths):
    return left + mid.join("─"*w for w in widths) + right

def _row(cells, widths):
    padded = []
    for text, w in zip(cells, widths):
        txt = str(text)
        if len(txt) > w:  # ตัดข้อความถ้ายาวเกิน
            txt = txt[:max(0, w-1)] + "…"
        padded.append(f"{txt:^{w}}")  # จัดกึ่งกลาง
    return "│" + "│".join(padded) + "│"

def print_daily_table(date_str, meals, exs, consumed, burned, tdee_goal, net):
    title = f"Summary for {date_str}"
    total_w = 70
    print("┌" + "─"*total_w + "┐")
    print("│" + f"{title:^{total_w}}" + "│")
    print("├" + "─"*total_w + "┤")

    print("│" + f"{'Meals Consumed':^{total_w}}" + "│")
    widths = [8, 20, 20, 20]
    print(_draw_line("├","┬","┤",widths))
    print(_row(["Meal #","Entree","Dessert","Drink"], widths))
    print(_draw_line("├","┼","┤",widths))
    if meals:
        for i, m in enumerate(meals, start=1):
            print(_row([i, m['entree'], m['dessert'], m['drink']], widths))
    else:
        print("│" + f"{'No meals logged.':^{total_w}}" + "│")
    print("├" + "─"*total_w + "┤")

    print("│" + f"{'Exercises Logged':^{total_w}}" + "│")
    if exs:
        for i, e in enumerate(exs, start=1):
            msg = f"{i}. {e['name']}  ({e['kcal']:>3} kcal burned)"
            print("│" + f"{msg:<{total_w}}" + "│")
    else:
        print("│" + f"{'No exercises logged.':^{total_w}}" + "│")
    print("├" + "─"*total_w + "┤")

    print("│" + f"{'Totals':^{total_w}}" + "│")
    print("├" + "─"*total_w + "┤")
    def line_pair(label, value):
        msg = f"{label:<15} {value:>8} {'kcal':>10}"
        print("│" + f"{msg:<{total_w}}" + "│")
    line_pair("Consumed:", consumed)
    line_pair("Burned:",   burned)
    line_pair("TDEE Goal:", tdee_goal)
    line_pair("Net Balance:", net)
    print("└" + "─"*total_w + "┘")


def show_full_history():
    if not history:
        print("No history yet.")
        return

    all_dates = sorted(history.keys())
    total_consumed = total_burned = 0
    print("\n--- Full History Summary ---\n")
    print("--- Daily Breakdown ---\n")
    for d in all_dates:
        meals = history[d]["meals"]
        exs   = history[d]["exercises"]
        c = sum(m["kcal"] for m in meals)
        b = sum(e["kcal"] for e in exs)
        print(f"Date: {d}")
        print(f"  - Consumed: {c} kcal | Burned: {b} kcal\n")
        total_consumed += c
        total_burned   += b

    days = len(all_dates)
    avg_c = int(round(total_consumed / days))
    avg_b = int(round(total_burned / days))
    total_tdee = tdee_goal * days
    overall_net = total_consumed - total_burned - total_tdee

    print("+" + "-"*41 + "+")
    print("|{:^41}|".format("Overall Summary"))
    print("|" + "-"*41 + "|")
    print("| {:25} {:>13} |".format("Days Logged:", f"{days}"))
    print("| {:25} {:>8} {:>4} |".format("Avg Daily Consumption:", f"{avg_c}", "kcal"))
    print("| {:25} {:>8} {:>4} |".format("Avg Daily Burn:", f"{avg_b}", "kcal"))
    print("|" + "-"*41 + "|")
    print("| {:25} {:>8} {:>4} |".format("Total Consumed:", f"{total_consumed}", "kcal"))
    print("| {:25} {:>8} {:>4} |".format("Total Burned:",   f"{total_burned}",   "kcal"))
    print("| {:25} {:>8} {:>4} |".format("Total TDEE Goal:", f"{total_tdee}",  "kcal"))
    print("| {:25} {:>8} {:>4} |".format("Overall Net Balance:", f"{overall_net}", "kcal"))
    print("+" + "-"*41 + "+")
             
while True:    
    print("--- Main Menu ---")
    print("1. Add Meals")
    print("2. Add Exercise")
    print("3. Remove an Entry")
    print("4. Show Summary for a Day")
    print("5. Show Full History")
    print("6. Exit")
    choice = input("Enter your choice: ").strip()
    
    if choice == "1":
        add_meals()
    elif choice == "2":
        add_exercise()
    elif choice == "3":
        remove_entry()
    elif choice == "4":
        show_summary_of_the_day()
    elif choice == "5":
        show_full_history()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
 
        
