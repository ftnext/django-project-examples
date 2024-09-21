# django-project-examples

## Preparation: `.env`

Create `xxx-example/polls_tutorial/.env`.

```
DEBUG=True
SECRET_KEY=(See below)
DATABASE_URL=sqlite:///db.sqlite3
```

Get `SECRET_KEY` in each example environment.

```shell
$ python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

## `venv-example`

```shell
$ python -m venv .venv --upgrade-deps
$ source .venv/bin/activate

(.venv) $ python -m pip install -r requirements.txt
(.venv) $ cd polls_tutorial
(.venv) $ python manage.py runserver
```

## `poetry-example`

```shell
$ python -m venv .venv --upgrade-deps
$ poetry install

$ cd polls_tutorial
$ poetry run python manage.py runserver
```

## `uv-example`

```shell
$ uv sync --frozen

$ cd polls_tutorial
$ uv run python manage.py runserver
```

## `hatch-example`

```shell
$ hatch env create

$ cd polls_tutorial
$ hatch run python manage.py runserver
```
