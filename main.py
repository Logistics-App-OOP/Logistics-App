
from core.application_data import Application_data
from core.command_factory import CommandFactory
from core.engine import Engine

app_data = Application_data()
cmd_factory = CommandFactory(app_data)
engine = Engine(cmd_factory)

engine.start()

# createroute 2025-02-11T14:30 Sydney Melbourne Perth
# registeremployee Uasim1702 Uasim Halak 123456789 Manager