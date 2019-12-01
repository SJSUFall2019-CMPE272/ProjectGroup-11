# place a space between every line of file to train each word as a document
import re
with open('test-health.tsv') as fin, open('test-health-space2.tsv', 'w') as fout:
    for line in fin:
        # change to lowercase if necessary and add newline
        changed_line = line.lower() + '\n'
        fout.write(changed_line)