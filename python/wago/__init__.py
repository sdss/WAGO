# encoding: utf-8

from sdsstools import get_logger, get_package_version

# pip package name
NAME = 'sdss-wago'


log = get_logger(NAME)
log.removeHandler(log.sh)
log.sh = None


# package name should be pip package name
__version__ = get_package_version(path=__file__,
                                  package_name=NAME,
                                  pep_440=True)


from .wago import *
