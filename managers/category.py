from db import db
from models import CategoryModel


class CategoryManager:
    @staticmethod
    def create(data, admin):
        data["admin_id"] = admin.id
        category = CategoryModel(**data)
        db.session.add(category)

        return category