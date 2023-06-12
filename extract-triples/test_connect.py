from unittest import TestCase
import pytest
import sys
import os

import logging, sys
logging.basicConfig(stream=sys.stderr,
                    level=logging.INFO,
                    format='%(asctime)s [%(name)s][%(levelname)s] %(message)s')
logging.getLogger('databricks.sdk').setLevel(logging.INFO)

class TestConnect(TestCase):
    
    def test_environment_setup(self):
        self.assertIsNotNone(os.getenv("DATABRICKS_CONFIG_PROFILE"))

    def test_connect_workspace(self):
        from databricks.sdk import WorkspaceClient
        client = WorkspaceClient(profile='E2DEMO')
        self.assertIsNotNone(client)
        
    def test_connect_workspace_group_verification(self):
        from databricks.sdk import WorkspaceClient
        client = WorkspaceClient(profile='E2DEMO')
        self.assertIsNotNone(client)
        groups = client.groups.list(count=2)
        self.assertIsNotNone(groups)
        
    def test_connect_account(self):
        from databricks.sdk import AccountClient
        client = AccountClient(profile='E2CERT')
        self.assertIsNotNone(client)
        
    def test_connect_account_group_verification(self):
        from databricks.sdk import AccountClient
        client = AccountClient(profile='E2CERT')
        self.assertIsNotNone(client)
        groups = client.groups.list(count=2)
        self.assertIsNotNone(groups)
    