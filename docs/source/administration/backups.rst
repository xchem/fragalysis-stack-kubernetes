#######
Backups
#######

Here, we describe the data and file backups that are kept to enable recovery of the
installation. In order to provide sufficient material to accomplish a complet recovery
of the installation we keep copies of the following: -

1.  The **rancher server**. A docker-based service running in a asmake RKE cluster
2.  The production and development cluster _infrastructure_ **database**,
    used by Keycloak for authentication and AWX, the ansible playbook server
3.  The production stack **database**
4.  The production stack **media** files

**************
Rancher Server
**************

This service is responsible for managing the cluster VMs and provides kubectl/k9s/lens
access to the clusters. Backup is relatively complex and is currently a manual
operation that requires the server to be stopped. We could invest time in an
automated backup but this would have to be one that can detect errors and alert a
human operator. Probably a day or two to develop.

-   **Backup process**: Manual
-   **Backup schedule**: We recommend a manual backup is taken on Fridays
    at the end of the day (prior to a Sunday-night/Monday-morning fs-trim issue)
-   **Backup location**: STFC S3 Echo bucket (``/nw-rancher``)

*************************************
Infrastructure Database (Development)
*************************************

This database manages Fragalysis & Squonk2 application logins in the development cluster,
providing federated access to CAS.

-   **Backup process**: This is handled by a **CronJob** container
    using the ``informaticsmatters/sql-backup`` conatiner image. As the server hosts
    mutiple databasee it uses the ``pg_dumpall`` utility to dump the server contents
    to a backup volume (in the cluster) and ``rclone`` to copy this off cluster to
    an S3 bucket
-   **Backup schedule**: Every day at 03:07, keeping 28 copies
-   **Backup location**: STFC S3 Echo bucket (``/im-infra-backup``)

************************************
Infrastructure Database (Production)
************************************

This database manages Fragalysis & Squonk2 application logins for the production cluster,
providing federated access to CAS. It is also used by the AWX ansible playbook server.

-   **Backup process**: This is handled by a **CronJob** container
    using the ``informaticsmatters/sql-backup`` conatiner image. As the server hosts
    mutiple databasee it uses the ``pg_dumpall`` utility to dump the server contents
    to a backup volume (in the cluster) and ``rclone`` to copy this off cluster to
    an S3 bucket
-   **Backup schedule**: Every day at 03:07, keeping 28 copies
-   **Backup location**: STFC S3 Echo bucket (``/im-infra-production-backup``)

*************************
Production Stack Database
*************************

This database is the Fragalysis django application database.

-   **Backup process**: This is handled by a **CronJob** container
    using the ``informaticsmatters/sql-backup`` container image. This backup
    only consists of the **frag** database, collected using the ``pg_dump``
    utility to dump the server contents to a backup volume (in the cluster) and
    ``rclone`` to copy this off cluster to an S3 bucket
-   **Backup schedule** Every hour, keeping 24 copies
-   **Backup location**: STFC S3 Echo bucket (``/nw-xch-prod-v2-production-stack-backup``)

**********************
Production Stack Media
**********************
The production Fragalysis media directory, consisting of about 135,000 individula files
consuming about 240GiB of disk space (September 2025).

-   **Backup process**: This is handled by a **CronJob** container
    using the ``/informaticsmatters/volume-replicator`` container image.
    The container uses ``rsync`` to synchronise data to an NFS volume
    and ``rclone`` to copy the data off the cluster to an S3 bucket
-   **Backup schedule**: Every day at 04:04, only the latest copy is kept
-   **Backup location**: STFC S3 Echo bucket (``/fragalysis-stack-production-media``)
