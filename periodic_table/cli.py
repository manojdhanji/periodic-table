from .lookup import (
    get_element_by_atomic_number,
    get_element_by_name,
    get_element_by_symbol,
    get_all_elements,
)
from .engine import electronic_configuration
from .noble_gas import noble_gas_shorthand
from .data import Element


# ------------------------------------------------------------
# Menu options (Strategy Pattern)
# ------------------------------------------------------------

OPTIONS = {
    1: {
        "msg": "Get element by atomic number",
        "act": get_element_by_atomic_number,
        "prompt": "Choose the atomic number of the element (1 - 118): ",
        "error": "Invalid atomic number!",
    },
    2: {
        "msg": "Get element by name",
        "act": get_element_by_name,
        "prompt": "Choose the name of the element: ",
        "error": "Invalid name!",
    },
    3: {
        "msg": "Get element by symbol",
        "act": get_element_by_symbol,
        "prompt": "Choose the symbol of the element (A - Z or Aa - Zz): ",
        "error": "Invalid symbol!",
    },
    4: {
        "msg": "Get all elements",
        "act": get_all_elements,
    },
}


# ------------------------------------------------------------
# Print helpers
# ------------------------------------------------------------

def print_element_info(choice: int, elm: Element | None) -> None:
    if elm is None:
        print(OPTIONS[choice]["error"])
        return

    print(f"\nElement: {elm.symbol} ({elm.name})")
    print("Electronic configuration:", electronic_configuration(elm.number))
    print("Noble gas shorthand:", noble_gas_shorthand(elm.number))


def print_elements(elements: list[Element]) -> None:
    for e in elements:
        print(
            f"Atomic number: {e.number}, "
            f"Symbol: {e.symbol}, "
            f"Name: {e.name}, "
            f"Atomic mass: {e.mass}"
        )


# ------------------------------------------------------------
# Intro text
# ------------------------------------------------------------

INTRO = """
There are 118 different elements currently on the periodic table.
Of the 118 elements that have been discovered, there are 90 elements (1 through 92 except for elements 43 and 61) that occur in nature in appreciable amounts.
Elements are composed of atoms - atoms are comprised of protons (positively charged), neutrons (neutral) and electrons (negatively charged).

The atomic number or proton number of a chemical element is the number of protons found in the nucleus of an atom.
The atomic number uniquely identifies a chemical element.

The atomic mass is the total number of protons and neutrons in the nucleus.
Each element has a unique symbol (an abbreviation).
"""


# ------------------------------------------------------------
# Main CLI loop
# ------------------------------------------------------------

def main() -> None:
    print(INTRO)

    cont = "Y"
    while cont == "Y":
        # Print menu
        for i, v in OPTIONS.items():
            print(i, v["msg"])
        print()

        try:
            choice = int(input("Choose a number between (1 - 4): "))

            if choice not in OPTIONS:
                print("Invalid choice!")
                continue

            option = OPTIONS[choice]

            # Option 4: no prompt, returns full list
            if choice == 4:
                print_elements(option["act"]())
            else:
                user_input = input(option["prompt"])
                elm = option["act"](user_input if choice != 1 else int(user_input))
                print_element_info(choice, elm)

        except ValueError as e:
            print("\t", e)

        cont = input("\nWould you like to continue (Yes: Y): ")[:1].upper()
        print()


if __name__ == "__main__":
    main()
