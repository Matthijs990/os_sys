import setuptools
import setuptools as s
try:
    import ready
except Exception:
    pass
def execute_from_command_line(argv=None):
    """Run a ManagementUtility."""
    utility = ManagementUtility(argv)
    utility.execute()

package_data = dict()

with open("README.md", "r") as fh:
    long_description = fh.read()
import sys
import os
def run_py_check():
    version = sys.version_info[:2]
    needing = (3, 3)
    da = ''.join(str(version[0]) + '.' + str(version[1]))

    data = dict(version=da,
                 needing=3.3)
    if version < needing:
        sys.stderr.write('\
    ==========================\n\
    Unsupported Python version\n\
    ==========================\n\
    This version of os_sys requires Python %(needing)s, but you\'re trying to\n\
    install it on Python %(version)s\n\
    \n\
    this is may be becuse you are using a version of pip that doesn\'t\n\
    understand the setup script. make shure you\n\
    have pip >= 9.0 and setuptools >= 40.0.0, then try again:\n\
    \n\
        python -m pip install --upgrade pip setuptools\n\
        python -m pip install os_sys\n\
    \nthis will install the latest version of os_sys\n\n\n' % data)
        class PythonVersionError(Exception):
            '''not right python version'''
            pass
        raise PythonVersionError('you need at least python 3.3')
from distutils.sysconfig import get_python_lib as gpl
with open('data_types.txt') as dem:
    raw_data_types = dem.read()
data_types = raw_data_types.split('/')
p = data_types
overlay_warning = False
def check():
    path = str(gpl()).join('os_sys')
    if os.path.isdir(path):
        print('\
========\n\
Warning!\n\
========\n\
you now installing os_sys on a mac, pc, laptop or something else where os_sys is al ready installd\n\
programs that use this lib while can give errors becuse you are not upgrading the lib on the right way\n\
if you want to upgrade this lib than you need to typ this on cmd:\n\
python -m pip install --upgrade os_sys', file=sys.stderr)
def run_after():
    if overlay_warning:
        sys.stderr.write('Warning: os_sys is al ready on your pc')
def all_dict():
    l = []
    for dirname, dirnames, filenames in os.walk('.'):
        # print path to all subdirectories first.
        for subdirname in dirnames:
            data = os.path.join(dirname, subdirname)
            if '__pycache__' in data:
                dirnames.remove('__pycache__')
            elif 'os_sys.egg-info' in data:
                dirnames.remove('os_sys.egg-info')
            elif 'build' in dirnames:
                dirnames.remove('build')
            elif 'dist' in dirnames:
                dirnames.remove('dist')
            elif 'docs' in dirnames:
                dirnames.remove('docs')
                
            else:
                data = data.replace('.\\', '')
                data = data.replace('\\', '.')
                l.append(data)
    return l

def run():
    run_py_check()
    check()
    run_after()
    return ''
re = os.path.abspath
def all_maps(d, plus=None):
    
    lijst = [os.path.join(d, f) for f in os.listdir(d)]
    ret = []
    num = 0
    while num < len(lijst):
        if '.' in lijst[num]:
            pass
        else:
            if plus == None:
                ret.append(lijst[num])
            else:
                ret.append(str(plus)+'|'+str(lijst[num]))
        num += 1
    return ret
lijst = all_dict()

lijst[0].join(str(run()))
num = 0
while num < len(lijst):
    
    to = num
    
    package_data.setdefault(lijst[to], []).extend(p)
    num += 1
lijst = all_maps(os.path.abspath('os_sys\commands'))
#als ik bij version er .dev achter zet dan is het een pre-releas

long_description = long_description.replace('evry', 'every')
setuptools.setup(
    name="os_sys",
    version="0.8.1",#.dev moet dan hier
    author="Matthijs labots",
    contact="python_libs",
    contact_email="py_libs@gmail.com",
    author_email="libs.python@gmail.com",
    description="a big lib with many usefull tools and it are not only os and sys tools...",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://python-libs-com.webnode.nl/",
    python_requires='>=3',
    entry_points={'console_scripts': [
        'os_sys-updater = os_sys.commands:update',
        'os_sys-download-setup_script = os_sys.commands:download_zip',
        'os_sys-if_not_work-write_new_scripts = os_sys.commands:init',
        'os_sys-admin = os_sys.commands:run',
        'os_sys-re_installer = os_sys.commands:re_install',
        'os_sys-run-py_check = os_sys.commands:run_py_check',
        'os_sys-admin-run = os_sys.commands:test',
        'os_sys-text-editor = os_sys.commands:make_text',
        
        
    ]},
    include_package_data=True,
    package_data=package_data,
    packages=list(package_data),
    install_requires=['progress', 'tqdm', 'progressbar', 'matplotlib', 'numpy',
                      'jupyter', 'pandas'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: IDLE',
        'Natural Language :: Dutch',
        'Natural Language :: English',
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python",
        'Topic :: Internet',
        'Topic :: Other/Nonlisted Topic',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering',

        ],
    project_urls={
        'all files': 'https://github.com/Matthijs990/os_sys',
        'Downloads': 'https://python-libs-com.webnode.nl/downloads/',
        'become a member': 'https://python-libs-com.webnode.nl/user-registration/',
        'download all files': 'https://github.com/Matthijs990/os_sys.git',
        'want to help': 'https://github.com/Matthijs990/os_sys/tree/master/do%20you%20want%20to%20help',
        'startpage': 'https://pypi.org/project/os-sys/',
        'made possible by': 'https://pypi.org',
        'help': 'https://github.com/Matthijs990/os_sys/issues',
        'github wiki(under development)': 'https://github.com/Matthijs990/os_sys/wiki',
        'just a chat to talk about python': 'https://github.com/Matthijs990/chat/issues/1',
        'github': 'https://github.com/Matthijs990/os_sys',
        'open os_sys wiki': 'https://python-libs-com.webnode.nl/open-os-sys-wiki/',
        'officail wiki(under development)': 'https://python-libs-com.webnode.nl/os-sys-wiki/',

    },
    
)


