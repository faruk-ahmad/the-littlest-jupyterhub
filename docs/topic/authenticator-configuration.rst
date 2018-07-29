.. _topic/authenticator-configuration:

=====================================
Configuring JupyterHub authenticators
=====================================

Any `JupyterHub authenticator <https://github.com/jupyterhub/jupyterhub/wiki/Authenticators>`_
can be used with TLJH. A number of them ship by default with TLJH:

#. `OAuthenticator <https://github.com/jupyterhub/oauthenticator>`_ - Google, GitHub, CILogon,
   GitLab, Globus, Mediawiki, auth0, generic OpenID connect (for KeyCloak, etc) and other
   OAuth based authentication methods.
#. `LDAPAuthenticator <https://github.com/jupyterhub/ldapauthenticator>`_ - LDAP & Active Directory.
#. `DummyAuthenticator <https://github.com/yuvipanda/jupyterhub-dummy-authenticator>`_ - Any username,
   one shared password. A :ref:`how-to guide on using DummyAuthenticator <howto/auth/dummy>` is also
   available.
#. `FirstUseAuthenticator <https://github.com/yuvipanda/jupyterhub-firstuseauthenticator>`_ - Users set
   their password when they log in for the first time. Default authenticator used in TLJH.

We try to have specific how-to guides & tutorials for common authenticators. Since we can not cover
everything, this guide shows you how to use any authenticator you want by using LDAPAuthenticator as an
example.

Configuring the authenticator
=============================

LDAPAuthenticator's `documentation <https://github.com/jupyterhub/ldapauthenticator#required-configuration>`_
lists the various configuration options you can set for LDAPAuthenticator. You can set them
in TLJH with the following pattern:

.. code-block:: bash

   sudo -E tljh-config set auth.<authenticator-name>.<config-option-name> <config-option-value>

When the documentation asks you to set ``LDAPAuthenticator.server_address`` to some
value, you can do that with the following command:

.. code-block:: bash
   
   sudo -E tljh-config set auth.LDAPAuthenticator.server_address = 'my-ldap-server'

Most authenticators require you set multiple configuration options before you can
enable them. Read the authenticator's documentation carefully for more information.

Enabling the authenticator
==========================

Once you have configured the authenticator as you want, it should be enabled. 

.. code-block:: bash

   sudo -E tljh-config set auth.type <fully-qualified-authenticator-name>

For LDAPAuthenticator, the fully qualified name is ``ldapauthenticator.LDAPAuthenticator``.
This is the same name that the documentation `asks <https://github.com/jupyterhub/ldapauthenticator#usage>`_
you to set ``c.JupyterHub.authenticator_class`` to.

For LDAPAuthenticator, this would be:

.. code-block:: bash

   sudo -E tljh-config set auth.type ldapauthenticator.LDAPAuthenticator

Once enabled, you need to reload JupyterHub for the config to take effect.

.. code-block:: bash

   sudo -E tljh-config reload

Try logging in a separate incognito window to check if your configuration works. This
lets you preserve your terminal in case there were errors. If there are
errors, :ref:`troubleshooting/logs` should help you debug them.
