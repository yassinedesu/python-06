"""Alembic 1: uses 'from ... import ...' to access root-level elements.py."""

from elements import create_water  # copies create_water into local scope


def main() -> None:
    """Run the alembic 1 experiment."""
    print("=== Alembic 1 ===")
    print("Using: 'from ... import ...' structure to access elements.py")
    # Call directly — no module prefix needed
    print(f"Testing create_water: {create_water()}")


if __name__ == "__main__":
    main()