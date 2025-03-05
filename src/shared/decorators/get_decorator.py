import inspect
from functools import wraps


def Get(route, method_name=None):
    """Decorator to define GET routes with a custom method name and pass Tornado objects."""

    def decorator(func):
        # We'll create two wrapper functions: one sync, one async.
        @wraps(func)
        def sync_wrapper(self, *args, **kwargs):
            # For sync functions, we just call them.
            return func(
                self,
                request=self.request,
                headers=self.request.headers,
                *args,
                **kwargs
            )

        @wraps(func)
        async def async_wrapper(self, *args, **kwargs):
            # For async functions, await them.
            return await func(
                self,
                request=self.request,
                headers=self.request.headers,
                *args,
                **kwargs
            )

        # Decide which wrapper to use based on whether `func` is a coroutine.
        if inspect.iscoroutinefunction(func):
            wrapper = async_wrapper
        else:
            wrapper = sync_wrapper

        # Store route info for your BaseController to consume.
        wrapper._route = {
            "path": route,
            "method": "GET",
            "handler": method_name or func.__name__
        }
        return wrapper

    return decorator
