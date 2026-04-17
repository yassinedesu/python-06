"""Alchemy package public interface."""

# noqa: F401 on each line — these imports exist solely to re-export names.
# flake8 would flag them as "imported but unused" without it.
from alchemy.elements import create_air  # noqa: F401
from alchemy.potions import healing_potion as heal  # noqa: F401
from alchemy.potions import strength_potion  # noqa: F401
from alchemy.transmutation import lead_to_gold  # noqa: F401

__version__: str = "1.0.0"
__author__: str = "Alchemist"
