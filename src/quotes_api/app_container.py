from dependency_injector import containers, providers
from endpoints import HQEndpoints


class AppContainer(containers.DeclarativeContainer):
    """Main IoC container for the application."""

    hq_endpoint = providers.Factory(HQEndpoints)