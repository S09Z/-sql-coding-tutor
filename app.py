import os
import torch
import streamlit as st
from langchain.llms import LlamaCpp
from sqlglot import parse_one, transpile
from chromadb import Client as ChromaClient
import psycopg2
import unittest

# PostgreSQL Connection
PG_CONNECTION = "dbname=sql_tutor user=postgres password=yourpassword host=localhost port=5432"

def load_llama():
    """Load LLaMA model using LlamaCpp."""
    return LlamaCpp(model_path="./models/llama-2-7b.Q4_0.gguf", temperature=0.5)

llama = load_llama()

def optimize_sql(query: str) -> str:
    """Optimize SQL query using SQLGlot."""
    try:
        parsed_query = parse_one(query)
        optimized_query = transpile(parsed_query, dialect="postgres")
        return optimized_query[0]
    except Exception as e:
        return f"Error optimizing SQL: {e}"

def run_explain_analyze(query: str) -> str:
    """Run EXPLAIN ANALYZE on PostgreSQL query."""
    try:
        with psycopg2.connect(PG_CONNECTION) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"EXPLAIN ANALYZE {query}")
                result = cursor.fetchall()
                return "\n".join([row[0] for row in result])
    except Exception as e:
        return f"Error running EXPLAIN ANALYZE: {e}"

def tutor_best_practices(sql_query: str) -> str:
    """Generate best practice suggestions for SQL queries."""
    prompt = f"""
    Analyze the following PostgreSQL query and suggest optimizations for best practices:
    
    {sql_query}
    
    Provide a detailed explanation and a refactored version.
    """
    return llama.generate(prompt)

# Streamlit UI
def main():
    st.title("🧠 AI-Powered PostgreSQL Coding Tutor")
    st.header("PostgreSQL Optimization & Best Practices")
    sql_input = st.text_area("Enter your PostgreSQL Query:")
    if st.button("Analyze SQL"):
        optimized_query = optimize_sql(sql_input)
        best_practices = tutor_best_practices(sql_input)
        explain_output = run_explain_analyze(sql_input)
        
        st.subheader("Optimized Query:")
        st.code(optimized_query, language="sql")
        
        st.subheader("Best Practices Suggestions:")
        st.write(best_practices)
        
        st.subheader("EXPLAIN ANALYZE Output:")
        st.code(explain_output, language="sql")

if __name__ == "__main__":
    main()
