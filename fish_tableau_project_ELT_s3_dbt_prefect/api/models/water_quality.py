from api.lib.db import build_from_record, build_from_records
import api.models as models


class WaterQuality:
    __table__="ny_water_qualities"
    columns=["id", "name", "basin", "description", "water_quality_class", "waterbody_class"]
    #NOTE: "columns" have to follow the same order as the ny_water_qualities table in create_tables.sql

    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            if k not in self.columns:
                raise ValueError(f"{k} not in {self.columns}")
            setattr(self, k, v)

    def fishes(self, conn):
        statement='''
        SELECT DISTINCT(a.*)
        FROM ny_fishes a
        INNER JOIN ny_water_qualities b ON LOWER(a.waterbody)=LOWER(b.name)
        WHERE a.waterbody=%s;
        '''
        cursor=conn.cursor()
        cursor.execute(statement, (self.name,))
        fish_records=cursor.fetchall()
        fish_objs=build_from_records(models.Fish, fish_records)
        return fish_objs
    
    def to_json(self, conn):
        waterquality_dict=self.__dict__

        fishes=self.fishes(conn)
        waterquality_dict["fishes"]=[fish.__dict__ for fish in fishes]
        
        return waterquality_dict

