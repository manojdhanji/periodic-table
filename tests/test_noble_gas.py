from periodic_table import noble_gas_shorthand, noble_gas_core

def test_sodium_gas_core():
    # Sodium has no noble gas core
    core_z, core_cfg = noble_gas_core(11)
    assert core_z == 10
    assert core_cfg == 'Ne'

def test_helium_shorthand():
    # Helium is itself a noble gas
    assert noble_gas_shorthand(2) == "1s2"


def test_neon_shorthand():
    # Neon shorthand should collapse to [He] 2s2 2p6
    assert noble_gas_shorthand(10) == "[He] 2s2 2p6"


def test_argon_shorthand():
    # Argon is a noble gas
    assert noble_gas_shorthand(18) == "[Ne] 3s2 3p6"


def test_selenium_shorthand():
    # Selenium: [Ar] 4s2 3d10 4p4
    short = noble_gas_shorthand(34)
    assert short.startswith("[Ar]")
    assert "4s2" in short
    assert "3d10" in short
    assert short.endswith("4p4")


def test_krypton_shorthand():
    # Krypton is a noble gas
    assert noble_gas_shorthand(36) == "[Ar] 4s2 3d10 4p6"


def test_invalid_atomic_number_low():
    try:
        assert noble_gas_shorthand(0) is None
    except ValueError:
        pass  # Expected to raise ValueError for invalid input


def test_invalid_atomic_number_high():
    try:
        assert noble_gas_shorthand(200) is None
    except ValueError:
        pass  # Expected to raise ValueError for invalid input
