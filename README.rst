Django Requests Panel
=====================

.. image:: https://travis-ci.org/gtnx/django-requests-panel.svg?branch=master
    :target: https://travis-ci.org/gtnx/django-requests-panel

A Django Debug Toolbar panel for requests

About
-----

This is a panel for `Django Debug Toolbar`_ 1.x that displays info about http requests made with the `requests`_ and `requests_futures`_ libraries. 

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

Run tests using nose & coverage:

    nosetests --with-coverage --cover-package requests_panel .


License
-------

Uses the `GNU GPL`_ license.


.. _Django Debug Toolbar: https://github.com/django-debug-toolbar/django-debug-toolbar
.. _GNU GPL: http://www.gnu.org/licenses/gpl-2.0.html
.. _requests: http://docs.python-requests.org/en/latest/
.. _requests_futures: https://github.com/ross/requests-futures
