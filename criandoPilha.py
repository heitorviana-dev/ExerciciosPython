from typing import List, Any


class StackList:
    def __init__(self) -> None:
        self.__items: List[Any] = []

    def push(self, item: Any) -> None:
        self.__items.append(item)

    def pop(self) -> Any:
        return self.__items.pop()

    def __repr__(self) -> str:
        return str(self.__items)

    def __iter__(self) -> Any:
        for valor in self.__items[::-1]:
            print(valor)


if __name__ == "__main__":
    pilha = StackList()
    operador = input("Quer adicionar(s) ou remover(n)? ")
    while operador == "s" or operador == "n":
        if operador == "s":
            item = input("Qual valor a ser adicionado? ")
            pilha.push(item)
            print("Valor adicionado com sucesso na pilha.")
            pilha.__iter__()
            print(f"Veja como a pilha está: {pilha.__repr__()}")
            operador = input("Quer adicionar(s) ou remover(n)? ")

        if operador == "n":
            try:
                item = pilha.pop()
                print(f"O valor removido foi {item}.")
                pilha.__iter__()
                print(f"Veja como a pilha está: {pilha.__repr__()}")
                operador = input("Quer adicionar(s) ou remover(n)? ")

            except IndexError:
                print("Não é possível remover elementos, a pilha está vazia.")
                operador = input("Quer adicionar(s) ou remover(n)? ")



