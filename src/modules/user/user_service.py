from modules.user.user_permissions_provider import UserPermissionsFactory
from modules.auth.auth_service import AuthService


class UserService:
    def __init__(self, user_permissions_factory: UserPermissionsFactory, auth_service: AuthService):
        self.user_permissions_factory = user_permissions_factory
        self.auth_service = auth_service

    def get_user(self, user_id: int):
        return {"id": user_id, "name": f"User {user_id}",
                "role": self.user_permissions_factory.connect_role("ADMIN", user_id).get_permissions(),
                "someInfoFromAuth": self.auth_service.get_auth_info(user_id)}
