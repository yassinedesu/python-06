"""Light spellbook: records light magic spells with validation.

Imports validate_ingredients from light_validator at module level.
This works without circular dependency because light_validator
does NOT import from this module at module level (it uses a late import).
"""

from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    """Return the allowed ingredient list for light magic.

    Returns:
        list[str]: ['earth', 'air', 'fire', 'water']
    """
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    """Record a light magic spell after validating its ingredients.

    Args:
        spell_name: The name of the spell to attempt to record.
        ingredients: The ingredients used, as a string.

    Returns:
        str: Confirmation the spell was recorded, or a rejection message.
    """
    validation_result: str = validate_ingredients(ingredients)

    if "INVALID" in validation_result:
        return f"Spell rejected: {spell_name} ({validation_result})"
    return f"Spell recorded: {spell_name} ({validation_result})"