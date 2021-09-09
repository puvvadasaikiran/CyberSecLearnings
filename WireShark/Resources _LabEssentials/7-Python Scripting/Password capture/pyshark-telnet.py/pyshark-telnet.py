#=====================================================                 
#TELNET:
#=====================================================                 

import pyshark

capture = pyshark.LiveCapture ('eth0')
for packet in capture:
    if 'TELNET' in packet:
        try:
            output = packet.telnet
            if 'Username' in str(output):
                print ('----------------------------------')
                print('USERNAME:')
            elif 'Password' in str(output):
                print ('----------------------------------')
                print('PASSWORD:')

            if packet.telnet.data:
                print(output)

        except:
            pass

