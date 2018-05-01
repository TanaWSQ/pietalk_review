# implementuje simple stupid key/value storage
from . import AppMessage


class Config:

    def __init__(self, autosave = True):
        self.msg = AppMessage.AppMessage()
        if autosave:
            self.msg.msg('autosave turned on')

        else:
            self.msg.warn('not using autosave function, you have to use save() manually')



    # mocked class
    # TODO: implement getKey
    def getKey(self, keyName):
        if keyName == 'testkey':
            return '48'

        else:
            return 'undefined key'

    # TODO: implement setKey
    def setKey(self, keyName, value):
        return 'to be implemented'

    # TODO: implement load method
    def load():
        self.msg.msg("not loading content, not implemented yet")

    # TODO: implement save method
    def save():
        self.msg.msg("not saving content, not implemented yet")
