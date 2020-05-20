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
    name = doc.getElementsByTagName("spell")[0]
    print(name.firstChild.data)

    spells = doc.getElementsByTagName("spell")
    for spell in spells:        
        name = spell.getElementsByTagName("roll")[0]
        level = spell.getElementsByTagName("level")[0]
        print("name: %s, level: %s" % (name.firstChild.data, level.firstChild.data)) 
"""
def getNodeText(node):
    nodelist = node.childNodes
    result = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            result.append(node.data)
    return ''.join(result)


if __name__ == "__main__":
    main()

