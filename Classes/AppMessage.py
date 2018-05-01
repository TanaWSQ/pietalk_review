from . import AppMessageConsole


#
# interface class for text notifications
#
class AppMessage:

    def msg(self, text):
        AppMessageConsole.msg(text)

    def warn(self, text):
        AppMessageConsole.warn(text)
