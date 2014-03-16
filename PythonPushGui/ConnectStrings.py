import StatusManager

def GetString_ServerHeader():
    return "http://192.168.56.101:8090/Autotest0/"

def GetString_GetClientId():
    str_getClientId='%3C?xml%20version=%221.0%22%20encoding=%22utf-16%22?%3E%3CRequest%20xmlns:xsi=%22http://www.w3.org/2001/XMLSchema-instance%22%20xmlns:xsd=%22http://www.w3.org/2001/XMLSchema%22%20clientID=%220%22%20op=%22GETCLIENTID%22%20xmlns=%22http://autotest.cisco.com/schema/transport%22%20/%3E'
    return str_getClientId;

def GetString_AddToStream():
    str_addToStream='%3C?xml%20version=%221.0%22%20encoding=%22utf-16%22?%3E%3CRequest%20xmlns:xsi=%22http://www.w3.org/2001/XMLSchema-instance%22%20xmlns:xsd=%22http://www.w3.org/2001/XMLSchema%22%20clientID=%22'+StatusManager.StatusManager.clientId+'%22%20op=%22CONNECTSTREAM%22%20xmlns=%22http://autotest.cisco.com/schema/transport%22%20/%3E'
    return str_addToStream;

def GetString_AddResource(resource):
    str_addResource='%3C?xml%20version=%221.0%22%20encoding=%22utf-16%22?%3E%3CRequest%20xmlns:xsi=%22http://www.w3.org/2001/XMLSchema-instance%22%20xmlns:xsd=%22http://www.w3.org/2001/XMLSchema%22%20clientID=%22'+StatusManager.StatusManager.clientId+'%22%20op=%22ADDTOSTREAM%22%20resourceID=%22'+resource+'%22%20xmlns=%22http://autotest.cisco.com/schema/transport%22%20/%3E'
    return str_addResource

def GetString_SendTR():
    str_sendTr='%3C?xml%20version=%221.0%22%20encoding=%22utf-16%22?%3E%3CRequest%20xmlns:xsi=%22http://www.w3.org/2001/XMLSchema-instance%22%20xmlns:xsd=%22http://www.w3.org/2001/XMLSchema%22%20clientID=%22'+StatusManager.StatusManager.clientId+'%22%20op=%22TOUCH%22%20xmlns=%22http://autotest.cisco.com/schema/transport%22%20/%3E'
    return str_sendTr

def GetString_GetClientId_Pure():
    str_getClientId='<?xml version=\"1.0\" encoding=\"utf-16\"?><Request xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" clientID=\"0\" op=\"GETCLIENTID\" xmlns=\"http://autotest.cisco.com/schema/transport\" />'
    return str_getClientId;

def GetString_AddToStreamPure():
    str_addToStream='<?xml version=\"1.0\" encoding=\"utf-16\"?><Request xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" clientID=\"'+StatusManager.StatusManager.clientId+'\" op=\"CONNECTSTREAM\" xmlns=\"http://autotest.cisco.com/schema/transport\" />'
    return str_addToStream;

def GetString_AddResourcePure(resource):
    str_addResource='<?xml version=\"1.0\" encoding=\"utf-16\"?><Request xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" clientID=\"'+StatusManager.StatusManager.clientId+'\" op=\"ADDTOSTREAM\" resourceID='+resource+' xmlns=\"http://autotest.cisco.com/schema/transport\" />'
    return str_addResource;