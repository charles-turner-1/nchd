from nchd import nchd
from pathlib import Path

_TEST_ROOT = Path(__file__).parent
_TEST_DATA_DIR = _TEST_ROOT / "data"


def test_main(capsys):
    """
    Bare bones test to check if the main function runs without errors.
    """
    fname = _TEST_DATA_DIR / Path("access-om2/output000/ocean/ocean.nc")
    invalid_fname = "invalid_fname"

    nchd.main(["invalid_fname"])
    out, err = capsys.readouterr()

    assert out == f"File {invalid_fname} does not exist.\n"
    assert err == ""

    nchd.main([str(fname)])
