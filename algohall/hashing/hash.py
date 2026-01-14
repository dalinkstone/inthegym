class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class Table:
    def __init__(self, size=7):
        self.size = size
        self.elements = [None] * self.size

    def hash(self, key: int) -> int:
        return ((8 * key) + 2) % 7

    def insert(self, key, value):
        index = self.hash(int(key))

        if self.elements[index] is None:
            self.elements[index] = Node(key, value)

        current = self.elements[index]
        prev = None

        while current:
            if current.key == key:
                current.value = value
                return

            prev = current
            current = current.next

        new_node = Node(key, value)
        prev.next = new_node

    def print_table(self) -> None:
        printable = []
        for i in range(self.size):
            current = self.elements[i]

            table = []

            while current:
                table.append(str(current.key))
                current = current.next

            if not table:
                printable.append("Null")
            else:
                printable.append(table)

        print(printable)


def main():
    table = Table()
    table.insert("3", 3)
    table.insert("18", 18)
    table.insert("42", 42)
    table.insert("31", 31)
    table.insert("40", 40)
    table.insert("56", 56)
    table.insert("71", 71)

    table.print_table()


if __name__ == "__main__":
    main()
