import sqlite3

# Crée une connexion à la base de données (si elle n'existe pas, elle sera créée)
conn = sqlite3.connect('elderco.db')

# Assurez-vous de commettre les modifications dans la base de données
conn.commit()

# Ferme la connexion
conn.close()

print('La base de données "elderco.db" a été créée.')
