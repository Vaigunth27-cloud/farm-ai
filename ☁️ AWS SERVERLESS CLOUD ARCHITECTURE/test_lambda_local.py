import os
import sys
import json
import unittest

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

# Add lambda directory to sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "lambda"))
from lambda_function import lambda_handler

class TestUrbanServerlessApi(unittest.TestCase):
    def test_health_check(self):
        event = {
            "rawPath": "/health",
            "requestContext": {"http": {"method": "GET"}}
        }
        res = lambda_handler(event)
        self.assertEqual(res["statusCode"], 200)
        body = json.loads(res["body"])
        self.assertEqual(body["status"], "healthy")
        self.assertEqual(body["region"], "ap-south-1")
        print("  ✓ GET /health passed (Status 200, healthy)")

    def test_cors_options(self):
        event = {
            "rawPath": "/api/v1/detect",
            "requestContext": {"http": {"method": "OPTIONS"}}
        }
        res = lambda_handler(event)
        self.assertEqual(res["statusCode"], 204)
        self.assertEqual(res["headers"]["Access-Control-Allow-Origin"], "*")
        print("  ✓ OPTIONS /api/v1/detect passed (Status 204, CORS preflight)")

    def test_detect_endpoint(self):
        event = {
            "rawPath": "/api/v1/detect",
            "requestContext": {"http": {"method": "POST"}},
            "body": json.dumps({"image_id": "IMG-ST01-001", "conf_threshold": 0.50})
        }
        res = lambda_handler(event)
        self.assertEqual(res["statusCode"], 200)
        body = json.loads(res["body"])
        self.assertIn("detections", body)
        self.assertGreater(body["detections_count"], 0)
        print(f"  ✓ POST /api/v1/detect passed ({body['detections_count']} detections, latency: {body['execution_time_ms']} ms)")

    def test_query_electrical_burden(self):
        event = {
            "rawPath": "/api/v1/query",
            "requestContext": {"http": {"method": "POST"}},
            "body": json.dumps({"query": "Which corridor has the highest electrical burden?"})
        }
        res = lambda_handler(event)
        self.assertEqual(res["statusCode"], 200)
        body = json.loads(res["body"])
        self.assertEqual(body["result"]["intent"], "highest_electrical_capacity")
        self.assertEqual(body["result"]["metrics"]["Street ID"], "ST08")
        print(f"  ✓ POST /api/v1/query passed (Resolved ST08 electrical load in {body['resolved_in_ms']} ms)")

    def test_query_lighting_spacing(self):
        event = {
            "rawPath": "/api/v1/query",
            "requestContext": {"http": {"method": "POST"}},
            "body": json.dumps({"query": "What is the streetlight spacing and dark spots on Avarampalayam Road?"})
        }
        res = lambda_handler(event)
        self.assertEqual(res["statusCode"], 200)
        body = json.loads(res["body"])
        self.assertEqual(body["result"]["intent"], "lighting_spacing_audit")
        self.assertEqual(body["result"]["metrics"]["Current Spacing"], "45.0 meters")
        print("  ✓ POST /api/v1/query passed (Resolved ST10 lighting spacing deficit)")

    def test_work_orders_filter(self):
        event = {
            "rawPath": "/api/v1/work-orders",
            "requestContext": {"http": {"method": "GET"}},
            "queryStringParameters": {"agency": "TANGEDCO", "priority": "P1-Critical"}
        }
        res = lambda_handler(event)
        self.assertEqual(res["statusCode"], 200)
        body = json.loads(res["body"])
        self.assertGreater(body["total_matching"], 0)
        print(f"  ✓ GET /api/v1/work-orders passed ({body['total_matching']} critical TANGEDCO orders returned)")

if __name__ == "__main__":
    print("\n=== Running Local Serverless Integration Tests (AWS Lambda Mock Event Harness) ===")
    unittest.main()
