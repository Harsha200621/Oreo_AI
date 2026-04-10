import googlemaps
from datetime import datetime

def get_directions(api_key, origin, destination, mode='driving', departure_time=None):
    """
    Get directions and navigation information using Google Maps API.

    Parameters:
    - api_key: Your Google Maps API key.
    - origin: Starting location.
    - destination: Ending location.
    - mode: Mode of transportation (default is 'driving'). Options: 'driving', 'walking', 'bicycling', 'transit'.
    - departure_time: Time of departure (optional, default is current time).

    Returns:
    - Directions and navigation information as a dictionary.
    """
    gmaps = googlemaps.Client(key=api_key)

    directions_result = gmaps.directions(origin,
                                         destination,
                                         mode=mode,
                                         departure_time=departure_time)

    return directions_result

def main():
    # Replace 'YOUR_API_KEY' with your actual Google Maps API key
    api_key = 'YOUR_API_KEY'

    origin = input("Enter the starting location: ")
    destination = input("Enter the destination: ")

    # You can change the mode of transportation if needed
    mode = 'driving'

    # Get directions
    directions = get_directions(api_key, origin, destination, mode)

    # Print out the steps in the directions
    print("Directions:")
    for step in directions[0]['legs'][0]['steps']:
        print(step['html_instructions'])

if __name__ == "__main__":
    main()
