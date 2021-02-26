#!/bin/python3

import xml.etree.ElementTree as ET

def pretty_xml(element: ET.Element, indent='\t', new_line='\n', level=1):
    if len(element):
        element.text = new_line + indent * level
        elements = list(element)
        for subelement in elements:
            subelement.tail = element.text
            if elements.index(subelement) == len(elements) - 1:
                subelement.tail = new_line + indent * (level-1)
            pretty_xml(subelement, indent, new_line, level=level + 1)
    else:
        if element.text is not None:
            element.text = element.text.strip()
            
configPath = f"Config.xml"
configTree = ET.parse(configPath)
configRoot = configTree.getroot()
#do some things
pretty_xml(configRoot)
configTree.write(configPath, encoding="UTF-8", xml_declaration=True, short_empty_elements=False)
