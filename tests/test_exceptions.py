from periodic_table import electronic_configuration


def test_chromium_exception():
    # Chromium: 4s1 3d5 (not 4s2 3d4)
    cfg = electronic_configuration(24)
    assert "4s1" in cfg
    assert "3d5" in cfg
    assert "4s2" not in cfg  # ensure the incorrect config is not present


def test_copper_exception():
    # Copper: 4s1 3d10 (not 4s2 3d9)
    cfg = electronic_configuration(29)
    assert "4s1" in cfg
    assert "3d10" in cfg
    assert "4s2" not in cfg


def test_molybdenum_exception():
    # Mo: 5s1 4d5 (not 5s2 4d4)
    cfg = electronic_configuration(42)
    assert "5s1" in cfg
    assert "4d5" in cfg
    assert "5s2" not in cfg


def test_silver_exception():
    # Ag: 5s1 4d10 (not 5s2 4d9)
    cfg = electronic_configuration(47)
    assert "5s1" in cfg
    assert "4d10" in cfg
    assert "5s2" not in cfg


def test_gold_exception():
    # Au: 6s1 4f14 5d10 (not 6s2 4f14 5d9)
    cfg = electronic_configuration(79)
    assert "6s1" in cfg
    assert "5d10" in cfg
    assert "6s2" not in cfg
