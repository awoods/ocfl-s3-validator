# OCFL S3 Validator

A Python OCFL Object validator for content in S3.

This validator is a simple wrapper for one small part of the Python OCFL validation utility: [ocfl-py](https://github.com/zimeon/ocfl-py). 
This validator only exposes OCFL Object validation for objects that are stored in an S3 object store.
The validator has been tested with: AWS, Wasabi, and IBM's S3 storage appliance, "ECS".
This validator takes S3 credentials, an optional "endpoint URL" for non-AWS S3 stores, an S3 bucket name, and the S3 path to the [OCFL Object root](https://ocfl.io/1.1/spec/#terminology) of an OCFL Object.
A [validation result](https://github.com/awoods/ocfl-s3-validator/blob/main/src/ocfl_s3_validator/validation_result.py) object is returned for each OCFL Object validation request.

# Usage

1. Create an ObjectValidator with:
    - S3 bucket name
    - S3 access key ID
    - S3 secret access key
    - S3 endpoint URL (optional: needed for non-AWS S3 providers)
2. Invoke 'validate()' method with:
    - S3 path to single OCFL object
3. The 'validate()' method returns a result object with:
    -   object_id (str): The ID of the object.
    -   ocfl_object_path (str): The path to the OCFL object.
    -   validation_status (bool): The status of the validation.
    -   error_message (str): The error message, if any.
    -   validation_timestamp (datetime): The timestamp of the validation.
4. The result object has a JSON representation by calling: 'result.as_json()'

## Example usage
- See object_validator.py '__main__'

```
from ocfl_s3_validator import ObjectValidator

def example():
    # Define variables used below: 'bucket_name', 'access_key_id', etc

    validator = ObjectValidator(bucket_name,
        access_key_id,
        secret_access_key,
        endpoint_url)
    result = validator.validate(object_id, object_path)

    print(result.as_json())
```

# Developer quick start

A quick set of commands to run after initial cloning this repository

```
uv venv --python 3.12.0
source .venv/bin/activate
uv sync
pytest
```