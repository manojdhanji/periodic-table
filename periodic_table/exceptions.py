# ------------------------------------------------------------
# Real-world electron configuration exceptions
# ------------------------------------------------------------
# These elements do NOT follow the idealized aufbau filling order.
# Their experimentally observed ground-state configurations differ
# due to subshell stabilization, electron-electron interactions,
# and relativistic effects (especially in heavy elements).
# ------------------------------------------------------------

EXCEPTIONS: dict[int, str] = {
    24: "1s2 2s2 2p6 3s2 3p6 4s1 3d5",   # Chromium
    29: "1s2 2s2 2p6 3s2 3p6 4s1 3d10",  # Copper
    42: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d5",   # Molybdenum
    47: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d10",  # Silver
    79: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s1 4f14 5d10",  # Gold
    90: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 6d2",  # Thorium
    # Add more if you want full realism for the lanthanides/actinides
}
