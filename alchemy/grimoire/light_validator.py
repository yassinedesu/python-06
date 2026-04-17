"""Light ingredient validator: no circular dependency.

Uses a late import (inside the function body) to access the allowed
ingredients list from light_spellbook. This prevents a circular import
at module load time because no top-level import of light_spellbook exists.
"""


def validate_ingredients(ingredients: str) -> str:
    """Validate ingredients against the light magic allowed list.

    Uses a late import of light_spell_allowed_ingredients to avoid
    circular dependency. By the time this function is called, all
    modules are fully loaded and the import simply reads from sys.modules.

    Args:
        ingredients: The ingredients string to validate.

    Returns:
        str: The ingredients string followed by ' - VALID' or ' - INVALID'.
    """
   
    from .light_spellbook import light_spell_allowed_ingredients

    allowed: list[str] = light_spell_allowed_ingredients()
    lower_ingredients: str = ingredients.lower()
   
    is_valid: bool = any(
        item in lower_ingredients for item in allowed
    )
    keyword: str = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {keyword}"