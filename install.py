import os
import subprocess
os.chdir("/opt/mycroft/skills/lifx-skill/lifx-python/")
subprocess.call(['python', '/opt/mycroft/skills/lifx-skill/lifx-python/setup.py', 'install'])
