"""Transmutation 1: imports the transmutation sub-package.

lead_to_gold is accessible via alchemy.transmutation because
alchemy/transmutation/__init__.py re-exports it.
"""

import alchemy.transmutation  

def main() -> None:
    """Run the transmutation 1 experiment."""
    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")
    
    print(
        f"Testing lead to gold: {alchemy.transmutation.lead_to_gold()}"
    )


if __name__ == "__main__":
    main()