"""
EksiEntry class for representing an entry under a 'baslik'
"""


from dataclasses import dataclass

@dataclass
class EksiEntry:
    author: str
    author_id: str
    comment_count: int
    favorite_count: int
    data_id: str
    is_favorite: bool
    is_pinned: bool
    content: str
    time: str

