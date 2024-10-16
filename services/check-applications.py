#!python

import os
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

if not os.path.exists("vault-pass-services.txt"):
    print("You must provide a vault-pass-services.txt file")
    sys.exit(1)

while True:
    result = subprocess.run(_CMD, check=True)
    if result.returncode != 0:
        sys.exit(2)
    time.sleep(_PERIOD_MINUTES * 60)
