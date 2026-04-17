"""Alchemy package public interface.

Exposes create_air (not create_earth) from elements,
heal alias and strength_potion from potions,
and lead_to_gold from transmutation.
"""

# noqa comments suppress 'imported but unused' (F401): these imports
# exist solely to re-export names through the package interface.
from alchemy.elements import create_air  # noqa: F401
from alchemy.potions import healing_potion as heal  # noqa: F401
from alchemy.potions import strength_potion  # noqa: F401
from alchemy.transmutation import lead_to_gold  # noqa: F401

__version__: str = "1.0.0"
__author__: str = "Alchemist"