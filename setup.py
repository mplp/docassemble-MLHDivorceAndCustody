import os
import sys
from setuptools import setup, find_namespace_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')

def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.MLHDivorceAndCustody',
      version='1.1.0',
      description=('Michigan divorce and child support tools'),
      long_description='# docassemble.MLHDivorceAndCustody\r\n\r\nMichigan divorce and custody tools\r\n\r\n## Authors:\r\nMichigan Legal Help\r\nLemma Legal\r\n\r\n## Changelog:\r\n* 4/30/26  1.1.0 multiple changes to wording and order of questions; fix some bugs; add testable but incomplete divorce answer\r\n* 4/10/26  1.0.3 fix small font on form; fix & standardize Ottawa case initiation form reference; fix child support calculator link; update title of tool\r\n* 4/6/26   1.0.2 patch Ottawa County court selection issue; fix minor code typos\r\n* 4/1/26   1.0.1 fix issue with children not displaying in complaint #7\r\n* 3/31/26  1.0.0 initial launch of divorce complaint and judgment of divorce tools',
      long_description_content_type='text/markdown',
      author='Michigan Legal Help',
      author_email='ekressmiller@lsscm.org',
      license='MIT',
      url='https://michiganlegalhelp.org/resources/divorce',
      packages=find_namespace_packages(),
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/MLHDivorceAndCustody/', package='docassemble.MLHDivorceAndCustody'),
     )
