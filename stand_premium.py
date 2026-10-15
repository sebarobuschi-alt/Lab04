from stand import Stand


class StandPremium(Stand):

    def __init__(self, id_s, tipo, superficie, padiglione, prezzo, espositore, caratteristica):
        super().__init__(id_s, superficie, padiglione, prezzo, tipo, espositore)
        self.caratteristica = caratteristica

    def __post_init__(self):
        self.tipo = "Premium"
        self.prezzo *= 1.30
    def __str__(self):
        if self.espositore:
            stato = "Disponibile"

        else:
            stato = "Occupato"

        return f"{self.id_s}: {self.tipo} | {self.superficie}mq - Padiglione: {self.padiglione} - Prezzo: {self.prezzo:.2f}€ - {stato}"