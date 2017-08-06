#!/Library/Frameworks/Python.framework/Versions/3.5/bin/anaconda/bin/python



########################
#
# text colors
#
########################

BLK="\033[30m"       # black
RED="\033[31m"       # red
GRN="\033[32m"       # green
YLW="\033[33m"       # yellow
BLU="\033[34m"       # blue
PNK="\033[35m"       # pink
CYN="\033[36m"       # cyan
WHT="\033[37m"       # white
NC ="\033[0;39m"     # reset

######################
#
# bg colors
#
######################

BLKBG="\033[40m"      # black
REDBG="\033[41m"      # red
GRNBG="\033[42m"      # green
YLWBG="\033[43m"      # yellow
BLUBG="\033[44m"      # blue
MAGBG="\033[45m"      # magenta
CYNBG="\033[46m"      # cyan
WHTBG="\033[47m"      # white
NCBG ="\033[49m"      # reset

######################
#
# fg on bg colors
#
######################

GRNONBLK = "\033[32;40m"
YLWONRED = "\033[33;41m"
WHTONBLK = "\033[37;40m"
WHTONBLU = "\033[37;44m"
WHTONRED = "\033[37;41;5m"
RSTCOLOR = "\033[39;49m"
RSTATTR  = "\033[0m"


def print_good(txt):
    """good"""
    print("{0}[+] {1} {2}".format(GRN, txt, NC))


def print_status(txt):
    """status"""
    print("{0}[*] {1} {2}".format(YLW, txt, NC))


def print_error(txt):
    """error"""
    print("{0}[!] {1} {2}".format(WHTONRED, txt, NC))


def print_line():
    """line"""
    print("{0}={1}".format(WHTONBLU, RSTATTR) * 30)


