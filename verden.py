import json
from parti import Parti
from politiker import Politiker

fil_storting = open("storting.json")
storting = json.load(fil_storting)
politikere_paa_storting = storting["dagensrepresentanter_oversikt"]["dagensrepresentanter_liste"]["dagensrepresentant"]

fil_regjering = open("regjering.json")
regjering = json.load(fil_regjering)

liste_med_politikere = []

for politiker in politikere_paa_storting:
    #if politiker["etternavn"]