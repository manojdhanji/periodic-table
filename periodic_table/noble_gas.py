from .data import NOBLE_GASES
from .engine import electronic_configuration

# ------------------------------------------------------------
# Noble gas core lookup
# ------------------------------------------------------------

def noble_gas_core(z: int) -> tuple[int, str] | None:
    """
    Return (atomic_number, symbol) of the noble gas before Z.
    Example: Z=34 -> (18, "Ar")
    """
    candidates = [n for n in NOBLE_GASES.keys() if n < z]
    if not candidates:
        return None
    core_z = max(candidates)
    return core_z, NOBLE_GASES[core_z]


# ------------------------------------------------------------
# Noble gas shorthand configuration
# ------------------------------------------------------------

def noble_gas_shorthand(z: int) -> str:
    """
    Return noble-gas shorthand configuration for atomic number Z.
    Example: Z=34 -> "[Ar] 4s2 3d10 4p4"
    """
    core = noble_gas_core(z)
    full = electronic_configuration(z)

    # Hydrogen and Helium have no noble-gas core
    if core is None:
        return full

    core_z, core_symbol = core
    core_full = electronic_configuration(core_z)

    # Tokenize both configurations
    full_tokens = full.split()
    core_tokens = core_full.split()

    # Remove the core portion from the full configuration
    remainder = full_tokens[len(core_tokens):]

    return f"[{core_symbol}] " + " ".join(remainder)
