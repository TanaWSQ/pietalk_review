from . import ConsoleColors as CC


#
# text notifications
# console implementation
#

def info(text):
    print( CC.OKGREEN, text, CC.ENDC )

def msg(text):
    print( CC.OKBLUE, text, CC.ENDC );


def warn(text):
    print( CC.WARNING, text, CC.ENDC )
