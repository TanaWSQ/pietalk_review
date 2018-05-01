#
# main application object
#

from . import Config
from . import User
from . import History
from . import Conversations


class Chat:
    def __init__(self):
        self.config = Config.Config()
        self.user = User.User()
        self.history = History.History()
        self.conversations = Conversations.Conversations()
        self.ts_last_update = 0

    # origos to malo byt
    def get_conversations(self):
        pass

    # return list of chatrooms available on server
    # @singleUserChatroom
    # #multipleUserChatroom
    # TODO: implement
    def get_rooms(self, i, int1):
        return ['#general', '@Ariel', '@Mulan', '@Pocahontas']

    # get list of update events from server
    # TODO: implement
    def get_updates(self):
        pass

