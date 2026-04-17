"""Alembic 1: uses 'from ... import ...' to access root-level elements.py."""

from elements import create_water


def main() -> None:
    """Run the alembic 1 experiment."""
    print("=== Alembic 1 ===")
    print("Using: 'from ... import ...' structure to access elements.py")
    print(f"Testing create_water: {create_water()}")


if __name__ == "__main__":
    main()
