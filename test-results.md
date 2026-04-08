# Test Execution Results

Generated: 2026-04-08T11:10:53.788Z

================================================================================

Command: python tests/test_f1api_endpoints.py
Exit Code: 0

Output:
============================================================
API Test Suite: F1 API endpoints
============================================================

Checking server connectivity...
✓ Server responding (status 200)


[TEST] GET /api/drivers/alonso - Happy path
    ── Request ──
    GET https://f1api.dev/api/drivers/alonso
    ── Response ──
    Status: 200
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/drivers/alonso", "total": 1, "driver": [{"driverId": "alonso", "name": "Fernando", "surname": "Alonso", "nationality": "Spain", "birthday": "1981-07-29", "number": 14, "shortName": "ALO", "url": "https://en.wikipedia.org/wiki/Fernando_Alonso"}]}
  ✓ PASSED

[TEST] GET /api/drivers/nonexistent-driver - Not found
    ── Request ──
    GET https://f1api.dev/api/drivers/nonexistent-driver-xyz-123
    ── Response ──
    Status: 404
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/drivers/nonexistent-driver-xyz-123", "message": "No driver found for this id, try with other one.", "status": 404}
  ✓ PASSED (404)

[TEST] GET /api/drivers/alonso - Invalid auth
    ── Request ──
    GET https://f1api.dev/api/drivers/alonso
    Headers: {"Authorization": "[REDACTED]"}
    ── Response ──
    Status: 200
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/drivers/alonso", "total": 1, "driver": [{"driverId": "alonso", "name": "Fernando", "surname": "Alonso", "nationality": "Spain", "birthday": "1981-07-29", "number": 14, "shortName": "ALO", "url": "https://en.wikipedia.org/wiki/Fernando_Alonso"}]}
  ✓ PASSED (status 200)

[TEST] GET /api/seasons - Happy path
    ── Request ──
    GET https://f1api.dev/api/seasons
    ── Response ──
    Status: 200
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/seasons", "limit": 30, "offset": 0, "total": 30, "championships": [{"championshipId": "f1_2026", "championshipName": "2026 Formula 1 World Championship", "url": "https://en.wikipedia.org/wiki/2026_Formula_One_World_Championship", "year": 2026}, {"championshipId": "f1_2025", "championshipName": "2025 Formula 1 World Championship", "url": "https://en.wikipedia.org/wiki/2025_Formula_One_World_Championship", "year": 2025}, {"championshipId":...
  ✓ PASSED

[TEST] GET /api/seasons/999999 - Not found
    ── Request ──
    GET https://f1api.dev/api/seasons/999999
    ── Response ──
    Status: 404
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/seasons/999999", "message": "No seasons found for this year, try with another one.", "status": 404}
  ✓ PASSED (404)

[TEST] GET /api/seasons - Invalid auth
    ── Request ──
    GET https://f1api.dev/api/seasons
    Headers: {"Authorization": "[REDACTED]"}
    ── Response ──
    Status: 200
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/seasons", "limit": 30, "offset": 0, "total": 30, "championships": [{"championshipId": "f1_2026", "championshipName": "2026 Formula 1 World Championship", "url": "https://en.wikipedia.org/wiki/2026_Formula_One_World_Championship", "year": 2026}, {"championshipId": "f1_2025", "championshipName": "2025 Formula 1 World Championship", "url": "https://en.wikipedia.org/wiki/2025_Formula_One_World_Championship", "year": 2025}, {"championshipId":...
  ✓ PASSED (status 200)

[TEST] GET /api/circuits - Happy path
    ── Request ──
    GET https://f1api.dev/api/circuits
    ── Response ──
    Status: 200
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/circuits", "limit": 30, "offset": 0, "total": 30, "circuits": [{"circuitId": "bahrein", "circuitName": "Bahrein International Circuit", "country": "Bahrein", "city": "Sakhir", "circuitLength": 5412, "lapRecord": "1:31:447", "firstParticipationYear": 2004, "numberOfCorners": 15, "fastestLapDriverId": "de_la_rosa", "fastestLapTeamId": "mclaren", "fastestLapYear": 2005, "url": "https://en.wikipedia.org/wiki/Bahrain_International_Circuit"}, ...
  ✓ PASSED

[TEST] GET /api/circuits/nonexistent - Not found
    ── Request ──
    GET https://f1api.dev/api/circuits/nonexistent-circuit-xyz
    ── Response ──
    Status: 404
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/circuits/nonexistent-circuit-xyz", "message": "No Circuit found for this id, try with other one.", "status": 404}
  ✓ PASSED (404)

[TEST] GET /api/circuits - Invalid auth
    ── Request ──
    GET https://f1api.dev/api/circuits
    Headers: {"Authorization": "[REDACTED]"}
    ── Response ──
    Status: 200
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/circuits", "limit": 30, "offset": 0, "total": 30, "circuits": [{"circuitId": "bahrein", "circuitName": "Bahrein International Circuit", "country": "Bahrein", "city": "Sakhir", "circuitLength": 5412, "lapRecord": "1:31:447", "firstParticipationYear": 2004, "numberOfCorners": 15, "fastestLapDriverId": "de_la_rosa", "fastestLapTeamId": "mclaren", "fastestLapYear": 2005, "url": "https://en.wikipedia.org/wiki/Bahrain_International_Circuit"}, ...
  ✓ PASSED (status 200)

[TEST] GET /api/teams - Happy path
    ── Request ──
    GET https://f1api.dev/api/teams
    ── Response ──
    Status: 200
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/teams", "limit": 30, "offset": 0, "total": 30, "teams": [{"teamId": "adams", "teamName": "Adams", "teamNationality": "American", "firstAppeareance": null, "constructorsChampionships": null, "driversChampionships": null, "url": "http://en.wikipedia.org/wiki/Adams_(constructor)"}, {"teamId": "afm", "teamName": "AFM", "teamNationality": "German", "firstAppeareance": null, "constructorsChampionships": null, "driversChampionships": null, "url...
  ✓ PASSED

[TEST] GET /api/teams/nonexistent - Not found
    ── Request ──
    GET https://f1api.dev/api/teams/nonexistent-team-xyz
    ── Response ──
    Status: 404
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/teams/nonexistent-team-xyz", "message": "No team found for this id, try with other.", "status": 404}
  ✓ PASSED (404)

[TEST] GET /api/teams - Invalid auth
    ── Request ──
    GET https://f1api.dev/api/teams
    Headers: {"Authorization": "[REDACTED]"}
    ── Response ──
    Status: 200
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/teams", "limit": 30, "offset": 0, "total": 30, "teams": [{"teamId": "adams", "teamName": "Adams", "teamNationality": "American", "firstAppeareance": null, "constructorsChampionships": null, "driversChampionships": null, "url": "http://en.wikipedia.org/wiki/Adams_(constructor)"}, {"teamId": "afm", "teamName": "AFM", "teamNationality": "German", "firstAppeareance": null, "constructorsChampionships": null, "driversChampionships": null, "url...
  ✓ PASSED (status 200)

============================================================
Results: 12 passed, 0 failed, 0 skipped
============================================================

================================================================================

