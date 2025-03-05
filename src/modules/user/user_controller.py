from .user_service import UserService
from shared.decorators.controller_decorator import Controller
from shared.decorators.get_decorator import Get
from shared.lib.base_controller import BaseController

@Controller
class UserController(BaseController):
    user_service: UserService

    @Get(r"/user/(\d+)", method_name="fetch_user")
    async def fetch_user(self, user_id, request=None, headers=None):
        user = self.user_service.get_user(int(user_id))
        self.write(user)
