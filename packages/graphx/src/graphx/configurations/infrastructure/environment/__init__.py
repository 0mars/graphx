import os

from registry.services import BootableService, Container


class EnvironmentService(BootableService):

    def boot(self, container: Container):
        from graphx.configurations.app.settings import Props

        container.set(Props.APP_URL, os.environ.get(Props.APP_URL.value))

        container.set(Props.NEO_URL, os.environ.get(Props.NEO_URL.value))
        container.set(Props.NEO_USERNAME, os.environ.get(Props.NEO_USERNAME.value))
        container.set(Props.NEO_PASSWORD, os.environ.get(Props.NEO_PASSWORD.value))

