#!/usr/bin/env python3
"""
API Test Suite
Tests for F1 public endpoints: /api/drivers/alonso, /api/seasons, /api/circuits, /api/teams
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


# Generic test helpers for endpoints

def run_happy_get(path, label):
    global passed, failed, skipped
    print(f"\n[TEST] GET {path} - Happy path ({label})")
    try:
        response = make_request('GET', path)
        if 'error' in response:
            print(f"  ✗ FAILED: {response['error']}")
            failed += 1
            return
        if response['status'] != 200:
            print(f"  ✗ FAILED: Expected status 200, got {response['status']}")
            failed += 1
            return
        content_type = response['headers'].get('content-type', '')
        if content_type and 'json' not in content_type.lower():
            # accept if body is valid JSON even if header is not json
            if not isinstance(response['body'], (list, dict)):
                print(f"  ✗ FAILED: Expected JSON content-type or JSON body, got {content_type}")
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


def run_not_found_get(path, label):
    global passed, failed, skipped
    print(f"\n[TEST] GET {path} - Not found ({label})")
    try:
        response = make_request('GET', path)
        if 'error' in response:
            print(f"  ✗ FAILED: {response['error']}")
            failed += 1
            return
        if response['status'] in [404, 400]:
            print(f"  ✓ PASSED ({response['status']})")
            passed += 1
        elif response['status'] == 200:
            body = response['body']
            if body is None or body == [] or body == {}:
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


def run_invalid_auth_get(path, label):
    global passed, failed, skipped
    print(f"\n[TEST] GET {path} - Invalid auth ({label})")
    try:
        response = make_request('GET', path, headers={'Authorization': 'Bearer invalid-token-12345'})
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


# Specific endpoint tests

def test_drivers_alonso():
    global passed, failed, skipped
    label = 'drivers/alonso'
    run_happy_get('/api/drivers/alonso', label)
    # Not found test: pick a driver id unlikely to exist
    run_not_found_get('/api/drivers/nonexistent-driver-12345', label)
    run_invalid_auth_get('/api/drivers/alonso', label)


def test_seasons():
    global passed, failed, skipped
    label = 'seasons'
    run_happy_get('/api/seasons', label)
    run_not_found_get('/api/seasons/nonexistent-season-12345', label)
    run_invalid_auth_get('/api/seasons', label)


def test_circuits():
    global passed, failed, skipped
    label = 'circuits'
    run_happy_get('/api/circuits', label)
    run_not_found_get('/api/circuits/nonexistent-circuit-12345', label)
    run_invalid_auth_get('/api/circuits', label)


def test_teams():
    global passed, failed, skipped
    label = 'teams'
    run_happy_get('/api/teams', label)
    run_not_found_get('/api/teams/nonexistent-team-12345', label)
    run_invalid_auth_get('/api/teams', label)


def main():
    """Run all tests"""
    print("=" * 60)
    print("API Test Suite - F1 endpoints")
    print("=" * 60)
    
    # Check if server is responding
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
    
    # Run tests
    test_drivers_alonso()
    test_seasons()
    test_circuits()
    test_teams()
    
    # Summary
    print("\n" + "=" * 60)
    print(f"Results: {passed} passed, {failed} failed, {skipped} skipped")
    print("=" * 60)
    
    sys.exit(0 if failed == 0 else 1)


if __name__ == '__main__':
    main()
