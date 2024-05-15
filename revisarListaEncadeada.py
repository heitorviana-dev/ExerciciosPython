class ShoppingListNode:
    def __init__(self, item_name):
        self.item_name = item_name
        self.next_item = None


class ShoppingList:
    def __init__(self):
        self.head = None

    def add_item(self, item_name):
        if not self.head:
            self.head = ShoppingListNode(item_name)
            print(f"O item {item_name} foi adicionado com sucesso.")

        else:
            current_item = self.head
            while current_item:
                if not current_item.next_item:
                    current_item.next_item = ShoppingListNode(item_name)
                    print(f"O item {item_name} foi adicionado com sucesso.")
                    return
                current_item = current_item.next_item

    def delete_item(self, item_name):
        if not self.head:
            print("A lista está vazia.")

        elif self.head.item_name == item_name:
            self.head = self.head.next_item
            print(f"O item {item_name} foi removido com sucesso.")

        else:
            current_item = self.head
            while current_item.next_item:
                if current_item.next_item.item_name == item_name:
                    current_item.next_item = current_item.next_item.next_item
                    print(f"O item {item_name} foi removido com sucesso.")
                current_item = current_item.next_item
            print(f"O item {item_name} não está na lista.")

    def __iter__(self):
        if not self.head:
            print("A lista está vazia.")
            return
        current_item = self.head
        while current_item:
            print(f"{current_item.item_name} ->", end=" ")
            current_item = current_item.next_item
            if not current_item:
                print("None", end=" ")
        print()


lista = ShoppingList()
lista.add_item("Sapato")
lista.add_item("Celular")
lista.add_item("Computador")
lista.__iter__()
lista.delete_item("Sapato")
lista.delete_item("Celular")
lista.__iter__()

