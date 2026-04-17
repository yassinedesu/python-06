"""Transmutation 2: accesses lead_to_gold purely through import alchemy."""

import alchemy


def main() -> None:
    """Run the transmutation 2 experiment."""
    print("=== Transmutation 2 ===")
    print("Import alchemy module only")
    print(f"Testing lead to gold: {alchemy.lead_to_gold()}")


if __name__ == "__main__":
    main()
