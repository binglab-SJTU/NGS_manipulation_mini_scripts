# NGS_manipulation_mini_scripts
**Some little scripts to help easier manipulation of NGS data.**

## 1. Extract_gene_expression.py
This script aimed to help to extract gene expression of different conditions for a specific gene list.

## USAGE:
      """
      python Extract_gene_expression.py --genelist inflammatory_gene_list.txt --exp genes.fpkm_tracking --output expression.txt --genecol 5 --expcol 10,14
      """
## Command Line:
Usage: Gene expression extraction [-h] [--genelist GENELIST] [--exp EXP] [--output OUTPUT] [--genecol GENECOL] [--expcol EXPCOL] [--sep SEP]
### Arguments:
`-h`, —help	show this help message and exit

`--genelist` GENELIST	the query gene list, each gene per line.

`--exp` EXP the expression file for gene extraction.

`--output` OUTPUT the output file name.

`--genecol` GENECOL the column number of gene name.

`--expcol` EXPCOL the column numbers of expression, seperated by ','.

`--sep` SEP the separation type between each column.
