from fastapi import Depends, HTTPException, APIRouter
from bson.objectid import ObjectId
from config.db import conn
from models.category_model import NewQuestion


questions = APIRouter()


@questions.post("/questions/add")
def add_question(new_question: NewQuestion):
    category_id = new_question.category_id
    question_data = {
        "_id": ObjectId(),
        "question": new_question.question,
        "answers": [
            {"_id": ObjectId(), **answer.dict()} for answer in new_question.answers
        ],
    }

    result = conn.local.category.update_one(
        {"_id": ObjectId(category_id)}, {"$push": {"questions": question_data}}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Category not found")

    updated_category = conn.local.category.find_one({"_id": ObjectId(category_id)})
    if updated_category:
        updated_category["_id"] = str(updated_category["_id"])
        updated_category["questions"] = [
            {
                **question,
                "_id": str(question["_id"]) if "_id" in question else None,
                "answers": [
                    {**answer, "_id": str(answer["_id"])}
                    for answer in question.get("answers", [])
                ],
            }
            for question in updated_category.get("questions", [])
        ]
    return updated_category
