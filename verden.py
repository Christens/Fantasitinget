import json
from parti import Parti
from politiker import Politiker

fil_storting = open("storting.json")
storting = json.load(fil_storting)
storting = storting["dagensrepresentanter_oversikt"]["dagensrepresentanter_liste"]["dagensrepresentant"]

fil_regjering = open("regjering.json")
regjering = json.load(fil_regjering)
regjering = regjering["regjeringsmedlemmer_oversikt"]["regjeringsmedlemmer_liste"]["regjeringsmedlem"]

liste_med_politikere = []
fornavn = []
etternavn = []

for politiker in storting:
    if politiker["fornavn"] not in fornavn:
        liste_med_politikere.append(Politiker(politiker["etternavn"],politiker["fornavn"],politiker["verdi"],politiker["parti"]["navn"]))
        fornavn.append(politiker["fornavn"])
        etternavn.append(politiker["etternavn"])

for politiker in regjering:
    if politiker["fornavn"] not in fornavn:
        liste_med_politikere.append(Politiker(politiker["etternavn"],politiker["fornavn"],politiker["verdi"],politiker["parti"]["navn"]))
        fornavn.append(politiker["fornavn"])
        etternavn.append(politiker["etternavn"])
