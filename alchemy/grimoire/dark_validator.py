"""Dark ingredient validator: intentionally causes a circular import.

WARNING: The top-level import of dark_spell_allowed_ingredients creates
a circular dependency with dark_spellbook.py. This module exists solely
to demonstrate what a circular import failure looks like at runtime.
"""


from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    """Validate ingredients against the dark magic allowed list.

    This function is never reached due to the ImportError on load.

    Args:
        ingredients: The ingredients string to validate.

    Returns:
        str: The ingredients string followed by ' - VALID' or ' - INVALID'.
    """
    allowed: list[str] = dark_spell_allowed_ingredients()
    lower_ingredients: str = ingredients.lower()
    is_valid: bool = any(
        item in lower_ingredients for item in allowed
    )
    keyword: str = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {keyword}"