class AuthService:
    def get_auth_info(self, user_id: int):
        return {"someAuthInfo": {"id": user_id}}
