class User:

    def __init__(self):
        self.updated = False
        self.nick = 'user.nick'
        self.status = 'user.status'

    def is_updated(self):
        return self.updated

    def get_nick(self):
        return self.nick

    # setting nick for user
    def set_nick(new_nick):
        self.updated = False
        self.nick = new_nick
        return self.sync()

    def get_status(self):
        return self.status

    # setting status message
    def set_status(new_status_message):
        self.updated = False
        self.status = new_status_message
        return self.sync()

    # push local user state to server
    # TODO - implement
    def sync():
        return False
