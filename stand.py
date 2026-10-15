from dataclasses import dataclass
from typing import Optional

@dataclass

class Stand:
    id_s: str

    superficie: int
    padiglione: int
    prezzo: float
    tipo : str = "Standard"
    espositore: Optional[str] = None


    def disponibile(self):
        return self.espositore is None

    def __str__(self):
        if self.espositore:
            stato = "Disponibile"

        else:
            stato = "Occupato"

        return f"{self.id_s}: {self.tipo} | {self.superficie}mq - Padiglione: {self.padiglione} - Prezzo: {self.prezzo:.2f}€ - {stato}"


