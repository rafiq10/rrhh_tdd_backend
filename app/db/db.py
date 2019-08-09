import sys
sys.path.append(".")

from sqlalchemy import create_engine
from sqlalchemy.orm import (scoped_session, sessionmaker, Session)
from general.utils.json.json import json2obj

engine = create_engine('mssql+pymssql://Rafal:Rfl2206@datacluster/TIS_FinanzasGlobal')

my_session = Session(bind=engine)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

def get_json_by_sql(my_sql):
  d, a = {}, []
                                              
  sess = my_session
  result = sess.execute(my_sql,{})
  for rowproxy in result:
    for column, value in rowproxy.items():
      d = {**d, **{column: value}}
    a.append(d)
                                          
  return json2obj(a) 