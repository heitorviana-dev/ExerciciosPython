from typing import Deque, Any
from collections import deque


class Queue:
    def __init__(self, maxlen=None) -> None:
        self.items: Deque[Any] = deque(maxlen=maxlen)

    def enqueue(self, *items: Any) -> None:
        for item in items:
            self.items.append(item)
        print("Items adicionados com sucesso.")

    def dequeue(self) -> Any:
        if not self.items:
            raise IndexError("A fila está vazia")
        print(f"O primeito elemento da fila foi removido com sucesso.")
        return self.items.popleft()

    def __repr__(self) -> str:
        return str(self.items)

    def __bool__(self) -> bool:
        return bool(self.items)

    def __len__(self) -> int:
        return len(self.items)

    def __iter__(self) -> None:
        if not self.items:
            print("A fila está vazia.")
        else:
            for item in self.items:
                print(f"{item} ->", end=" ")
            print("None")

    def search_by_index(self, index: int) -> Any:
        for i in range(len(self.items)):
            if i == index:
                print(f"O item {self.items[i]} está na posição {i}.")


