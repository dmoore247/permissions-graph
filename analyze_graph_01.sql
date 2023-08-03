-- Databricks notebook source
use main.triplestore

-- COMMAND ----------

truncate TABLE main.triplestore.raw_quads

-- COMMAND ----------

desc main.triplestore.raw_quads

-- COMMAND ----------

select * from raw_quads

-- COMMAND ----------

-- DBTITLE 1,Distinct graphs
select distinct g from raw_quads

-- COMMAND ----------

select * from raw_quads where g = 'ex:graph_account_users'

-- COMMAND ----------

INSERT INTO raw_quads(s,p,o,g)
SELECT DISTINCT s,p,o,'ex:mine' from raw_quads

-- COMMAND ----------

select count(1) from raw_quads where g = 'ex:mine'

-- COMMAND ----------

select s,p,o from raw_quads where g = 'ex:mine'

-- COMMAND ----------

-- DBTITLE 1,Predicates
with graph AS (select s,p,o from raw_quads where g = 'ex:mine')
select distinct p from graph



-- COMMAND ----------

with graph AS (select s,p,o from raw_quads where g = 'ex:mine')
select DISTINCT graph.*, r1.p, r1.o
from graph
JOIN graph r1 ON r1.s = graph.s
where graph.p = 'dbx:memberOf'
order by graph.s, graph.p, graph.o, r1.p

-- COMMAND ----------

select distinct 
  q.s, q.p, q.o, r1.p, r1.o
from raw_quads q
JOIN (select s,p,o from raw_quads where p = 'dbx:instanceProfile' and g = 'ex:mine') r1 ON r1.s = q.s
where 
q.g = 'ex:mine' and
q.p = 'dbx:email'


-- COMMAND ----------


