#!/usr/bin/env python
#
# Run with: -
#  python check-nodes.py [period_minutes]

import os
import subprocess
import sys
import time

# The command(s) to run the playbook...
_DEV_CMD = [
    "ansible-playbook",
    "site-check-nodes.yaml",
    "--vault-password-file",
    "vault-pass-services.txt",
    "--extra-vars",
    "cluster=dev",
]

_PROD_CMD = [
    "ansible-playbook",
    "site-check-nodes.yaml",
    "--vault-password-file",
    "vault-pass-services.txt",
    "--extra-vars",
    "cluster=prod",
]

# Default period between playbook runs...
# (which can be changed by providing a numeric (greater than 5) command line argument)
_PERIOD_MINUTES = 5
if len(sys.argv) > 1:
    _PERIOD_MINUTES = int(sys.argv[1])
_PERIOD_MINUTES = max(_PERIOD_MINUTES, 5)

# For this playbook we need a vault password file...
if not os.path.exists("vault-pass-services.txt"):
    print("You must provide a vault-pass-services.txt file")
    sys.exit(1)

# Go - continuously...
while True:
    print("+> Running the DEV playbook...")
    result = subprocess.run(_DEV_CMD, check=True)
    if result.returncode != 0:
        sys.exit(2)
    print("+> Running the PROD playbook...")
    result = subprocess.run(_PROD_CMD, check=True)
    if result.returncode != 0:
        sys.exit(2)
    print(f"+> Sleeping ({_PERIOD_MINUTES})...")
    time.sleep(_PERIOD_MINUTES * 60)
