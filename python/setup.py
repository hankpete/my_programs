from distutils.core import setup
import py2exe

# setup(windows = [{'script': "go_to_bed.pyw"}],
#         zipfile = None,
#         options = {'py2exe': {'bundle_files': 1, 'compressed': True},
#                     "dll_excludes": ["tcl85.dll", "tk85.dll"]})

# setup(console=['go_to_bed.pyw'],
#     options = {"dll_excludes": {"tcl85.dll", "tk85.dll"}}
#     )

setup(console=['bed2.pyw'])
