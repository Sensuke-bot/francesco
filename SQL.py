import mysql.connector

db = mysql.connector.connect(host='localhost', user = 'root', password = '', database = 'test')

# Creare databe e tabelle

cursor = db.cursor()


cursor.execute('SHOW DATABASES')

for x in cursor:
    print(x)


cursor.execute(" CREATE TABLE clienti (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR (225))")

# se vogliamo creare una tabella

cursor.execute("SHOW TABLES")

for y in cursor:
    print(y)


#creiamo il cursore

sql =  "INSER INTO clienti (nome, cognome) VALUES (%s, %s)" # <== questa e` una query
values = [('Luca, "Rossi'), ('Anna', "Neri")] # l'id si auto aggiorna per i comandi prima.

cursor.executemany(sql, values) # serve per inserire piu` elementi insieme
db.commit() # con cursor e` l'esecutore. Commit e` cio` che fa le cose e le esegue nel senso fisico.


# per vedere l'id di un elemento

print('id riga inserita: ', cursor.lastrowid)

# per selezionare i dati e consultarti

select = "SELECT * FROM clienti WHERE  cognome = 'Rossi' " # al posto del * potremmo mettere i nomi delle categorie come id e nomi
#  WHERE serve per determinare i parametri da trovare
cursor.execute(select)
result = cursor.fetchall() # possiamo fare fatchone e ci fara` vedere una sola riga

for riga in result:
    print(riga)


# order by e limit

obl = "SELECT * FROM clienti ORDER  MY nome" #DESC fa apparire i risultati al contrario alfabetico se invece usassimo
# LIMIT potremmo ottenere un limite di risultati deciso da noi che indicheranno il numero delle righe

cursor.execute(obl)
result = cursor.fetchall()

for r in result:
    print(r)

# eliminare i dati con DELETE

kill = "DELETE FROM clienti WHERE nome = %s AND cognome = %s"
values = [()] #tuple di vari elementi
cursor.execute(kill, values)
db.commit() # sava le modifiche

print('numero di righe cancellate: ', cursor.rowcount) # num di righe toccate dalla query

# UPDATE

up = " UPDATE clienti SET nome = %s WHERE id = %s"
values = [()]
cursor.execute(up, values)
db.commit()
print("righe modifiche: ", cursor.rowcount)

# JOIN
# servono almeno due tabelle.
# prende le carrispondenze tra i dati in piu` tabelle.
# con LEFT JOIN possiamo riferirci unicamente alla tabella di destra. Con FROM ci riferiamo alla tabella di sinistra


join = "SELECT \
       nome, cognome, citta.nome_citta \
       FROM clienti \
       INNER JOIN citta ON clienti.citta = citta.id"

# DROP TABLE

delet = "DROP TABLE nome della tabella"

# nel caso di un controllo aggiuntivo

delet = "DROP TABLE IF EXISTS nome della tabella"

