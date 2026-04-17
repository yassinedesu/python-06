"""Alembic 2: uses 'import ...' to access alchemy/elements.py."""

import alchemy.elements  # loads alchemy package, then alchemy.elements


def main() -> None:
    """Run the alembic 2 experiment."""
    print("=== Alembic 2 ===")
    print("Accessing alchemy/elements.py using 'import ...' structure")
    # Must use full dotted path to access the function
    print(f"Testing create_earth: {alchemy.elements.create_earth()}")


if __name__ == "__main__":
    main()