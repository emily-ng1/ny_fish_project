from api.lib.db import build_from_record, build_from_records
import api.models as models


class Fish:
    __table__="ny_fishes"
    columns=["id", "year", "county", "waterbody", "town", "month", "number", "species", "size_inches"]

    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            if k not in self.columns:
                raise ValueError(f"{k} not in {self.columns}")
            setattr(self, k, v)


    def waterbody_classes(self, conn):
        statement='''
        SELECT DISTINCT(a.*)
        FROM ny_water_qualities a
        INNER JOIN ny_fishes b ON LOWER(a.name)=LOWER(b.waterbody)
        WHERE a.name=%s;
        '''
        cursor=conn.cursor()
        cursor.execute(statement, (self.waterbody,))
        waterbody_records=cursor.fetchall()
        waterbody_objs=build_from_records(models.WaterQuality, waterbody_records)
        return waterbody_objs
    
    def to_json(self, conn):
        fish_dict=self.__dict__

        waterbody_classes=self.waterbody_classes(conn)
        fish_dict["waterbody_classes"]=[waterbody_class.__dict__ for waterbody_class in waterbody_classes]

        return fish_dict

