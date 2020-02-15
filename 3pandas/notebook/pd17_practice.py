import xml.etree.ElementTree as ET
import pandas as pd
tree = ET.parse('C:/Repository/python_basic/3pandas/coffee/practice.xml')
root = tree.getroot()
# root = ET.fromstring(practice_as_string)

print(root.tag)
print(root.attrib)

for child in root:
    print(child.tag, child.attrib)

print(root[0][1].text)

