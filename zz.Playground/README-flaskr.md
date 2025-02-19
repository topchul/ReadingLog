# flask Official Tutorial

## [Tutorial](https://flask.palletsprojects.com/en/stable/tutorial/)

## [Project Layout](https://flask.palletsprojects.com/en/stable/tutorial/layout/)

* `install`
  ```bash
  python -m venv [path]/{VirtualENV name}
  activates
  pip install flask
  ```

* `hello.py`
  * (Linux/macOS)

    ```bash
    export FLASK_APP=hello.py
    flask run
    ```

  * Windows CMD

    ```cmd
    set FLASK_APP=hello.py
    ```

  * Windows PowerShell

    ```powershell
    $env:FLASK_APP="hello.py"
    flask run
    ```

'''plain/text
/home/user/Projects/flask-tutorial
├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── .venv/
├── pyproject.toml
└── MANIFEST.in
'''

* `.gitignore`

## [Application Setup](https://flask.palletsprojects.com/en/stable/tutorial/factory/)

* `flaskr/__init__.py`
  * `def create_app(test_config=None):`

```plain/text
\$ flask --app flaskr run --debug
```

## [Define and Access the Database](https://flask.palletsprojects.com/en/stable/tutorial/database/)

* `flaskr/db.py`
  * `def get_db():`
  * `def close_db(e=None):`
* `flaskr/schema.sql`
* `flaskr/db.py`
  * `def init_db():`
  * `@click.command('init-db')` `def init_db_command():`
  * `sqlite3.register_converter("timestamp", lambda ...)`
* `flaskr/db.py`
  * `def init_app(app):`
* `flaskr/__init__.py`
  * `def create_app():`

```plain/text
\$ flask --app flaskr run init-db
Initialized the datebase.
```

## [Blueprints and Views](https://flask.palletsprojects.com/en/stable/tutorial/views/)

* `flaskr/auth.py`
  * `bp = Blueprint('auth', __name__, url_prefix='/auth')`
* `flaskr/__init__.py`
  * `def create_app():`
* `flaskr/auth.py`
  * `@bp.route('/register', methods=...)` `def register():`
  * `@bp.route('/login', methods=...)` `def login():`
  * `@bp.before_app_reqest` `def load_logged_in_user():`
  * `@bp.route('/logout')` `def logout():`
  * `def login_required(view):` `@functools.wraps(view)`

## [Templates](https://flask.palletsprojects.com/en/stable/tutorial/templates/)

* `flaskr/templates/base.html`
* `flaskr/templates/auth/register.html`
* `flaskr/templates/auth/login.html`

## [Static Files](https://flask.palletsprojects.com/en/stable/tutorial/static/)

* `flaskr/static/sytle.css`

## [Blog Blueprint](https://flask.palletsprojects.com/en/stable/tutorial/blog/)

* `flaskr/blog.py`
  * `bp = Blueprint('blog', __name__)`
* `flaskr/__init__.py`
  * `def create_app():` `app.register_blueprint(blog.bp)`
* `flaskr/blog.py`
  * `@bp.route('/')` `def index():`
* `flaskr/templates/blog/index.html`
* `flaskr/blog.py`
  * `@bp.route('/create', methods=...)` `@login_required` `def create():`
* `flaskr/templates/blog/create.html`
* `flaskr/blog.py`
  * `def get_post(id, check_auth=True):`
* `flaskr/blog.py`
  * `@bp.route('/<int:id>/update', methods=...)` `@login_required` `def update(id):`)
* `flaskr/templates/blog/update.html`
* `flaskr/blog.py`
  * `@bp.route('/<int:id>/delete', methods=...)` `@login_required` `def delete(id):`)

## [Make the Project Installable](https://flask.palletsprojects.com/en/stable/tutorial/install/)

다음과 같이 설치 가능하게 하기 : `pip install yourproject.whl`

* `pyproject.toml`
  * [Packaging tutorial](https://packaging.python.org/tutorials/packaging-projects/)

```plain/text
\$ pip install -e .
```

```plain/text
\$ pip list

Package      Version Editable project location
------------ ------- -------------------------------------------
blinker      1.9.0
click        8.1.8
colorama     0.4.6
Flask        3.1.0
flaskr       1.0.0   C:\Playground\SCMs\ReadingLog\zz.Playground
itsdangerous 2.2.0
Jinja2       3.1.5
MarkupSafe   3.0.2
pip          24.3.1
Werkzeug     3.1.3
```

now can call from anywhere : `PS C:\> flask --app flaskr run`

## [Test Coverage](https://flask.palletsprojects.com/en/stable/tutorial/tests/)

`pytest` 와 `coverage` 설치

```plain/text
\$ pip install pytest coverage
```

* `tests/data.sql` default database
* `tests/conftest.py` define fixtures (app, client, runner)

* `tests/test_factory.py`
  * `test_config()`
  * `test_hello()`

* `tests/db.py`
  * `test_get_close_db(app)` recycle connection & closing
  * `test_init_db_command(runner, monkeypatch)` initializing db command

* `tests/conftest.py`
  * `class AuthAuctions(object)` define (login, logout) action for fixture (auth)
* `tests/test_auth.py` register, login, logout

* `tests/test_blog.py` index, author_require, exists, create, update, delete

* `pyproject.toml` test tool config

  ```plain/text
  \$ pytest
  
  ========================= test session starts ==========================
  platform linux -- Python 3.6.4, pytest-3.5.0, py-1.5.3, pluggy-0.6.0
  rootdir: /home/user/Projects/flask-tutorial
  collected 23 item
  
  tests/test_auth.py ........                                      [ 34%]
  tests/test_blog.py ............                                  [ 86%]
  tests/test_db.py ..                                              [ 95%]
  tests/test_factory.py ..                                         [100%]

  ====================== 24 passed in 0.64 seconds =======================
  ```

`\$ coverage run -m pytest`
`\$ coverage report`
`\$ coverage html` generates files `htmlcov`

## [Deploy to Production](https://flask.palletsprojects.com/en/stable/tutorial/deploy/)

### Build and Install

```plain/text
\$ pip install build
\$ python -m build --wheel
```

`\$ pip install flaskr-1.0.0-py3-none-any.whl` - install own wheel package to venv

`\$ flask --app flaskr init-db` - need to run init-db again to create the database in instance folder

### Configure the Secret Key

```plain/text
\$ python -c "import secrets; print(secrets.token_hex())"
8145c8d2a9bdfee450dfb6e3cdc2f65f6a119d7b85a64575f73c39bd72874ff4

```

```python
# .venv/var/flaskr-instance/config.py
SECRET_KEY = '8145c8d2a9bdfee450dfb6e3cdc2f65f6a119d7b85a64575f73c39bd72874ff4'
```

### Run with a Production Server

`$ pip install waitress`

```plain/text
\$ waitress-serve --call "flaskr:create_app"
INFO:waitress:Serving on http://0.0.0.0:8080
```
