#/usr/bin/env python

from ciscoconfparse import CiscoConfParse

#open the configfile

config = CiscoConfParse("cisco_ipsec.txt")


#question 8
print "question 8:------------------------"
crypto = config.find_objects(r"crypto map CRYPTO")
for entry in crypto:
	print entry.text
	for child in entry.all_children:
		print child.text


#question 9
print "question 9:--------------------------"
crypto_pfs = config.find_objects_w_child(parentspec=r"crypto map CRYPTO", childspec=r"pfs group2")
for entry in crypto_pfs:
        print entry.text
        for child in entry.all_children:
                print child.text

#question 10
print "question 10:--------------------------"
crypto_pfs = config.find_objects_wo_child(parentspec=r"crypto map CRYPTO", childspec=r"transform-set AES-SHA")
for entry in crypto_pfs:
        print entry.text
        for child in entry.all_children:
                print child.text

