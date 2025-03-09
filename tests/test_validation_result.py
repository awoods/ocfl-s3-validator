from datetime import datetime
import json
import pytest
from ocfl_s3_validator.validation_result import ValidationResult


def test_validation_result_init_success():
    obj_id = "test_object_id"
    ocfl_path = "test/ocfl/path"
    result = ValidationResult(obj_id, ocfl_path)

    assert result.object_id == obj_id
    assert result.ocfl_object_path == ocfl_path
    assert result.validation_status is False
    assert result.error_message is None
    assert result.validation_timestamp is not None

    # Parse the timestamp from the instance
    today = datetime.now()
    result_timestamp = datetime.fromisoformat(result.validation_timestamp)
    assert result_timestamp.year == today.year
    assert result_timestamp.month == today.month
    assert result_timestamp.day == today.day


def test_validation_result_init_missing_object_id():
    ocfl_path = "test/ocfl/path"
    with pytest.raises(ValueError, match="object_id is required"):
        ValidationResult(object_id=None, ocfl_object_path=ocfl_path)


def test_validation_result_init_missing_ocfl_object_path():
    obj_id = "test_object_id"
    with pytest.raises(ValueError, match="ocfl_object_path is required"):
        ValidationResult(object_id=obj_id, ocfl_object_path=None)


def test_validation_result_as_json():
    obj_id = "test_object_id"
    ocfl_path = "test/ocfl/path"
    result = ValidationResult(object_id=obj_id, ocfl_object_path=ocfl_path)
    result.validation_status = True
    result.error_message = "No error"
    result.validation_timestamp = "2023-10-04T12:00:00Z"

    expected_json = json.dumps({
        "object_id": obj_id,
        "ocfl_object_path": ocfl_path,
        "validation_status": True,
        "error_message": "No error",
        "validation_timestamp": "2023-10-04T12:00:00Z"
    })

    assert result.as_json() == expected_json
