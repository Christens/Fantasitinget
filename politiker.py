class Politiker:
    def __init__(self, etternavn, fornavn, verdi, parti):
        self._etternavn = etternavn
        self._fornavn = fornavn
        self._verdi = verdi
        self._parti = parti
        self._poeng = 0
        self._status = False

    def bytt_status(self):
        if self._status == True:
            self._status = False
        elif self._status == False:
            self._status == True

    def hent_status(self):
        return self._status

    # def blir_valgt(self, politiker):  (Tror ikke denne metoden er nødevendig like vel)
    #     politiker.bytt_status()       (Vi kan bare bruke "bytt_status()")

    def hent_etternavn(self):
        return self._etternavn

    def hent_fornavn(self):
        return self._fornavn

    def hent_parti(self):
        return self._parti

    def hent_verdi(self):
        return self._verdi

    def hent_poeng(self):
        return self._poeng

    def oppdater_poeng(self):
        pass

