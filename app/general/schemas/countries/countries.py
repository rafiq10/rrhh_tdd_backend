import graphene
from db.db import engine, my_session, get_json_by_sql

class CountryModel(graphene.ObjectType, country=graphene.String(required=False)):
  country = graphene.String()
  bankCode = graphene.String()
  bankCheckDigits = graphene.String()

def get_countries(country=''):
  print('in')
  my_sql ='select countryEsp as country, countryBankCode as bankCode, bankCheckDigits from tblCountriesEsp'
  print(country)
  if not (country == ''):
    my_sql = my_sql + " where countryEsp = '"+ country + "'"

  return get_json_by_sql(my_sql)
