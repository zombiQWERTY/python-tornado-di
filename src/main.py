import tornado.ioloop
import tornado.web
from modules.application_container import ApplicationContainer


if __name__ == "__main__":
    application_container = ApplicationContainer()
    application_container.wire(modules=[__name__])

    routes = ApplicationContainer.make_routes(application_container)

    tornado.web.Application(routes).listen(8888)
    print("Server running on http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
