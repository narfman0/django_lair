=============================
django_lair
=============================

.. image:: https://badge.fury.io/py/django_lair.png
    :target: https://badge.fury.io/py/django_lair

.. image:: https://travis-ci.org/narfman0/django_lair.png?branch=master
    :target: https://travis-ci.org/narfman0/django_lair

Analytics and metrics app to both store and display user actions

Documentation
-------------

django_lair will ingest user metrics, store in django configured database,
and show views for the user

Quickstart
----------

Install django_lair::

    pip install django_lair

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_lair.apps.DjangoLairConfig',
        ...
    )

Add django_lair's URL patterns:

.. code-block:: python

    from django_lair import urls as django_lair_urls


    urlpatterns = [
        ...
        url(r'^', include(django_lair_urls)),
        ...
    ]

 Migrate app::

     ./manage.py migrate django_lair

Features
--------

* Stores users and shows list view of metrics hit
* Provides simplistic (to be expanded :)) list view of saved datums

TODO
----

* User detail graph
* Metric detail view graph
* Home dashboard unique users per day

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox
