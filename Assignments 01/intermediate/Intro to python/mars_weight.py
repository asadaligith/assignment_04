

def mars_weight():
    print("\nCalculate Your Weight on Other Planets in Our Solar System\n")
    print("Available planets: Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune")

    try:
        Earth_weight = float(input("Enter your weight on Earth (kg): "))
    except ValueError:
        print("Please enter a valid number for weight.")
        return

    solar_planet = input("Enter a planet name from our solar system: ").strip().lower()

    gravity_map = {
        "mercury": 0.376,
        "venus": 0.889,
        "mars": 0.378,
        "jupiter": 2.36,
        "saturn": 1.081,
        "uranus": 0.815,
        "neptune": 1.14
    }

    if solar_planet in gravity_map:
        weight = Earth_weight * gravity_map[solar_planet]
        rounded_weight = round(weight, 2)
        print(f"\nYour weight on ---{solar_planet.title()}--- is {rounded_weight} kg.\n")
    else:
        print("Invalid Input! Please enter a correct planet name.")


if __name__ == '__main__':
    mars_weight()

        


