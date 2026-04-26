from .data import ELEMENTS, Element

# ------------------------------------------------------------
# Lookup dictionaries for O(1) access
# ------------------------------------------------------------

BY_NUMBER: dict[int, Element] = {e.number: e for e in ELEMENTS}
BY_SYMBOL: dict[str, Element] = {e.symbol: e for e in ELEMENTS}
BY_NAME:   dict[str, Element] = {e.name: e for e in ELEMENTS}

# ------------------------------------------------------------
# Lookup functions
# ------------------------------------------------------------

def get_element_by_atomic_number(atomic_number: int) -> Element | None:
    """Return the element with the given atomic number, or None if not found."""
    return BY_NUMBER.get(atomic_number)


def get_element_by_symbol(symbol: str) -> Element | None:
    """Return the element with the given symbol (case-insensitive)."""
    if not symbol:
        return None
    return BY_SYMBOL.get(symbol.title())


def get_element_by_name(name: str) -> Element | None:
    """Return the element with the given name (case-insensitive)."""
    if not name:
        return None
    return BY_NAME.get(name.title())


def get_all_elements() -> list[Element]:
    """Return the full list of elements."""
    return ELEMENTS
