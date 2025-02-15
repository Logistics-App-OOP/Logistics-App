
from core.application_data import Application_data
from core.command_factory import CommandFactory
from core.engine import Engine

app_data = Application_data()
cmd_factory = CommandFactory(app_data)
engine = Engine(cmd_factory)

engine.start()


# registeremployee Uasim1702 Uasim Halak 123456789 Manager
# login Uasim1702 123456789
# createpackage IvanIvanov 0404040404 Sydney Melbourne 45
# createpackage IvanGeorgiev 0402020202 Sydney Perth 45
# createroute 2025-02-11T14:30 Sydney Perth 
# createroute 2025-02-11T14:30 Sydney Melbourne AliceSprings
# createroute 2025-02-11T14:30 Adelaide Melbourne
# createroute 2025-02-11T14:30 Adelaide Melbourne Sydney
# createroute 2025-02-16T10:00 Sydney Melbourne Perth Adelaide Brisbane Darwin
# createroute 2025-02-14T23:00 Sydney Melbourne Adelaide Perth
# assigntrucktoroute 1
# assigntrucktoroute 2
# assignpackagetoroute 1 1
# assignpackagetoroute 1 2
# viewroutes
# viewpackages
# viewtrucks
# findroutes Sydney Melbourne
# findroutes Perth Sydney
# findpackage 2
