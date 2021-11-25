pgquery
========


CLI to inquery a remote PostgreSQL database 


Preparing the Development
-------------------------

1. Ensure ``pip`` and ``pipenv`` are installed
2. Clone repository: ``git clone git@github.com:example/pgquery``
3. ``cd`` into the repository
4. Fetch development dependencies ``make instal``
5. Activate virtualenv: ``pipenv shell``

Usage
-----

Pass in the ip of the database server, database name, and table name (the s3 destination is for future development)


::

        $ pgquery ip, dbname, tblname, --driver/-d s3 bucketname


Running Tests
-------------

Run test locally using ``make`` if virtualenv is active

::
        $ make

if virtualenv isn't active then use:

::
        $ pipenv run make


