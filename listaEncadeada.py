class ShoppingListNode:
    def __init__(self, item_name):
        self.item_name = item_name
        self.next_item = None


class ShoppingList:
    def __init__(self):
        self.head = None

    def add_item(self, item_name):
        new_item = ShoppingListNode(item_name)
        if not self.head:  # Verifica se a lista está vazia
            self.head = new_item
        else:
            current_item = self.head
            while current_item.next_item:  # Procura o último nó, percorrendo a lista
                current_item = current_item.next_item
            current_item.next_item = new_item

    def delete_item(self, item_name):
        if not self.head:  # Verifico se a lista está vazia
            print("A lista está vazia.")
            return

        if self.head.item_name == item_name:  # Verifico se o nó que eu quero remover é o nó head
            self.head = self.head.next_item
            return

        current_item = self.head
        while current_item.next_item:  # Enquanto o valor do next_item do próximo nó não for None, executa o bloco
            if current_item.next_item.item_name == item_name:
                current_item.next_item = current_item.next_item.next_item
                print(f"O item {item_name} foi removido.")
                return
            current_item = current_item.next_item

        print("O item não está na lista.")

    def show_items(self):
        if not self.head:
            print("A lista está vazia.")

        else:
            current_item = self.head
            while current_item:
                print(f"{current_item.item_name}", end=" ")
                print()
                current_item = current_item.next_item


if __name__ == "__main__":
    shoppingList = ShoppingList()
    shoppingList.add_item("Sapato")
    shoppingList.add_item("Celular")
    shoppingList.show_items()
    shoppingList.delete_item("Aparelho")
    shoppingList.show_items()
    shoppingList.delete_item("Celular")
    shoppingList.show_items()






