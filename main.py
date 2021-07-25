from tornado import ioloop, gen, web
import tornado
from services.maxsum import MaxSum 



def create_app():
    return web.Application([
        (r'/maxsum', MaxSum),
    ])

if __name__ == "__main__":
    app = create_app()
    app.listen(8080)
    ioloop.IOLoop.current().start()