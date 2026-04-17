"""Kaboom 1: triggers a circular import by importing dark_spellbook.

The print statements before the import are intentional — the subject's
expected output requires them to appear before the crash traceback.
noqa: E402 suppresses flake8's 'module level import not at top of file'.
"""

print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")

# noqa: E402 — import must come after the prints to match expected output.
# Loading dark_spellbook triggers dark_validator which loops back → crash.
from alchemy.grimoire.dark_spellbook import dark_spell_record  # noqa: E402

print(f"Testing dark spell: {dark_spell_record('Dark', 'bats')}")
