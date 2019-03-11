import os
__all__ = ['find_packages', 'setup']
def all_dict(dictory, ex=False, exceptions=None, file_types=None, maps=True, files=False, print_data=False):
    import os
    data = []
    string_data = ''
    e = exceptions
    if 'list' in str(type(e)) or e == None:
        pass
    else:
        raise TypeError('expected a list but got a %s' % type(e))
    e = file_types
    if 'list' in str(type(e)) or e == None:
        pass
    else:
        raise TypeError('expected a list but got a %s' % type(e))
    
    print_ = True if print_data == 'print' or print or True else False
    
    for dirname, dirnames, filenames in os.walk(dictory):
        # print path to all subdirectories first.
        if maps:
            for subdirname in dirnames:
                dat = os.path.join(dirname, subdirname)
                data.append(dat)
                string_data = string_data + '\n' + dat
                if print_:
                    print(dat)

        # print path to all filenames.
        if files:
            for filename in filenames:
                s = False
                fname_path = filename
                file = fname_path.split('.')
                no = int(len(file) - 1)
                file_type = file[no]
                if not e == None:
                    for b in range(0, len(e)):
                        if e[b] == file_type:
                            s = True
                            
                if e == None:
                    s = True
                if s:
                    s = False   
                            
                    dat = os.path.join(dirname, filename)
                    data.append(dat)
                    string_data = string_data + '\n' + dat
                    if print_:
                        
                        print(dat)
        
        

        # Advanced usage:
        # editing the 'dirnames' list will stop os.walk() from recursing into there.
        if not exceptions == None:
            
            for ip in range(0, int(len(exceptions))):
                exception = exceptions[ip]
                
                if exception in dirnames:
                    # don't go into any .git directories.
                    dirnames.remove(exception)
                elif exception in filename and data:
                    data.remove(exception)
        if len(dirnames) == 1 and ex:
            break
    
    return [data, string_data]

def find_packages(path):
    package = all_dict(path, True, None, None, maps=False, files=True)[0]
    return package
def return_file_data(packages, path):
    mystr = ''
    for i in range(0, len(packages)):
        with open(packages[i]) as fh:
            e = fh.read()
            mystr = mystr + '##########' + str(packages[i]).replace(path, '') + '>>>>>>>>>>>>>>>' + str(e).replace('\\n', '\n')
    return mystr
def write_info(path, data):
    file = os.path.join(path, str(data['name'] + '.info'))
    w = open(file, 'w+')
    for i in range(0, len(data)):
        w.write(list(data)[i] + '=' + str(data[list(data)[i]]) + '\n')
    w.close()
def write_packages(data, name, path, rpath):
    import random
    lijst = list()
    data = data.replace(rpath, str(name + '\\'))
    for i in range(random.randint(10, 50)):
        lijst.append(str(random.randint(0, 9)))
                     
    file = os.path.join(path, str(name + '-'.join(lijst) + '.py_install'))
    with open(file, 'w+') as fh:
        fh.write(str(data))
def write_packages_data(data, name, path, rpath):
    import random
    lijst = list()
    data = data.replace(rpath, str(name + '\\'))
    for i in range(random.randint(10, 50)):
        lijst.append(random.randint(0, 9))
                     
    file = os.path.join(path + str(name + '-'.join(lijst) + '.py_data'))
    with open(file, 'w+', encoding='utf-8') as fh:
        fh.write(str(data))
    return
def setup(**args):
    import sys
    print(args)
    class argumentError(Exception):
        'item error'
    
    try:
        print(args['name'])
        print(args['version'])
        print(args['path'])
        print(args['packages'])
    except Exception as ex:
        print('you need to have at least path, packages and version in setup', file=sys.stderr)
        raise ArgumentError('error you have not typed one or more of the requerd arguments') from ex
    path = os.path.join(args['path'], str('dist-version-' + str(args['version'])))
    print(path)
    file_data = return_file_data(args['packages'], path)
    try:
        os.makedirs(path)
    except:
        pass
    try:
        args['package_data']
    except:
        pass
    else:
        write_packages_data(return_file_data(all_dict(path), True, None, None, False, True)[0], args['name'], path=path, rpath=args['path'])
    write_packages(data=file_data, name=args['name'], rpath=args['path'], path=path)
    write_info(data=args, path=path)
    print('the packages are placed in %s:\n\
this is a path to where your install and data files are placed files' % path)
    

    
    
