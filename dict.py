#!/anaconda3/bin/python

import sys, getopt
from gtts import gTTS

def print_usage():
    print ("Usage:",sys.argv[0],"-l <IETF language tag, default en> [-s - if slow] [-h - shows help]")

lang = 'en' #English
# es - Spanish
# ru - Russian

slow = False

try:
    opts, args = getopt.getopt(sys.argv[1:],"hl:s")
except getopt.GetoptError:
    print_usage()
    sys.exit(1)

for o, a in opts:
    if o == "-h":
        print_usage()
        sys.exit(0)
    elif o == "-l":
        lang = a
    elif o == "-s":
        slow = True



for word in sys.stdin:
    w = word.rstrip().lstrip()
    tts = gTTS(w, lang=lang, slow=slow)
    print(w)
    tts.save(w+'('+lang+')'+'.mp3')
