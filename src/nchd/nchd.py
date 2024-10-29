"""
A command line utility to provide a better version of `ncdump -h` for netCDF files.
"""

from rich import print
from typing import Optional, Sequence
import argparse
import os
from netCDF4 import Dataset


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", help="The netCDF file to display")
    args = parser.parse_args(argv)
    # print(args)

    file = args.file
    if not os.path.exists(file) or not os.path.isfile(file):
        print(f"File {file} does not exist.")
        return 1
    else:
        ds = Dataset(file)
        print(ds)

    return 0


if __name__ == "__main__":
    exit(main())
