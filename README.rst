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
and show views for the user. Provides an API in your django application to
POST user data in key, value form to support arbitrary types of data.

Clients generate their own UUID and save locally. There is no special
authentication or authorization.

Quickstart
----------

Install django_lair::

    pip install django_lair

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_lair',
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

Usage
-----

For the top level dashboard, navigate to `<endpoint>/datum/`, e.g.::

    http://localhost:8000/datum/

To add metric data, POST to endpoint `/datum/create/` with user, metric
name, and metric value information::

    curl --data "user=abcdefgh-1234-1234-9876-abcdefghijkl&name=metric1&value=value1" http://localhost:8000/datum/create/

Each field is mandatory, so be sure to include uuid, name, and value in the POST.

Features
--------

* Stores users and shows list view of metrics hit
* Provides simplistic list view of saved datums including unique user graphs
* Provides detailed user page with frequency graph
* Search, sort, and filter paginated tables of user data

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox
