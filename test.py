import unittest
from app import optimize_sql, tutor_best_practices, run_explain_analyze

class TestCodingTutor(unittest.TestCase):
    def test_sql_optimization(self):
        query = "SELECT * FROM users WHERE email = 'test@example.com';"
        optimized_query = optimize_sql(query)
        self.assertIn("SELECT", optimized_query)
        
    def test_best_practices_sql(self):
        sql_query = "SELECT * FROM orders WHERE order_date > '2023-01-01';"
        response = tutor_best_practices(sql_query)
        self.assertIn("INDEX", response)

    def test_explain_analyze(self):
        query = "SELECT * FROM users WHERE email = 'test@example.com';"
        explain_output = run_explain_analyze(query)
        self.assertIn("Seq Scan", explain_output)

if __name__ == "__main__":
    unittest.main()
