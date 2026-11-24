# Unit Converter

def km_to_m(km):
    return km * 1000


def kg_to_g(kg):
    return kg * 1000


def m_to_cm(m):
    return m * 100


if __name__ == "__main__":
    print("===== Unit Converter =====")
    print("1. Kilometres to Metres")
    print("2. Kilograms to Grams")
    print("3. Metres to Centimetres")

    choice = int(input("Enter your choice (1-3): "))
    value = float(input("Enter the value: "))

    if value < 0:
        print("Negative values are not allowed!")
    elif choice == 1:
        print(value, "km =", km_to_m(value), "m")
    elif choice == 2:
        print(value, "kg =", kg_to_g(value), "g")
    elif choice == 3:
        print(value, "m =", m_to_cm(value), "cm")
    else:
        print("Invalid choice!")