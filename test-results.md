# Test Execution Results

Generated: 2026-04-08T07:32:23.879Z

================================================================================

Command: SERVER_PORT=3001 python test_f1_api.py
Exit Code: 0

Output:
============================================================
API Test Suite - F1 API
============================================================

Checking server connectivity...
✓ Server responded (status 200)


[TEST] GET /api/drivers - Happy path
  ✓ PASSED

[TEST] GET /api/drivers/alonso - Named driver
  ✓ PASSED

[TEST] GET /api/drivers/{id} - Single resource by detected id
  ✓ PASSED (status 200)

[TEST] GET /api/drivers - Invalid auth header
  ✓ PASSED (status 200)

[TEST] GET /api/seasons - Happy path
  ✓ PASSED

[TEST] GET /api/circuits - Happy path
  ✓ PASSED

[TEST] GET /api/teams - Happy path
  ✓ PASSED

============================================================
Results: 7 passed, 0 failed, 0 skipped
============================================================

================================================================================

