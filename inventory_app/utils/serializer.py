from bson import ObjectId


def serialize_doc(doc):
    if not doc:
        return doc

    doc["_id"] = str(doc["_id"])

    for key, value in doc.items():
        if isinstance(value, ObjectId):
            doc[key] = str(value)

        if isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    for k, v in item.items():
                        if isinstance(v, ObjectId):
                            item[k] = str(v)

    return doc


def serialize_list(docs):
    return [serialize_doc(doc) for doc in docs]