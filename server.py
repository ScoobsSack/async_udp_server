from aiohttp import web
import json


async def handle(request):
    response_object = {'status': 'success'}
    return web.Response(text=json.dumps(response_object), status=200)


app = web.Application()
app.router.add_post("/", handle)


web.run_app(app, port=5555)
