import inspect
from functools import wraps


def Post(route, method_name=None):
    """Decorator to define POST routes with a custom method name and pass Tornado objects."""

    def decorator(func):
        @wraps(func)
        def sync_wrapper(self, *args, **kwargs):
            return func(
                self,
                request=self.request,
                headers=self.request.headers,
                *args,
                **kwargs
            )

        @wraps(func)
        async def async_wrapper(self, *args, **kwargs):
            return await func(
                self,
                request=self.request,
                headers=self.request.headers,
                *args,
                **kwargs
            )

        if inspect.iscoroutinefunction(func):
            wrapper = async_wrapper
        else:
            wrapper = sync_wrapper

        wrapper._route = {
            "path": route,
            "method": "POST",
            "handler": method_name or func.__name__
        }
        return wrapper

    return decorator
