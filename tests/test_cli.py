import subprocess
import sys
import os


def run_cli(input_data: str) -> subprocess.CompletedProcess:
    """
    Helper to run the CLI with given input and return the completed process.
    """
    return subprocess.run(
        [sys.executable, "-m", "periodic_table.cli"],
        input=input_data.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env={**os.environ, "PYTHONIOENCODING": "utf-8"},
    )


def test_cli_list_all_elements():
    # Option 4 = list all elements
    result = run_cli("4\n")
    output = result.stdout.decode()

    assert result.returncode == 0
    assert "Hydrogen" in output
    assert "118" in output or "Oganesson" in output


def test_cli_lookup_by_atomic_number():
    # Option 1, then enter 29 (Copper)
    result = run_cli("1\n29\n")
    output = result.stdout.decode()

    assert result.returncode == 0
    assert "Copper" in output
    assert "Cu" in output


def test_cli_lookup_by_symbol():
    # Option 2, then enter "Se"
    result = run_cli("3\nSe\n")
    output = result.stdout.decode()

    assert result.returncode == 0
    assert "Selenium" in output
    assert "Se" in output
    assert "[Ar] 4s2 3d10 4p4" in output


def test_cli_quit():
    # Option 5 = quit
    result = run_cli("5\n")
    output = result.stdout.decode()

    assert result.returncode == 1
    assert "Invalid choice!" in output
