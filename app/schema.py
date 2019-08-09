from general.utils.json.json import json2obj
import json
from collections import namedtuple
import graphene

from graphene_sqlalchemy import SQLAlchemyObjectType
from db.db import engine, my_session
from general.schemas.schema import CountryModel, get_countries, UserModel, get_users
from config_combos.schema import CombosModel, get_combo_tables


class CustomQueries(graphene.ObjectType):
  countries = graphene.List(CountryModel, country=graphene.String(required=False))
  combo_tables = graphene.List(CombosModel)
  users = graphene.List(UserModel)

  def resolve_users(self, args=None):
    return get_users()

  def resolve_countries(self, info, country=''):
    return get_countries(country)

  def resolve_combo_tables(self, args=None):
    return get_combo_tables()


schema = graphene.Schema(query = CustomQueries)