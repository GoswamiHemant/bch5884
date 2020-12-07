#!/usr/bin/env python3
#Hemant Goswami

import matplotlib.pyplot as plt
from  matplotlib.pyplot import rcParams
rcParams['figure.figsize'] = 18, 5


#Parsing the fasta file
def ParseFile(Name_of_file):
    data = str()
    with open(Name_of_file) as f:
        for line in f:
            temp = str(line)
            temp = temp.replace('\n', '')
            temp = temp.lower()
            data += temp
                
    return data

#Finding 21 nucleotides long repeat sequences and their frequency 

data = ParseFile("DNAFASTA.fasta")

length_list = [21]

for length in length_list:
    sequence = {}
    key = data[:length]
    sequence[key] = 1   #number assigned to every unique sequence
    for i in range(0,len(data)-length):
        key = data[i:i+21]
        if key in sequence.keys():
            sequence[key] += 1   #if the unique sequence is hit one more time
        else:
            sequence[key] = 1
    for key,value in sequence.copy().items():
        if value < 5:
            sequence.pop(key)  #remove repeats if occurrence is less than 5 times
    print("\n\n The",length, "nucleotide long repeat sequence in the given DNA sequence is")
    print(sequence)
    plt.bar(*zip(*sequence.copy().items()), color='orange', width=0.3,)
    plt.title('Occurrence of 21 nucleotide long repeats in S. sulfotaricus')
    plt.xlabel('Unique repeats', color='green', fontsize=16)
    plt.ylabel('Frequency', color='green', fontsize=16)
    plt.savefig("21ntdrepeats.png", format="png")
    plt.show()

#Finding 22 nucleotides long repeat sequences and their frequency 
length_list = [22]

for length in length_list:
    sequence = {}
    key = data[:length]
    sequence[key] = 1    #number assigned to every unique sequence
    for i in range(0,len(data)-length):
        key = data[i:i+22]
        if key in sequence.keys():
            sequence[key] += 1 #add +1 if the same sequence is hit one more time
        else:
            sequence[key] = 1
    for key,value in sequence.copy().items():
        if value < 5:
            sequence.pop(key)  #remove repeats if occurrence is less than 5 times
    print("\n\n The",length, "nucleotide long repeat sequence in the given DNA sequence is")
    print(sequence)
    plt.bar(*zip(*sequence.copy().items()), color='purple', width=0.3,)
    plt.title('Occurrence of 22 nucleotide long repeats in S. sulfotaricus')
    plt.xlabel('Unique repeats', color='green', fontsize=16)
    plt.ylabel('Frequency', color='green', fontsize=16)
    plt.savefig("22ntdrepeats.png", format="png")
    plt.show()

#Finding 22 nucleotides long repeat sequences and their frequency  
length_list = [23]

for length in length_list:
    sequence = {}
    key = data[:length]
    sequence[key] = 1
    for i in range(0,len(data)-length):
        key = data[i:i+23]
        if key in sequence.keys():
            sequence[key] += 1
        else:
            sequence[key] = 1
    for key,value in sequence.copy().items():
        if value < 5:
            sequence.pop(key)
    print("\n\nThe",length, "nucleotide long repeat sequence in the given DNA sequence is")
    print(sequence)
    plt.bar(*zip(*sequence.copy().items()), color='maroon', width=0.1,)
    plt.title('Occurrence of 23 nucleotide long repeats in S. sulfotaricus')
    plt.xlabel('Unique repeats', color='green', fontsize=16)
    plt.ylabel('Frequency', color='green', fontsize=16)
    plt.savefig("23ntdrepeats.png", format="png")
    plt.show()

#similarly we can search for repeats of any length. Because CRISPR repeats are usually 21-35 bases long, so I would search for all the 21-35 bases. However, here I am just searching 21-23 bases long repeats. 

#writing html file
def writehtml():
	f=open("hem_CRISPR_repeat_finder.html", 'w')
	f.write("<DOCTYPE html>")
	f.write("<html>")
	f.write("<head>")
	f.write("<style> body { background:lightblue; } \n")
	f.write("</style>\n")
	f.write("<h1> CRISPR repeat analysis in Sulfolobus sulfotaricus genomic DNA sequence </h1>\n")
	f.write("</head>")
	f.write("<body>\n")
	f.write("<p>  My research involves the structural and biochemical cjaracterization of  of novel type V CRISPR-Cas proteins. CRISPR stands for Clustered Regularly Interspaced Short Palindromic Sequence. An evolutionalary struggle of billions of years between prokaryotes and viruses have led to the development of adaptive immune system in bacteria. CRISPR-Cas based immunity is found in 90% of archaea and 50% of bacteria. Based on the CRISPR-Cas loci, CRISPR Cas systems have been classified into six distinct types and each uses a set of special Cas proteins for DNA interference. Type I and type III CRIPPR systems employs a multi-protein complex for crRNA binding and DNA cleavage, while type II (Cas9) and type V CRISPR (Cas12) systems utilize a single protein, that recognizes its crRNA and cleaves the target DNA. Cas9 protein uses a distinct domain, HNH or RuvC, to cleave each strand of DNA while Cas12 uses just RuvC domain to cleave both the strands of DNA. </p>\n")
	f.write("<p> Recently I found that Sulfolobus sulfotaricus contains DNA sequesnce similar to Cas12 genes. So to verify if these sequences are really Cas protein genes, we want to identify the CRISPR repeats downstream of promising Cas genes because these repeats are an integral part of CRISPR-Cas array. </p>\n")
	f.write('<p> <img src="21ntdrepeats.png"> </p>')
	f.write('<p> <img src="22ntdrepeats.png"> </p>')
	f.write('<p> <img src="23ntdrepeats.png"> </p>')
	f.write("</body>")
	f.write("</html>")
	f.close()
writehtml()
print("Done!")
