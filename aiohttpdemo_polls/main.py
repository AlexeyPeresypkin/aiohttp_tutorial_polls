import aiohttp_jinja2
import jinja2
from aiohttp import web

from middlewares import setup_middlewares
from db import pg_context
from settings import config, BASE_DIR
from routes import setup_routes

app = web.Application()
setup_routes(app)
setup_middlewares(app)
app['config'] = config
aiohttp_jinja2.setup(
    app,
    loader=jinja2.FileSystemLoader(
        str(BASE_DIR / 'aiohttpdemo_polls' / 'templates')
    ))
app.cleanup_ctx.append(pg_context)
web.run_app(app)
