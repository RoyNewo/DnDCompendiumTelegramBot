'''
import xml.dom.minidom
doc = xml.dom.minidom.parse("Compendiums\\Spells Compendium 1.3.0.xml")
def main():
    spells = doc.getElementsByTagName("spell")
    for spell in spells:        
        name = spell.getElementsByTagName("roll")[0]
        level = spell.getElementsByTagName("level")[0]
        print("nickname:%s, salary:%s" %
              (getNodeText(name), getNodeText(level)))

    name = doc.getElementsByTagName("spell")[0]
    print(name.firstChild.data)
    spells = doc.getElementsByTagName("spell")
    for spell in spells:        
        name = spell.getElementsByTagName("roll")[0]
        level = spell.getElementsByTagName("level")[0]
        print("name: %s, level: %s" % (name.firstChild.data, level.firstChild.data)) 


def getNodeText(node):
    nodelist = node.childNodes
    result = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            result.append(node.data)
    return ''.join(result)

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
roll = my_str("")
l = my_str(0)

            
            if root[i][j].tag == "name":
                Name = root[i][j].text
            if root[i][j].tag == "text":
                if root[i][j].text != None:
                    text = text + root[i][j].text
                else:
                    text = text + "\\n "

    cadena = ""
    
    for x in root[0].findall("./text"):
        if x.text != None:
            cadena = cadena + x.text
        else:
            cadena = cadena + "\\n "

#        print(x.text)
    print(cadena)

'''