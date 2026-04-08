# Test Execution Results

Generated: 2026-04-08T10:56:50.968Z

================================================================================

Command: python tests/f1_api_test.py
Exit Code: 0

Output:
============================================================
API Test Suite - F1 endpoints
============================================================

Checking server connectivity...
✓ Server responding (status 200)


[TEST] GET /api/drivers/alonso - Happy path (drivers/alonso)
  ✓ PASSED

[TEST] GET /api/drivers/nonexistent-driver-12345 - Not found (drivers/alonso)
  ✓ PASSED (404)

[TEST] GET /api/drivers/alonso - Invalid auth (drivers/alonso)
  ✓ PASSED (status 200)

[TEST] GET /api/seasons - Happy path (seasons)
  ✓ PASSED

[TEST] GET /api/seasons/nonexistent-season-12345 - Not found (seasons)
  ✓ PASSED (404)

[TEST] GET /api/seasons - Invalid auth (seasons)
  ✓ PASSED (status 200)

[TEST] GET /api/circuits - Happy path (circuits)
  ✓ PASSED

[TEST] GET /api/circuits/nonexistent-circuit-12345 - Not found (circuits)
  ✓ PASSED (404)

[TEST] GET /api/circuits - Invalid auth (circuits)
  ✓ PASSED (status 200)

[TEST] GET /api/teams - Happy path (teams)
  ✓ PASSED

[TEST] GET /api/teams/nonexistent-team-12345 - Not found (teams)
  ✓ PASSED (404)

[TEST] GET /api/teams - Invalid auth (teams)
  ✓ PASSED (status 200)

============================================================
Results: 12 passed, 0 failed, 0 skipped
============================================================

================================================================================

