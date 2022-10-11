from items import Anime, Episode, RequestForm, Genre, Kind, Order, Character, User, UserRate


class Parser:
    catalog_name = 'CATALOG'
    is_primary = False

    def get_manga(self, manga: Anime) -> Anime:
        return manga

    def get_character(self, character: Character) -> Character:
        return character

    def search_manga(self, params: RequestForm) -> list[Anime]:
        return []

    def get_chapters(self, manga: Anime) -> list[Episode]:
        return []

    def get_preview(self, manga: Anime):
        return

    def get_character_preview(self, character: Character):
        return

    def get_genres(self) -> list[Genre]:
        return []

    def get_kinds(self) -> list[Kind]:
        return []

    def get_orders(self) -> list[Order]:
        return []

    def get_relations(self, manga: Anime) -> list[Anime]:
        return []

    def get_characters(self, manga: Anime) -> list[Character]:
        return []


class LibParser:
    def __init__(self):
        pass

    def search_manga(self, params: RequestForm) -> list[Anime]:
        return []

    def get_user(self) -> User:
        return User(None, 'Войти', None)

    def create_user_rate(self, manga: Anime):
        pass

    def check_user_rate(self, manga: Anime):
        pass

    def delete_user_rate(self, user_rate: UserRate):
        pass

    def get_user_rate(self, manga: Anime) -> UserRate:
        pass

    def update_user_rate(self, user_rate: UserRate):
        pass
