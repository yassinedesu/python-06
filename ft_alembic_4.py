"""Alembic 4: imports the alchemy package and shows selective exposure.

create_air is accessible; create_earth is intentionally hidden.
mypy will flag alchemy.create_earth — this is on purpose to demonstrate
that the type checker also sees the package interface boundary.
"""

import alchemy


def main() -> None:
    """Run the alembic 4 experiment."""
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
 
    print(f"Testing create_air: {alchemy.create_air()}")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")

    print(f"Testing the hidden create_earth: {alchemy.create_earth()}")


if __name__ == "__main__":
    main()