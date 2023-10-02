from api.lib.db import build_from_record, build_from_records
import api.models as models


class WaterbodyModel:
    __table__="waterbodies"
    __constraint__ = "unique_waterbodies"
    columns=["id", "waterbody_name", "waterbody_class", "description", "basin_name", "water_quality_class"]

    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            if k not in self.columns:
                raise ValueError(f"{k} not in {self.columns}")
            setattr(self, k, v)


    def fish_classes(self, conn):
        statement='''
        SELECT a.*
        FROM fishes a
        INNER JOIN dates b ON a.date_id=b.id
        WHERE a.date_id=%s;
        '''
        cursor=conn.cursor()
        cursor.execute(statement, (self.id,))
        fish_records=cursor.fetchall()
        fish_objs=build_from_records(models.FishModel, fish_records)
        return fish_objs


    def to_json(self, conn):
        waterbody_dict=self.__dict__

        fish_classes=self.fish_classes(conn)
        waterbody_dict["fish_classes"]=[fish_class.__dict__ for fish_class in fish_classes]
        return waterbody_dict