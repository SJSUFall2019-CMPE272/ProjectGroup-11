# place each field of csv on a separate line, categorized as IT support
import re
with open('MOCK_DATA_TEST_HEALTH.csv') as fin, open('test-health.tsv', 'w') as fout:
    for line in fin:
        if ('\n' in line):
            # last field will not have a comma at the end, append
            extra_comma_line = line.replace('\n', ',')
        changed_line = extra_comma_line.replace(',', '\tHEALTH\n')
        fout.write(changed_line)