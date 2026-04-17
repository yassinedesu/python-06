"""Transmutation 2: accesses lead_to_gold purely through import alchemy.

lead_to_gold is accessible because alchemy/__init__.py imports it from
alchemy.transmutation, which in turn gets it from recipes.py.
"""

import alchemy  # runs alchemy/__init__.py, which chains to lead_to_gold


def main() -> None:
    """Run the transmutation 2 experiment."""
    print("=== Transmutation 2 ===")
    print("Import alchemy module only")
    # Works because of __init__.py chaining
    print(f"Testing lead to gold: {alchemy.lead_to_gold()}")


if __name__ == "__main__":
    main()