"""Transmutation recipes: demonstrates absolute and relative imports."""

import elements  # absolute: root elements.py
from ..elements import create_air  # relative: go up to alchemy/
from ..potions import strength_potion  # relative: go up to alchemy/


def lead_to_gold() -> str:
    """Transmute lead into gold using the philosopher's recipe.

    Returns:
        str: The full transmutation recipe description string.
    """
    air: str = create_air()
    strength: str = strength_potion()
    fire: str = elements.create_fire()
    return (
        f"Recipe transmuting Lead to Gold: brew '{air}' and "
        f"'{strength}' mixed with '{fire}'"
    )
