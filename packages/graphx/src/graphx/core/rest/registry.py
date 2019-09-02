from graphx.configurations.app import settings
from graphx.core.rest.definitions import NodeConfigurator
from graphx.core.rest.resources import NodeCollection
from registry.services import BootableService, Container


class NodeService(BootableService):
    def boot(self, container: Container):
        falcon = container.get(settings.Props.FALCON)

        provider = container.get(settings.Props.DI_PROVIDER)
        provider.add_configurator(NodeConfigurator)
        injector = provider.get_injector()

        falcon.add_route("/v1/nodes", injector.get(NodeCollection))
