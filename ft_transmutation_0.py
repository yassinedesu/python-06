"""Transmutation 0: accesses recipes.py directly via import."""

import alchemy.transmutation.recipes


def main() -> None:
    """Run the transmutation 0 experiment."""
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    print(
        f"Testing lead to gold: "
        f"{alchemy.transmutation.recipes.lead_to_gold()}"
    )


if __name__ == "__main__":
    main()