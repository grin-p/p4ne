from ipaddress import IPv4Network
import random

low_net=0x0B000000
max_net=0xDF000000

low_mask=8
max_mask=24

net_count=50

class IPv4RandomNetwork(IPv4Network):
    def __init__(self, net_1=0x00000000, net_2=0xFFFFFFFF, mask_1=0, mask_2=32):
        IPv4Network.__init__(self, (random.randint(net_1, net_2), random.randint(mask_1,mask_2)), strict=False)

    def regular(self):
        return self.is_global

    def key_value(self):
        key=(int(self.network_address)) + (int(self.netmask)<<32)
        return key

def fun1(x):
    return x.key_value()

i=0
L = []
while i<net_count:
    cur_net=IPv4RandomNetwork(low_net,max_net,low_mask,max_mask)
    L.append(cur_net)
    # print(str(cur_net))
    # print(cur_net.network_address)
    # print(cur_net.with_hostmask)
    i+=1

for x in sorted(L, key=fun1):
    print(x)