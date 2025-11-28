############################
Ad hoc maintenance (Ansible)
############################

From a suitable machine that shares the cluster network the inventory in this
repository's ``topology`` directory allows you to run `ad hoc`_ commands against
any number of machines.

In the following examples, ansible commands are run on the bastion, from the
clone of this repository in ``~/git/fragalysis-stack-kubernetes/topology``.

As a simple example, to reboot the NFS server you could run::

    ansible nfs -a "/sbin/reboot"

By default ad-hoc commands use the ansible `command`_ module, but you can specify
any module on the command-line. Here we switch to using the ``shell`` module::

    ansible nfs -m ansible.builtin.shell -a 'echo $TERM'

The inventory file contains references to the SSH keys used to access each machine
named in the inventory.

Familiarise yourself with the inventory file (``topology/inventory.yaml``),
especially its groups. You should find every machine in one group or another.
At the time of writing the following groups are named in the inventory: -

-   **rke** (the Rancher docker machine)
-   **nfs** (the NFS server, shared with all clusters)
-   **xch_dummy** (machines that form the 'dummy' cluster)
-   **xch_dev** (machines that form the 'development' cluster)
-   **xch_prod** (machines that form the 'production' cluster)

Additionally you will find groups for each of the cluster's ``ctrl``, ``etcd``,
and ``worker`` nodes.

The following command will update the package cache (equivalent to ``apt update``) and
upgrade all packages to their latest version (equivalent to ``apt upgrade``) for all the
machines in the inventory::

    ansible all -m ansible.builtin.apt -a "update_cache=yes upgrade=dist" --become

.. note::
    Please remember to keep the ``inventory.yaml`` file up tto date with the machines
    you want to maintain. If the inventory is changed, and you are collecting
    ``sysstats`` information you may also need to resynchronise the inventory on AWX.

.. _ad hoc: https://docs.ansible.com/projects/ansible/latest/command_guide/intro_adhoc.html
.. _command: https://docs.ansible.com/projects/ansible/latest/collections/ansible/builtin/command_module.html
0