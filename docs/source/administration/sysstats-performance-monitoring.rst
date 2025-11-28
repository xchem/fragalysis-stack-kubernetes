#################################
Performance Monitoring (sysstats)
#################################

**********
Collection
**********

For clusters where the linux `sysstats`_ monitoring tool is available you can run
our playbook to collect daily machine statistics and write them to an S3 bucket and path.

The playbook uses the standard tool ``sadf`` to generate raw statistics, which are
then written to a ``.csv`` file.

Wew collect **CPU** and **Memory** statistics. To simplify post-processing the columns
in the files are separated by the TAB character. New values are available based on
an *interval*, which is set when ``sysstats`` is installed, typically 10 minutes.

``sysstats`` is installed and configured by default on our cluster hardware.
The ``.csv`` created by the playbook are kept on S3 until removed
(currently a manual process).

For CPU stats ``sadf`` generates a number of values at each time interval in the file::

    nw-xch-prod-xchem-2404-etcd-y3	133	2025-11-19 23:58:26 UTC	all	%user	2.33
    nw-xch-prod-xchem-2404-etcd-y3	133	2025-11-19 23:58:26 UTC	all	%nice	0.02
    nw-xch-prod-xchem-2404-etcd-y3	133	2025-11-19 23:58:26 UTC	all	%system	2.11
    nw-xch-prod-xchem-2404-etcd-y3	133	2025-11-19 23:58:26 UTC	all	%iowait	0.22
    nw-xch-prod-xchem-2404-etcd-y3	133	2025-11-19 23:58:26 UTC	all	%steal	0.15
    nw-xch-prod-xchem-2404-etcd-y3	133	2025-11-19 23:58:26 UTC	all	%idle	95.17

A number of values For **Memory** are also generated::

    nw-xch-prod-xchem-2404-etcd-y3	133	2025-11-19 23:58:26 UTC	-	kbmemfree	1186804
    nw-xch-prod-xchem-2404-etcd-y3	133	2025-11-19 23:58:26 UTC	-	kbavail	6711360
    nw-xch-prod-xchem-2404-etcd-y3	133	2025-11-19 23:58:26 UTC	-	kbmemused	905168
    nw-xch-prod-xchem-2404-etcd-y3	133	2025-11-19 23:58:26 UTC	-	%memused	11.14
    nw-xch-prod-xchem-2404-etcd-y3	133	2025-11-19 23:58:26 UTC	-	kbbuffers	378148
    nw-xch-prod-xchem-2404-etcd-y3	133	2025-11-19 23:58:26 UTC	-	kbcached	4528596
    nw-xch-prod-xchem-2404-etcd-y3	133	2025-11-19 23:58:26 UTC	-	kbcommit	3476356
    nw-xch-prod-xchem-2404-etcd-y3	133	2025-11-19 23:58:26 UTC	-	%commit	42.77
    nw-xch-prod-xchem-2404-etcd-y3	133	2025-11-19 23:58:26 UTC	-	kbactive	3458768
    nw-xch-prod-xchem-2404-etcd-y3	133	2025-11-19 23:58:26 UTC	-	kbinact	2217484
    nw-xch-prod-xchem-2404-etcd-y3	133	2025-11-19 23:58:26 UTC	-	kbdirty	240

Columns are: -

-   Machine name
-   Interval (seconds)
-   Data and time
-   ``all`` for CPU and ``-`` for Memory
-   Statistic name
-   Statistic value

The playbook and its corresponding **Schedule** in AWX creates ``.csv`` files with a
name that's ``[vm]-cpu-[YYYY-MM-DD].csv`` for CPU stats, and ``[vm]-mem-[YYYY-MM-DD].csv``
for memory stats. e.g.::

    nw-xch-prod-xchem-2404-etcd-y3-mem-2025-11-19.csv
    nw-xch-prod-xchem-2404-etcd-y3-cpu-2025-11-19.csv

Worker machines, where our Pods run, will have the word ``app`` or ``worker`` in the
``[VM]`` section of the filename.

All VMs in the **dummy**, **dev**, and **prod** clusters are *scraped* for statistics
at 5am each day, where the the previous day's stats are collected.

The statistics files can be found in the `sysstats` bucket path.

*******
Summary
*******

A second playbook, which runs shortly after the collection of raw statistics,
takes the previous day's files and generates a summary that consists of: -

-   Average non-idle VCPU cores used
-   Maximum non-idle VCPU cores used
-   Total VCPU cores available
-   Maximum memory consumed
-   Total memory available

The total VCPU cores and memory is the sum of all cores and memory on each
machine in the summary.

The playbook and its corresponding **Schedule** in AWX creates a ``summary.csv`` file
that contains a header line and then a line for each day that has been processed::

    Date, nproc (avg), nproc (peak), nproc (total), mem (MB peak), mem (MB total)
    2025-11-20, 16.7, 28.1, 392, 562793, 2624644
    2025-11-21, 16.6, 25.0, 392, 555470, 2624644
    2025-11-22, 16.6, 25.2, 392, 552781, 2624644
    2025-11-23, 16.6, 24.9, 392, 559744, 2624644
    2025-11-24, 16.7, 33.1, 392, 579070, 2624644
    2025-11-25, 17.1, 29.4, 392, 566701, 2624644
    2025-11-26, 17.3, 29.0, 392, 567824, 2624644

*********
Playbooks
*********

The playbooks are located in the ``topology/playbooks`` directory of this repo.

The playbook that is Scheduled to run to collect the statistics
is ``generate-sadf-for-yesterday.yaml``, which is expected to write collected
results to S3.

The playbook that is Scheduled to run to summarise the statistics
is ``summarise-collected-sadf.yaml``. It updates the ``sysstats/summary.csv`` file.

**********************
Displaying the summary
**********************

If you have credentials you can display the ``summary.csv`` file with ``rclone``.
For example, from the bastion::

    export AWS_ACCESS_KEY_ID=00000000
    export AWS_SECRET_ACCESS_KEY=00000000
    rclone cat dls-echo:/sysstats/summary.csv

Playbook variables
==================

The following variables (and environment variables) need to be provided to run the
*yesterday* playbook. Ansible variables unless otherwise stated: -

-   ``s3_bucket``
-   ``s3_url``
-   ``AWS_ACCESS_KEY_ID`` (Environment variable)
-   ``AWS_SECRET_ACCESS_KEY`` (Environment variable)

These variables are provided by the **Job Template** configured in AWX.

Inventory
=========

The playbooks rely on an Ansible *inventory* to identify the machines (VMs) that
form the clusters. The inventory is imported as an *inventory source* in AWX
(the inventory in AWX is called **Clusters**).

The inventory (a YAML file) can be found in this repository::

    ``topology/inventory.yaml``

If you add ro remove nodes in any of the clusters you **MUST** update this
topology file (re-tag the repository) and *synchronise* the AWX **Clusters**
*inventory source* so that AWX can operate on the new machines.

***
AWX
***

You will find two items in the AWX server: an **Inventory** and a **Hob Template**.

Inventory
=========

The **Clusters** *Inventory* on AWX has a *Source* that is this repository's *Project*
with the *Inventory File* set to ``topology/inventory.yaml``.

.. warning::
    If changes are made to the inventory you **MUST** *Sync* the AWX *Inventory*
    so that the playbooks can collect statistics for the correct machines.

Job Templates
=============

The **Collect cluster sysstats (sadf)** *Job Template* on AWX uses the playbooks in
this repo, providing suitable credentials and variables. It has a *Schedule* that
ensures it is run at 05:00 (UTC) every day.

The **Summarise cluster sysstats (sadf)** *Job Template* on AWX has a *Schedule* that
ensures it is run at 05:15 (UTC) every day.

.. _sysstats: https://en.wikipedia.org/wiki/Sysstat
