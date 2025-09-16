#############
Data Recovery
#############

In the event of data loss you will need to recostruct the missing components
(databases and files) using installation instrutions and backups. What follows
is a brief outline of steps to recover losts systems, based on what's been lost.
We outline the reovery of: -

1.  Production stack database
2.  Production stack media directory
3.  Infrastructure database (Development or Production)
4.  The Rancher server data

In all cases we assume that you have kubernetes clusters and the applications.
This section does not cover the creation of the underlying clusters
or the installation of the original applications. This section is simply about
restoring data to a pre-existing installation.

.. epigraph::

    You can read detailed documentation relating to the provisioning of a cluster,
    and installation of the key applications by referring to our
    :doc:`installation guide <../installation/index>`.

**************
Stack database
**************

A convenient ansible playbook that can be used to restore backed-up databases
can be found in the Informatics Matters `bandr-ansible`_ respository. From
a clone of the respository you should create a suitable Python environment
and install the required packages. With this done you should prepare
a suitable set of ``parameters.yaml`` variables to control the playbook.
Here is a set used recently (replace the values as appropriate)::

    recovery_image_tag: 15.7
    recovery_host: database
    recovery_database: frag
    recovery_database_secret: database
    recovery_database_admin_user: admin
    recovery_namespace: production-stack
    recovery_volume_pvc: recovery
    recovery_volume_size_g: 40
    recovery_volume_storageclass: csi-cinder-sc-delete
    recovery_volume_pvc_name: recovery
    recovery_sa: stack

    recovery_use_rclone_bucket_and_path: /nw-xch-prod-v2-production-stack-backup
    recovery_rclone_s3_endpoint: https://s3.echo.stfc.ac.uk
    recovery_rclone_s3_provider: Ceph

You then need to provide Kubernetes cluster credentials and bucket credentials
via a few key environment variables::

    export K8S_AUTH_HOST=https://????
    export K8S_AUTH_API_KEY=????
    export K8S_AUTH_VERIFY_SSL=false

    export AWS_ACCESS_KEY_ID=????
    export AWS_SECRET_ACCESS_KEY=????

And then run the recovery playbook::

    ansible-playbook site-recovery.yaml -e @parameters.yaml


Recovery of the ``frag`` database will only take a few minutes, with most of the
time consumed by the recovery process copying files from the backup bucket.

***********
Stack media
***********

This is most easily accomplished from within a shell in the Production stack **Pod**.
From there you should move to the Django media directory (``/code/media``).
You will need to install the Python ``awscli`` package and know the S3 credetnials
that give you access the bucket where the media files are kept::

    pip install awscli

    export AWS_ACCESS_KEY_ID=????
    export AWS_SECRET_ACCESS_KEY=????
    export AWS_DEFAULT_REGION=
    export AWS_ENDPOINT_URL_S3=https://s3.echo.stfc.ac.uk

    aws s3 cp --recursive s3://fragalysis-stack-production-media /code/media

Be prepared for the recovery of the media volume to take significant time.
With 240Gi of files to transfer (September 2025), at about 50-60MiB/s
expect recovery to take about an hour.

************************
Infrastructure databases
************************

As the infrastructure database server contains multiple databases we currently rely
on the `pg_dumpall` utility in order to get a complete copy of the server.
backups are performed every day, and are kept for a numebr of days,
perfomed by a **CronJob** operating ion the corresponding ``im-infra`` **Namespaces**.

Backups are located in an Echo S3 bucket: -

-   Development cluster: ``/im-infra-backup``
-   Prodcution cluster: ``/im-infra-production-backup``

Armed with the prevailing Postgress admin user and password, recovery can be
performed manually via a Pod shell or using an AWX playbook. We test recovery using
the ``site-recovery.yaml`` playbook (version **2024.1**) from our `bandr-ansible`_
respository.

**************
Rancher server
**************

Recovery of the Rancher server relies on manual backups that are kept on an S3
bucket (typically ``/nw-rancher``). You can follow the Rancher instructions for
recovery of data on a docker installation using their own instructions::

-   See `restore-docker-installed-rancher`_

.. _bandr-ansible: https://github.com/InformaticsMatters/bandr-ansible
.. _restore-docker-installed-rancher: https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/backup-restore-and-disaster-recovery/restore-docker-installed-rancher
