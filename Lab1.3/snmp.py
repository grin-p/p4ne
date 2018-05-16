from pysnmp.hlapi import *

community_name="public"
ipaddr_string="10.31.70.107"
port_int=161
MIB_string="'1.3.6.1.2.1.2.2.1.2'"

result = getCmd(SnmpEngine(),
	CommunityData(community_name, mpModel=0),
	UdpTransportTarget((ipaddr_string, port_int)),
	ContextData(),
	ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0))

print(result)

result2 = nextCmd(MIB_string, lexicographicMode=False)

#fot x in result