#!/usr/bin/env python3
"""
API Test Suite
Tests for F1 API public endpoints: /api/drivers/alonso, /api/seasons, /api/circuits, /api/teams

Base URL hint from Jira: https://f1api.dev

This test file uses only Python stdlib (http.client, json, urllib) and follows the required template.
"""

import http.client
import json
import os
import sys
import time
from urllib.parse import urlparse

# Configuration — port is auto-detected by the execution system
SERVER_PORT = os.environ.get("SERVER_PORT", "3001")
BASE_URL = os.environ.get("API_BASE_URL", f"http://localhost:{SERVER_PORT}")
TIMEOUT = 10  # seconds
passed = 0
failed = 0
skipped = 0


def make_request(method, path, body=None, headers=None):
    """Make HTTP request to the API"""
    if headers is None:
        headers = {}
    
    # Add default Content-Type for JSON
    if body is not None and 'Content-Type' not in headers:
        headers['Content-Type'] = 'application/json'
    
    # Store request info for reporting
    request_info = {
        'method': method,
        'url': BASE_URL + path,
        'headers': {k: v for k, v in headers.items()},
        'body': body
    }
    
    # Parse URL
    url = urlparse(BASE_URL + path)
    
    try:
        # Create connection (HTTPS or HTTP based on scheme)
        if url.scheme == 'https':
            import ssl
            context = ssl.create_default_context()
            conn = http.client.HTTPSConnection(url.netloc, timeout=TIMEOUT, context=context)
        else:
            conn = http.client.HTTPConnection(url.netloc, timeout=TIMEOUT)
        
        # Prepare body
        body_data = json.dumps(body) if body is not None else None
        
        # Make request
        conn.request(method, url.path + ('?' + url.query if url.query else ''), 
                    body=body_data, headers=headers)
        
        # Get response
        response = conn.getresponse()
        response_data = response.read().decode('utf-8')
        
        # Try to parse JSON
        try:
            response_body = json.loads(response_data) if response_data else None
        except json.JSONDecodeError:
            response_body = response_data
        
        # Get response headers (normalize to lowercase keys for consistent lookup)
        raw_headers = dict(response.getheaders())
        norm_headers = {k.lower(): v for k, v in raw_headers.items()}
        
        conn.close()
        
        return {
            'status': response.status,
            'body': response_body,
            'headers': norm_headers,
            'request': request_info
        }
    except Exception as e:
        return {
            'status': 0,
            'body': None,
            'headers': {},
            'error': str(e),
            'request': request_info
        }


def truncate(obj, max_len=500):
    """Truncate a JSON-serializable object's string representation for display"""
    s = json.dumps(obj, ensure_ascii=False, default=str) if not isinstance(obj, str) else obj
    return s[:max_len] + '...' if len(s) > max_len else s


def print_req_res(response):
    """Print request and response details for the test report"""
    req = response.get('request', {})
    print(f"    ── Request ──")
    print(f"    {req.get('method', '?')} {req.get('url', '?')}")
    if req.get('headers'):
        # Redact Authorization header values
        safe_headers = {k: ('[REDACTED]' if k.lower() == 'authorization' else v) for k, v in req['headers'].items()}
        print(f"    Headers: {json.dumps(safe_headers, ensure_ascii=False)}")
    if req.get('body'):
        print(f"    Body: {truncate(req['body'])}")
    print(f"    ── Response ──")
    print(f"    Status: {response.get('status', '?')}")
    if response.get('body') is not None:
        print(f"    Body: {truncate(response['body'])}")


# -- Tests for /api/drivers/alonso --

def test_drivers_alonso_happy_path():
    """Test: GET /api/drivers/alonso - Happy path"""
    global passed, failed, skipped
    print("\n[TEST] GET /api/drivers/alonso - Happy path")
    try:
        response = make_request('GET', '/api/drivers/alonso')
        print_req_res(response)
        if 'error' in response:
            print(f"  ✗ FAILED: {response['error']}")
            failed += 1
            return
        if response['status'] != 200:
            print(f"  ✗ FAILED: Expected status 200, got {response['status']}")
            failed += 1
            return
        if response['body'] is None:
            print(f"  ✗ FAILED: Empty response body")
            failed += 1
            return
        print("  ✓ PASSED")
        passed += 1
    except Exception as e:
        print(f"  ✗ FAILED: {str(e)}")
        failed += 1


def test_drivers_alonso_not_found():
    """Test: GET /api/drivers/nonexistent - Not found"""
    global passed, failed, skipped
    print("\n[TEST] GET /api/drivers/nonexistent-driver - Not found")
    try:
        response = make_request('GET', '/api/drivers/nonexistent-driver-xyz-123')
        print_req_res(response)
        if 'error' in response:
            print(f"  ✗ FAILED: {response['error']}")
            failed += 1
            return
        if response['status'] in [404, 400]:
            print(f"  ✓ PASSED ({response['status']})")
            passed += 1
        elif response['status'] == 200:
            body = response['body']
            if body in (None, [], {}, ""):
                print("  ✓ PASSED (200 with empty response)")
                passed += 1
            else:
                print(f"  ✗ FAILED: Expected 404 or empty response, got 200 with data")
                failed += 1
        else:
            print(f"  ✗ FAILED: Expected 404 or 200-empty, got {response['status']}")
            failed += 1
    except Exception as e:
        print(f"  ✗ FAILED: {str(e)}")
        failed += 1


def test_drivers_alonso_invalid_auth():
    """Test: GET /api/drivers/alonso - Invalid auth"""
    global passed, failed, skipped
    print("\n[TEST] GET /api/drivers/alonso - Invalid auth")
    try:
        response = make_request('GET', '/api/drivers/alonso', headers={'Authorization': 'Bearer invalid-token-12345'})
        print_req_res(response)
        if 'error' in response:
            print(f"  ✗ FAILED: {response['error']}")
            failed += 1
            return
        if response['status'] in [200, 401, 403]:
            print(f"  ✓ PASSED (status {response['status']})")
            passed += 1
        else:
            print(f"  ✗ FAILED: Expected 200/401/403, got {response['status']}")
            failed += 1
    except Exception as e:
        print(f"  ✗ FAILED: {str(e)}")
        failed += 1


# -- Tests for /api/seasons --

def test_seasons_happy_path():
    """Test: GET /api/seasons - Happy path"""
    global passed, failed, skipped
    print("\n[TEST] GET /api/seasons - Happy path")
    try:
        response = make_request('GET', '/api/seasons')
        print_req_res(response)
        if 'error' in response:
            print(f"  ✗ FAILED: {response['error']}")
            failed += 1
            return
        if response['status'] != 200:
            print(f"  ✗ FAILED: Expected status 200, got {response['status']}")
            failed += 1
            return
        if response['body'] is None:
            print(f"  ✗ FAILED: Empty response body")
            failed += 1
            return
        print("  ✓ PASSED")
        passed += 1
    except Exception as e:
        print(f"  ✗ FAILED: {str(e)}")
        failed += 1


def test_seasons_not_found():
    """Test: GET /api/seasons/999999 - Not found"""
    global passed, failed, skipped
    print("\n[TEST] GET /api/seasons/999999 - Not found")
    try:
        response = make_request('GET', '/api/seasons/999999')
        print_req_res(response)
        if 'error' in response:
            print(f"  ✗ FAILED: {response['error']}")
            failed += 1
            return
        if response['status'] in [404, 400]:
            print(f"  ✓ PASSED ({response['status']})")
            passed += 1
        elif response['status'] == 200:
            body = response['body']
            if body in (None, [], {}, ""):
                print("  ✓ PASSED (200 with empty response)")
                passed += 1
            else:
                print(f"  ✗ FAILED: Expected 404 or empty response, got 200 with data")
                failed += 1
        else:
            print(f"  ✗ FAILED: Expected 404 or 200-empty, got {response['status']}")
            failed += 1
    except Exception as e:
        print(f"  ✗ FAILED: {str(e)}")
        failed += 1


def test_seasons_invalid_auth():
    """Test: GET /api/seasons - Invalid auth"""
    global passed, failed, skipped
    print("\n[TEST] GET /api/seasons - Invalid auth")
    try:
        response = make_request('GET', '/api/seasons', headers={'Authorization': 'Bearer invalid-token-12345'})
        print_req_res(response)
        if 'error' in response:
            print(f"  ✗ FAILED: {response['error']}")
            failed += 1
            return
        if response['status'] in [200, 401, 403]:
            print(f"  ✓ PASSED (status {response['status']})")
            passed += 1
        else:
            print(f"  ✗ FAILED: Expected 200/401/403, got {response['status']}")
            failed += 1
    except Exception as e:
        print(f"  ✗ FAILED: {str(e)}")
        failed += 1


# -- Tests for /api/circuits --

def test_circuits_happy_path():
    """Test: GET /api/circuits - Happy path"""
    global passed, failed, skipped
    print("\n[TEST] GET /api/circuits - Happy path")
    try:
        response = make_request('GET', '/api/circuits')
        print_req_res(response)
        if 'error' in response:
            print(f"  ✗ FAILED: {response['error']}")
            failed += 1
            return
        if response['status'] != 200:
            print(f"  ✗ FAILED: Expected status 200, got {response['status']}")
            failed += 1
            return
        if response['body'] is None:
            print(f"  ✗ FAILED: Empty response body")
            failed += 1
            return
        print("  ✓ PASSED")
        passed += 1
    except Exception as e:
        print(f"  ✗ FAILED: {str(e)}")
        failed += 1


def test_circuits_not_found():
    """Test: GET /api/circuits/nonexistent - Not found"""
    global passed, failed, skipped
    print("\n[TEST] GET /api/circuits/nonexistent - Not found")
    try:
        response = make_request('GET', '/api/circuits/nonexistent-circuit-xyz')
        print_req_res(response)
        if 'error' in response:
            print(f"  ✗ FAILED: {response['error']}")
            failed += 1
            return
        if response['status'] in [404, 400]:
            print(f"  ✓ PASSED ({response['status']})")
            passed += 1
        elif response['status'] == 200:
            body = response['body']
            if body in (None, [], {}, ""):
                print("  ✓ PASSED (200 with empty response)")
                passed += 1
            else:
                print(f"  ✗ FAILED: Expected 404 or empty response, got 200 with data")
                failed += 1
        else:
            print(f"  ✗ FAILED: Expected 404 or 200-empty, got {response['status']}")
            failed += 1
    except Exception as e:
        print(f"  ✗ FAILED: {str(e)}")
        failed += 1


def test_circuits_invalid_auth():
    """Test: GET /api/circuits - Invalid auth"""
    global passed, failed, skipped
    print("\n[TEST] GET /api/circuits - Invalid auth")
    try:
        response = make_request('GET', '/api/circuits', headers={'Authorization': 'Bearer invalid-token-12345'})
        print_req_res(response)
        if 'error' in response:
            print(f"  ✗ FAILED: {response['error']}")
            failed += 1
            return
        if response['status'] in [200, 401, 403]:
            print(f"  ✓ PASSED (status {response['status']})")
            passed += 1
        else:
            print(f"  ✗ FAILED: Expected 200/401/403, got {response['status']}")
            failed += 1
    except Exception as e:
        print(f"  ✗ FAILED: {str(e)}")
        failed += 1


# -- Tests for /api/teams --

def test_teams_happy_path():
    """Test: GET /api/teams - Happy path"""
    global passed, failed, skipped
    print("\n[TEST] GET /api/teams - Happy path")
    try:
        response = make_request('GET', '/api/teams')
        print_req_res(response)
        if 'error' in response:
            print(f"  ✗ FAILED: {response['error']}")
            failed += 1
            return
        if response['status'] != 200:
            print(f"  ✗ FAILED: Expected status 200, got {response['status']}")
            failed += 1
            return
        if response['body'] is None:
            print(f"  ✗ FAILED: Empty response body")
            failed += 1
            return
        print("  ✓ PASSED")
        passed += 1
    except Exception as e:
        print(f"  ✗ FAILED: {str(e)}")
        failed += 1


def test_teams_not_found():
    """Test: GET /api/teams/nonexistent - Not found"""
    global passed, failed, skipped
    print("\n[TEST] GET /api/teams/nonexistent - Not found")
    try:
        response = make_request('GET', '/api/teams/nonexistent-team-xyz')
        print_req_res(response)
        if 'error' in response:
            print(f"  ✗ FAILED: {response['error']}")
            failed += 1
            return
        if response['status'] in [404, 400]:
            print(f"  ✓ PASSED ({response['status']})")
            passed += 1
        elif response['status'] == 200:
            body = response['body']
            if body in (None, [], {}, ""):
                print("  ✓ PASSED (200 with empty response)")
                passed += 1
            else:
                print(f"  ✗ FAILED: Expected 404 or empty response, got 200 with data")
                failed += 1
        else:
            print(f"  ✗ FAILED: Expected 404 or 200-empty, got {response['status']}")
            failed += 1
    except Exception as e:
        print(f"  ✗ FAILED: {str(e)}")
        failed += 1


def test_teams_invalid_auth():
    """Test: GET /api/teams - Invalid auth"""
    global passed, failed, skipped
    print("\n[TEST] GET /api/teams - Invalid auth")
    try:
        response = make_request('GET', '/api/teams', headers={'Authorization': 'Bearer invalid-token-12345'})
        print_req_res(response)
        if 'error' in response:
            print(f"  ✗ FAILED: {response['error']}")
            failed += 1
            return
        if response['status'] in [200, 401, 403]:
            print(f"  ✓ PASSED (status {response['status']})")
            passed += 1
        else:
            print(f"  ✗ FAILED: Expected 200/401/403, got {response['status']}")
            failed += 1
    except Exception as e:
        print(f"  ✗ FAILED: {str(e)}")
        failed += 1


def main():
    """Run all tests"""
    print("=" * 60)
    print("API Test Suite: F1 API endpoints")
    print("=" * 60)
    
    # Connectivity check
    print("\nChecking server connectivity...")
    try:
        response = make_request('GET', '/')
        if 'error' in response:
            print(f"⚠ WARNING: Server not responding: {response['error']}")
            print("Tests will likely fail with connection errors\n")
        else:
            print(f"✓ Server responding (status {response['status']})\n")
    except Exception as e:
        print(f"⚠ WARNING: Could not connect to server: {str(e)}\n")
    
    # Run tests for drivers
    test_drivers_alonso_happy_path()
    test_drivers_alonso_not_found()
    test_drivers_alonso_invalid_auth()

    # Run tests for seasons
    test_seasons_happy_path()
    test_seasons_not_found()
    test_seasons_invalid_auth()

    # Run tests for circuits
    test_circuits_happy_path()
    test_circuits_not_found()
    test_circuits_invalid_auth()

    # Run tests for teams
    test_teams_happy_path()
    test_teams_not_found()
    test_teams_invalid_auth()

    # Summary
    print("\n" + "=" * 60)
    print(f"Results: {passed} passed, {failed} failed, {skipped} skipped")
    print("=" * 60)

    # Exit code rules: 0 if failed == 0 else 1
    sys.exit(0 if failed == 0 else 1)


if __name__ == '__main__':
    main()
