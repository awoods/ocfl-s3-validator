

import os

import ocfl

from ocfl_s3_validator.validation_result import ValidationResult

class ObjectValidator:
    """
    A class to validate objects stored in an S3 bucket using the OCFL validator.
    Attributes:
        bucket_name (str): The name of the S3 bucket.
        validator (ocfl.Validator): An instance of the OCFL Validator.
    Methods:
        validate(path: str) -> bool:
            Validates the object at the given path in the S3 bucket.

    Author: awoods
    Since: 2023-10-04
    """

    def __init__(self,
                 bucket_name: str,
                 access_key_id: str,
                 secret_access_key: str,
                 endpoint_url: str=None):
        """
        Initializes the ObjectValidator with the given S3 bucket credentials.
        Args:
            bucket_name (str): The name of the S3 bucket.
            access_key_id (str): The AWS access key ID.
            secret_access_key (str): The AWS secret access key.
            endpoint_url (str, optional): The custom endpoint URL for the S3 service. Defaults to None.
        Raises:
            ValueError: If any of the required arguments (bucket_name, access_key_id, secret_access_key) are None.
        """
        
        if bucket_name is None:
            raise ValueError("bucket_name is required")
        if access_key_id is None:
            raise ValueError("access_key_id is required")
        if secret_access_key is None:
            raise ValueError("secret_access_key is required")
        
        os.environ['AWS_ACCESS_KEY_ID'] = access_key_id
        os.environ['AWS_SECRET_ACCESS_KEY'] = secret_access_key
        if endpoint_url is not None:
            os.environ['AWS_ENDPOINT_URL'] = endpoint_url

        self.bucket_name = bucket_name
        self.ocfl_validator = ocfl.Validator()

    def validate(self, object_id: str, path: str) -> bool:
        """
        Validates the object at the given path in the S3 bucket.
        Args:
            path (str): The path to the object in the S3 bucket.
        Returns:
            ValidationResult: The result of the validation.
        Raises:
            ValueError: If the path is None.
        """
        result = ValidationResult(object_id, path)
        
        if path is None:
            raise ValueError("path is required")
        
        is_valid = self.ocfl_validator.validate(f"s3://{self.bucket_name}/{path}")
        if not is_valid:
            result.validation_status = False
            result.error_message = f"{self.ocfl_validator}"
        else:
            result.validation_status = True

        return result
    

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()

    bucket_name = os.getenv("EXAMPLE_BUCKET_NAME")
    access_key_id = os.getenv("EXAMPLE_AWS_ACCESS_KEY_ID")
    secret_access_key = os.getenv("EXAMPLE_AWS_SECRET_ACCESS_KEY")
    endpoint_url = os.getenv("EXAMPLE_AWS_ENDPOINT_URL")
    object_id = os.getenv("EXAMPLE_ID")
    object_path = os.getenv("EXAMPLE_PATH")

    validator = ObjectValidator(bucket_name,
                                access_key_id,
                                secret_access_key,
                                endpoint_url)
    result = validator.validate(object_id, object_path)

    print(result.as_json())