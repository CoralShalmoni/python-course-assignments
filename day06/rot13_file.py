import sys
import os
import codecs
import tempfile
import shutil


def rot13(text: str) -> str:
    """Return `text` encoded with ROT13."""
    return codecs.decode(text, "rot_13")


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>", file=sys.stderr)
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.isfile(file_path):
        print(f"Error: '{file_path}' is not a regular file.", file=sys.stderr)
        sys.exit(1)

    #Reading the original file
    with open(file_path, "r", encoding="utf-8") as f:
        original = f.read()

    transformed = rot13(original)

    #Writing to a temporary file first, then moving to place atomically.
    dir_name = os.path.dirname(os.path.abspath(file_path)) or "."
    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        delete=False,
        dir=dir_name,
    ) as tmp:
        tmp.write(transformed)
        temp_name = tmp.name

    shutil.move(temp_name, file_path)


if __name__ == "__main__":
    main()
