from api.lib.db import build_from_record, build_from_records
import api.models as models


class DateModel:
    __table__="dates"
    __constraint__ = "unique_dates"
    columns=["id", "month", "year"]

    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            if k not in self.columns:
                raise ValueError(f"{k} not in {self.columns}")
            setattr(self, k, v)


    def fish_classes(self, conn):
        #Return all the associated fishes restocked on the specified date
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
        date_dict=self.__dict__

        fish_classes=self.fish_classes(conn)
        date_dict["fish_classes"]=[fish_class.__dict__ for fish_class in fish_classes]
        return date_dict

