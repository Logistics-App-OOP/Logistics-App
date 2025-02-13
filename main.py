
from core.application_data import Application_data
from core.command_factory import CommandFactory
from core.engine import Engine

app_data = Application_data()
cmd_factory = CommandFactory(app_data)
engine = Engine(cmd_factory)

engine.start()

# createroute 2025-02-11T14:30 Sydney Perth 
# createroute 2025-02-11T14:30 Sydney Melbourne
# createroute 2025-02-11T14:30 Adelaide Melbourne
# createroute 2025-02-11T14:30 Adelaide Melbourne Sydney
# registeremployee Uasim1702 Uasim Halak 123456789 Manager
# login Uasim1702 123456789