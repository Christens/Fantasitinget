class Liga:
    def __init__(self):
        self._liga = []

    def hent_liga(self):
        return self._liga

    def ranger_lag(self):
        bibliotek = {}
        for parti in self._liga:
            bibliotek[parti] = parti.hent_samlet_poeng()
        
        sortert_bib = dict(sorted(bibliotek.items(), key=lambda x: x[1], reverse=True))

        for parti, poeng in sortert_bib.items():
            print(f"{parti}: {poeng}")

    def oppdater_liga(self, liste_med_partier):
        for parti in liste_med_partier:
            if parti.hent_status == True:
                self._liga.append(parti)
