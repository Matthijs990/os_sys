#installer
#python3.7
#devlopment
import os, sys
__all__ = ['install']
def all_dict(dictory, ex=False, exceptions=None, file_types=['py_install'], maps=False, files=True, print_data=False):
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
def install(path):
    print('searching files...', file=sys.stderr)
    file = all_dict(path)[0][0]
    print('building...', file=sys.stderr)
    with open(file) as fh:
        mystr = str(fh.read())
    mystr = mystr.rsplit('##########')
    print('installing...', file=sys.stderr)
    for i in mystr:
        path, data = i.rsplit('>>>>>>>>>>>>>>>')
        print('prosessing file: %s...' % path, file=sys.stderr)
        data = str(data)
        from distutils.sysconfig import get_python_lib as gpl
        path2 = gpl()
        with open(os.path.join(path2, path), mode='w+') as kk:
            kk.write(str(data))
    print('done!', file=sys.stderr)
            
