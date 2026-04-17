"""Kaboom 0: records a light spell flawlessly via the grimoire module."""

from alchemy.grimoire import light_spell_record


def main() -> None:
    """Run the kaboom 0 experiment."""
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    # "Earth, wind and fire" contains "earth" — matches the allowed list
    result: str = light_spell_record("Fantasy", "Earth, wind and fire")
    print(f"Testing record light spell: {result}")


if __name__ == "__main__":
    main()
