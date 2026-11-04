A collection of Ansible **Roles** responsible for the deployment of numerous
applications, which primarily includes the "Fragalysis Stack".

## Policies
- Test code is not expected here (it is very old code)
- Playbook `site-` files in the project root drive each role
- Roles are in the `roles` directory
- The Fragalysis stack role is `fragalysis-stack`

Other useful **Roles** include: -

- `media-replicator`
- `ta-authenticator`
- `database-replicator`

Directories that aren't obviously related to Ansible should be consider "unreliable".
Why? This project started with the ability to deploy NFS, Rancher, and run investigative
tooling, and many of these features and services are no longer in use.

## Site file naming convention
The site file naming convention is `site-<role>[-<task>].yaml`. So, to deploy the
stack one runs the `site-fragalysis-stack.yaml`. To execute the `update` tasks
in the Stacks' **Role** you'd run `site-fragalysis-stack-update.yaml`.
