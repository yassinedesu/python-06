"""Distillation 1: accesses potions via the alchemy package interface.

heal is an alias for healing_potion, defined in alchemy/__init__.py.
"""

import alchemy  # runs __init__.py, which exposes strength_potion and heal


def main() -> None:
    """Run the distillation 1 experiment."""
    print("=== Distillation 1 ===")
    print("Using: 'import alchemy' structure to access potions")
    # strength_potion is re-exported from __init__.py
    print(f"Testing strength_potion: {alchemy.strength_potion()}")
    # heal is healing_potion aliased in __init__.py
    print(f"Testing heal alias: {alchemy.heal()}")


if __name__ == "__main__":
    main()