from codecs import open

filename = '../files/bible_f_col.txt'

def process_line(line):
    print line

with open(filename, 'r', encoding='latin1') as fd:
    for lineno, line in enumerate(fd):
        process_line(line)

        if lineno > 5:
            break
