import graphene
from db.db import engine, my_session, get_json_by_sql


class UserModel(graphene.ObjectType):
  TF = graphene.String()
  country = graphene.String()
  fullName = graphene.String()

  import graphene
from db.db import engine, my_session, get_json_by_sql


def get_users():
    my_sql ='select * from tblUsers2'
    
    return get_json_by_sql(my_sql)