import math

def calculate_circle_area():
    print("╔" + "═" * 38 + "╗")
    print("║{:^38}║".format("CALCULATOR: AREA OF CIRCLE"))
    print("╠" + "═" * 38 + "╣")

    try:
        ChuaRad = float(input("  ▸ Enter Radius: "))
        ChuaArea = math.pi * (ChuaRad ** 2)

        print("╟" + "─" * 38 + "╢")
        print(f"  RESULTING AREA: {ChuaArea:,.4f}")
        print("╚" + "═" * 38 + "╝")
    except ValueError:
        print("  [!] Error: Please enter a valid number.")

if __name__ == "__main__":
    calculate_circle_area()