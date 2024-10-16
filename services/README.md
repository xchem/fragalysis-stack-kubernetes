# Services
A series of 'systemd' services and launch scripts, used primarily for the execution
of automated (Ansible) tasks (within a pre-configured Python virtual environment)

You will need to adjsut the service files to match your own environment
(especially any `ExecStart` or `WorkingDirectory` directives).

## Running ansible from a venv as a service
The assumption is that you have installed a virtual environment on the control machine.
From the environment install the project requirements (you may need to use sudo):-

    sudo pip install -r requirements.txt

With this done you now simply need to run the Python from the virtual environment
to pickup your required packages. Running ansible is a little more involved
and so each service comes with a Python script to simplify things, which what the
various `.service` files do.
