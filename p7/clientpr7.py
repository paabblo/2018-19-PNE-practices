from Seqp7 import Seq
import requests
import sys

SERVER = 'http://rest.ensembl.org/'
extension = "sequence/id/ENSG00000165879"
PORT = 8000
headers ={"Content-Type": "application/json", "Accept": "application/json"}

request = requests.get(SERVER + extension, headers = headers)

if not request.ok:
    request.raise_for_status()
    sys.exit()

decoded = request.json()

sequence = Seq(decoded['seq'])

bases = "A", "C", "T", "G"
percentage_bases = {}
basescount = {}
numofbases = ''
pop = ''
ttl_length = sequence.len()

# -- doing count and percentage operations
for index in bases:
    percentage_bases.update({index: sequence.perc(index)})
    basescount.update({index: sequence.count(index)})

for index in bases:
    if str(sequence.count(index)) > str(numofbases) : pop, numofbases = index, sequence.count(index)

# -- print results
print("Number of bases {}\n".format(ttl_length))
print("FRAT1 has {} T bases\n".format(basescount["T"]))
print("The most common base is {} and his percentage is {}%\n".format(pop, str(sequence.perc(pop))))
print("The percentage of each base is {}\n".format(percentage_bases))