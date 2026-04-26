from .config import SUBSHELL_CAPACITY, ORBITALS
from .exceptions import EXCEPTIONS

# ------------------------------------------------------------
# Full electron configuration (Aufbau principle)
# ------------------------------------------------------------

def electronic_configuration(atomic_number: int) -> str:
    """
    Return the full electron configuration string for a given atomic number.
    Applies real-world exceptions when necessary.
    """
    if not (1 <= atomic_number <= 118):
        raise ValueError("Invalid atomic number")

    # Real-world exception?
    if atomic_number in EXCEPTIONS:
        return EXCEPTIONS[atomic_number]

    remaining = atomic_number
    config_parts: list[str] = []
    i = 0

    while remaining > 0 and i < len(ORBITALS):
        n_shell, subshell = ORBITALS[i]
        capacity = SUBSHELL_CAPACITY[subshell]

        fill = min(remaining, capacity)
        config_parts.append(f"{n_shell}{subshell}{fill}")

        remaining -= fill
        i += 1

    return " ".join(config_parts)
