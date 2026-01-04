import json
import string
import random
import os

DB_FILE = "urls.json"
SHORT_CODE_LENGTH = 6


def load_data():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)


def generate_short_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(SHORT_CODE_LENGTH))


def shorten_url(original_url):
    data = load_data()

    while True:
        short_code = generate_short_code()
        if short_code not in data:
            break

    data[short_code] = original_url
    save_data(data)
    return short_code


def get_original_url(short_code):
    data = load_data()
    return data.get(short_code)


def main():
    while True:
        print("\n--- URL Shortener ---")
        print("1. Shorten URL")
        print("2. Get original URL")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            original_url = input("Enter original URL: ")
            short_code = shorten_url(original_url)
            print(f"Short URL code: {short_code}")

        elif choice == "2":
            code = input("Enter short code: ")
            original_url = get_original_url(code)
            if original_url:
                print(f"Original URL: {original_url}")
            else:
                print("❌ Short code not found.")

        elif choice == "3":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()