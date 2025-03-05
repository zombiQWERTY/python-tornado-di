import tornado.web
import inspect


class BaseController(tornado.web.RequestHandler):
    """Base class for all controllers, handling automatic method dispatching."""

    def initialize(self, **kwargs):
        """Dynamically set injected dependencies as instance attributes."""
        for key, value in kwargs.items():
            setattr(self, key, value)

    async def prepare(self):
        """Intercept the request and dispatch to the correct handler before execution."""
        method = self.request.method.upper()
        await self._dispatch(method, *self.path_args, **self.path_kwargs)

    async def _dispatch(self, method, *args, **kwargs):
        """
        Find the correct handler method and call it. If the result is awaitable,
        await it. This handles both sync and async (possibly decorated) methods.
        """
        route = next((r for r in getattr(self, "_routes", []) if r["method"] == method), None)

        if route and hasattr(self, route["handler"]):
            handler_method = getattr(self, route["handler"])
            # Always call the handler method first...
            result = handler_method(*args, **kwargs)
            # ... then await if necessary
            if inspect.isawaitable(result):
                await result
            return

        self.set_status(405)
        self.write({"error": f"Method {method} Not Allowed"})

    async def get(self, *args, **kwargs):
        """Intercept GET requests and dispatch them asynchronously."""
        await self._dispatch("GET", *args, **kwargs)

    async def post(self, *args, **kwargs):
        """Intercept POST requests and dispatch them asynchronously."""
        await self._dispatch("POST", *args, **kwargs)
