fr=open("1.srt", "r")
fw=open("11.srt", "w+")
c=fr.read()
onlyascii=''.join([s for s in c if ord(s) < 127])
fw.write(onlyascii)