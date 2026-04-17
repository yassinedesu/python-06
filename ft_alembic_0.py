"""Alembic 0: uses 'import ...' to access root-level elements.py."""

import elements  # loads the entire elements module object


def main() -> None:
    """Run the alembic 0 experiment."""
    print("=== Alembic 0 ===")
    print("Using: 'import ...' structure to access elements.py")
    # Access via dot notation on the module object
    print(f"Testing create_fire: {elements.create_fire()}")


if __name__ == "__main__":
    main()