"""An interactive scientific calculator for the command line."""

import math


def calculate(operator: str, values: list[float]) -> float:
    """Run an operation, rejecting results that are undefined over the reals."""

    if operator == "+":
        result = values[0] + values[1]

    elif operator == "-":
        result = values[0] - values[1]

    elif operator == "*":
        result = values[0] * values[1]

    elif operator == "/":
        if values[1] == 0:
            raise ValueError("Division by zero is undefined.")
        result = values[0] / values[1]

    elif operator == "%":
        if values[1] == 0:
            raise ValueError("Modulo by zero is undefined.")
        result = values[0] % values[1]

    elif operator == "**":
        base, exponent = values

        if base == 0 and exponent == 0:
            raise ValueError("0^0 is undefined.")
        
        if base == 0 and exponent < 0:
            raise ValueError("Zero cannot be raised to a negative power.")
        
        result = base ** exponent
        if isinstance(result, complex):
            raise ValueError("This power has no real-number result.")
        
    elif operator == "sqrt":
        if values[0] < 0:
            raise ValueError("Square root of a negative number is not real.")
        result = math.sqrt(values[0])

    elif operator == "log":
        number, base = values

        if number <= 0:
            raise ValueError("A logarithm's number must be positive.")
        
        if base <= 0 or base == 1:
            raise ValueError("A logarithm's base must be positive and different from 1.")
        result = math.log(number, base)

    elif operator == "ln":
        if values[0] <= 0:
            raise ValueError("Natural logarithm is defined only for positive numbers.")
        result = math.log(values[0])

    elif operator == "log10":
        if values[0] <= 0:
            raise ValueError("Base-10 logarithm is defined only for positive numbers.")
        result = math.log10(values[0])

    elif operator == "abs":
        result = abs(values[0])

    elif operator == "fact":
        if values[0] < 0 or not values[0].is_integer():
            raise ValueError("Factorial is defined here only for non-negative whole numbers.")
        result = math.factorial(int(values[0]))

    elif operator in {"sin", "cos", "tan"}:
        angle = values[0]
        radians = math.radians(angle)

        if operator == "sin":
            result = math.sin(radians)

        elif operator == "cos":
            result = math.cos(radians)

        else:
            if math.isclose(math.cos(radians), 0.0, abs_tol=1e-12):
                raise ValueError("Tangent is undefined at 90° + 180° × any integer.")
            result = math.tan(radians)

    else:
        raise ValueError("Unknown operation.")

    if isinstance(result, float) and not math.isfinite(result):
        raise ValueError("The result is outside the calculator's real-number range.")
    return result


OPERATIONS = {
    "+": (2, "Add two numbers"),
    "-": (2, "Subtract the second number from the first"),
    "*": (2, "Multiply two numbers"),
    "/": (2, "Divide the first number by the second"),
    "%": (2, "Modulo (remainder) of two numbers"),
    "**": (2, "Raise the first number to the second power"),
    "sqrt": (1, "Square root"),
    "log": (2, "Logarithm (number, base)"),
    "ln": (1, "Natural logarithm"),
    "log10": (1, "Base-10 logarithm"),
    "abs": (1, "Absolute value"),
    "fact": (1, "Factorial"),
    "sin": (1, "Sine (angle in degrees)"),
    "cos": (1, "Cosine (angle in degrees)"),
    "tan": (1, "Tangent (angle in degrees)"),
}


def main() -> None:
    print("Scientific Calculator")
    print("Angles for sin, cos, and tan are entered in degrees.")
    print("The calculator reports when an operation is undefined over the real numbers.")

    while True:
        print("\nAvailable operations:")
        for symbol, (_, description) in OPERATIONS.items():
            print(f"  {symbol:5} {description}")
        operator = input("\nChoose an operation (or q to quit): ").strip().lower()

        if operator == "q":
            print("Goodbye!")
            break
        
        if operator not in OPERATIONS:
            print("Unknown operation. Please choose one from the list.")
            continue

        count = OPERATIONS[operator][0]
        try:
            values = [float(input(f"Number {index + 1}: ")) for index in range(count)]
            if not all(math.isfinite(value) for value in values):
                raise ValueError("Please enter finite numbers, not infinity or NaN.")
            result = calculate(operator, values)
            print(f"Result: {result:g}")
        except (ValueError, OverflowError) as error:
            print(f"Could not calculate: {error}")


if __name__ == "__main__":
    main()
