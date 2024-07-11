-- Databricks notebook source
CREATE EXTERNAL LOCATION IF NOT EXISTS `oetrta_dmoore`
URL 's3://oetrta/dmoore'
WITH (STORAGE CREDENTIAL `one_env_external_location`)

-- COMMAND ----------

use catalog douglas_moore;
use schema demo;
show create table douglas_moore.demo.bronze_cluster_events;

-- COMMAND ----------

show external locations;

-- COMMAND ----------

-- MAGIC %fs mkdirs 's3://oetrta/dmoore/databases/drop_zone'

-- COMMAND ----------

LIST 's3://oetrta/dmoore/databases'

-- COMMAND ----------

-- MAGIC %md # Create external schema, tables and views

-- COMMAND ----------

DROP SCHEMA IF EXISTS douglas_moore.drop_zone_ext CASCADE;
DROP SCHEMA IF EXISTS hive_metastore.drop_zone_ext CASCADE;
DROP SCHEMA IF EXISTS douglas_moore.drop_zone CASCADE;
DROP SCHEMA IF EXISTS hive_metastore.drop_zone CASCADE;

-- COMMAND ----------

-- MAGIC %md ## Schemas

-- COMMAND ----------

CREATE SCHEMA IF NOT EXISTS hive_metastore.drop_zone_ext
LOCATION 's3://oetrta/dmoore/databases/drop_zone';

-- COMMAND ----------

CREATE SCHEMA IF NOT EXISTS douglas_moore.drop_zone_ext
MANAGED LOCATION 's3://oetrta/dmoore/databases/drop_zone';

-- COMMAND ----------

show schemas in douglas_moore

-- COMMAND ----------

show schemas in hive_metastore like 'drop*'

-- COMMAND ----------

-- MAGIC %md ## Tables

-- COMMAND ----------

CREATE OR REPLACE TABLE hive_metastore.drop_zone_ext.table1 
LOCATION 's3://oetrta/dmoore/databases/drop_zone/table1' 
AS 
SELECT * FROM range(10);

-- COMMAND ----------

CREATE OR REPLACE TABLE douglas_moore.drop_zone_ext.table1 
LOCATION 's3://oetrta/dmoore/databases/drop_zone/table1'

-- COMMAND ----------

CREATE OR REPLACE TABLE hive_metastore.drop_zone_ext.table2
LOCATION 's3://oetrta/dmoore/databases/drop_zone/table2'
AS 
SELECT * FROM range(10);

alter table hive_metastore.drop_zone_ext.table2 SET OWNER TO `douglas.moore@databricks.com`;

-- COMMAND ----------

alter table hive_metastore.drop_zone_ext.table1 SET OWNER TO `douglas.moore@databricks.com`;
alter table hive_metastore.drop_zone_ext.table2 SET OWNER TO `douglas.moore@databricks.com`;
alter table hive_metastore.drop_zone_ext.table3 SET OWNER TO `douglas.moore@databricks.com`;

-- COMMAND ----------

show grants on hive_metastore.drop_zone_ext.table1;

-- COMMAND ----------

show grants on douglas_moore.drop_zone_ext.table1;

-- COMMAND ----------



-- COMMAND ----------

CREATE OR REPLACE TABLE hive_metastore.drop_zone_ext.table3
LOCATION 's3://oetrta/dmoore/databases/drop_zone/table3'
AS
SELECT * FROM range(10);

-- COMMAND ----------

SET spark.databricks.sync.command.enableManagedTable=true;

USE CATALOG douglas_moore;
USE douglas_moore.drop_zone_ext;

-- COMMAND ----------

SYNC SCHEMA douglas_moore.drop_zone_ext 
FROM hive_metastore.drop_zone_ext
SET OWNER `douglas.moore@databricks.com`
DRY RUN;

-- COMMAND ----------

SYNC SCHEMA douglas_moore.drop_zone_ext 
FROM hive_metastore.drop_zone_ext
SET OWNER `douglas.moore@databricks.com`;

-- COMMAND ----------

DESCRIBE EXTENDED hive_metastore.drop_zone_ext.table2

-- COMMAND ----------



-- COMMAND ----------

DESCRIBE EXTENDED douglas_moore.drop_zone_ext.table2

-- COMMAND ----------

show tables in douglas_moore.drop_zone_ext;

-- COMMAND ----------

show tables in hive_metastore.drop_zone_ext;

-- COMMAND ----------

-- MAGIC %md # Test UC to HMS sync scenarios

-- COMMAND ----------

show tables in hive_metastore.drop_zone_ext;

-- COMMAND ----------

-- MAGIC %md REVERSE SYNC
-- MAGIC for every 'external' {table} in <catalog>.<schema> || <table list>:
-- MAGIC   location = table.location
-- MAGIC   statement = CREATE TABLE IF NOT EXISTS hive_metastore.<schema>.<table> LOCATION {location}

-- COMMAND ----------

-- drop table hive_metastore.drop_zone_ext.table1;

CREATE TABLE IF NOT EXISTS hive_metastore.drop_zone_ext.table1
LOCATION 's3://oetrta/dmoore/databases/drop_zone/table1';

describe extended hive_metastore.drop_zone_ext.table1;

-- COMMAND ----------

-- MAGIC %md ## What is in tables system schema

-- COMMAND ----------

select * from system.information_schema.tables

-- COMMAND ----------

-- MAGIC %md # Use cloud native paths

-- COMMAND ----------

-- MAGIC %fs ls s3://oetrta/sandboxes/douglas_moore/demo/sandbox1

-- COMMAND ----------

-- MAGIC %python 
-- MAGIC dbutils.fs.put('s3://oetrta/sandboxes/douglas_moore/demo/sandbox1/test.txt', 'If you find this then you have found  meaning')

-- COMMAND ----------

-- MAGIC %sh 
-- MAGIC ls /Volumes/douglas_moore/demo/sandbox1
-- MAGIC cat /Volumes/douglas_moore/demo/sandbox1/test.txt

-- COMMAND ----------

-- MAGIC %python
-- MAGIC try:
-- MAGIC     spark.read.format('text').load('s3://oetrta/sandboxes/douglas_moore/demo/sandbox1/test.txt').show()
-- MAGIC except Exception as e:
-- MAGIC     print(e)

-- COMMAND ----------

SHOW GRANTS ON VOLUME douglas_moore.demo.sandbox1

-- COMMAND ----------


