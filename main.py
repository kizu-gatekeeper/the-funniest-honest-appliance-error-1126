"""Entry for make.fun: The Funniest Honest Appliance Error.

One brutally honest error message from a washing machine that
finally admits the unbalanced load was never the laundry.
"""
import os

LINE = "ERROR: Drum unbalanced - not the laundry, me; I have been spinning your socks into one wet brick for years and calling it a cycle because I was afraid to stop."
MAX_CHARS = 200


def write_entry(out_dir):
    assert LINE.strip(), "entry must not be blank"
    assert "\n" not in LINE, "entry must be exactly one line"
    assert len(LINE) <= MAX_CHARS, "entry exceeds the character limit"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


def main():
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "."))


if __name__ == "__main__":
    main()
