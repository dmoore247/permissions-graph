from config import ACCOUNT_HOST, ACCOUNT_ID, HOST, TRIPLE_STORE
from databricks.sdk import AccountClient

client = AccountClient(host=account_host, token=token, account_id=account_id)



