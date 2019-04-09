import os
try:
    user_paths = os.environ['PYTHONPATH'].split(os.pathsep)
except KeyError:
    user_paths = []

import sys
site_packages = next(p for p in sys.path if 'site-packages' in p)
print(site_packages)

