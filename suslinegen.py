# Licensed under the GNU GPL v3. See https://www.gnu.org/licenses/gpl-3.0.txt for details.

import random
import requests
import sys

# URL of my raw sus_lines.txt on GitHub
url = "https://raw.githubusercontent.com/Ryan-the-python-coder/suslinemakermemory/refs/heads/main/sus_lines.txt"

# Warning
print("⚠️ WARNING: SUGGESTIVE CONTENT AHEAD ⚠️")
print("This generator will show playful, suggestive, innuendo-filled lines.")
print("If you're uncomfortable with these types of things or under 13, close this window now.\n")
input("Press Enter to continue or close the window to exit...")

# Fetch the sus_lines.txt from GitHub
response = requests.get(url)
if response.status_code == 200:
    sus_lines = [line.strip() for line in response.text.splitlines() if line.strip()]
else:
    raise RuntimeError("⚠️ Failed to fetch sus_lines.txt from GitHub. Exiting script.")

if not sus_lines:
    raise RuntimeError("⚠️ No sus lines found in the fetched file. Exiting script.")

# Shuffle the lines
remaining_lines = sus_lines.copy()
random.shuffle(remaining_lines)

keep_going = True
while keep_going:
    # Ask how many lines to show
    while True:
        try:
            count = int(input("\nHow many sus lines would you like to see? "))
            break
        except ValueError:
            print("Please enter a valid number.")

    # Pick lines from remaining
    if count > len(remaining_lines):
        print(f"Only {len(remaining_lines)} lines remaining. Showing all of them.")
        count = len(remaining_lines)

    chosen_lines = remaining_lines[:count]
    remaining_lines = remaining_lines[count:]

    print("\n💬 Here are your sus lines:")
    for line in chosen_lines:
        print(f"- {line}")

    # Refill and reshuffle if exhausted
    if not remaining_lines:
        remaining_lines = sus_lines.copy()
        random.shuffle(remaining_lines)
        print("\n🔄 All lines used! Shuffling the list again for more fun.")

    # Ask if the user wants more — force y or n
    while True:
        more = input("\nDo you want more sus lines? (y/n) ").strip().lower()
        if more in ['y', 'n']:
            break
        else:
            print("Please type 'y' for yes or 'n' for no.")

    if more == 'n':
        keep_going = False

# Contributing instructions
print("\nWant to add your own sus lines?")
print("We welcome contributions from the community! To suggest new sus lines:\n")
print("1. Go to https://github.com/Ryan-the-python-coder/suslinemakermemory")
print("2. Fork the repository.")
print("3. Add your submission(s) to sus_lines.txt (one line per entry).")
print("4. Submit a Pull Request to the main repository.")
print("All submissions will be reviewed before being approved and moved to the main branch.")
