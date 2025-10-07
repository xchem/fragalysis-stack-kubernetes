############################
Off-cluster backup locations
############################

We use the following 'out-of-cluster' locations for backup storage: -

DLS/Echo
********

-   `discourse-backups` for discourse backups
-   `fragalysis-stack-production-media` for the V2 production media directory backups
    where you will find directories for the last 7 days
-   `fragalysis-stack-xchem-data`
-   `im-fragnet` for various fragmentation sourcefiles and neo4j CSV files
-   `im-infra-backup` for the development Squonk2 infrastructure database
-   `im-infra-integration-test-backup` for the integration test Squonk2 infrastructure database
-   `im-infra-production-backup` for the production Squonk2 infrastructure database
-   `im-infra-test-backup` for the test Squonk2 infrastructure database
-   `nw-rancher` for the manual backup of the cluster Rancher server
-   `nw-xch-dev` for the dev kubernetes etcd cluster backups
-   `nw-xch-prod` for the production kubernetes etcd cluster backups
    django database. Where you should find hourly, daily, weekly, and monthly backups.
-   `nw-xch-prod-production-stack-backup` for the legacy production fragalysis stack
    django database.
-   `nw-xch-prod-v2-production-stack-backup` for the V2 (current) production fragalysis stack
    django database. Where you should find hourly, daily, weekly, and monthly backups.
