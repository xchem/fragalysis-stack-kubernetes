#################
Stack Replication
#################

AWX Jobs (that create Kubernetes **CronJobs** and **Jobs**) are used to perform regular
Database and Media backups to an NFS volume to allow the material to be
replicated between stacks either on the Production or Development cluster.

- The Production cluster is home to the **Staging** and **Production** stacks
- The Development cluster is home to stacks controlled by individual developers
- An NFS provisioner takes care of PVC allocations for use within each cluster
- NFS volumes are created to allow files to be shared between the clusters

***********
Replication
***********

Replication of a stack relies on a database dump and copy of media files.
This is performed every day at 02:04 UTC.

- The **database** backup is driven by the ``postgres-replicator-backup`` **CronJob**
  in the ``production-stack`` namespace.
- The **media** backup is driven by the ``media-replicator`` **CronJob**
  in the ``production-stack`` namespace.

Details
=======

The **Production** PostgreSQL backup relies on a ``/backup`` volume used by
the corresponding ``postgres-back-hourly`` **CronJob**. The volume will
have an ``/hourly`` directory where you will find hourly backups (for the last
24 hours) in compressed backup files in the ``/hourly``directory.
A typical file wil be named ``/backup-2022-11-28T08:51:08Z-dumpall.sql.gz``.

The backup size is about 3.3GiB (Nov 2023).

Backups are created from within the CronJob using a ``pg_dump`` of the **frag**
database, which is written to a pre-provisioned volume on the NFS server
(``/nfs/kubernetes-db-replica``).

Database credentials can be found in the ``database`` **Secret**
in the ``production-stack`` **Namespace**. You'll find the ``root_password``
(for the built-in postgres user) and a ``user_password`` (for the the
fraglaysis user). There is a ``frag`` database with all privileges granted to
the ``fragalysis`` user.

Media content is backed up by the ``media-replicator`` **CronJob**. The files
are written to another pre-provisioned volume on the NFS server
(``/nfs/kubernetes-media-replica``).
