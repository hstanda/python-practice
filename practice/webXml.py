# import xml.etree.ElementTree as ET
# data = '''
# <person>
#   <name>Chuck</name>
#   <phone type="intl">
#     +1 734 303 4456
#   </phone>
#   <email hide="yes" />
# </person>
# '''
# # print(data)

# tree = ET.fromstring(data)
# print(tree.find("name").text)
# print(tree.find("phone").text)



import xml.etree.ElementTree as ET

input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))

# Code: http://www.py4e.com/code3/xml2.py