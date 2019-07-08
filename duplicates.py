#! /usr/bin/env python3

import srt

f = open("0.srt", "r")
content = f.read()
onlyascii = ''.join([c for c in content if ord(c) < 127])
sg = srt.parse(onlyascii)
sub = list(sg)

seen = set()
uniq = []

for x in sub:
    if x not in seen:
        uniq.append(x)
        seen.add(x)

print(uniq)
