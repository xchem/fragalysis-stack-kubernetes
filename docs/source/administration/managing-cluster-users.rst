######################
Managing Cluster Users
######################

Users who need to access the cluster, either to manage it or develop and debug
applications, are normally given a Kubernetes config file (a KUBECONFIG).
These are obtained from Rancher based on users known to Rancher and their
cluster roles. As a policy decision everyone who needs access needs a presence on
Rancher but (for now) and membership of clusters they need access to.

*************
Adding a user
*************

For each user we create an account on the rancher server.
This is done by an admin user on Rancher: -

1.  Navigate to **Users & Authentication**
2.  Select **Create**, and provide a **Username**, **Display Name**,
    and **Generate a random password**
3.  The user should be a **Restricted Administrator**

Keep the username and generated password safe.

Now add the user to the required clusters: -

1.  Navigate to **Cluster Management**
2.  Select the required cluster (e.g. ``nw-xch-dev``) and select **Config**
3.  Under **Member Roles** select remove the new user (who wil be a **Cluster Owner**)
4.  Select **+ Add Member** (to add the member again)
5.  Select an appropriate user and select the **Custom** role
6.  The custom role should include **View All Projects** and **View Nodes** and save it
7.  Scroll to the bottom of the configuration page and select **Save**

*******************************
Getting a KUBECONFIG for a user
*******************************

Rather than give users access to the Rancher console an admin user logs into Rancher
as the user that the KUBECONFIG is required for.

1.  Login as the required user
2.  Select the appropriate cluster from the home page
3.  From the top of the page select **Download KubeConfig**

Preserve the config and send it to the user.

Rancher creates a KUBECONFIG along with an Access Token. Once created the token
can be found on the user's **Account and API Keys** page along with its scope
(a character code for the cluster) and expiry typically 90 days.

The typical ``ctrl`` clusters in the downloaded KUBECONFIG (on the IP ``192.168``)
are not of any use so it might be worth removing the ``ctrl`` clusters from the
``clusters`` list in thew KUBECONFIG, along with the matching ``contexts`` in the file.

***************************
Disabling a KUBECONFIG file
***************************

If you need to disable a user's KUBECONFIG file you simply delete the
corresponding **Kubeconfig token** from the user's **Account and API Keys**
(after logging into Rancher as the user).
