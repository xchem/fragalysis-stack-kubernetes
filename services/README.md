# Services
A series of 'systemd' services and launch scripts, used primarily for the execution
of automated (Ansible) tasks (within a pre-configured Python virtual environment)

You will probably need to adjust the service files to match your own environment
(especially any `Environment`, `ExecStart`, and `WorkingDirectory` directives).

## Running ansible from a virtual environment as a service
The assumption is that you have installed a virtual environment on the control machine.
From the environment install the project services requirements, which may differ
from the main project requirements:-

    pip install -r services-requirements.txt

With this done you now simply need to run ansible using Python from the virtual environment.
Running ansible is a little more involved and so each service comes with a Python script
to simplify things, which is what the various `.service` files use.

## Installing services
Firstly, edit the specific service file to match your needs and then install it.
Then, as an example, you can install the the `check-applications` service with the
following sequence of commands (assuming you're in the project root): -

    SERVICE=check-applications

    sudo cp services/${SERVICE}.service /lib/systemd/system
    sudo chmod 644 /lib/systemd/system/${SERVICE}.service
    sudo systemctl daemon-reload
    sudo systemctl enable ${SERVICE}
    sudo systemctl start ${SERVICE}

You can inspect the status of the service with: -

    systemctl status ${SERVICE}

And inspect any detailed logs (for services where their StandardOutput is not null)
with: -

    sudo journalctl -u ${SERVICE} -f
