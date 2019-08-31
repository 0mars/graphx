from graphx.configurations.infrastructure.db import DataBaseService
from graphx.configurations.infrastructure.environment import EnvironmentService
from graphx.configurations.infrastructure.logging import LoggingService
from graphx.entrypoints.rest.health.registry import HealthService
from graphx.entrypoints.rest.swagger.registry import SwaggerService
from registry.services import Props as BaseProps

services = [
    LoggingService(),
    EnvironmentService(),
    DataBaseService(),
    HealthService(),
    SwaggerService()
]


class Props(BaseProps):
    DI_PROVIDER = 0
    FALCON = 1

    APP_URL = 'APP_URL'

    NEO_URL = 'NEO_URL'
    NEO_USERNAME = 'NEO_USERNAME'
    NEO_PASSWORD = 'NEO_PASSWORD'
