"""Constants."""

from enum import IntEnum


class Limits(IntEnum):
    """Constants with the value type 'int'."""

    URL_TYPE_NAME_MAX_CHAR = 50
    COLLECTION_NAME_MAX_CHAR = 50
    COLLECTION_DESCRIPTION_MAX_CHAR = 300
    MARKBOOK_TITLE_MAX_CHAR = 100
    MARKBOOK_DESCRIPTION_MAX_CHAR = 300