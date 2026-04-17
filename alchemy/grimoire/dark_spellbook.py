"""Dark spellbook: intentionally creates a circular dependency.

WARNING: Importing this module will raise ImportError.
This is intentional — it demonstrates what circular imports look like
and why they must be avoided in real code.

The cycle: dark_spellbook imports dark_validator (top-level),
dark_validator imports dark_spellbook (top-level) → explosion.
"""


from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    """Return the allowed ingredient list for dark magic.

    Returns:
        list[str]: ['bats', 'frogs', 'arsenic', 'eyeball']
    """
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    """Record a dark magic spell after validating its ingredients.

    Args:
        spell_name: The name of the dark spell to record.
        ingredients: The ingredients used in the dark spell.

    Returns:
        str: Confirmation the spell was recorded or rejected.
    """
    validation_result: str = validate_ingredients(ingredients)
    if "INVALID" in validation_result:
        return f"Dark spell rejected: {spell_name} ({validation_result})"
    return f"Dark spell recorded: {spell_name} ({validation_result})"