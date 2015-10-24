import sys
import re
import string
import unicodedata
import io
from sbs import Splitter

class Parser(object):
    def __init__(self):
        self._is_number_prefix = re.compile(u'^\d\. ')
        self._max_len = 0

    def sb_word(self, w):
        wt = self._extract_word(w)
        if wt[1] == 'sb.':
            return wt[0]

    def _extract_word(self, l):
        if self._is_number_prefix.match(l):
            s = l[3:].split(';')
        else:
            s = l.split(';')
        return (s[0], s[1][:-1].strip())

    def strip_accents(self, string):
        accents=('COMBINING ACUTE ACCENT', 'COMBINING GRAVE ACCENT', 'COMBINING TILDE')
        accents = set(map(unicodedata.lookup, accents))
        chars = [c for c in unicodedata.normalize('NFD', string) if c not in accents]
        return unicodedata.normalize('NFC', ''.join(chars))

if len(sys.argv) < 3:
    print "Usage: run.py RO2012.opslagsord.med.homnr.og.ordklasse.txt corpus.txt"
    exit(-1)

p = Parser()
s = Splitter()
s.load(filter(None, map(p.sb_word, io.open(sys.argv[1], 'r'))))

k = 0
for l in map(unicode.strip, io.open(sys.argv[2], 'r')):
    if len(l) != 0:
        for w in l.split(' '):
            # print w,
            w =  p.strip_accents(w.lower())
            splits = s.split(w)
            if splits:
                print "%s (%s)" % (w, splits)
                k += 1
                if k > 100:
                    exit(0)
