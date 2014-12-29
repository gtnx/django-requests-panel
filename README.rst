Django Requests Panel
=====================

A Django Debug Toolbar panel for requests

About
-----

This is a panel for `Django Debug Toolbar`_ 1.x that displays info about http requests made with the `requests`_ library. 

Installation
------------

Install using ``pip``::

    pip install django-requests-panel

or install the development version from source::

    pip install git+git@github.com:gtnx/django-requests-panel.git


Usage
-----

Add ``requests_panel`` to your ``INSTALLED_APPS`` so that we can find the templates in the panel.

Add ``requests_panel.panels.RequestsDebugPanel`` to your ``DEBUG_TOOLBAR_PANELS``.

Testing
-------

There are no tests yet. 

License
-------

Uses the `GNU GPL`_ license.


.. _Django Debug Toolbar: https://github.com/django-debug-toolbar/django-debug-toolbar
.. _GNU GPL: http://www.gnu.org/licenses/gpl-2.0.html
.. _requests: http://docs.python-requests.org/en/latest/
