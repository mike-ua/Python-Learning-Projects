'''
Delivery Calculator, April 2024, Step 1, Starting base
Part I: retreives the correct tariffs
Part II: checks for validity of zones and calculates a tariff based on the higher zone rate
Part III: 'main' orchestrates the app via 'try/except' (and converts to 'int') based on input values of users
Future iterations will add additional functionality
'''

def get_tariff_rate(zone):
    # Return the tariff rate for a given zone making use of a dictionary and 'get' method
    zone_tariffs = {1: 30, 2: 60, 3: 90}
    return zone_tariffs.get(zone, "Invalid zone")

def calculate_tariff(from_zone, to_zone):
    # Calculate the delivery tariff based on the higher rate between two zones.
    from_tariff = get_tariff_rate(from_zone)
    to_tariff = get_tariff_rate(to_zone)

    # Check if either zone is invalid and return a message if so
    if from_tariff == "Invalid zone" or to_tariff == "Invalid zone":
        return "One or both of your zones are invalid. Please enter zones 1, 2, or 3."
    
    # Calculate the higher tariff
    higher_tariff = max(from_tariff, to_tariff)
    return f"The delivery tariff for your package is: {higher_tariff}"

def main():
    print("Welcome to ABC Delery Company! Let's calculate a delivery rate.")

    try:
        from_zone = int(input("Please enter the zone you're sending from (1, 2, or 3): "))
        to_zone = int(input("Please enter the destination zone (1, 2, or 3): "))
        print(calculate_tariff(from_zone, to_zone))
    except ValueError:
        print("Invalid input. Please enter numeric values for zones.")

if __name__ == "__main__":
    main()