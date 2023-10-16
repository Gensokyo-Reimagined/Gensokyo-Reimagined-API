<p align="center">
    <img src="https://cdn.staticaly.com/gh/Gensokyo-Reimagined/Gensokyo-Reimagined-Web/main/public/logo.svg" width="200" height="auto" alt="Gensokyo-Reimagined">
</p>

<div align="center">

# Gensokyo-Reimagined-API

</div>

## How to run

This is a fastapi project, so if you want to run it, you have to run it with uvicorn/gunicorn

### Preparatory phase

It is recommended to use `python -m venv venv` to create a virtual environment and then enter the virtual environment

Then run `pip install -r requirements.txt` to install the dependency

### Start running

If you need hot reload in your development environment, run `uvicorn main:app --reload`

**For production environments**, it is recommended to install the `gunicorn` package (`pip isntall gunicorn`).

Then run the `gunicorn main: app - 4 - k w uvicorn. Workers. UvicornWorker`

> [!NOTE]
> more details can be found [here](https://fastapi.tiangolo.com/deployment/server-workers/)

## Config

If there is no `config.yml` in the project root directory, you can follow the example below to fill out the configuration file and save it to `config.yml` in the project root directory

```yaml
database:
  host: [mysql ip]
  port: [mysql port]
  user: [user name]
  password: [user password]
  database: [database name]
```