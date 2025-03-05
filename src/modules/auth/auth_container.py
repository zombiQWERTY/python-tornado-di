from dependency_injector import containers, providers
from .auth_service import AuthService


class AuthContainer(containers.DeclarativeContainer):
    auth_service = providers.Singleton(AuthService)
