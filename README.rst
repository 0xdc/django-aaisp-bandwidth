aaisp
====

Quick start
-----------

1. Add "aaisp" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'aaisp',
    ]

2. Include the aaisp URLconf in your project urls.py like this::

    url(r'^aaisp/', include('aaisp.urls')),

3. Run `python manage.py migrate` to create the aaisp models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/aaisp/ to view templates.
