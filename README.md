# Sanic-Starter
A good starting point with Sanic using Class based views, Alembic and SQLAlchemy.


### Getting started
Clone the repo, open up terminal and run:

`make init`

This will create a `python3` virtual environment and install all of the
dependencies. Also it will create a `.env` file for you with empty export
`DATABASE_URL` which needs to get filled to perform migrations.



### Caveats
`make init` assumes you have `python3` installed and `pip3` in your `$PATH`.


You must import all of the new models you create into your `app/models/__init__.py`
file underneath the `Base = declarative_base()` constant. This will ensure
that your models will be picked up automatically when running `make revision`.


`DATABASE_URL` is the environment variable being used to run the migrations.
You will have to create your own database and update the `export DATABASE_URL="database url here"`.
using something like [`autoenv`](https://github.com/kennethreitz/autoenv) makes exporting settings easy.
If you have a different or preferred way of doing this you will
have to update the `/alembic/env.py` file to reflect your preferred way.


### Commands
`make run` - Runs the Sanic server

`make revision` - Checks all of the `Base.metadata` and generates a new
migration script under /alembic/versions


`make upgrade` - Runs the revision head and upgrades all database schema.


`make downgrade` - Drops all of the revision heads tables.