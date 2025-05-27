import sys

def load_colors(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def print_menu(colors):
    print("Please select one or more colors by number or name (e.g., 1,3 or blue,yellow):")
    for i, color in enumerate(colors, 1):
        print(f"{i}. {color}")

def resolve_selections(selection, colors):
    result = []
    lower_colors = [c.lower() for c in colors]
    entries = [s.strip() for s in selection.split(',') if s.strip()]
    
    for entry in entries:
        if entry.isdigit():
            idx = int(entry) - 1
            if 0 <= idx < len(colors):
                result.append(colors[idx])
            else:
                print(f"Ignored invalid number: {entry}")
        else:
            if entry.lower() in lower_colors:
                result.append(colors[lower_colors.index(entry.lower())])
            else:
                print(f"Ignored unknown color: {entry}")
    return result

def get_user_input(colors):
    while True:
        selection = input("Enter your selection(s): ").strip()
        selected_colors = resolve_selections(selection, colors)
        if selected_colors:
            return selected_colors
        print("No valid selections. Try again.")

def parse_command_line_args(colors):
    if len(sys.argv) < 2:
        return None

    arg = sys.argv[1]
    selected_colors = resolve_selections(arg, colors)
    if selected_colors:
        return selected_colors
    print("No valid selections from command line. Falling back to prompt.")
    return None

def main():
    colors = load_colors('colors.txt')
    selections = parse_command_line_args(colors)

    if not selections:
        print_menu(colors)
        selections = get_user_input(colors)

    print("You selected:")
    for color in selections:
        print(f"- {color}")

if __name__ == "__main__":
    main()
