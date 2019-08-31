import falcon
from injector_provider.providers import InjectorProvider
from graphx.configurations.app import settings
from graphx.configurations.app.middlewares import RequireJSON
from falcon_marshmallow import Marshmallow
from registry.services import Container, Registry

app = falcon.API(middleware=[
    RequireJSON(),
    Marshmallow()
])

container = Container()

container.set(settings.Props.DI_PROVIDER, InjectorProvider())
container.set(settings.Props.FALCON, app)

service_registry = Registry()

for service in settings.services:
    service_registry.register(service)

service_registry.boot(container)
