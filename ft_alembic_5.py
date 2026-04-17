"""Alembic 5: uses 'from alchemy import ...' to access the package."""

from alchemy import create_air


def main() -> None:
    """Run the alembic 5 experiment."""
    print("=== Alembic 5 ===")
    print("Accessing the alchemy module using 'from alchemy import ...'")
    print(f"Testing create_air: {create_air()}")


if __name__ == "__main__":
    main()