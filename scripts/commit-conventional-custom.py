import sys
import re

ALLOWED_PREFIXES = ["feat", "fix", "build", "chore", "ci", "docs", "style", "refactor", "perf", "test"]
TERMINAL_RED = '\033[0;31m'
TERMINAL_BLUE = '\033[0;36m'
TERMINAL_YELLOW = '\033[0;33m'
TERMINAL_NO_COLOR = '\033[0m'

def parse_git_branch():
    try:
        branches = subprocess.check_output(['git', 'branch']).decode('utf-8')
        branch = next((line for line in branches.split('\n') if line.startswith('*')), None)
        return branch.strip()[1:]
    except subprocess.CalledProcessError:
        return None

def parse_git_branch_for_issue():
    branch = parse_git_branch()
    match = re.search(r'[A-Z]+-\d+', branch)
    return match.group() if match else None

def main():
    message_file = sys.argv[1]
    with open(message_file, 'r') as file:
        message = file.read().strip()

    parsed_message = message.split()
    first_word = parsed_message[0]
    prefix = first_word.rstrip(':')

    if prefix not in ALLOWED_PREFIXES:
        print(f"{TERMINAL_RED} ======ERROR====== {TERMINAL_NO_COLOR}")
        print("Commit message format should be:")
        print(f"{TERMINAL_BLUE}   <prefix>: <message> (<ticket>) {TERMINAL_NO_COLOR}")
        print(f"Allowed prefixes: {TERMINAL_YELLOW} {', '.join(ALLOWED_PREFIXES)}  {TERMINAL_NO_COLOR}")
        sys.exit(1)

    parsed_message_length = len(parsed_message)
    ticket = parsed_message[parsed_message_length - 1]

    if not re.match(r'\([A-Z]{1,3}-\d+\).*', ticket):
        ticket_from_branch = parse_git_branch_for_issue()

        if not ticket_from_branch:
            print(f"{TERMINAL_RED} ======ERROR====== {TERMINAL_NO_COLOR}")
            print("TICKET should be present (ticket has format like AZ19-1289:")
            print(" - as part of the Branch name")
            print(" - between parenthesis \"( )\" at the end of the commit message as:")
            print(f"    {TERMINAL_BLUE} <prefix>: <message> (<ticket>) {TERMINAL_NO_COLOR}")
            sys.exit(1)

        print(f"New commit message: {message} ({ticket_from_branch})")
        with open(message_file, 'w') as file:
            file.write(f"{message} ({ticket_from_branch})")

if __name__ == "__main__":
    main()
