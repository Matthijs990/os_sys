import sys
data = str(sys.version).split(' ')
class VersionError(Exception):
    'not the right python version'
int_data = str(data[0]).split('.')
if int(int_data[0]) >= 3 and int(int_data[1]) >= 0:
    pass
else:
    raise VersionError('you need python3 or newer')



class AError(Exception):
    'a exception was found'
class PingTimeoutError(Exception):
    'timeout'
class Woops_It_Looks_Like_That_Someting_Wents_Wrong_Error(Exception):
    'somting wents wrong'
class Wifi_Error(Exception):
    'a wifi error is found'
import sys
class file():
    None
def print_warn(*args):
    lijst = list(args)
    try:
        values = dict(first=lijst[0],
                      file=lijst[1],
                      problem=lijst[2],
                      becuse=lijst[3],
                      solution=lijst[4],
                      msg=lijst[5],
                      )
    except Exception:
        values = dict(first=lijst[0],
                      file=lijst[1],
                      problem=lijst[2],
                      becuse='something is wrong',
                      solution=lijst[3],
                      msg=lijst[4],
                      )
    f = sys.stderr
    d = file
    print('warning!(from the fail module):', file=f)
    print('  %(first)s(most recent call):' % values, file=f)
    print('     where this warning is form %(file)s:' % values, file=f)
    print('       the problem is %(problem)s:' % values, file=f)
    print('         becuse %(becuse)s:' % values, file=f)
    print('           the solution may be %(solution)s:' % values, file=f)
    print('warning: %(msg)s' % values, file=f)


