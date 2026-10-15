from dataclasses import dataclass

@dataclass

class Espositore:
    id_e : str
    nome_e : str
    cognome_e : str

    def __str__(self):
        return f"{self.id_e} | Nome: {self.nome_e} | Cognome: {self.cognome_e}"


