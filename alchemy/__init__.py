"""Alchemy package public interface.

Exposes create_air (not create_earth) from elements,
heal alias and strength_potion from potions,
and lead_to_gold from transmutation.
"""

from alchemy.elements import create_air
from alchemy.potions import healing_potion as heal
from alchemy.potions import strength_potion
from alchemy.transmutation import lead_to_gold
__version__: str = "1.0.0"
__author__: str = "Alchemist"