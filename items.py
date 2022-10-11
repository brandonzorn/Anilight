from const.lists import LibList


class BaseItem:
    def __init__(self, item_id: str, name: str, russian: str):
        self.id = item_id
        self.name = name
        self.russian = russian

    def get_name(self) -> str:
        if self.russian:
            return self.russian
        return self.name


class Anime(BaseItem):
    def __init__(self, item_id, catalog_id, name, russian):
        super().__init__(item_id, name, russian)
        self.catalog_id = catalog_id
        self.kind = None
        self.description: str = ""
        self.score = 0
        self.status = None
        self.genres: list[Genre] = []


class Episode:
    def __init__(self, chapter_id: str, episode_num: int, title: str, language: str):
        self.id = chapter_id
        self.episode_num = episode_num
        self.title = title
        self.language = language

    def get_name(self) -> str:
        if self.title:
            return f"{self.episode_num} - {self.title}"
        return f"{self.episode_num}"


class Genre(BaseItem):
    def __init__(self, item_id, name, russian, kind):
        super().__init__(item_id, name, russian)
        self.kind = kind


class Order(BaseItem):
    def __init__(self, item_id, name, russian):
        super().__init__(item_id, name, russian)


class Kind(BaseItem):
    def __init__(self, item_id, name, russian):
        super().__init__(item_id, name, russian)


class Status:
    def __init__(self, name, russian):
        self.name = name
        self.russian = russian

    def get_name(self) -> str:
        if self.russian:
            return self.russian
        return self.name


class Character(BaseItem):
    def __init__(self, item_id, name, russian, description, role):
        super().__init__(item_id, name, russian)
        self.description = description
        self.role = role


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


class User:
    def __init__(self, user_id, nickname, avatar):
        self.id = user_id
        self.nickname = nickname
        self.avatar = avatar


class UserRate:
    def __init__(self, rate_id, user_id, target_id, score, status, chapters):
        self.id = rate_id
        self.user_id = user_id
        self.target_id = target_id
        self.score = score
        self.status = status
        self.chapters = chapters


class HistoryNote:
    def __init__(self, note_id, episode: Episode, anime: Anime, is_completed: bool):
        self.id = note_id
        self.episode = episode
        self.anime = anime
        self.is_completed = is_completed

    def get_name(self):
        return f'{self.anime.get_name()}: {self.episode.get_name()}'
