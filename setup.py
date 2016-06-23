from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
    excludes=['_ssl',  # Exclude _ssl
                                    'pyreadline', 'difflib', 'doctest', 'locale',
                                    'optparse', 'pickle', 'calendar'],  # Exclude standard library
    dll_excludes=['msvcr71.dll'],  # Exclude msvcr71
    compressed=True,  # Compress library.zip
    options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
    windows = [{'script': "KeepMeAwake.py", "icon_resources": [(1, "KeepMeAwake.ico")]}],
    zipfile = None,
)