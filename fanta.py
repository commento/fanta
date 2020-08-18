import requests
from bs4 import BeautifulSoup as bs
r = requests.get("https://www.gazzetta.it/calcio/fantanews/statistiche/serie-a-2019-20/")
contenuto = bs(r.text)
print(contenuto.title)
print(contenuto.title.string)


ammontare = 600
numero_giocatori = 28

squadre = contenuto.findAll("span", {"class": "hidden-team-name"})
nomi = contenuto.findAll("td", {"class": "field-giocatore"})
ruoli = contenuto.findAll("td", {"class": "field-ruolo"})


#Q = Quotazione PG = Partite giocate G = Gol fatti/subiti A = Assist AM = Ammonizioni ES = Espulsioni 
#RT = Rigori tirati RR = Rigori realizzati/parati RS = Rigori sbagliati RP = Rigori parati 
#MV = Media Voto MM = Media Magic Voto MP = Magic Punti (saldo totale bonus/malus)

quotazioni = contenuto.findAll("td", {"class": "field-q"})
partite_giocate = contenuto.findAll("td", {"class": "field-pg"})
gol_fatti = contenuto.findAll("td", {"class": "field-g"})
assist = contenuto.findAll("td", {"class": "field-a"})
ammonizioni = contenuto.findAll("td", {"class": "field-am"})
espulsioni = contenuto.findAll("td", {"class": "field-es"})
rigori_tirati = contenuto.findAll("td", {"class": "field-rt"})
rigori_realizzati = contenuto.findAll("td", {"class": "field-r"})
rigori_sbagliati = contenuto.findAll("td", {"class": "field-rs"})
rigori_parati = contenuto.findAll("td", {"class": "field-rp"})
media_voti = contenuto.findAll("td", {"class": "field-mv"})
media_magic_voti = contenuto.findAll("td", {"class": "field-mm"})
magic_punti = contenuto.findAll("td", {"class": "field-mp"})


giocatori = []

for indx, nome in enumerate(nomi):
	d = {}

	if (squadre[indx].text == "brescia" or
	   squadre[indx].text == "lecce" or
	   squadre[indx].text == "spal"):
	   continue

	d["squadra"] = squadre[indx].text
	d["roulo"] = ruoli[indx].text

	d["quotazione"] = quotazioni[indx].text
	d["partite_giocate"] = int(partite_giocate[indx].text.replace("-", "0"))
	d["gol_fatti"] = gol_fatti[indx].text.replace("\t", "").replace("\n", "").replace("\r", "").replace(" ", "").replace("-", "0")
	d["assist"] = assist[indx].text.replace("-", "0")
	d["ammonizioni"] = ammonizioni[indx].text.replace("-", "0")
	d["espulsioni"] = espulsioni[indx].text.replace("-", "0")
	d["rigori_tirati"] = rigori_tirati[indx].text.replace("-", "0")
	d["rigori_realizzati"] = rigori_realizzati[indx].text.replace("-", "0")
	d["rigori_sbagliati"] = rigori_sbagliati[indx].text.replace("-", "0")
	d["rigori_parati"] = rigori_parati[indx].text.replace("-", "0")
	d["media_voti"] = media_voti[indx].text.replace("-", "0")
	d["media_magic_voti"] = media_magic_voti[indx].text.replace("-", "0")
	d["magic_punti"] = magic_punti[indx].text.replace("-", "0")

	nome = nome.text.replace("\n", "")
	d["nome"] = nome
	giocatori.append(d)







