# implementuje simple stupid key/value storage
from . import AppMessage


class Config:

    def __init__(self, autosave = True):
        self.msg = AppMessage.AppMessage()
        self.dict = {}
        if autosave:
            self.msg.msg('autosave turned on')

        else:
            self.msg.warn('not using autosave function, you have to use save() manually')

        self.msg.info('config load - done\n')

    # mocked class
    # TODO: implement getKey
    # def getKey(self, keyName):
    #     if keyName in self.dict:
    #         return self.dict[keyName]
    #
    #     else:
    #         return 'undefined key'
    #
    # # TODO: implement setKey
    # def setKey(self, keyName, value):
    #     self.dict[keyName] = value
    #     return value
    #
    def getKey(self, keyName):
        if keyName == 'testkey':
            return '48'
        else:
            return arr.get(keyName, "undefined")

    # TODO: implement setKey
    def setKey(self, keyName, value):
        global arr
        arr = {keyName:value}
        return arr
    # TODO: implement load method
    def load():
        self.msg.msg("not loading content, not implemented yet")

    # TODO: implement save method
    def save():
        self.msg.msg("not saving content, not implemented yet")
