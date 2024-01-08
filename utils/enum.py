from enum import Enum

class RoleEnum(Enum):
    superadmin=1
    service_provider=2
    customer=3
    admin=4


class GenderEnum(Enum):
    male = "Male"
    female = "Female"
    Not_to_say = None
    
    

class SocialTypeEnum(Enum):
    google = 1
    facebook = 2
    instagram = 3
    apple = 4
    twitter = 5
    


class ScreenEnum(Enum):
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    service ="service"
    badge = "badge"
    
    