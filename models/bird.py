import enum
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, Enum, ForeignKeyConstraint, func
#longtext found from this link https://stackoverflow.com/questions/61684135/how-to-represent-longtext-in-sqlalchemy
from sqlalchemy.dialects.mysql import LONGTEXT
db = SQLAlchemy()