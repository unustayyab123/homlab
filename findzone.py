#!/usr/bin/env python3
'''
Finds the zone for a given IP and virtual router
'''

import argparse
import requests
import sys


from requests.packages.urllib3.exceptions import (  # pylint: disable=E0401
    InsecureRequestWarning
)
from xml.etree import ElementTree


def setarguments():
    """set up command line arguments. Returns args"""
    parser = argparse.ArgumentParser('Find the zone for a given IP '
                                     'and Virtual Router')
    parser.add_argument('virtualrouter',
                        help='Virtual Router name')
    parser.add_argument('ipaddr',
                        help="IP address to locate ")
    parser.add_argument('credentialfile',
                        help="Credential File")
    return parser.parse_args()


def fibLookup(server, key, virtualrouter, ipaddr, proxies=None):
    '''
    Perform a FIB Lookup for a given IP in a given Virtual Router and return
    the outgoing interface
    '''
    requests.packages.urllib3.disable_warnings(  # pylint: disable=E1101
        InsecureRequestWarning
    )
    baseURL = 'https://' + server + '/api/'
    payload = {
        'type': 'op',
        'cmd': '<test><routing><fib-lookup>'
               '<virtual-router>{}</virtual-router>'
               '<ip>{}</ip>'
               '</fib-lookup></routing></test>'.format(
                   virtualrouter,
                   ipaddr
               ),
        'key': key
    }
    resp = requests.get(baseURL,
                        params=payload,
                        proxies=proxies,
                        verify=False)
    resp.raise_for_status()
    tree = ElementTree.fromstring(resp.content)
    return tree.find('result/interface').text


def zoneForInterface(server, key, interface, proxies=None):
    '''
    Find the zone for an interface
    '''
    requests.packages.urllib3.disable_warnings(  # pylint: disable=E1101
        InsecureRequestWarning
    )
    baseURL = 'https://' + server + '/api/'
    payload = {
        'type': 'op',
        'cmd': '<show><interface>{}</interface></show>'.format(
            interface,
        ),
        'key': key
    }
    resp = requests.get(baseURL,
                        params=payload,
                        proxies=proxies,
                        verify=False)
    resp.raise_for_status()
    tree = ElementTree.fromstring(resp.content)
    return tree.find('result/ifnet/zone').text


if __name__ == '__main__':
    args = setarguments()
    try:
        with open(args.credentialfile, 'r') as credfile:
            credfilecontents = credfile.readlines()
            server = credfilecontents[0].strip()
            key = credfilecontents[1].strip()
    except FileNotFoundError as err:
        print(err)
        print('File not found. Exiting.')
        sys.exit()
    except IndexError as err:
        print('Invalid credential file. Exiting')
        sys.exit()

    interface = fibLookup(server, key, args.virtualrouter, args.ipaddr)
    zone = zoneForInterface(server, key, interface)
