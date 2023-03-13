import findzone
import requests
# output123 = findzones.end_command(remote123,"show clock")

device = {
        'virtualrouter': 'Tahakom-VR',
        'ip': '192.168.200.1',
        'credentialfile': 'creds',
         }

output123 = findzone()
print(output123)