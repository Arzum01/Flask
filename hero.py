import flask
from flask import Flask
import sqlite3

app = Flask(__name__)
connection = sqlite3.connect("heroes.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS heroes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    health INTEGER,
    power INTEGER,
    class TEXT
)
""")

heroes = [
    ("Arthur", 100, 80, "Warrior"),
    ("Merlin", 80, 95, "Mage"),
    ("Robin", 90, 75, "Archer"),
    ("Thor", 120, 100, "Warrior"),
    ("Gandalf", 85, 98, "Mage")
]

quesry = cursor.executemany("""INSERT INTO heroes(name,health,power,class) VALUES (?,?,?,?)""", heroes)

connection.commit()
connection.close()

@app.route("/")
def welcome():
    return f'Welcome to RPG Hero System'

@app.route("/heroes")
def heroes_show():
    connection = sqlite3.connect("heroes.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM heroes")
    heroes = cursor.fetchall()
    result = ""
    for hero in heroes:
        result += f"""
        name: {hero[1]},
        health: {hero[2]},
        power: {hero[3]},
        class: {hero[4]}"""
    connection.close()
    return result

@app.route("/hero/<int:id>")
def hero_find(id):
    connection = sqlite3.connect("heroes.db")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM heroes WHERE id=?', (id,))
    hero = cursor.fetchone()
    connection.close()
    if hero:
        return f"""Hero found: {hero[1]}"""
    return "Hero not found"
    
@app.route("/mages")
def mages():
    connection = sqlite3.connect("heroes.db")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM heroes WHERE class="Mage"')
    mages = cursor.fetchall()
    result = ""
    for mage in mages:
        result += f"""{mage[1]}-{mage[2]} <br> """
    connection.close()
    if result == "":
        return "No Mages Found"
    else:
        return result
    
@app.route("/strong")
def powerful():
    connection = sqlite3.connect("heroes.db")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM heroes WHERE power>80')
    power = cursor.fetchall()
    connection.close()
    return str(power)

@app.route("/battle/<int:id1>/<int:id2>")
def battle_result(id1, id2):
    connection = sqlite3.connect("heroes.db")
    cursor = connection.cursor()
    cursor.execute("SELECT name,power FROM heroes WHERE id=?", (id1,))
    hero1 = cursor.fetchone()

    cursor.execute("SELECT name, power FROM heroes WHERE id=?", (id2,))
    hero2 = cursor.fetchone()
    connection.close()

    if not hero1 or not hero2:
        return "Heroes are not found"
    
    hero1_name, hero1_power = hero1[0], hero1[1]
    hero2_name, hero2_power = hero2[0], hero2[1]

    if hero1_power > hero2_power:
        return f"""{hero1_name} wins"""
    elif hero1_power < hero2_power:
        return f"""{hero2_name} wins"""
    else:
        return f'TIE!'
    
app.run(debug=True)