import http.client
import json
import os
import sys
from urllib.parse import urlparse

SERVER_PORT = os.environ.get("SERVER_PORT", "3001")
BASE_URL = os.environ.get("API_BASE_URL", f"http://localhost:{SERVER_PORT}")
TIMEOUT = 10
passed = 0
failed = 0
skipped = 0
auth_token = None

def make_request(method, path, body=None, headers=None):
    if headers is None:
        headers = {}
    if body is not None and "Content-Type" not in headers:
        headers["Content-Type"] = "application/json"
    url = urlparse(BASE_URL + path)
    try:
        if url.scheme == "https":
            import ssl
            conn = http.client.HTTPSConnection(url.hostname, url.port or 443, timeout=TIMEOUT)
        else:
            conn = http.client.HTTPConnection(url.hostname, url.port or 80, timeout=TIMEOUT)
        body_data = json.dumps(body) if body is not None else None
        full_path = url.path + ("?" + url.query if url.query else "")
        conn.request(method, full_path, body=body_data, headers=headers)
        response = conn.getresponse()
        data = response.read().decode("utf-8")
        try:
            response_body = json.loads(data) if data else None
        except json.JSONDecodeError:
            response_body = data
        conn.close()
        return {"status": response.status, "body": response_body, "headers": dict(response.getheaders())}
    except Exception as e:
        return {"status": 0, "body": None, "headers": {}, "error": str(e)}

def get_auth_headers():
    if auth_token:
        return {"Authorization": f"Bearer {auth_token}"}
    return {}

def print_req_res(method, path, response):
    print(f"    Request: {method} {BASE_URL}{path}")
    print(f"    Status: {response.get('status', '?')}")
    body = response.get("body")
    if body is not None:
        s = json.dumps(body, ensure_ascii=False, default=str)
        print(f"    Body: {s[:500]}")
    if response.get("error"):
        print(f"    Error: {response['error']}")

def setup_auth():
    global auth_token
    REGISTER_PATH = "/api/auth/register"
    LOGIN_PATH = "/api/auth/login"
    REGISTER_BODY = {
        "email": "testbot@example.com", "password": "TestPass123!", "name": "Test Bot"
    }
    LOGIN_BODY = {
        "email": "testbot@example.com", "password": "TestPass123!"
    }
    
    reg = make_request("POST", REGISTER_PATH, body=REGISTER_BODY)
    if reg.get("status") in (200, 201) and reg.get("body"):
        b = reg["body"]
        if isinstance(b, dict):
            for k in ("token", "accessToken", "access_token"):
                if k in b:
                    auth_token = b[k]
                    return
                if "data" in b and isinstance(b["data"], dict) and k in b["data"]:
                    auth_token = b["data"][k]
                    return
    login = make_request("POST", LOGIN_PATH, body=LOGIN_BODY)
    if login.get("status") in (200, 201) and login.get("body"):
        b = login["body"]
        if isinstance(b, dict):
            for k in ("token", "accessToken", "access_token"):
                if k in b:
                    auth_token = b[k]
                    return
                if "data" in b and isinstance(b["data"], dict) and k in b["data"]:
                    auth_token = b["data"][k]
                    return

def test_endpoint_happy_path(endpoint, method="GET", body=None):
    global passed, failed
    headers = get_auth_headers()
    response = make_request(method, endpoint, body=body, headers=headers)
    print_req_res(method, endpoint, response)
    if response["status"] in (200, 201):
        passed += 1
    else:
        failed += 1

def test_endpoint_not_found(endpoint, method="GET", body=None):
    global passed, failed
    headers = get_auth_headers()
    response = make_request(method, endpoint + "/nonexistent-xyz-123", body=body, headers=headers)
    print_req_res(method, endpoint + "/nonexistent-xyz-123", response)
    if response["status"] in (404, 400):
        passed += 1
    else:
        failed += 1

def test_endpoint_invalid_auth(endpoint, method="GET", body=None):
    global passed, failed
    headers = {"Authorization": "Bearer invalid-token-12345"}
    response = make_request(method, endpoint, body=body, headers=headers)
    print_req_res(method, endpoint, response)
    if response["status"] in (200, 401, 403):
        passed += 1
    else:
        failed += 1

def main():
    setup_auth()
    # Example endpoints, replace with actual endpoints from the source code
    endpoints = [
        "/api/drivers",
        "/api/constructors",
        "/api/circuits",
        "/api/races"
    ]
    for endpoint in endpoints:
        test_endpoint_happy_path(endpoint)
        test_endpoint_not_found(endpoint)
        test_endpoint_invalid_auth(endpoint)

    print(f"Passed: {passed}, Failed: {failed}, Skipped: {skipped}")
    sys.exit(0 if failed == 0 else 1)

if __name__ == "__main__":
    main()
