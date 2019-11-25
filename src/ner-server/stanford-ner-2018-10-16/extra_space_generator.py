# place a space between every line of file to train each word as a document
import re
with open('train.tsv') as fin, open('train2.tsv', 'w') as fout:
    for line in fin:
        changed_line = line + '\n'
        fout.write(changed_line)