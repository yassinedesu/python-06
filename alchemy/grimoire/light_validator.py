"""Light ingredient validator: no circular dependency."""


def validate_ingredients(ingredients: str) -> str:
    """Validate ingredients against the light magic allowed list.

    Uses a late import of light_spell_allowed_ingredients to avoid
    circular dependency. By the time this function is called, all
    modules are fully loaded and the import reads from sys.modules.

    Args:
        ingredients: The ingredients string to validate.

    Returns:
        str: The ingredients string followed by ' - VALID' or ' - INVALID'.
    """
    # Late import: executed only when this function is called, not at module
    # load time. This breaks the circular dependency with light_spellbook.py.
    from .light_spellbook import light_spell_allowed_ingredients

    allowed: list[str] = light_spell_allowed_ingredients()
    lower_ingredients: str = ingredients.lower()
    is_valid: bool = any(item in lower_ingredients for item in allowed)
    keyword: str = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {keyword}"
