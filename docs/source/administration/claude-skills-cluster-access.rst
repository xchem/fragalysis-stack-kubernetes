##############################
Claude Skills (Cluster Access)
##############################

There is a “skill” that simplifies the collection of a user's ``KUBECONFIG``.
To install it, and use it in your claude session you will need access to our
“private” GitHub repository.

We use our ``im-claude`` GitHub account for Claude work on Fragalysis.

Install the skills (from a claude session) with the following command: -

One-time setup::

	  /plugin marketplace add informaticsmatters/claude-skills

Then install the plugins you want, i.e.::

	  /plugin install fragalysis-skills@im-claude-skills

******
Skills
******

- ``get-rancher-kubeconfigs``

Getting rancher kubeconfigs
===========================
This is done by accessing the Rancher console as the user whose ``KUBECONFIG`` you
need, and the skill expects this information via the following environment variables::

		RANCHER_HOST
		RANCHER_USER
		RANCHER_USER_PASSWORD

Set ``RANCHER_HOST`` to ``130.246.213.177`` , and the other variables to the
username and password of the user (on Rancher) that you need a new ``KUBECONFIG`` for.

KUBECONFIG files usually expire after 90 days.
