
import xml.etree.ElementTree as ET
import sqlite3 as lite
import glob
import sys
# Creamos unas clase para poder manejar variables de una manera global en las funciones
class my_str:
    def __init__(self, my_string):
        self.str_as_list = [my_string]

    def change_str(self, new_str):
        self.str_as_list = [new_str]

    def string(self):
        return str(self.str_as_list[0])
    def my_int(self):
        return int(self.str_as_list[0])
    def my_bool(self):
        return bool(self.str_as_list[0])
    def __str__(self):
        return self.str_as_list[0]

# Funciones creadas para asignar valores y tambien para poder llamar a las funciones en una manera al estilo switch case
def nombreHechizo(lista, contador):
    Name.change_str(lista)
def nivelHechizo(lista, contador):
    Level.change_str(int(lista))
def escuelaHechizo(lista, contador):
    school.change_str(lista)
def tiempoHechizo(lista, contador):
    time.change_str(lista)
def ritaulHechizo(lista, contador):
    if lista == "False":
        ritual.change_str(False)
    else:
        ritual.change_str(True)
def rangoHechizo(lista, contador):
    Range.change_str(lista)
def componentesHechizo(lista, contador):
    components.change_str(lista)
def duracionHechizo(lista, contador):
    duration.change_str(lista)
def claseHechizo(lista,contador):
    classes.change_str(lista)
def descripcionHechizo(lista, contador):
    if lista != None:
        text.change_str(str(text) + lista)
    else:
        text.change_str(str(text) + "\\n ")
        
def dadoHechizo(lista, contador):
    #Pasamos la cadena a una variable de cadena, luego partimos el string con split se crea una lista, y con un bucle hacemos un print
    texto = str(text)
    dado = str(roll)
    for linea in range(len(str(text).split('\\n '))):
        print(texto.split('\\n ')[linea])
    for linea2 in range(len(str(roll).split('\\n '))):
        print(dado.split('\\n ')[linea2])

    print("roll ", contador.string() ,": ", str(lista).split('\\n')[0])
    opcion = int(input("1 - attackroll, 2 - damage1, 3 - damage2, 4 - damage3, 5 - damage4, 6 - slotdamage: "))
    if opcion == 1:
        attackroll.change_str(lista)
    if opcion == 2:
        damage1.change_str(lista)
    if opcion == 3:
        damage2.change_str(lista)
    if opcion == 4:
        damage3.change_str(lista)
    if opcion == 5:
        damage4.change_str(lista)
    if opcion == 6:
        slotdamage.change_str(lista)
    l.change_str(l.my_int() + 1)

# Vaiables globales, y diccionario para llamar a las funciones

switcher = {'name': nombreHechizo, 'level': nivelHechizo, 'school': escuelaHechizo, 'ritual': ritaulHechizo, 'time': tiempoHechizo, 'range': rangoHechizo, 'components': componentesHechizo, 'duration': duracionHechizo, 'classes': claseHechizo, 'text': descripcionHechizo, 'roll': dadoHechizo}
Name = my_str("")
Level = my_str(0)
school = my_str("")
ritual = my_str(False)
time = my_str("")
Range = my_str("")
components = my_str("")
duration = my_str("")
classes = my_str("")
text = my_str("")
attackroll = my_str("")
damage1 = my_str("")
damage2 = my_str("")
damage3 = my_str("")
damage4 = my_str("")
slotdamage = my_str("")
roll = my_str("")
l = my_str(0)

def main():
    database = []
    spell = []
    i = 0
    j = 0
    k = 0
    tree = None
    root = None
    # para coger varios archivos utilizamos la libreria glob y recorremos los ficheros
    filenames = glob.glob("DnDCompendiumTelegramBot\\Spells\\*.xml")
    for filename in filenames:
        with open(filename, 'r', encoding="utf-8") as content:

            tree = ET.parse(content)
            root = tree.getroot()
            i = 0
            j = 0
            k = 0            
            for i in range(len(root)):
                Name.change_str("")
                Level.change_str(0)
                school.change_str("")
                ritual.change_str(False)
                time.change_str("")
                Range.change_str("")
                components.change_str("")
                duration.change_str("")
                classes.change_str("")
                text.change_str("")
                attackroll.change_str("")
                damage1.change_str("")
                damage2.change_str("")
                damage3.change_str("")
                damage4.change_str("")
                slotdamage.change_str("")
                roll.change_str("")
                l.change_str(0)
                k = 0        
                for x in root[i].findall("./roll"):            
                    roll.change_str( str(roll) + "roll " + str(k) + ": " + x.text + " \\n ")                    
                    k += 1

                for j in range(len(root[i])):
                    #print(root[i][j].tag)
                    switcher[root[i][j].tag](root[i][j].text, l)
                    j += 1
                    

                spell = [Name.string(),Level.my_int(),school.string(),ritual.my_bool(),time.string(),Range.string(),components.string(),duration.string(),classes.string(),text.string(),attackroll.string(),damage1.string(),damage2.string(),damage3.string(),damage4.string(),slotdamage.string()]
                database.append(list(spell))
                
                '''
                for ls in database:
                    print(ls)
                print(len(database))
                spell.clear()
                i += 1
                '''
    con = lite.connect('DnDCompendiumTelegramBot\\DnD 5e.db')
    with con:
        cur = con.cursor()
        cur.executemany("INSERT INTO Spells VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",database)



    
if __name__ == "__main__":
    main()

