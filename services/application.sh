#!/bin/bash

# Run the 'site-check' playbook every 2 minutes
# using the 'expected' Ptyhon virtual environment.
while true; do
    sleep 120
    ${INSTALLATION_DIR}/venv/bin/python ansible-playbook site-check-applications.yaml ----vault-password-file vault-pass-services.txt
done
