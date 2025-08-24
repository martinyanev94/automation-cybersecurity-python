from cerberus import Validator

schema = {
    'email': {'type': 'string', 'format': 'email'},
    'age': {'type': 'integer', 'min': 0, 'max': 120}
}

v = Validator(schema)

# Test data
document = {'email': 'valid@example.com', 'age': 25}

if v.validate(document):
    print("Validation succeeded.")
else:
    print("Validation failed:", v.errors)
