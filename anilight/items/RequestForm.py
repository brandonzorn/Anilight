from anilight.items import Genre, Kind
from anilight.items.Order import Order

from const.lists import LibList


class RequestForm:
    def __init__(self):
        self.limit: int = 50
        self.search: str = ''
        self.page: int = 1
        self.genres: list[Genre] = []
        self.order: Order = Order('', '', '')
        self.kinds: list[Kind] = []
        self.lib_list = LibList.planned

    @property
    def offset(self):
        return (self.page - 1) * 50

    def clear(self):
        self.limit = 50
        self.search = ''
        self.page = 1
        self.genres = []
        self.order = Order('', '', '')
        self.kinds = []
        self.lib_list = LibList.planned
