"""

import csv

with open('eggs.csv', mode='w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Banked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wunderful Spam'])
    spamwriter.writerows(['Spam'] * 5 + ['Banked Beans'])


with open('exemploRestval.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['nome', 'idade', 'cidade'], restval='N/A')
    writer.writeheader()
    writer.writerow({'nome': 'Ana', 'idade': 30})


with open('exemploExtrasaction.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['nome', 'idade'], extrasaction='ignore')
    writer.writeheader()
    writer.writerow({'nome': 'Ana', 'idade': 30, 'cidade': 'SP'})

"""

# --------------------------------------------------------------------
import json

print(json.dumps(['foo', {'Bar': ('baz', None, 1.0, 2)}]))

print(json.dumps("\"foo\bar"))

print(json.dumps('\u1234'))

print(json.dumps('\\'))

print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))

print(json.dumps({'Carla': 7, 'Bruno': 5, 'Ana': 9}, sort_keys= True, separators=(',',':'), indent= 4))

