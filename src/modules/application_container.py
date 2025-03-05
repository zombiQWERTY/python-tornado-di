from dependency_injector import containers, providers

from .user.user_container import UserContainer
from .user.user_container import get_routes as user_routes
from .auth.auth_container import AuthContainer


class ApplicationContainer(containers.DeclarativeContainer):
    auth_container = providers.Container(AuthContainer)
    user_container = providers.Container(UserContainer, auth_service=auth_container.auth_service)

    @staticmethod
    def make_routes(container: containers.DeclarativeContainer):
        return user_routes(container.user_container())
