from graphx.configurations.infrastructure.db.definitions import GraphConfigurator
from registry.services import BootableService, Container


class DataBaseService(BootableService):

    def boot(self, container: Container):
        from graphx.configurations.app.settings import Props

        url = container.get(Props.NEO_URL)
        username = container.get(Props.NEO_USERNAME)
        password = container.get(Props.NEO_PASSWORD)

        configurator = GraphConfigurator(url, username, password)

        provider = container.get(Props.DI_PROVIDER)
        provider.add_configurator(configurator)

