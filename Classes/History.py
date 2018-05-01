# small SQL course


class History:
    def __init__(self):
        pass

    # INSERT INTO
    def add(self, time, user, channel, type, content):
        pass

    # export of history data in defined format
    # a) txt
    # b) json
    # c) csv
    def export(self, format):
        pass

    # erase local history
    def flush(self):
        pass

    # SELECT, ORDER BY
    def getCompleteHistory(self):
        pass

    # SELECT, ORDER BY, LIMIT
    def getLatestMessagesByCount(self, count):
        pass

    # SELECT, ORDER BY, WHERE
    def getLatestMessagesByTime(self, since):
        pass
