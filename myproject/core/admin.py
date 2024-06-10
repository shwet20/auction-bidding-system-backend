def get_model_fields(model, exclude_fields=[]):
    return [
        field.name for field in model._meta.fields if field.name not in exclude_fields
    ]