import graphene
from flask import current_app, g
from btb.api.models import db
from sqlalchemy import text
from promise import Promise
from promise.dataloader import DataLoader


class IndustryLoader(DataLoader):
    def batch_load_fn(self, keys):
        current_app.logger.debug("load %s", keys)

        with db.engine.begin() as conn:
            sql = text(
                """
select 
    *
from 
    btb_data.industry
where 
    id = any(cast(:keys as uuid[]))
and is_active = True
"""
            )
            data = conn.execute(sql, keys=keys)

            d = {str(i["id"]): i for i in data}

            # must return result in same order
            return Promise.resolve([d.get(str(id), None) for id in keys])


def industries(root, info):
    current_app.logger.debug("skills")

    with db.engine.begin() as conn:
        sql = text(
            """
select 
    *
from 
    btb_data.industry
where
    is_active = True
"""
        )
        result = conn.execute(sql)
        return result.fetchall()
