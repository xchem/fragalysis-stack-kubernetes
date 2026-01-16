###############################
Rotating the Fragalysis DB User
###############################

Instructions for changing (rotating) the Database user for a stack,
used typically for security reasons for example.

The stack's user for the Django database is called ``fragalysis``
(the database is called ``frag``). To change the password we alter the user in the
database (and then update the chosen password in the corresponding AWX **Job Template**).
the basic steps are: -

-   Shutdown the Stack
-   Alter the database password
-   Alter the Kubernetes Secret
-   Update the Job Template variables
-   Restart the stack

The following instructions should be suitable for the **V2 Production Stack**.

******************
Shutdown the Stack
******************

Scale down the **Stack**, **Beat** and **Worker** Pods. This prevents accidental access
of the database while the Password is being changed.

***************************
Alter the database password
***************************

Using a suitable ``KUBECONFIG``, shell into the database pod and use ``psql``
to change the fragalysis user's password. Replace ``SECRET`` in the following example
with the new password::

    kubectl exec -it database-0 -n v2-production-stack -- bash
    psql -U admin

    ALTER USER fragalysis WITH PASSWORD 'SECRET';

    \q
    exit

Keep a copy of the password in case you need to refer to it later.

***************************
Alter the Kubernetes Secret
***************************

Using Lens (or another Kubernetes IDE), locate the database Secret in the
``v2-production-stack`` Namespace and edit it, replacing the ``user_password``
with the new value.

*********************************
Update the Job Template variables
*********************************

Now **EDIT** the V2 Production stack AWX Job Template (which is responsible for the
Secret that holds the user password). The template is called
**Production Fragalysis Stack**, and the **Variables** section of the template will
have a variable that you need to change: -

1.  The password variable is called ``database_user_password``.
    Replace the current value with the new password.
    **Crucially: DO NOT** alter the ``database_root_password``.

Save the template

*****************
Restart the stack
*****************

Scale up the **Stack**, **Beat** and **Worker** Pods. They will pick-up the
new Secret and password. Make sure the Pods are running, and there are no obvious
errors relating to database access in the logs. As the Stack starts one of the
early actions is to migrate the Django database. If the password is wrong this will fail.
