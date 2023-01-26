class Parti:
    def __init__(self, samlet_verdi, samlet_poeng, stemmer):
        self._parti = []
        self._samlet_verdi = samlet_verdi
        self._samlet_poeng = samlet_poeng
        self._stemmer = stemmer
    
    def hent_politiker(self, etternavn):
        # ta inn etternavn og returnere politkeren
        for politiker in self._parti:
            if etternavn == etternavn:
                pass
            # return poltiker 
            
    def hent_samlet_verdi(self):
        return self._samlet_verdi

    def hent_samlet_poeng(self):
        return self._samlet_poeng

    def hent_stemmer(self):
        return self._stemmer

    def oppdater_stemmer(self):
        pass
    # self._stemmer - oppdater_samlet_verdi 

    def oppdatert_samlet_verdi(self):
        for politiker in self._parti:
            self._samlet_verdi += politiker.hent_verdi()

    def oppdater_parti(self):
        pass

    def fjern_politiker(self):
        pass