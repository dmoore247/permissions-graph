import pytest
from databricks.connect import DatabricksSession
from databricks.sdk.core import Config
from databricks.sdk import WorkspaceClient, AccountClient

from extract_principals import extract_principals

@pytest.fixture(scope="session")
def get_spark():
    config = Config()
    print(config)
    assert config
    spark = DatabricksSession.builder.sdkConfig(config).getOrCreate()
    yield spark

class TestExtract:
    def test_get_spark(self, get_spark):
        spark = get_spark
        assert spark is not None
        assert spark.version == "3.4.0"
        assert spark.range(10) is not None

    def test_extract_account(self, get_spark):
        spark = get_spark
        # Setup connections
        clients = [
            {
                "name": "account",
                "client": AccountClient(profile="E2CERT")
            }
            ]
        counter = extract_principals(spark=spark, clients=clients)
        assert counter == 2

    def test_extract_workspace(self, get_spark):
        spark = get_spark
        # Setup connections
        clients = [
            {
                "name": "workspace",
                "client": WorkspaceClient(profile="E2DEMO")
            }
            ]
        counter = extract_principals(spark=spark, clients=clients)
        assert counter == 2

