"""
Periodic Table Package
----------------------

Provides:
- Element data
- Lookup utilities
- Electron configuration engine
- Noble-gas shorthand
"""

from .data import ELEMENTS, Element
from .lookup import (
    get_element_by_atomic_number,
    get_element_by_symbol,
    get_element_by_name,
    get_all_elements,
)
from .engine import electronic_configuration
from .noble_gas import noble_gas_shorthand, noble_gas_core

__all__ = [
    "Element",
    "ELEMENTS",
    "get_element_by_atomic_number",
    "get_element_by_symbol",
    "get_element_by_name",
    "get_all_elements",
    "electronic_configuration",
    "noble_gas_shorthand",
]
