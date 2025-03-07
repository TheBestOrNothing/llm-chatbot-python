import streamlit as st

# Connect to Neo4j

# pip3 install neo4j-driver
# python3 example.py

from neo4j import GraphDatabase, basic_auth

driver = GraphDatabase.driver(
  "neo4j://54.87.252.41:7687",
  auth=basic_auth("neo4j", "chokes-cockpits-helmsmen"))

cypher_query = '''
MATCH (m:Movie {title:$movie})<-[:RATED]-(u:User)-[:RATED]->(rec:Movie)
RETURN distinct rec.title AS recommendation LIMIT 20
'''

with driver.session(database="neo4j") as session:
  results = session.read_transaction(
    lambda tx: tx.run(cypher_query,
                      movie="Crimson Tide").data())
  for record in results:
    print(record['recommendation'])

driver.close()
