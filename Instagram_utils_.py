import enum

def all_fields_value(enum:enum.Enum):
    
    return [e.value for e in enum]

def all_fields_url(enum:enum.Enum):
    res = ""
    all = all_fields_value(enum)
    for index,elem in enumerate(all):
        res += elem
        if index == len(all) - 1:
            return res
        res += ","
    return res

class User_fields(enum.Enum):
    account_type = "account_type"
    username = "username"
    media_count = "media_count"
    id = "id"

