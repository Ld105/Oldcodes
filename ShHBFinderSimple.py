#!/usr/bin/env python

#Hearthbleed Finder Simple-Simplezao
#By Ld105
#Salve pro v0ldin-yunkers-tio uli
#Achem suas Keys de API no site da shodan
#https://account.shodan.io/login



import sys
import re
import socket
import shodan

SHODAN_API_KEY = (Key)

try:
api = shodan.shodan(key)

 print "[Ld105]Finding Hearthbleeds,wait fucking hacker pervert[Ld105]"

     def results           
          try:
        results = api.search(vuln:cve-2014-0160)
		api.streams.ports([443, 8443])
 
print ' U found some vuln sites but u not found a social life '
print  'Hearthbleed Vulnerable sites Found: %s' % results['all']

if  results['all'] = 0:
"U foundnt vulnerable sites too :C"
sys.exit()
 else results['all'] >= 1:
 print 'Adrr %s' % result['ip_str']
 
        
