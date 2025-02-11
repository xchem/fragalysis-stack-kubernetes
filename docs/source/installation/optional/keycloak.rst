########
Keycloak
########

`Keycloak`_ is an open source software product to allow single sign-on with
Identity and Access Management aimed at modern applications and services.
The Fragalysis Stack can be configured to authenticate and authorise access
through Keycloak.

************
Installation
************

You can skip this section if you have your own Keycloak server - this section
deals with installing Keycloak using our Infrastructure.

You can deploy Keycloak using our Infrastructure. It will install a
Keycloak service and supporting PostgreSQL database into your cluster.
If you do not have your own server you can follow our guide:
:doc:`../basic/infrastructure-installation`.

*   These instructions assume you're using **Keycloak 26**
    or a version that's compatible.
*   These instructions also assume that you are using the *custom* Keycloak
    image that has been built from the `xchem-keycloak`_ repository.
    Images built there contain customisations to features like Keycloak *Themes*.

Follow our guide:
:doc:`../basic/infrastructure-installation`.

*************
Configuration
*************

OIDC login federation
=====================

With Keycloak installed you now need to login, using the admin user
and password you used in the installation steps above, and configure
the running server.

Fragalysis uses the library mozilla-django-oidc to authenticate with Keycloak.
(See: https://mozilla-django-oidc.readthedocs.io/en/stable/installation.html)

You will need to set up a different client in Keycloak for *every* environment
you have for your site - local, development, staging, production. This is so
that the callback urls can be correctly configured.

A minimal client configuration for the site: **fragalysis.some-company.com**,
in the Keycloak realm: **some-realm**, would need to contain:

On the *Settings* tab:

*   Client_id: *(Required)*
*   Client Protocol: *open-connect*
*   Valid Redirect URLs

    * https://fragalysis.some-company.com/oidc/callback/
    * http://fragalysis.some-company.com/oidc/callback/
    * http://fragalysis.some-company.com/viewer/react/landing

*   ID Token Signature Algorithm: *RS256*.

From the *Credentials* tab, the generated client-secret must be also noted
for inclusion in the Fragalysis environment parameters.

Parameter definitions for Keycloak are defined in
``roles/fragalysis-stack/defaults/main.yaml``. Look for variables that start
``stack_oidc_``.

Note that the realm parameter should contain the fully formed address of the
Keycloak server. For example::

    stack_oidc_keycloak_realm: https://keycloak.xchem-dev.diamond.ac.uk/auth/realms/xchem

Custom Themes
=============

If you are using the image built from our `xchem-keycloak`_ repository,
you can customise the Keycloak themes to fit your requirements as our image
contains a login customisation for the OIDC login option.

Themes are usually Realm-specific and you will need to be logged in as the
Keycloak administrator to make changes.

Once logged-in to the Keycloak admin console, select the Realm you want
to customise, and then select the **Realm Settings** page from the side-bar.
From here you will see a **Themes** tab on the main. Click on this tab
and choose the customisation you want to make. Our image comes with a ```fragalysis``
**Login theme**.

Once you've made changes, hit the **Save** button and you should see a
**Realm successfully updated** pop-up.

.. _keycloak: https://www.keycloak.org
.. _xchem-keycloak: https://github.com/xchem/fragalysis-keycloak
