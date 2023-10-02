from api.lib.db import build_from_record, build_from_records
import api.models as models


class FishModel:
    __table__="fishes"
    __constraint__ = "unique_fishes"
    columns=["id", "waterbody_id", "date_id", "species_name", "size_inches", "number"]

    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            if k not in self.columns:
                raise ValueError(f"{k} not in {self.columns}")
            setattr(self, k, v)


    def date_classes(self, conn):
        statement='''
        SELECT DISTINCT(a.*)
        FROM dates a
        INNER JOIN fishes b ON a.id=b.date_id
        WHERE a.id=%s;
        '''
        cursor=conn.cursor()
        cursor.execute(statement, (self.date_id,))
        date_records=cursor.fetchall()
        date_objs=build_from_records(models.DateModel, date_records)
        return date_objs

    def waterbody_classes(self, conn):
        statement='''
        SELECT DISTINCT(a.*)
        FROM waterbodies a
        INNER JOIN fishes b ON a.id=b.waterbody_id
        WHERE a.id=%s;
        '''
        cursor=conn.cursor()
        cursor.execute(statement, (self.waterbody_id,))
        waterbody_records=cursor.fetchall()
        waterbody_objs=build_from_records(models.WaterbodyModel, waterbody_records)
        return waterbody_objs

    def to_json(self, conn):
        fish_dict=self.__dict__

        date_classes=self.date_classes(conn)
        fish_dict["date_classes"]=[date_class.__dict__ for date_class in date_classes]

        waterbody_classes=self.waterbody_classes(conn)
        fish_dict["waterbody_classes"]=[waterbody_class.__dict__ for waterbody_class in waterbody_classes]

        return fish_dict