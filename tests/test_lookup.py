from periodic_table import (
    get_element_by_atomic_number,
    get_element_by_symbol,
    get_element_by_name,
    get_all_elements,
)

def test_lookup_by_atomic_number():
    elm = get_element_by_atomic_number(34)
    assert elm.symbol == "Se"
    assert elm.name == "Selenium"

def test_lookup_by_symbol():
    elm = get_element_by_symbol("Cu")
    assert elm.number == 29
    assert elm.name == "Copper"

def test_lookup_by_name():
    elm = get_element_by_name("gold")
    assert elm.symbol == "Au"
    assert elm.number == 79
    
def test_lookup_by_atomic_number_invalid():
    elm = get_element_by_atomic_number(999)  # out of range
    assert elm is None

def test_lookup_by_symbol_invalid():
    elm = get_element_by_symbol("Xx")  # not a real element
    assert elm is None

def test_lookup_by_name_invalid():
    elm = get_element_by_name("unobtainium")  # fictional
    assert elm is None

def test_get_all_elements():
    elements = get_all_elements()
    assert len(elements) == 118
    assert elements[0].symbol == "H"
