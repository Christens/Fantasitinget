class Parti:
    def __init__(self, samlet_verdi, samlet_poeng, stemmer):
        self._parti = [] #liste med politkerne som er valg ttil partiet
        self._samlet_verdi = samlet_verdi
        self._samlet_poeng = samlet_poeng
        self._stemmer = stemmer
    
    def hent_politiker(self, etternavn):
        # ta inn etternavn og returnere politkeren
        for politiker in self._parti:
            if politiker.hent_etternavn() == etternavn:
                return self._parti.index(politiker)

    def oppdater_samlet_poeng(self):
        for politiker in self._parti:
            self._samlet_poeng += politiker.hent_poneg()

    def hent_samlet_poeng(self):
        return self._samlet_poeng

    def hent_stemmer(self):
        return self._stemmer

    def oppdater_samlet_verdi(self):
        for politiker in self._parti:
            self._samlet_verdi += politiker.hent_verdi()

    def hent_samlet_verdi(self):
        self.oppdater_samlet_verdi()
        return self._samlet_verdi

    def oppdater_stemmer(self):
        self._stemmer -= self.hent_samlet_verdi()

    def oppdater_parti(self, liste_med_politikerne):
        for politiker in liste_med_politikerne:
            if politiker.hent_status() == True:
                self._parti.append(politiker)

    def fjern_politiker(self, etternavn):
        n = self.hent_politiker(etternavn)
        self._parti[n].bytt_status()
        self.oppdater_samlet_poeng()
        self.oppdater_samlet_verdi()
        self.oppdater_stemmer()