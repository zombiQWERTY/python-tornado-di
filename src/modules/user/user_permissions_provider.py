from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, id):
        self.id = id

    @abstractmethod
    def get_permissions(self):
        pass


class AdminUser(User):
    def get_permissions(self):
        return ["read", "write", "delete"]


class RegularUser(User):
    def get_permissions(self):
        return ["read", "write"]


class GuestUser(User):
    def get_permissions(self):
        return ["read"]


class UserPermissionsFactory:
    @staticmethod
    def connect_role(role, id):
        role_map = {
            "admin": AdminUser,
            "regular": RegularUser,
            "guest": GuestUser
        }
        return role_map.get(role.lower(), GuestUser)(id)
