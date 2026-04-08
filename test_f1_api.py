#!/usr/bin/env python3
"""
API Test Suite
Tests for F1 API public endpoints

Endpoints tested:
- GET /api/drivers
- GET /api/drivers/alonso
- GET /api/seasons
- GET /api/circuits
- GET /api/teams

Notes:
- BASE_URL is read from API_BASE_URL env var, otherwise defaults to http://localhost:{SERVER_PORT}
- Uses only Python standard library modules
"""

import http.client
import json
import os
import sys
import time
from urllib.parse import urlparse, quote

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
            'headers': norm_headers
        }
    except Exception as e:
        return {
            'status': 0,
            'body': None,
            'headers': {},
            'error': str(e)
        }


def _is_nonempty_json(body):
    return body is not None and not (body == [] or body == {})


def _extract_candidate_id(body):
    """Try to extract a plausible id/slug from list response body.
    Looks for keys like 'id', '_id', 'driverId', 'code', 'slug', 'name'.
    Returns string id or None.
    """
    if not body:
        return None
    items = None
    if isinstance(body, list):
        items = body
    elif isinstance(body, dict):
        # common wrappers: { data: [...] } or { results: [...] }
        for k in ('data', 'results', 'items'):
            if k in body and isinstance(body[k], list):
                items = body[k]
                break
        if items is None:
            # maybe the body itself contains keys representing items
            # try to find nested list
            for v in body.values():
                if isinstance(v, list):
                    items = v
                    break
    if not items:
        return None
    # pick first item
    first = items[0] if items else None
    if not isinstance(first, dict):
        return None
    for key in ('id', '_id', 'driverId', 'driver_id', 'code', 'slug', 'name'):
        if key in first and first[key]:
            return str(first[key])
    # fallback: if there's a url-like field, try to parse last segment
    for key in ('url', 'href'):
        if key in first and isinstance(first[key], str):
            parts = first[key].rstrip('/').split('/')
            if parts:
                return parts[-1]
    return None


def test_get_drivers_list():
    """Test: GET /api/drivers - Happy path"""
    global passed, failed, skipped
    print("\n[TEST] GET /api/drivers - Happy path")
    try:
        response = make_request('GET', '/api/drivers')
        if 'error' in response:
            print(f"  ✗ FAILED: {response['error']}")
            failed += 1
            return
        if response['status'] != 200:
            print(f"  ✗ FAILED: Expected status 200, got {response['status']}")
            failed += 1
            return
        # lenient content-type check
        content_type = response['headers'].get('content-type', '')
        if content_type and 'json' not in content_type.lower():
            if not isinstance(response['body'], (list, dict)):
                print(f"  ✗ FAILED: Expected JSON content-type, got {content_type}")
                failed += 1
                return
        if not _is_nonempty_json(response['body']):
            print(f"  ✗ FAILED: Empty or missing response body")
            failed += 1
            return
        print("  ✓ PASSED")
        passed += 1
    except Exception as e:
        print(f"  ✗ FAILED: {str(e)}")
        failed += 1


def test_get_driver_alonso():
    """Test: GET /api/drivers/alonso - Named driver"""
    global passed, failed, skipped
    print("\n[TEST] GET /api/drivers/alonso - Named driver")
    try:
        response = make_request('GET', '/api/drivers/alonso')
        if 'error' in response:
            print(f"  ✗ FAILED: {response['error']}")
            failed += 1
            return
        if response['status'] != 200:
            print(f"  ✗ FAILED: Expected status 200, got {response['status']}")
            failed += 1
            return
        if not _is_nonempty_json(response['body']):
            print(f"  ✗ FAILED: Empty response body")
            failed += 1
            return
        print("  ✓ PASSED")
        passed += 1
    except Exception as e:
        print(f"  ✗ FAILED: {str(e)}")
        failed += 1


def test_get_driver_by_detected_id():
    """Test: GET /api/drivers/{id} - detect an ID from list and fetch single resource"""
    global passed, failed, skipped
    print("\n[TEST] GET /api/drivers/{id} - Single resource by detected id")
    try:
        list_resp = make_request('GET', '/api/drivers')
        if 'error' in list_resp:
            print(f"  ✗ FAILED: {list_resp['error']}")
            failed += 1
            return
        if list_resp['status'] != 200:
            print(f"  ⚠ SKIPPED: Cannot get drivers list (status {list_resp['status']})")
            skipped += 1
            return
        candidate = _extract_candidate_id(list_resp['body'])
        if not candidate:
            print("  ⚠ SKIPPED: No suitable id/slug found in drivers list to test single-resource endpoint")
            skipped += 1
            return
        # encode candidate to be safe
        candidate_enc = quote(candidate, safe='')
        single_resp = make_request('GET', f'/api/drivers/{candidate_enc}')
        if 'error' in single_resp:
            print(f"  ✗ FAILED: {single_resp['error']}")
            failed += 1
            return
        # Accept 200 as happy; also allow 400/404 as valid not-found/invalid-id
        if single_resp['status'] in (200, 400, 404):
            print(f"  ✓ PASSED (status {single_resp['status']})")
            passed += 1
        else:
            print(f"  ✗ FAILED: Unexpected status {single_resp['status']}")
            failed += 1
    except Exception as e:
        print(f"  ✗ FAILED: {str(e)}")
        failed += 1


def test_get_seasons_list():
    """Test: GET /api/seasons - Happy path"""
    global passed, failed, skipped
    print("\n[TEST] GET /api/seasons - Happy path")
    try:
        response = make_request('GET', '/api/seasons')
        if 'error' in response:
            print(f"  ✗ FAILED: {response['error']}")
            failed += 1
            return
        if response['status'] != 200:
            print(f"  ✗ FAILED: Expected status 200, got {response['status']}")
            failed += 1
            return
        if not _is_nonempty_json(response['body']):
            print(f"  ✗ FAILED: Empty response body")
            failed += 1
            return
        print("  ✓ PASSED")
        passed += 1
    except Exception as e:
        print(f"  ✗ FAILED: {str(e)}")
        failed += 1


def test_get_circuits_list():
    """Test: GET /api/circuits - Happy path"""
    global passed, failed, skipped
    print("\n[TEST] GET /api/circuits - Happy path")
    try:
        response = make_request('GET', '/api/circuits')
        if 'error' in response:
            print(f"  ✗ FAILED: {response['error']}")
            failed += 1
            return
        if response['status'] != 200:
            print(f"  ✗ FAILED: Expected status 200, got {response['status']}")
            failed += 1
            return
        if not _is_nonempty_json(response['body']):
            print(f"  ✗ FAILED: Empty response body")
            failed += 1
            return
        print("  ✓ PASSED")
        passed += 1
    except Exception as e:
        print(f"  ✗ FAILED: {str(e)}")
        failed += 1


def test_get_teams_list():
    """Test: GET /api/teams - Happy path"""
    global passed, failed, skipped
    print("\n[TEST] GET /api/teams - Happy path")
    try:
        response = make_request('GET', '/api/teams')
        if 'error' in response:
            print(f"  ✗ FAILED: {response['error']}")
            failed += 1
            return
        if response['status'] != 200:
            print(f"  ✗ FAILED: Expected status 200, got {response['status']}")
            failed += 1
            return
        if not _is_nonempty_json(response['body']):
            print(f"  ✗ FAILED: Empty response body")
            failed += 1
            return
        print("  ✓ PASSED")
        passed += 1
    except Exception as e:
        print(f"  ✗ FAILED: {str(e)}")
        failed += 1


def test_invalid_auth_on_drivers():
    """Test: GET /api/drivers with invalid auth token"""
    global passed, failed, skipped
    print("\n[TEST] GET /api/drivers - Invalid auth header")
    try:
        response = make_request('GET', '/api/drivers', headers={'Authorization': 'Bearer invalid-token-12345'})
        if 'error' in response:
            print(f"  ✗ FAILED: {response['error']}")
            failed += 1
            return
        # Accept either 200 (public) or 401/403 (protected)
        if response['status'] in (200, 401, 403):
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
    global passed, failed, skipped
    print("=" * 60)
    print("API Test Suite - F1 API")
    print("=" * 60)
    # Check server connectivity (GET /)
    print("\nChecking server connectivity...")
    try:
        response = make_request('GET', '/')
        if 'error' in response or response['status'] == 0:
            print(f"⚠ WARNING: Server not responding: {response.get('error')}")
            print("Tests will likely fail with connection errors\n")
        else:
            print(f"✓ Server responded (status {response['status']})\n")
    except Exception as e:
        print(f"⚠ WARNING: Could not connect to server: {str(e)}\n")
    # Run tests
    test_get_drivers_list()
    test_get_driver_alonso()
    test_get_driver_by_detected_id()
    test_invalid_auth_on_drivers()
    test_get_seasons_list()
    test_get_circuits_list()
    test_get_teams_list()
    # Summary
    print("\n" + "=" * 60)
    print(f"Results: {passed} passed, {failed} failed, {skipped} skipped")
    print("=" * 60)
    sys.exit(0 if failed == 0 else 1)

if __name__ == '__main__':
    main()
