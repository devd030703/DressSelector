import os
from sqlalchemy import create_engine


def get_engine():
    user = os.environ['FOOTFALL_USERNAME']
    password = os.environ['FOOTFALL_PWD']
    host = 'main-cluster.czbkyyrppxdz.eu-west-1.redshift.amazonaws.com'
    dbname = 'footfall'

    return create_engine(
        f"postgresql+psycopg2://{user}:{password}@{host}/{dbname}?port=5439"
    )
