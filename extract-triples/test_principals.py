from unittest import TestCase

class TestPrincipals(TestCase):
    def test_import(self):
        from principals import walk_groups, get_group_triples, get_group_member_triples
        from principals import walk_users, get_user_triples
        self.assertTrue(True)
   
    def test_get_account_connect(self):
        from principals import walk_groups
        from databricks.sdk import AccountClient
        client = AccountClient(profile="E2CERT")
        assert client.config.account_id is not None
        assert client.config.host is not None
        client.groups.list(count=2) is None   
    
    def test_get_account_group(self):
        from principals import walk_groups
        from databricks.sdk import AccountClient
        client = AccountClient(profile="E2CERT")
        self.assertIsNotNone(client.config.account_id)
        triples = walk_groups(client)
        self.assertIsInstance(triples, list)
        self.assertTrue(len(triples) > 10)
        
    def test_get_account_users(self):
        from principals import walk_users
        from databricks.sdk import AccountClient
        client = AccountClient(profile="E2CERT")
        self.assertIsNotNone(client.config.account_id)
        triples = walk_users(client)
        self.assertIsInstance(triples[:50], list)
        self.assertIsInstance(triples[0], tuple)
        self.assertGreater(len(triples), 1)
       