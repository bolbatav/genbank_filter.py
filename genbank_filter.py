#!/usr/bin/env python3
import sys
import argparse

def read_fasta(fasta):
	with open(fasta, 'r') as inf:
		raw_fasta=inf.readlines()
	if not raw_fasta[0].startswith('>'):
		print(f'The {file} alignment file is not a valid Fasta file.' )
		sys.exit()
	for i in range(len(raw_fasta)):
		raw_fasta[i]=raw_fasta[i].strip()
	alignment={}
	for i in range(len(raw_fasta)):
		if '>' in raw_fasta[i]:
			h=i
			raw_fasta[h]=raw_fasta[h].replace(' ', '_')
			alignment[raw_fasta[h]]=[]
			continue
		else:
			alignment[raw_fasta[h]]+=[raw_fasta[i].upper()]
			continue
	for i in alignment.keys():
		alignment[i]=''.join(alignment[i])
	return alignment

def write_fasta(filename, alignment):
	text=''
	for i in alignment.keys():
		text=text+i+'\n'+alignment[i]+'\n'
	with open(filename, 'w') as outf:
		outf.write(text)

parser=argparse.ArgumentParser(description='Cpmpares MultiFASTA files and filters identical sequences into a separate file.')
parser.add_argument('files', metavar='file', type=str, nargs='+', help='List of files to compare.')
arguments=parser.parse_args()

alignments={}
repeats={}
if len(arguments.files)<2:
	print('You must provide at least two files to compare.')
	sys.exit()
for f in arguments.files:
	alignments[f]=read_fasta(f)
for a in list(alignments):
	check=alignments.pop(a)
	for k in alignments.keys():
		for ck in list(check):
			if ck in alignments[k]:
				repeats[ck]=check.pop(ck)
				for al in alignments.keys():
					if ck in alignments[al]:
						del alignments[al][ck]
	alignments[a]=check
	#write_fasta(a, check)
alignments['repeats.fas']=repeats
print(len(repeats), 'common sequences found in the alignments.')
if not len(repeats):
	sys.exit()
for a in alignments.keys():
	write_fasta(a, alignments[a])
#write_fasta('repeats.fas', repeats)
