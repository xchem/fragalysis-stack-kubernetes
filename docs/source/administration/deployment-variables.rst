####################
Deployment Variables
####################

The stack is deployed using AWX and Ansible **Job Templates** that use
playbooks (**Roles**) in the `Fragalysis Stack Kubernetes`_ **Project**.
The stack, and its related components (volumes, services, secrets) are all controlled
by Ansible variables exposed in the playbooks. Many Ansible variables are used to set
Pod (Container) environment variables.

************************
The Stack Ansible 'Role'
************************

The role for the stack can be found in the Fragalysis Stack Kubernetes
repository under `roles/fragalysis-stack`. There you will find a number of
playbooks including the main stack playbook `site-fragalysis-stack.yaml`

************************
Role Variables (default)
************************

The role variables in `roles/fragalysis-stack/default/main.yaml` are considered
the *important* set of variables a user is expected to define. The vast majority
have sensible defaults and almost all are documented or their values should obvious.

Users are expected to review this file and set variables in their Job Templates to
satisfy their requirements.

*********************
Role Variables (vars)
*********************

The role variables in `roles/fragalysis-stack/vars/main.yaml` are considered
the *less important* set of variables where sensible defaults have been set and where
user-defined values are not normally required.

Users should still review this file to understand the less common variables in order
to decide whether they need to be changed to satisfy their requirements.

The `vars` variables are typically used for things like CPU, Memory, and image names,
which rarely need to be changed.

.. _Fragalysis Stack Kubernetes: https://github.com/xchem/fragalysis-stack-kubernetes
