# Databricks notebook source
from rdflib.plugins.sparql import parser, algebra

def extract_triples(query_algebra):
    # Get the WHERE clause
    where_clause = query_algebra.where
    # Get the triple patterns from the WHERE clause
    tp = []
    for clause in where_clause:
        if clause.name == "BGP":
            tp += list(clause.triples)
    return tp

statement = "SELECT ?s ?p ?o WHERE {?s ?p ?o.}"
query_tree = parser.parseQuery(statement)
q_algebra = algebra.translateQuery(query_tree)

triples = extract_triples(q_algebra)
print(triples)

# COMMAND ----------

#bgp1.py
from rdflib.plugins.sparql import parser, algebra

def translate_bgp_to_sql(bgp):
    sql = "SELECT * FROM triples"
    for s, p, o in bgp.triples:
        if isinstance(s, algebra.Variable):
            sql += f" JOIN triples AS {s.n3()}_{p.n3()}_{o.n3()} ON subject={s.n3()}"
        if isinstance(p, algebra.Variable):
            sql += f" JOIN triples AS {s.n3()}_{p.n3()}_{o.n3()} ON predicate={p.n3()}"
        if isinstance(o, algebra.Variable):
            sql += f" JOIN triples AS {s.n3()}_{p.n3()}_{o.n3()} ON object={o.n3()}"
    return sql

statement = "SELECT ?s ?p ?o WHERE {?s ?p ?o.}"
query_tree = parser.parseQuery(statement)
q_algebra = algebra.translateQuery(query_tree)

bgp = q_algebra.algebra.keys()

#sql_query = translate_bgp_to_sql(bgp)
#print(sql_query)


# COMMAND ----------

# MAGIC %pip install --quiet rdflib

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

def extract_triples(query_algebra):
    # Get the WHERE clause
    where_clause = query_algebra["where"]
    # Get the triple patterns from the WHERE clause
    tp = []
    for clause in where_clause:
        if clause["type"] == "bgp":
            tp += clause["triples"]
    return tp

# COMMAND ----------

from rdflib.plugins.sparql import parser, algebra
statement = "SELECT ?s ?p ?o WHERE {?s ?p ?o.}"
query_tree = parser.parseQuery(statement)
q_algebra = algebra.translateQuery(query_tree)

triples = extract_triples(q_algebra)
print(triples)

# COMMAND ----------

#create table triples(s STRING, p STRING, o STRING);

tables = {'t0': [('id', 's')], 't1': [('cluster_id', 'o')], 't2': [('id', 's'), ('name', 'o')], 't3': [('id', 's'), ('email', 'o')]}



# COMMAND ----------


