"""Alembic 4: imports the alchemy package and shows selective exposure.

create_air is accessible via __init__.py; create_earth is intentionally
hidden. The call to alchemy.create_earth() raises AttributeError at
runtime AND a mypy [attr-defined] error — both are required by the subject.
"""

import alchemy


def main() -> None:
    """Run the alembic 4 experiment."""
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    # create_air is exposed in __init__.py — works fine
    print(f"Testing create_air: {alchemy.create_air()}")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    # create_earth is NOT in __init__.py — AttributeError at runtime.
    # mypy also reports [attr-defined] here — intentional per subject.
    print(f"Testing the hidden create_earth: {alchemy.create_earth()}")


if __name__ == "__main__":
    main()
