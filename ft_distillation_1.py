"""Distillation 1: accesses potions via the alchemy package interface.

heal is an alias for healing_potion, defined in alchemy/__init__.py.
"""

import alchemy


def main() -> None:
    """Run the distillation 1 experiment."""
    print("=== Distillation 1 ===")
    print("Using: 'import alchemy' structure to access potions")
    
    print(f"Testing strength_potion: {alchemy.strength_potion()}")
    
    print(f"Testing heal alias: {alchemy.heal()}")


if __name__ == "__main__":
    main()