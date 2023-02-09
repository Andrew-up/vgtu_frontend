import xml.etree.ElementTree as ET
root_node = ET.parse('project.xml').getroot()
app = root_node.find('app')
version = app.find('version')
server = root_node.find('server')
server_addr = server.find('addr')
server_port = server.find('port')

print(version.text)
print(server_addr.text)
print(server_port.text)

et = ET.parse('project.xml')
app_n = et.find('app')
version_n = app_n.find('version')
et.write('file_new.xml')

# with open("project.xml", "w") as f:
#     tree.write(f)



