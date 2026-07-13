import math

class BaseRepository:

    model = None

    @classmethod
    def create(cls, db, obj):
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj
    @classmethod
    def get_by_id(cls, db, id):
        return db.query(cls.model)\
        .filter(cls.model.id == id)\
        .first()
    
    @classmethod
    def delete(cls, db, obj):

        db.delete(obj)

        db.commit()
    @classmethod
    def update(cls, db, obj):

        db.commit()

        db.refresh(obj)

        return obj
    
    def get_all(cls, db):

        return db.query(cls.model).all()
    
    @classmethod
    def paginate(cls, db, params):
        query = db.query(cls.model)
        if params.search:
            query = query.filter(
                cls.model.name.ilike(f"%{params.search}%")
            )
        total = query.count()

        sort_column = getattr(cls.model, params.sort, cls.model.id)

        if params.order.lower() == "desc":
            query = query.order_by(sort_column.desc())
        else:
            query = query.order_by(sort_column.asc())

        offset = (params.page - 1) * params.limit

        items = (
            query
            .offset(offset)
            .limit(params.limit)
            .all()
        )

        return {
            "data": items,
            "pagination": {
                "page": params.page,
                "limit": params.limit,
                "total": total,
                "total_pages": math.ceil(total / params.limit),
                "has_next": params.page < math.ceil(total / params.limit),
                "has_previous": params.page > 1
            }
        }
    