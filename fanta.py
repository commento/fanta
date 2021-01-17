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
	d["ruolo"] = ruoli[indx].text

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


giocatori_per_rigori_tirati = sorted(giocatori, key = lambda i: int(i['rigori_realizzati']),reverse=True)


print()
print("GIOCATORI SOTTO CON QUOTAZIONE SOTTO I 21 CON RIGORI REALIZZATI")
for indx, g in enumerate(giocatori_per_rigori_tirati):
 	if int(g["quotazione"]) < 21 and int(g['rigori_realizzati']) != 0:
 		print(indx, "nome:", g["nome"],'rigori_realizzati:',  g['rigori_realizzati'],"squadra:", g["squadra"])


giocatori_con_presenza = list(filter(lambda x: x["partite_giocate"] != 0, giocatori))


giocatori_per_gol_fatti_su_partite = sorted(giocatori_con_presenza, key = lambda i: int(i['gol_fatti'])/i["partite_giocate"],reverse=True)


print()
print("GIOCATORI SOTTO CON QUOTAZIONE SOTTO I 21 CON COEFFICIENTE GOL_FATTI/PARTITE_GIOCATE MAGGIORE DI 0")
for indx, g in enumerate(giocatori_per_gol_fatti_su_partite):
	if int(g["quotazione"]) < 21 and int(g['gol_fatti'])/g["partite_giocate"] != 0:
		print(indx, "nome:", g["nome"], "gol_fatti:", g['gol_fatti'], "partite_giocate:", g["partite_giocate"], "squadra:", g["squadra"], "gol_fatti/partite_giocate:", int(g['gol_fatti'])/g["partite_giocate"])


giocatori_per_media_su_partite = sorted(giocatori_con_presenza, key = lambda i: float(i["media_voti"]),reverse=True)

print()
print("GIOCATORI SOTTO CON QUOTAZIONE SOTTO I 21 CON MEDIA VOTO SUPERIORE AL 6")
for indx, g in enumerate(giocatori_per_media_su_partite):
	if int(g["quotazione"]) < 21 and float(g["media_voti"]) > 6:
		print(indx, "nome:", g["nome"], "quotazione:", g["quotazione"], "media_voti:", g['media_voti'], "partite_giocate:", g["partite_giocate"], "squadra:", g["squadra"])



giocatori_per_magic_su_partite = sorted(giocatori_con_presenza, key = lambda i: float(i["magic_punti"]),reverse=True)

print()
print("GIOCATORI SOTTO CON QUOTAZIONE SOTTO I 21 CON VOTO MAGIC POSITIVO")
for indx, g in enumerate(giocatori_per_magic_su_partite):
	if int(g["quotazione"]) < 21 and float(g["magic_punti"]) > 0:
		print(indx, "nome:", g["nome"], "quotazione:", g["quotazione"], "ruolo", g["ruolo"], "magic_punti:", g['magic_punti'], "partite_giocate:", g["partite_giocate"], "squadra:", g["squadra"])







