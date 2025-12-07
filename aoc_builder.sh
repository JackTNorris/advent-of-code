#!/usr/bin/env bash
set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Usage: $0 YEAR_DIR_NAME"
  echo "e.g.  $0 2024"
  exit 1
fi

YEAR="$1"

# Create the year dir if it doesn't exist
mkdir -p "$YEAR"

for day in $(seq 1 25); do
  dir="$YEAR/day$day"
  py="$dir/solution$day.py"
  txt="$dir/input.txt"

  # Make the day dir
  mkdir -p "$dir"

  # Make input.txt if missing
  if [ ! -f "$txt" ]; then
    touch "$txt"
    echo "Created: $txt"
  fi

  # Make solutionN.py if missing
  if [ ! -f "$py" ]; then
    cat > "$py" <<EOF
#!/usr/bin/env python3

from pathlib import Path


def part1(data: str):
    # TODO: implement Day ${day} part 1
    return None


def part2(data: str):
    # TODO: implement Day ${day} part 2
    return None


if __name__ == "__main__":
    data = Path("input.txt").read_text().rstrip("\\n")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
EOF
    chmod +x "$py"
    echo "Created: $py"
  fi
done
