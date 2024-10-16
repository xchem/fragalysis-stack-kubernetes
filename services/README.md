# Services
A series of 'systemd' services and launch scripts, used primarily for the execution
of automated (Ansible) tasks (within a pre-configured Python virtual environment)

You will need to adjust the service files to match your own environment
(especially any `Environment`, `ExecStart`, `User`, and `WorkingDirectory` directives).

## Running ansible from a venv as a service
The assumption is that you have installed a virtual environment on the control machine.
From the environment install the project requirements:-

    pip install -r services-requirements.txt

With this done you now simply need to run the Python from the virtual environment
to pickup your required packages. Running ansible is a little more involved
and so each service comes with a Python script to simplify things, which what the
various `.service` files do.

## Installing services
Edit the specific service file to match your needs and then install it. For example,
you can install the the `check-applications` service with the following sequence of
commands (assuming you're in the project root): -

    SERVICE=check-applications

    sudo cp services/${SERVICE}.service /lib/systemd/system
    sudo chmod 644 /lib/systemd/system/${SERVICE}.service
    sudo systemctl daemon-reload
    sudo systemctl enable ${SERVICE}
    sudo systemctl start ${SERVICE}

You can inspect the status of the service with: -

    systemctl status ${SERVICE}

And inspect detailed logs with: -

    sudo journalctl -u ${SERVICE}
