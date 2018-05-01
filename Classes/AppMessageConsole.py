from . import ConsoleColors as CC


#
# text notifications
# console implementation
#


def msg(text):
    print( CC.OKBLUE, text, CC.ENDC );


def warn(text):
    print( CC.WARNING, text, CC.ENDC )
