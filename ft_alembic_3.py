"""Alembic 3: uses 'from ... import ...' to access alchemy/elements.py."""

from alchemy.elements import create_air


def main() -> None:
    """Run the alembic 3 experiment."""
    print("=== Alembic 3 ===")
    print(
        "Accessing alchemy/elements.py using "
        "'from ... import ...' structure"
    )
    print(f"Testing create_air: {create_air()}")


if __name__ == "__main__":
    main()
