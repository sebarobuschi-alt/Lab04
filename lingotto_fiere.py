from csv import reader
from stand import Stand
from stand_prese_extra import StandPreseExtra
from espositori import Espositore


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
            with open(file_path,'r') as in_file:
                csv_reader = reader(in_file)
                for row in csv_reader:
                    id = row[0].strip()
                    if id[0] == 'S':

                        if row[4] is '':
                            s = Stand(id,
                                      row[1].strip,
                                      int(row[2].strip),
                                      int(row[3].strip),
                                      )
                        else:
                            s = StandPreseExtra(id,
                                      row[1].strip,
                                      int(row[2].strip),
                                      int(row[3].strip),
                                      int(row[4].strip)
                                      )

                        self.stand.append(s)
                    elif id[0] == 'E':
                        e = Espositore(id,
                                       row[1].strip,
                                       row[2].strip,
                                       row[3].strip,
                                       )
                        self.espositori.append(e)
        except FileNotFoundError:
            print("Errore! File inserito non valido")


    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        trovato_e = False
        trovato_s = False
        for e in self.espositori:
            if codice_espositore == e.id_e:
                trovato_e = True
                break
        if not trovato_e:
            raise Exception(f"Errore! Codice({codice_espositore}) non trovato ")


        for s in self.stand:
            if codice_stand == s.id_s:
                trovato_s = True
                break
        if not trovato_s:
            raise Exception(f"Errore! Codice({codice_stand}) non trovato ")








    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
