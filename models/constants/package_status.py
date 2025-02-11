class PackageStatus:
    RECEIVED = "Received"
    ON_ROUTE = "On route"
    DELIVERED = "Delivered"
    
    _order = (RECEIVED, ON_ROUTE, DELIVERED)

    @classmethod
    def next(cls, current):
        if current not in cls._order:
            raise ValueError(f"Invalid status: {current}")
        
        idx = cls._order.index(current)
        if idx < len(cls._order) - 1:
            return cls._order[idx + 1]
        return current
