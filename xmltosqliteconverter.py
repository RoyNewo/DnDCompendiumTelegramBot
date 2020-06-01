"""
import xml.dom.minidom
doc = xml.dom.minidom.parse("Compendiums\\Spells Compendium 1.3.0.xml")
def main():
    spells = doc.getElementsByTagName("spell")
    for spell in spells:        
        name = spell.getElementsByTagName("roll")[0]
        level = spell.getElementsByTagName("level")[0]
        print("nickname:%s, salary:%s" %
              (getNodeText(name), getNodeText(level)))
"""
"""
    name = doc.getElementsByTagName("spell")[0]
    print(name.firstChild.data)
    spells = doc.getElementsByTagName("spell")
    for spell in spells:        
        name = spell.getElementsByTagName("roll")[0]
        level = spell.getElementsByTagName("level")[0]
        print("name: %s, level: %s" % (name.firstChild.data, level.firstChild.data)) 
"""
"""
def getNodeText(node):
    nodelist = node.childNodes
    result = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            result.append(node.data)
    return ''.join(result)
"""
import xml.etree.ElementTree as ET
class my_str:
    def __init__(self, my_string):
        self.str_as_list = [my_string]

    def change_str(self, new_str):
        self.str_as_list = [new_str]

    def __str__(self):
        return self.str_as_list[0]

switcher = {'name': nombreHechizo, 'level': nivelHechizo, 'school': escuelaHechizo, 'ritual': ritaulHechizo, 'time': tiempoHechizo, 'range': rangoHechizo, 'components': componentesHechizo, 'duration': duracionHechizo, 'text': descripcionHechizo, 'roll': dadoHechizo}
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

def nombreHechizo(lista):
    Name.change_str(lista)
def nivelHechizo(lista):
    Level.change_str(int(lista))
def escuelaHechizo(lista):
    school.change_str(lista)
def tiempoHechizo(lista):
    time.change_str(lista)
def ritaulHechizo(lista):
    if lista == "False":
        ritual.change_str(False)
    else:
        ritual.change_str(True)


def main():
    tree = ET.parse('Compendiums\\Spells Compendium 1.3.0.xml')
    root = tree.getroot()
    '''
    print(root[1][0].tag, root[1][0].text)
    print(len(root))
    print(len(root[0]))
    '''
    i = 0
    j = 0
    database = []
    spell = []

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
        for j in range(len(root[i])):
            switcher[root[i][j].tag](root[i][j].text)
            if root[i][j].tag == "name":
                Name = root[i][j].text
            if root[i][j].tag == "text":
                if root[i][j].text != None:
                    text = text + root[i][j].text
                else:
                    text = text + "\\n "
            

        spell =[Name,Level,school,ritual,time,Range,components,duration,classes,text,attackroll,damage1,damage2,damage3,damage4,slotdamage]
        database.append(spell)
        spell.clear()




    cadena = ""
    
    for x in root[0].findall("./text"):
        if x.text != None:
            cadena = cadena + x.text
        else:
            cadena = cadena + "\\n "

#        print(x.text)
    print(cadena)
    
if __name__ == "__main__":
    main()

