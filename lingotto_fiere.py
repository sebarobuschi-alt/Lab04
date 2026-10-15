from csv import reader
from stand import Stand
from stand_premium import StandPremium
from stand_prese_extra import StandPreseExtra
from espositori import Espositore
from operator import attrgetter


class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome
        self.stand = []
        self.espositori = []


    """Aggiungere setter e getter se necessari"""
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,nome):
        self.__nome = nome
    def aggiorna_nome(self,nuovo_nome):
        self.__nome = nuovo_nome
        return self
    def __str__(self):
        return f"Nome centro fieristico: {self.__nome}"

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        try:

            with (open(file_path,'r') as in_file):
                csv_reader = reader(in_file)
                for row in csv_reader:
                    id = row[0].strip()
                    if id[0] == 'S':
                        superficie_s=int(row[1].strip())
                        padiglione_s=int(row[2].strip())
                        prezzo_s=float(row[3].strip())
                        extra = row[4].strip() if len(row) > 4 else ""

                        if extra == "":
                            s = Stand(id_s=id,
                                      tipo="Standard",
                                      superficie = superficie_s,
                                      padiglione = padiglione_s,
                                      prezzo = prezzo_s,
                                      espositore = None)
                        elif extra.isdigit():
                            s = StandPreseExtra(
                                id_s=id,
                                tipo="Prese_extra",
                                superficie=superficie_s,
                                padiglione=padiglione_s,
                                prezzo=prezzo_s,
                                caratteristica=int(extra),
                                espositore=None
                                                    )
                        else:
                               s = StandPremium(id_s=id,
                                tipo = "Premium",
                                superficie=superficie_s,
                                padiglione=padiglione_s,
                                prezzo=prezzo_s,
                                caratteristica = extra,
                                espositore = None
                                                )



                        self.stand.append(s)
                    elif id[0] == 'E':
                        e = Espositore( id_e = id,
                                       nome_e = row[1].strip(),
                                       cognome_e = row[2].strip()
                                       )
                        self.espositori.append(e)
        except FileNotFoundError:
            print("Errore! File inserito non valido")


    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        trovato_e = False
        trovato_s = False
        for e in self.espositori:
            if str(codice_espositore).strip().upper() == str(e.id_e).strip().upper():
                trovato_e = True
                break
        if not trovato_e:
            raise Exception(f"Errore! Codice({codice_espositore}) non trovato ")

        s_da_assegnare = None

        for s in self.stand:
            if str(codice_stand).strip().upper() == str(s.id_s).strip().upper():
                s_da_assegnare = s
                trovato_s = True
                break

        if not trovato_s:
            raise Exception(f"Errore! Codice({codice_stand}) non trovato ")
        for stand in self.stand:
            if codice_espositore == stand.espositore:
                raise ValueError(f"L'espositore {codice_espositore} è gia assegnato a uno stand")


        s_da_assegnare.espositore = codice_espositore
        return s_da_assegnare



    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        self.espositori.sort(key=attrgetter("cognome_e", "nome_e"))


        for espositore in self.espositori:
            stand_assegnato = None
            for stand in self.stand:
                if espositore.id_e == stand.espositore:
                    stand_assegnato = stand
                    break
            if stand_assegnato:
                print(f"{espositore} - {stand_assegnato.id_s}")
            else:
                print(f"{espositore}")

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        self.stand.sort(key=attrgetter("id_s"))
        return self.stand