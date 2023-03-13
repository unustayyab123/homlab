#!/usr/bin/env python3
'''
Palo Alto API Key Credential functions
'''

import requests
import sys
from xml.etree import ElementTree
from requests.packages.urllib3.exceptions import (  # pylint: disable=E0401
    InsecureRequestWarning
)


def getAPIKey(server, user, password, proxies=None):
    '''
    Get the API key for the user
    '''
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    baseURL = 'https://' + server + '/api/'
    payload = {
        'type': 'keygen',
        'user': user,
        'password': password
    }
    resp = requests.get(baseURL,
                        params=payload,
                        proxies=proxies,
                        verify=False)
    resp.raise_for_status()
    tree = ElementTree.fromstring(resp.content)
    return tree.find('result/key').text


if __name__ == '__main__':
    '''
    If ran, write the API key to .creds, with the server
    '''
    import getpass
    username = input('Username: ')
    password = getpass.getpass()
    server = input('Server: ')
    try:
        key = getAPIKey(server, username, password, proxies={'https': None})
    except requests.exceptions.HTTPError as err:
        print(err)
        print('Are you sure you have the right credentials?')
        sys.exit()
    except requests.exceptions.ConnectionError as err:
        print('Unable to connect to host')
        sys.exit()
    with open('.creds', 'w') as credfile:
        credfile.writelines(server + '\n')
        credfile.writelines(key)
    print('Credentials stored in .creds')
