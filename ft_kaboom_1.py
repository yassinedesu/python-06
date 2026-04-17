"""Kaboom 1: attempts to import dark_spellbook, triggering a circular import.

This script raises an uncaught ImportError to demonstrate exactly what
circular dependency failure looks like. Do NOT fix it — the crash is
the point.
"""

print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")


from alchemy.grimoire.dark_spellbook import dark_spell_record

print(f"Testing dark spell: {dark_spell_record('Dark', 'bats')}")