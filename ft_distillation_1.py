"""Distillation 1: accesses potions via the alchemy package interface."""

import alchemy


def main() -> None:
    """Run the distillation 1 experiment."""
    print("=== Distillation 1 ===")
    print("Using: 'import alchemy' structure to access potions")
    # strength_potion is re-exported from alchemy/__init__.py
    print(f"Testing strength_potion: {alchemy.strength_potion()}")
    # heal is healing_potion aliased in alchemy/__init__.py
    print(f"Testing heal alias: {alchemy.heal()}")


if __name__ == "__main__":
    main()
