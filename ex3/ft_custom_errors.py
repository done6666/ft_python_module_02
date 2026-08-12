#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown watering error") -> None:
        super().__init__(message)


def check_plant(plant_name: str, is_healthy: bool) -> None:
    if not is_healthy:
        raise PlantError(f"The {plant_name} plant is wilting!")


def check_water_tank(liters: int) -> None:
    if liters < 5:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    print()
    print("Testing PlantError...")
    try:
        check_plant("tomato", False)
    except PlantError as error:
        print(f"Caught PlantError: {error}")

    print()
    print("Testing WaterError...")
    try:
        check_water_tank(0)
    except WaterError as error:
        print(f"Caught WaterError: {error}")

    print()
    print("Testing catching all garden errors...")
    try:
        check_plant("tomato", False)
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    try:
        check_water_tank(0)
    except GardenError as error:
        print(f"Caught GardenError: {error}")

    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
