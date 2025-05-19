def calculate_mpg(miles, gallons):
    """
    Calculate miles per gallon.
    :param miles: distance traveled in miles
    :param gallons: fuel used in gallons
    :return: mpg value
    """
    if gallons <= 0:
        raise ValueError("Gallons must be greater than zero.")
    return miles / gallons

if __name__ == "__main__":
    try:
        miles = float(input("Enter miles driven: "))
        gallons = float(input("Enter gallons used: "))
        mpg = calculate_mpg(miles, gallons)
        print(f"Your vehicle's fuel efficiency is {mpg:.2f} mpg.")
    except ValueError as e:
        print(f"Error: {e}")
