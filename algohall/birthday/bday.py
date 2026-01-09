class Solution:

    def __init__(self) -> None:
        self.__birthdays: list[int] = []

    def set_birthdays(self, input_birthdays: list) -> None:
        self.__birthdays = input_birthdays

    def get_birthdays(self) -> list[int]:
        return self.__birthdays

def check_birthdays(birthdays: list[int]) -> list[int]:
    seen = set()

    for birthday in birthdays:
        if birthday in seen:
            return f"We have seen this birthday {birthday}"
        
        seen.add(birthday)

    return "Every birthday is unique"

def main():

    input_birthdays: list[int] = [7, 10, 11, 4, 5, 3, 2, 8, 21, 15, 11, 9, 19]

    result = check_birthdays(input_birthdays)

    print(f"{result}")

if __name__ == "__main__":
    main()
