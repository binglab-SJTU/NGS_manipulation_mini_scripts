import sys,os
import argparse

parser = argparse.ArgumentParser(prog='Extract gene expression data')
parser.add_argument('--genelist',type=str,help="the genelist file, each gene per line")
parser.add_argument('--exp',type=str,help="expression file")
parser.add_argument('--output',type=str,help="the name of outfile")
parser.add_argument('--genecol',type=int,help="the column number of genes")
parser.add_argument('--expcol',type=str,help="the column numbers of expression, different expression should be seperated by ,")
parser.add_argument('--sep',type=str,default='\t',help="the seperation type between columns")
args = parser.parse_args()

gene_list_file = open(args.genelist,'r')
fpkm_file = open(args.exp,'r')
outfile = open(args.output,'w')
genelist = []
for line in gene_list_file:
	genelist.append(line.strip())
gene_list_file.close()
		
expression_col = [int(i.strip()) - 1  for i in args.expcol.split(',')]
		
for line in fpkm_file:
	content = line.strip().split(args.sep)
	header1 = [content[args.genecol - 1]]
	header2 = [content[i] for i in expression_col]
	header = header1 + header2
	outfile.write('\t'.join(header) + '\n')
	for line in fpkm_file:
		content = line.strip().split(args.sep)
		if content[args.genecol - 1] in genelist or content[args.genecol - 1].upper() in genelist:
			g1 = [content[args.genecol - 1]]
			g2 = [content[i] for i in expression_col]
			gtotal = g1 + g2
			outfile.write('\t'.join(gtotal) + '\n')
fpkm_file.close()
outfile.close()
