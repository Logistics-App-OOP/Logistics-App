from core.application_data import Application_data
from core.command_factory import CommandFactory
from core.engine import Engine

app_data = Application_data()
cmd_factory = CommandFactory(app_data)
engine = Engine(cmd_factory)
engine.start()
app_data.save_data()


#registeremployee Uasim1702 Uasim Halak 123456789 Manager  !(We already have it)
# registeremployee JohnDoe John Doe 987654321 Normal
# registeremployee AliceSmith Alice Smith 456123789 Manager
# login Uasim1702 123456789
# login JohnDoe 987654321
# login AliceSmith 456123789
# createpackage PeterParker 0411223344 Melbourne Brisbane 30
# createpackage MaryJane 0400112233 Perth Darwin 55
# createpackage TonyStark 0433221100 Adelaide Sydney 70
# createpackage SteveRogers 0455667788 Sydney Perth 90
# createpackage NatashaRomanoff 0499887766 Brisbane AliceSprings 40
# createpackage SteveRogers 0455667788 Sydney Adelaide 90
# createroute 2025-02-20-09:00 Sydney Melbourne Adelaide
# createroute 2025-02-21-12:45 Brisbane Perth
# createroute 2025-02-22-06:30 Darwin AliceSprings Sydney
# createroute 2025-02-23-15:10 Adelaide Melbourne Sydney Brisbane
# createroute 2025-02-19-08:00 Perth Melbourne Sydney Brisbane AliceSprings Darwin
# assigntrucktoroute 3
# assigntrucktoroute 4
# assigntrucktoroute 5
# assigntrucktoroute 1
# assignpackagetoroute 3 3
# assignpackagetoroute 4 4
# assignpackagetoroute 5 5
# assignpackagetoroute 2 3
# assignpackagetoroute 1 4
# assignpackagetoroute 6 1
# findroutes Melbourne Brisbane
# findroutes Darwin Sydney
# findroutes Adelaide Sydney
# findroutes Perth AliceSprings
# findpackage 1
# findpackage 2
# findpackage 5
# findpackage 7
# createpackage IvanIvanov 0404040404 Sydney Melbourne 45
# createpackage IvanGeorgiev 0402020202 Sydney Perth 45
# createroute 2025-02-16-14:30 Sydney Perth 
# createroute 2025-02-16-14:30 Sydney Melbourne AliceSprings
# createroute 2025-02-16-14:30 Adelaide Melbourne
# createroute 2025-02-16-14:30 Adelaide Melbourne Sydney
# createroute 2025-02-16-10:00 Sydney Melbourne Perth Adelaide Brisbane Darwin
# createroute 2025-02-16-17:00 Sydney Melbourne Adelaide Perth
# assigntrucktoroute 1
# assigntrucktoroute 2
# assignpackagetoroute 1 1
# assignpackagetoroute 1 2
# findroutes Sydney Melbourne
# findroutes Perth Sydney
# findpackage 2
# findpackage 3
# assigntrucktoroute 6
# assignpackagetoroute 1 6
# viewroutes
# viewpackages
# viewtrucks