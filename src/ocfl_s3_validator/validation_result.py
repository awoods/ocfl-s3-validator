import json
from datetime import datetime


class ValidationResult:
    """
    Represents the result of a validation process.
    Attributes:
        object_id (str): The ID of the object.
        ocfl_object_path (str): The path to the OCFL object.
        validation_status (bool): The status of the validation.
        error_message (str): The error message, if any.
        validation_timestamp (datetime): The timestamp of the validation.

    Author: awoods
    Since: 2023-10-04
    """
    def __init__(self, object_id: str, ocfl_object_path: str):
        """
        Initializes the ValidationResult with the given object ID and OCFL object path.
        Args:
            object_id (str): The ID of the object.
            ocfl_object_path (str): The path to the OCFL object.
        Raises:
            ValueError: If any of the required arguments (object_id, ocfl_object_path) are None.
        """
        if object_id is None:
            raise ValueError("object_id is required")
        if ocfl_object_path is None:
            raise ValueError("ocfl_object_path is required")
        
        self.object_id = object_id
        self.ocfl_object_path = ocfl_object_path
        self.validation_status = False
        self.error_message = None
        self.validation_timestamp = datetime.now().replace(microsecond=0).isoformat()

    def __str__(self):
        return f"ValidationResult(object_id={self.object_id}, "\
        f"ocfl_object_path={self.ocfl_object_path}, "\
        f"validation_status={self.validation_status}, "\
        f"error_message={self.error_message}, "\
        f"validation_timestamp={self.validation_timestamp})"

    def __repr__(self):
        return self.__str__()
    
    def as_json(self):
        """
        Returns a JSON representation of the ValidationResult.
        Returns:
            str: A JSON string representing the ValidationResult.
        """
        return json.dumps(self.__dict__)