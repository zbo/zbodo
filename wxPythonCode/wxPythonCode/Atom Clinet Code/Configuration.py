from xml.dom.minidom import parse, parseString
class Configuration:
    ModuleName=""
    GroupName=""
    MenuName=""

class ConfigReader:
    def __BuildClient(self,xml):
        result=Configuration()
        for node in xml.childNodes:
            if node.localName==None:
                continue
            elif node.localName=='ModuleName':
                result.ModuleName=node.childNodes[0].data
            elif node.localName=='GroupName':
                result.GroupName=node.childNodes[0].data
            elif node.localName=='MenuName':
                result.MenuName=node.childNodes[0].data
        return result

    def ReadConfig(self):
        dom = parse('config.xml')
        config_element = dom.getElementsByTagName("Config")[0]
        clients = config_element.getElementsByTagName("Client")
        allClientsConfigure=[]
        for clientConfXml in clients:
            clientConfig=self.__BuildClient(clientConfXml)
            allClientsConfigure.append(clientConfig)
        return allClientsConfigure

if __name__ == '__main__':
    instance=ConfigReader()
    allconfig=instance.ReadConfig()
    print allconfig


  