def categoryEntity(item) -> dict:
    return {
        "id": item["_id"],
        "name": item["name"],
    }


def categoriesEntity(entity) -> list:
    [categoryEntity(item) for item in entity]
