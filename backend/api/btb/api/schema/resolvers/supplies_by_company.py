from graphene import ID, String, ObjectType
from flask import g
from btb.api.models import db
from sqlalchemy import text


def supplies_by_company(root, info):
    with db.engine.begin() as conn:
        result = conn.execute(
            text("select * from btb_data.team_supply where company_id = :id"), id=root["id"]
        )

        return result.fetchall()
