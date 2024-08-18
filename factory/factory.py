class StandardRide:
    def get_ride_type(self) -> str:
        return "Standard Ride"

    def calculate_fare(self, distance: float) -> float:
        return 5.0 + 1.0 * distance

    def estimated_time_of_arrival(self, distance: float) -> str:
        return f"Approximately {int(distance / 10)} minutes"

    def __repr__(self) -> str:
        return self.get_ride_type()

class PremiumRide:
    def get_ride_type(self) -> str:
        return "Premium Ride"

    def calculate_fare(self, distance: float) -> float:
        return 10.0 + 2.0 * distance

    def estimated_time_of_arrival(self, distance: float) -> str:
        return f"Approximately {int(distance / 12)} minutes"

    def __repr__(self) -> str:
        return self.get_ride_type()

class SharedRide:
    def get_ride_type(self) -> str:
        return "Shared Ride"

    def calculate_fare(self, distance: float) -> float:
        return 3.0 + 0.5 * distance

    def estimated_time_of_arrival(self, distance: float) -> str:
        return f"Approximately {int(distance / 8)} minutes"

    def __repr__(self) -> str:
        return self.get_ride_type()

class RideSharingFactory:
    @staticmethod
    def get_ride_service(ride_type: str):
        if ride_type == 'Standard':
            return StandardRide()
        elif ride_type == 'Premium':
            return PremiumRide()
        elif ride_type == 'Shared':
            return SharedRide()
        else:
            raise ValueError("Unsupported ride type")

def main():
    ride_types = ['Standard', 'Premium', 'Shared']
    distance = 10  # Example distance

    factory = RideSharingFactory()

    for ride_type in ride_types:
        ride_service = factory.get_ride_service(ride_type)
        print(f"Ride Type: {repr(ride_service)}")
        print(f"Fare: ${ride_service.calculate_fare(distance)}")
        print(f"ETA: {ride_service.estimated_time_of_arrival(distance)}")
        print()  # For better readability

if __name__ == "__main__":
    main()
