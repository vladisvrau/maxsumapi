from tornado import ioloop, web
from services.maxsum import MaxSum 


def create_app():
    """Create App
    Creates the web server instance
    """
    return web.Application([
        (r'/maxsum', MaxSum),
    ])


if __name__ == "__main__":
    PORT = 8080
    app = create_app()

    app.listen(PORT)
    ioloop.IOLoop.current().start()