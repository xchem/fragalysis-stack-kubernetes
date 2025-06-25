######################
Installing AWX (Basic)
######################

.. note:: Allow 1 hour to complete this task,
          which involves installation of the operator and an AWX server instance

Installed versions (at the time of writing): -

- Operator **2.19.1**
- AWX **24.6.1**

Installation and configuration of the AWX server is achieved using the
kubernetes `AWX operator`_. Clone the project and follow the **Basic Installation**
section of the guide.

With the operator installed you will need to create an AWX server using a Kubernetes
**Kustomization**. This will rely on also creating secrets used to configure the AWX
server, secrets that define the AWX URL, its database and username and passwords.

Here we use the infrastructure database previously configured.

The ``Kustomization.yaml`` file (located in the root of the clone repository) will
probably look like this::

    ---
    apiVersion: kustomize.config.k8s.io/v1beta1
    kind: Kustomization

    resources:
    - awx-im-infra-secrets.yaml
    - awx-im-infra.yaml
    namespace: awx

inm our case the **Kustomization** defines two resources::

    awx-im-infra-secrets.yaml
    awx-im-infra.yaml

Our ``awx-im-infra-secrets.yaml`` defines two Kubernetes **Secrets**, named:-

*   ``awx-im-infra-postgres-configuration``
*   ``awx-im-infra-secret-key``

The first provides the following secrets::

    database (awx)
    host (database.im-infra.svc)
    password (****)
    port (5432)
    ssimode (prefer)
    target_session_attrs`` (read-write)
    type (unmanaged)
    username (awx)

And the second provides::

    secret_key

The ``awx-im-infra.yaml`` resource defines an **AWX** (custom resource) and probably
looks like this::

    ipv6_disabled: true
    control_plane_priority_class: im-application-high
    secret_key_secret: awx-im-infra-secret-key
    postgres_configuration_secret: awx-im-infra-postgres-configuration
    service_type: ClusterIP
    ingress_type: ingress
    ingress_class_name: nginx
    ingress_tls_secret: awx-im-infra-tls
    ingress_annotations: |
      cert-manager.io/cluster-issuer: letsencrypt-nginx-production
    hostname: awx.xchem.diamond.ac.uk

With the **Kustomization** and resources defined, create the AWX server::

    kubectl apply -k .

#######################
Configuring AWX (Basic)
#######################

.. note:: Allow several hours to complete this task,
          which involves configuring and checking the AWX application server

With an AWX server running you now have to configure it, which will require at least
some of the following objects:

*   An organisation
*   Credentials
*   A team
*   Users
*   Projects
*   Job Templates
*   Workflows

..  image:: ../../images/awx-production-templates.png

.. _awx operator: https://github.com/ansible/awx-operator
