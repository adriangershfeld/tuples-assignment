# Task 1: Formatting Flight Itineraries
# Create a Python function that takes a list of tuples as an argument. 
# Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). 
# The function should format and return a string that lists each itinerary. 
# For example, if the input is `[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]`, the output should be a string formatted as:
# "Itinerary 1: Alice - From New York to London
# Itinerary 2: Bob - From Tokyo to San Francisco"

def format_itineraries(itineraries):
    formatted_string = "\n".join(
        f"Itinerary {index + 1}: {traveler_name} - From {origin} to {destination}"
        for index, (traveler_name, origin, destination) in enumerate(itineraries)
    )
    print(formatted_string)

format_itineraries([("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")])