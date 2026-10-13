from stand import Stand


class StandPreseExtra(Stand):
    def __init__(self,id_s,superficie,padiglione,prezzo,prese_extra):
        super().__init__(id_s,superficie,padiglione,prezzo)
        self.prese_extra = prese_extra
    def check_prese(self,prese_extra,prezzo):
        if prese_extra is str:
            prezzo *= (1 + 0.07 * prese_extra)
        elif prese_extra is int:
            prezzo *= 1.30


    def __str__(self):
        return f'{super().__str__()} - {self.prese_extra}'