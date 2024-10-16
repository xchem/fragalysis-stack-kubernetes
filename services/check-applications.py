#!/usr/bin/env python
#
# Run with: -
#  python check-applications.py [period_minutes]

import os
import subprocess
import sys
import time

# The command to run the playbook...
_CMD = [
    "ansible-playbook",
    "site-check-applications.yaml",
    "--vault-password-file",
    "vault-pass-services.txt"
]

# Default period between playbook runs...
_PERIOD_MINUTES = 2
if len(sys.argv) > 1:
    _PERIOD_MINUTES = int(sys.argv[1])

# For this playbook we need a vault password file...
if not os.path.exists("vault-pass-services.txt"):
    print("You must provide a vault-pass-services.txt file")
    sys.exit(1)

# Go - continuously...
while True:
    print("+> Running the playbook...")
    result = subprocess.run(_CMD, check=True)
    if result.returncode != 0:
        sys.exit(2)
    print(f"+> Sleeping ({_PERIOD_MINUTES} minutes)...")
    time.sleep(_PERIOD_MINUTES * 60)
