###############################
Claude Skills (Release Process)
###############################

There are a number of “skills” that simplify releasing the stack and its underlying
backend and frontend container images. To install these, and use them in your claude
session you will need an account that can access (write) to the repositories,
and access to our “private” GitHub repository.

We use our ``im-claude`` GitHub account for Claude work on Fragalysis.

Install the skills (from a claude session) with the following command: -

One-time setup::

	  /plugin marketplace add informaticsmatters/claude-skills

Then install the plugins you want, i.e.::

	  /plugin install fragalysis-skills@im-claude-skills

******
Skills
******

- ``release-staging``
- ``release-the-stack``

Releasing the backend (or frontend)
===================================
Start from a clone of any repository (like backend or frontend).
You then instruct Claude to **Release staging**. Claude will ask whether you want to
release the f/e or b/e. Claude will then make a number of precautionary check
before merging staging branch to production (after checking you you).

After the merge a suitable tag will be chosen and you'll be asked to confirm this.

Releasing the stack
===================
This relies on the existence of a ticket in the **Releases** swim-line.
The ticket should name all the project issues that need to be contained in the release.
Claude will check that these tickets are in the correct lanes before making a release.

The release ticket should also name the backend and frontend revisions that need
to go into the stack, e.g.::

	  Backend: 2026.07.1
    Frontend: 2026.08.1

Then just tell Claude to **Release the stack using <release ticket number>**.
The ticket will be checked, the referred issues will be checked that they are in
the correct swim-lanes and a release will be made.
