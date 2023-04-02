


#Build instances from records
def build_from_record(Class, record):
    if not record: return None

    obj=Class()
    attr=dict(zip(Class.columns, record))
    obj.__dict__=attr
    return obj

def build_from_records(Class, records):
    return [build_from_record(Class, record) for record in records]
