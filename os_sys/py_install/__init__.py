from . import make_install_files as _builder
from . import install as _ins
__all__ = ['builder', 'installer']
builder = _builder
installer = _ins.install
def install_exe():
    installer(input('path to install files:\n'))
