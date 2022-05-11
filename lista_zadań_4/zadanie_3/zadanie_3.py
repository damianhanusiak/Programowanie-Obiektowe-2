from abc import ABC, abstractmethod


class Temperature(ABC):
    def __init__(self, temperature):
        super().__init__()
        self.temperature = temperature

    def __str__(self):
        return f"{self.temperature} w skali Celsjusza"
