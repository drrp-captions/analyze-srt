#! /usr/bin/env python3

import srt
import glob

def analyze():
    write_header("Filename","word_count", "duration", "wps")
    jwct, jtime, jwps = analyze_files(glob.glob("*.srt"))
    write_report("Total",jwct,jtime,jwps)

def write_header(filename,words,time,wps):
    f = open("report.csv", "a+")
    f.write(f"{filename},{words},{time},{wps}\n")
    f.close()

def write_report(filename,words,time,wps):
    f = open("report.csv", "a+")
    f.write(f"{filename},{words},{time:.3f},{wps:.3f}\n")
    f.close()

def analyze_files(files):
    jwct = 0
    jtime = 0.0

    for f in files:
        wct, time = analyze_file(f)
        jwct += wct
        jtime += time

    jwps = jwct/jtime
    print(f"\nTotal words = {jwct}, duration  = {jtime:.3f} secs and average wps: {jwps:.3f}")
    return jwct, jtime, jwps

def analyze_file(filename):
    f = open(filename, "r")       # open file
    content = f.read()            # read contents into string
    onlyascii = ''.join([c for c in content if ord(c) < 127])
    sg = srt.parse(onlyascii)     # convert string to subtitle groups
    sub = list(sg)                # Convert subtitle groups to a list

    wct, time = srt_avg(sub)
    wps = wct/time
    print(f"{filename}: Word count = {wct}, duration = {time:.3f} secs and wps: {wps:.3f}")
    write_report(filename,wct,time,wps)
    return wct, time

def srt_avg(sub):
    # print(sub)
    time = 0.0
    wct = 0

    for l in sub:
        wc = len(l.content.split())
        dur = (l.end - l.start).total_seconds()
        wps = wc/dur
        time += dur                         # calculate total duration
        wct  += wc                          # calculate total word count

    return wct, time

analyze()

