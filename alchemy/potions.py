"""Alchemy potions module: brews potions using all four elements."""

import elements  # absolute: root elements.py — fire and water
from .elements import create_earth, create_air  # relative: alchemy elements


def healing_potion() -> str:
    """Brew a healing potion using earth and air elements.

    Returns:
        str: Description of the brewed healing potion.
    """
    earth: str = create_earth()
    air: str = create_air()
    return f"Healing potion brewed with '{earth}' and '{air}'"


def strength_potion() -> str:
    """Brew a strength potion using fire and water elements.

    Returns:
        str: Description of the brewed strength potion.
    """
    fire: str = elements.create_fire()
    water: str = elements.create_water()
    return f"Strength potion brewed with '{fire}' and '{water}'"
