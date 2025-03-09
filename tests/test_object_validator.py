import os
from ocfl_s3_validator.object_validator import ObjectValidator
import pytest
from unittest.mock import MagicMock, patch


class TestObjectValidator:

    @pytest.fixture(autouse=True)
    def clear_env_vars(monkeypatch):
        """
        Automatically clear specific environment variables after each test.
        """
        yield  # Run the test first
        os.environ.pop("AWS_ACCESS_KEY_ID", None)
        os.environ.pop("AWS_SECRET_ACCESS_KEY", None)
        os.environ.pop("AWS_ENDPOINT_URL", None)

    def test_valid(self):
        validator = ObjectValidator("bucket",
                                    "access-key",
                                    "secret-key",
                                    "endpoint-url")

        # Mock the validate method
        validator.ocfl_validator.validate = MagicMock(return_value=True)

        result = validator.validate("id", "path")
        assert result.validation_status, "'result' should be 'true'"
        validator.ocfl_validator.validate.assert_called_once_with(
            "s3://bucket/path")

    def test_invalid(self):
        validator = ObjectValidator("bucket",
                                    "access-key",
                                    "secret-key",
                                    "endpoint-url")

        # Mock the validate method
        validator.ocfl_validator.validate = MagicMock(return_value=False)

        result = validator.validate("id", "path")
        assert not result.validation_status, "'result' should be 'false'"
        validator.ocfl_validator.validate.assert_called_once_with(
            "s3://bucket/path")

    def test_init_success(self):
        with patch('ocfl.Validator') as MockValidator:
            validator = ObjectValidator("bucket-name",
                                        "access-key",
                                        "secret-key",
                                        "endpoint-url")
            assert validator.bucket_name == "bucket-name"
            assert validator.ocfl_validator == MockValidator.return_value
            assert os.environ['AWS_ACCESS_KEY_ID'] == "access-key"
            assert os.environ['AWS_SECRET_ACCESS_KEY'] == "secret-key"
            assert os.environ['AWS_ENDPOINT_URL'] == "endpoint-url"

    def test_init_success_no_endpoint(self):
        with patch('ocfl.Validator') as MockValidator:
            validator = ObjectValidator("bucket-name",
                                        "access-key",
                                        "secret-key")
            assert validator.bucket_name == "bucket-name"
            assert validator.ocfl_validator == MockValidator.return_value
            assert os.environ['AWS_ACCESS_KEY_ID'] == "access-key"
            assert os.environ['AWS_SECRET_ACCESS_KEY'] == "secret-key"
            assert 'AWS_ENDPOINT_URL' not in os.environ

    def test_init_missing_bucket_name(self):
        with pytest.raises(ValueError, match="bucket_name is required"):
            ObjectValidator(None, "access-key", "secret-key")

    def test_init_missing_access_key_id(self):
        with pytest.raises(ValueError, match="access_key_id is required"):
            ObjectValidator("bucket-name", None, "secret-key")

    def test_init_missing_secret_access_key(self):
        with pytest.raises(ValueError, match="secret_access_key is required"):
            ObjectValidator("bucket-name", "access-key", None)
