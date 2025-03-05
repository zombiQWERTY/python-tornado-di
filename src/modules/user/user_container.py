from dependency_injector import containers, providers
from .user_controller import UserController
from .user_permissions_provider import UserPermissionsFactory
from .user_service import UserService


class UserContainer(containers.DeclarativeContainer):
    user_permissions_factory = providers.Factory(
        UserPermissionsFactory,
    )

    auth_service = providers.Dependency()

    user_service = providers.Singleton(UserService,
                                       user_permissions_factory=user_permissions_factory,
                                       auth_service=auth_service)


def get_routes(user_container: UserContainer):
    routes = []
    for route in getattr(UserController, "_routes", []):
        routes.append((route["path"], UserController, {"user_service": user_container.user_service()}))
    return routes
