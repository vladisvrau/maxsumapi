from tornado.web import RequestHandler

class CustomHandler(RequestHandler):
    async def options(self):
        self.set_status(204)
        self.finish()