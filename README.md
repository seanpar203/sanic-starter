# Sanic-Starter
A good starting point with Sanic using blueprints, alembic and sqlalchemy.


### Getting started
Clone the repo, open up terminal and run:

`make init`

This will create a `python3` virtual environment and install all of the
dependencies.



### Caveats
You must import all of the new models you create into your `app/models/__init__.py`
file underneath the `Base = declarative_base()` constant. This will ensure
that your models will be picked up automatically when running `make revision`.


`DATABASE_URL` is the environment variable being used to run the migrations.
You will have to create your own database and either a `.env` file with `export DATABASE_URL="database url here"`
using something like [`autoenv`](https://github.com/kennethreitz/autoenv) makes this very easy with these existing settings.
If you have a different or preferred way of doing this you will have to update the
`/alembic/env.py` file to reflect your preferred way.


### Commands

`make revision` - Checks all of the `Base.metadata` and generates a new
migration script under /alembic/versions


`make upgrade` - Runs the revision head and upgrades all database schema.


`make downgrade` - Drops all of the revision heads tables.