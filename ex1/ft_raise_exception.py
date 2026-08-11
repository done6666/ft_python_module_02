#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    value: int = int(temp_str)

    if value < 0:
        raise ValueError(f"{value}°C is too cold for plants (min 0°C)")
    elif value > 40:
        raise ValueError(f"{value}°C is too hot for plants (max 40°C)")
    return value


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    for value in ("25", "abc", "100", "-50"):
        print()
        print(f"Input data is '{value}'")
        try:
            temperature: int = input_temperature(value)
        except Exception as error:
            print(f"Caught input_temperature error: {error}")
        else:
            print(f"Temperature is now {temperature}°C")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
