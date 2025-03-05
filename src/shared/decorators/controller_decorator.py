def Controller(cls):
    """Marks a class as a Controller and collects route metadata."""
    cls._routes = []

    for attr_name in dir(cls):
        attr = getattr(cls, attr_name)
        if callable(attr) and hasattr(attr, "_route"):
            cls._routes.append(attr._route)

    return cls
