from typing import List, Any


class Stack:
    def __init__(self) -> None:
        self.items: List[Any] = list()

    def push(self, *items: Any) -> None:
        for item2 in items:
            self.items.append(item2)

    def pop(self) -> Any:
        if not self.items:
            raise IndexError("A pilha está vazia.")
        print("O último elemento foi removido da pilha.")
        return self.items.pop()

    def __iter__(self) -> Any:
        for item1 in self.items[::-1]:
            print(f"|{item1}|")


if __name__ == "__main__":
    pilha = Stack()
    operador = input("Quer adicionar(s) ou remover(n)? ")
    while operador == "s" or operador == "n":
        if operador == "s":
            item = input("Qual valor a ser adicionado? ")
            pilha.push(item)
            print("Valor adicionado com sucesso na pilha.")
            pilha.__iter__()
            operador = input("Quer adicionar(s) ou remover(n)? ")

        if operador == "n":
            try:
                item = pilha.pop()
                print(f"O valor removido foi {item}.")
                pilha.__iter__()
                operador = input("Quer adicionar(s) ou remover(n)? ")

            except IndexError:
                print("Não é possível remover elementos, a pilha está vazia.")
                operador = input("Quer adicionar(s) ou remover(n)? ")
