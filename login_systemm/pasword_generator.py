import string
import random

def generate_password(length: int, characters: list, required: list = None) -> str:
    """
    Generate a password of given length.
    required is a list of characters that MUST appear at least once.
    """
    if length <= 0:
        raise ValueError("Password length must be greater than 0.")
    if not characters:
        raise ValueError("Character list cannot be empty.")

    if required:
        if length < len(required):
            raise ValueError(f"Password length must be at least {len(required)} "
                             f"to include all required characters.")
        guaranteed = [random.choice(required)]
    else:
        guaranteed = []

    remaining_count = length - len(guaranteed)
    rest = [random.choice(characters) for _ in range(remaining_count)]

    password_list = guaranteed + rest
    random.shuffle(password_list)

    return "".join(password_list)


def main():
    alphabet = list(string.ascii_letters)
    numbers = [str(n) for n in range(10)]

    symbols_input = input('Enter symbols (space separated): ').strip()
    symbols = list(set(symbols_input.split())) if symbols_input else []

    if not symbols:
        print("No symbols added. Using letters and numbers only.")

    all_characters = alphabet + numbers + symbols

    try:
        length = int(input('Enter password length: '))
    except ValueError:
        print("Please enter a valid number.")
        return

    password = generate_password(length, all_characters, required=symbols or None)
    print(f"Your password is: {password}")


if __name__ == "__main__":
    main()