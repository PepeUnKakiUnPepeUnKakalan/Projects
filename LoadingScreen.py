from ChristopherColumbus import *
import sys
import platform
def loading(bool):
  if bool == "t":
    timbur("Running python...")
    timbur("Current version of Python is...")
    ahh(3)
    timbur(sys.version)
    ahh(1)
    timbur(platform.python_version())
    ahh(.5)
    timbur("running python code...")
    ahh(1)
    clear()
  else:
    timbur("Skipping loading screen...")
    ahh(1)
    clear()