############################
Off-cluster backup locations
############################

We use the following 'out-of-cluster' locations for backup storage: -

DLS/Echo
********

======================================= ===========
Bucket/Path                             Purpose
======================================= ===========
discourse-backups                       Discourse backups
fragalysis-stack-production-media       V2 production media directory backups
                                        where you will find directories for the last 7 days
fragalysis-stack-xchem-data             Misc. data backups
im-fragnet                              Various fragmentation sourcefiles and neo4j CSV files
im-infra-backup                         Development Squonk2 infrastructure database
im-infra-integration-test-backup        Integration test Squonk2 infrastructure database
im-infra-production-backup              Production Squonk2 infrastructure database
im-infra-test-backup                    Test Squonk2 infrastructure database
nw-rancher                              Manual backup of the cluster Rancher server
nw-xch-dev                              Dev kubernetes etcd cluster backups
nw-xch-prod                             Production kubernetes etcd cluster backups
nw-xch-prod-production-stack-backup     The legacy production fragalysis stack
                                        django database.
nw-xch-prod-v2-production-stack-backup  The V2 (current) production fragalysis stack
                                        django database. Where you should find hourly,
                                        daily, weekly, and monthly backups.
======================================= ===========
