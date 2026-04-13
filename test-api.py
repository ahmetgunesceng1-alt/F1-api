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
    # Step 1: Register (read exact fields from source code)
    reg = make_request("POST", "/api/auth/register", body={
        "email": "testbot@example.com", "password": "TestPass123!", "name": "Test Bot"
    })
    # Try to extract token from register response
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
    # Step 2: Login
    login = make_request("POST", "/api/auth/login", body={
        "email": "testbot@example.com", "password": "TestPass123!"
    })
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

def test_endpoint(method, path, expected_statuses):
    global passed, failed, skipped
    response = make_request(method, path, headers=get_auth_headers())
    print_req_res(method, path, response)
    if response["status"] in expected_statuses:
        passed += 1
    else:
        failed += 1

def main():
    setup_auth()
    test_endpoint("GET", "/api/drivers/alonso", [200, 401, 403])
    test_endpoint("GET", "/api/seasons", [200, 401, 403])
    test_endpoint("GET", "/api/circuits", [200, 401, 403])
    test_endpoint("GET", "/api/teams", [200, 401, 403])

    print(f"Passed: {passed}, Failed: {failed}, Skipped: {skipped}")
    sys.exit(0 if failed == 0 else 1)

if __name__ == "__main__":
    main()
