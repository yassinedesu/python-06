"""Transmutation recipes: demonstrates absolute and relative imports together.

Absolute import: root elements.py (crosses package boundary).
Relative imports: alchemy/elements.py and alchemy/potions.py (stay inside
the alchemy package using .. to navigate to the parent).
"""

import elements  # absolute: root elements.py — not part of alchemy package
from ..elements import create_air  # relative: go up to alchemy/, then elements
from ..potions import strength_potion  # relative: go up to alchemy/, then potions


def lead_to_gold() -> str:
    """Transmute lead into gold using the philosopher's recipe.

    Combines air element, strength potion, and fire element.

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