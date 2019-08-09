import graphene
from db.db import engine, my_session, get_json_by_sql


class CombosModel(graphene.ObjectType):
  TABLE_NAME = graphene.String()

def get_combo_tables():
  my_sql = """SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES 
              WHERE
                TABLE_CATALOG = 'TIS_FinanzasGlobal' 
                and TABLE_TYPE='BASE TABLE'
                and left(TABLE_NAME,8) = 'RRHH_cmb'
              order by TABLE_NAME"""
  
  return get_json_by_sql(my_sql)