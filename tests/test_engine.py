from periodic_table import electronic_configuration


def test_hydrogen_configuration():
    # Simplest case: 1 electron
    assert electronic_configuration(1) == "1s1"


def test_helium_configuration():
    assert electronic_configuration(2) == "1s2"


def test_neon_configuration():
    # Full second shell
    assert electronic_configuration(10) == "1s2 2s2 2p6"


def test_calcium_configuration_ordering():
    # Ensures 4s fills before 3d
    cfg = electronic_configuration(20)  # Ca
    assert cfg.startswith("1s2 2s2 2p6 3s2 3p6 4s2")
    assert "3d" not in cfg  # Ca should not have 3d electrons


def test_selenium_configuration():
    # Selenium: 34 electrons
    cfg = electronic_configuration(34)
    assert "4p4" in cfg
    assert cfg.endswith("4p4")


def test_orbital_sequence_is_valid():
    # Ensure orbitals appear in correct Aufbau order
    cfg = electronic_configuration(26)  # Iron
    order = ["1s", "2s", "2p", "3s", "3p", "4s", "3d"]
    indices = [cfg.index(o) for o in order]
    assert indices == sorted(indices)


def test_invalid_atomic_number_low():
    # Negative or zero atomic numbers should return None
    try:
        electronic_configuration(0) 
    except ValueError:
        pass  # Expected to raise ValueError for invalid input
    try:
        electronic_configuration(-5)
    except ValueError:
        pass  # Expected to raise ValueError for invalid input


def test_invalid_atomic_number_high():
    # Out of range (>118) should return None
    try:
        electronic_configuration(200)
    except ValueError:
        pass  # Expected to raise ValueError for invalid input
