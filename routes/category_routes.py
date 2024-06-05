from fastapi import APIRouter
from config.db import conn
from models.category_model import Category
from schema.category_schemas import categoriesEntity

categories = APIRouter()


@categories.get("/categories")
def get_categories():
    categories = conn.local.category.find()
    result = []
    for category in categories:
        category["_id"] = str(category["_id"])
        for question in category.get("questions", []):
            question["_id"] = str(question["_id"])
            answer_id = None
            for answer in question["answers"]:
                if answer["is_answer"]:
                    answer_id = str(answer["_id"])
                answer["_id"] = str(answer["_id"])
            question["answer_id"] = answer_id
        result.append(category)
    return result


@categories.post("/categories/add")
def create_category(category: Category):
    new_category = dict(category)
    id = conn.local.category.insert_one(new_category).inserted_id
    return str(id)
