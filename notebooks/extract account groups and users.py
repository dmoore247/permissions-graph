# Databricks notebook source
# MAGIC %md ## Setup

# COMMAND ----------

# MAGIC %pip install --quiet databricks-sql-connector databricks-sdk botocore

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

import os
from principals import *
from databricks.sdk import AccountClient
from utils import save_graph
from config import *

# COMMAND ----------

token = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiToken().get()


# COMMAND ----------

client = AccountClient(host=account_host, token=token, account_id=account_id)

# COMMAND ----------

# MAGIC %md ## Walk groups

# COMMAND ----------

triples = walk_groups(client=client)
len(triples)

# COMMAND ----------

triples

# COMMAND ----------

# Save to KG
graph_name = "e2-demo groups 20230609"

save_graph(spark, triples, graph_name)

# COMMAND ----------

# MAGIC %md ## Walk Users

# COMMAND ----------

triples, count = walk_users(client)
pp.pprint((count, len(triples), triples))

# COMMAND ----------

len(triples)

# COMMAND ----------

triples_df = spark.createDataFrame(triples)

# COMMAND ----------

triples_df.count()

# COMMAND ----------

display(triples_df)

# COMMAND ----------

# Save to KG
graph_name = "e2-demo users 20230609"

save_graph(spark, triples, graph_name)

# COMMAND ----------


