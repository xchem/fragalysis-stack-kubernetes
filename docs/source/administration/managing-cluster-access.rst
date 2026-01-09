#######################
Managing Cluster Access
#######################

Users who need to access the cluster, either to manage it or develop and debug
applications, are given a Kubernetes config file that's obtained from the Rancher
server using a login that's dedicated to the intended user. For example there's a login
for **tim**, and **alan**.

Essentially an administrator logs into Rancher, using the dedicated user login,
and then downloads a kubeconfig for the use for each cluster they want to access.

What the user can access is controlled by the Rancher **Projects** that will have
been setup for each cluster. **Namespaces** are allocated to projects.
So, to access any developer stacks Namespace the user is made a **Member** of the
**Fragalysis (Developer)** project on in the development cluster (an administrator
is responsible for setting up the **Projects** in each cluster, and making sure they
contain appropriate **Namespaces**).

In this way a developer can have access to stacks while protecting the **System** and
**Infrastructure** namespaces from accidental access or corruption.

************
Adding users
************

It is a Rancher administrator's job to add a **User** account for everyone entitled
to access the cluster. For each user we create an account on the rancher server,
done via an admin login on Rancher: -

1.  Navigate to **Users & Authentication**
2.  Select **Create**, and provide a **Username**, **Display Name**,
    and **Generate a random password**
3.  The user should be a **Standard User** (with nothing else required)

Keep the user credentials safe - you'll need them when you want to create
a KUBECONFIG file for the user.

********************************
Managing Projects and Namespaces
********************************

It is the cluster administrator's role to create **Projects** (for each cluster)
and *Move* **Namespaces** into them. Users can only access Namespaces where the user
is a *Member* of the corresponding *Project*.

Via an admin login, create the **Projects** you need and then **Move** appropriate
**Namespaces** into them. A Namespace can only belong to one Project.

In the `nw-xch-dev` cluster we typically have these **Projects**: -

-   ``Fragalysis``
-   ``Graph``
-   ``Infrastructure``
-   ``Squonk``
-   ``System``
-   ``TA Authenticator``

In the `nw-xch-prod` cluster we typically have these **Projects**: -

-   ``Fragalysis (Legacy)``
-   ``Fragalysis (Production)``
-   ``Fragalysis (Staging)``
-   ``Graph``
-   ``Infrastructure``
-   ``Squonk``
-   ``System``
-   ``TA Authenticator``

***************************
Providing Users with access
***************************

Let's assume that we have...

-   Rancher **Clusters**
-   A Rancher **User** account for each person who needs access
-   **Projects** (and **Namespaces**)

What we do is...

1.  Create a KUBECONFIG (via a Rancher login dedicated to the user)
2.  Manage Project (Namespace) access (via a Rancher admin login)

Project access is independent of the user KUBECONFIG - you can download a KUBECONFIG
and then manage user access separately, at any time.

Create a KUBECONFIG
===================

Using a login dedicated to the corresponding user: -

1.  Navigate to the cluster
2.  Use the **Download KubeConfig** icon in the top-right of the cluster page

Do this for each cluster you want the user to have access to.

Preserve the config and send it to the user.

You might want to rename the downloaded file to include the user's name, e.g.
``nw-xch-dev-alan.yaml``

Rancher is configured to generate a new API key for each ``KUBECONFIG`` that's generated.
Each ``KUBECONFIG`` has its own API key and the keys can be seen on the
**Accounts & API Keys** page where you can see their expiry period and its *scope*
(a character code used by Rancher to identify the cluster).

``KUBECONFIG`` API keys will expire after 90 days.

The ``KUBECONFIG`` contains some superfluous material. The typical ``ctrl`` clusters
in it (on the IP ``192.168``) are of no use so it might be worth removing these clusters
from the ``clusters`` list along with the matching ``contexts`` in the file. But that's
just to be *tidy*.

Users only need one ``KUBECONFIG`` file for each cluster, and the **MUST** be told
not to circulate the file - it must only be used by the user it was made for.

Manage Project access
=====================

A user with a ``KUBECONFIG`` cannot access kubernetes resources unless they have been
made a **Member** of the **Project** the resource object **Namespace** belongs to.

From a Rancher admin login: -

1.  Navigate to the corresponding cluster's **Projects/Namespaces** page
2.  Using the Project's ``...`` Select **Edit Config**
3.  In the **Members** panel **Add** the user and **Select** the user as a **Member**
4.  **Add** the user and then hit **Save**

***************************
Disabling a KUBECONFIG file
***************************

If you need to disable a user's KUBECONFIG file delete the
corresponding **API Key** from the user's **Account and API Keys**
(using the Rancher login you used to create the ``KUBECONFIG``).

######################
Configuring API expiry
######################

API key generation is controlled by the Rancher **Global Settings**. As an admin user
you can see these settings, which are: -

-   ``kubeconfig-generate-token``, which must be set to **true**
-   ``kubeconfig-default-token-ttl-minutes``, which is set to **129600** (90 days)
