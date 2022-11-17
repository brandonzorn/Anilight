class Chapter:
    def __init__(self, chapter_id: str, ep: str, title: str, url: str, kind: str, author: str):
        self.id = chapter_id
        self.ep = ep
        self.title = title
        self.url = url
        self.kind = kind
        self.author = author

    def get_name(self) -> str:
        return f"{self.kind}--{self.ep}--{self.author}"
