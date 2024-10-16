#!/usr/bin/env python

import subprocess
import sys
import time

_PERIOD_MINUTES = 2
if len(sys.argv) > 1:
    _PERIOD_MINUTES = int(sys.argv[1])

_CMD = [
    "ansible-playbook",
    "site-check-applications.yaml",
    "--vault-password-file",
    "vault-pass-services.txt"
]

while True:
    result = subprocess.run(_CMD, check=True)
    if result.returncode != 0:
        sys.exit(1)
    time.sleep(_PERIOD_MINUTES * 60)
