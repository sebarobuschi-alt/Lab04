from stand import Stand


class StandPreseExtra(Stand):

    def __init__(self, id_s, tipo, superficie, padiglione, prezzo, espositore, caratteristica):
        super().__init__(id_s, superficie, padiglione, prezzo, tipo, espositore)
        self.caratteristica = caratteristica
    def __post_init__(self):
        self.tipo = "Prese Extra"
        self.prezzo *= (1 + 0.07 *int(self.caratteristica))

    def __str__(self):
        if not self.espositore:
            stato = "Disponibile"

        else:
            stato = "Occupato"

        return f"{self.id_s}: {self.tipo} | {self.superficie}mq - Padiglione: {self.padiglione} - Prezzo: {self.prezzo:.2f}€ - Prese aggiuntive: {self.caratteristica} - {stato}"