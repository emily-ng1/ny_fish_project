


class Fish:
    __table__="ny_fishes"
    columns=["id", "year", "county", "waterbody", "town", "month", "number", "species", "size_inches"]

    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            if k not in self.columns:
                raise ValueError(f"{k} not in {self.columns}")
            setattr(self, k, v)
