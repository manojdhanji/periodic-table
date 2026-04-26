# Periodic Table — Electron Configuration Engine
*This project is designed with a clear separation of concerns, making it easy to extend, test, port to JavaScript, or integrate into a UI.*
This project was built to provide a clean, accurate, and extensible electron‑configuration engine suitable for teaching, demos, and UI visualization. 
Most online tools hard‑code configurations; this engine computes them algorithmically using the Aufbau principle and real‑world exceptions.

## ✨ Features
- 118 elements with atomic number, symbol, name, and mass
- Electron configuration engine using the Aufbau principle
- Real‑world exceptions (Cr, Cu, Mo, Ag, Au, Th, etc.)
- Noble‑gas shorthand (e.g., Se -> [Ar] 4s2 3d10 4p4)
- Lookup utilities for name, symbol, atomic number
- Simple CLI for interactive use
- Modular architecture suitable for teaching, demos, or UI integration

## Project Structure
```text
periodic_table/
│
├── __init__.py          # Public API
├── data.py              # Element definitions
├── lookup.py            # Search utilities
├── config.py            # Aufbau constants
├── exceptions.py        # Real-world configuration overrides
├── engine.py            # Electron configuration engine
├── noble_gas.py         # Noble-gas shorthand logic
└── cli.py               # Interactive command-line interface
```
## How it all works

### Electron Configuration Engine
*The engine follows:*
- Aufbau principle
- Subshell capacities
- Orbital filling order
- Real‑world exceptions (e.g., Cr: 4s¹ 3d⁵)

### Noble‑Gas Shorthand
```code
Full:  1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p4
Core:  [Ar]
Short: [Ar] 4s2 3d10 4p4
```

### Lookup Utilities
Search by:
- atomic number
- symbol
- name

## Requirements
Python 3.10+ (due to | union type syntax)

## Installation
```text
pip install .
```

## Usage
Python API
```python
from periodic_table import (
    get_element_by_symbol,
    electronic_configuration,
    noble_gas_shorthand,
)

elm = get_element_by_symbol("Se")
print(elm.name)  # Selenium

print(electronic_configuration(elm.number))
print(noble_gas_shorthand(elm.number))
```

## CLI
```text
python -m periodic_table.cli
```

## Menu
The CLI offers the following menu
- Lookup by atomic number
- Lookup by name
- Lookup by symbol
- List all elements

```text
There are 118 different elements currently on the periodic table.
Of the 118 elements that have been discovered, there are 90 elements (1 through 92 except for elements 43 and 61) that occur in nature in appreciable amounts.
Elements are composed of atoms - atoms are comprised of protons (positively charged), neutrons (neutral) and electrons (negatively charged).

The atomic number or proton number of a chemical element is the number of protons found in the nucleus of an atom.
The atomic number uniquely identifies a chemical element.

The atomic mass is the total number of protons and neutrons in the nucleus.
Each element has a unique symbol (an abbreviation).

1 Get element by atomic number
2 Get element by name
3 Get element by symbol
4 Get all elements

Choose a number between (1 - 4): 3
Choose the symbol of the element (A - Z or Aa - Zz): Se

Element: Se (Selenium)
Electronic configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p4
Noble gas shorthand: [Ar] 4s2 3d10 4p4

Would you like to continue (Yes: Y):
```

## Tests
This project includes a complete pytest suite covering:

- Lookups
- Engine behavior
- Noble‑gas shorthand
- Exception handling
- CLI subprocess behavior

### Run all tests
```text
pytest -q
```

### Run a single test
```text
pytest tests/test_engine.py::test_selenium_configuration
```

