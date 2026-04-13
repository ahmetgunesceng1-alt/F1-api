# Test Execution Results

Generated: 2026-04-13T13:14:40.762Z

================================================================================

Command: python test-api.py
Exit Code: 0

Output:
[TEST] test_drivers_happy_path
    Request: GET https://f1api.dev/api/drivers/alonso
    Status: 200
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/drivers/alonso", "total": 1, "driver": [{"driverId": "alonso", "name": "Fernando", "surname": "Alonso", "nationality": "Spain", "birthday": "1981-07-29", "number": 14, "shortName": "ALO", "url": "https://en.wikipedia.org/wiki/Fernando_Alonso"}]}
PASSED ✅
[TEST] test_drivers_not_found
    Request: GET https://f1api.dev/api/drivers/nonexistent
    Status: 404
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/drivers/nonexistent", "message": "No driver found for this id, try with other one.", "status": 404}
PASSED ✅
[TEST] test_drivers_invalid_auth
    Request: GET https://f1api.dev/api/drivers/alonso
    Status: 200
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/drivers/alonso", "total": 1, "driver": [{"driverId": "alonso", "name": "Fernando", "surname": "Alonso", "nationality": "Spain", "birthday": "1981-07-29", "number": 14, "shortName": "ALO", "url": "https://en.wikipedia.org/wiki/Fernando_Alonso"}]}
PASSED ✅
[TEST] test_seasons_happy_path
    Request: GET https://f1api.dev/api/seasons
    Status: 200
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/seasons", "limit": 30, "offset": 0, "total": 30, "championships": [{"championshipId": "f1_2026", "championshipName": "2026 Formula 1 World Championship", "url": "https://en.wikipedia.org/wiki/2026_Formula_One_World_Championship", "year": 2026}, {"championshipId": "f1_2025", "championshipName": "2025 Formula 1 World Championship", "url": "https://en.wikipedia.org/wiki/2025_Formula_One_World_Championship", "year": 2025}, {"championshipId":
PASSED ✅
[TEST] test_seasons_invalid_auth
    Request: GET https://f1api.dev/api/seasons
    Status: 200
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/seasons", "limit": 30, "offset": 0, "total": 30, "championships": [{"championshipId": "f1_2026", "championshipName": "2026 Formula 1 World Championship", "url": "https://en.wikipedia.org/wiki/2026_Formula_One_World_Championship", "year": 2026}, {"championshipId": "f1_2025", "championshipName": "2025 Formula 1 World Championship", "url": "https://en.wikipedia.org/wiki/2025_Formula_One_World_Championship", "year": 2025}, {"championshipId":
PASSED ✅
[TEST] test_circuits_happy_path
    Request: GET https://f1api.dev/api/circuits
    Status: 200
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/circuits", "limit": 30, "offset": 0, "total": 30, "circuits": [{"circuitId": "bahrein", "circuitName": "Bahrein International Circuit", "country": "Bahrein", "city": "Sakhir", "circuitLength": 5412, "lapRecord": "1:31:447", "firstParticipationYear": 2004, "numberOfCorners": 15, "fastestLapDriverId": "de_la_rosa", "fastestLapTeamId": "mclaren", "fastestLapYear": 2005, "url": "https://en.wikipedia.org/wiki/Bahrain_International_Circuit"}, 
PASSED ✅
[TEST] test_circuits_invalid_auth
    Request: GET https://f1api.dev/api/circuits
    Status: 200
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/circuits", "limit": 30, "offset": 0, "total": 30, "circuits": [{"circuitId": "bahrein", "circuitName": "Bahrein International Circuit", "country": "Bahrein", "city": "Sakhir", "circuitLength": 5412, "lapRecord": "1:31:447", "firstParticipationYear": 2004, "numberOfCorners": 15, "fastestLapDriverId": "de_la_rosa", "fastestLapTeamId": "mclaren", "fastestLapYear": 2005, "url": "https://en.wikipedia.org/wiki/Bahrain_International_Circuit"}, 
PASSED ✅
[TEST] test_teams_happy_path
    Request: GET https://f1api.dev/api/teams
    Status: 200
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/teams", "limit": 30, "offset": 0, "total": 30, "teams": [{"teamId": "adams", "teamName": "Adams", "teamNationality": "American", "firstAppeareance": null, "constructorsChampionships": null, "driversChampionships": null, "url": "http://en.wikipedia.org/wiki/Adams_(constructor)"}, {"teamId": "afm", "teamName": "AFM", "teamNationality": "German", "firstAppeareance": null, "constructorsChampionships": null, "driversChampionships": null, "url
PASSED ✅
[TEST] test_teams_invalid_auth
    Request: GET https://f1api.dev/api/teams
    Status: 200
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/teams", "limit": 30, "offset": 0, "total": 30, "teams": [{"teamId": "adams", "teamName": "Adams", "teamNationality": "American", "firstAppeareance": null, "constructorsChampionships": null, "driversChampionships": null, "url": "http://en.wikipedia.org/wiki/Adams_(constructor)"}, {"teamId": "afm", "teamName": "AFM", "teamNationality": "German", "firstAppeareance": null, "constructorsChampionships": null, "driversChampionships": null, "url
PASSED ✅

Tests passed: 9
Tests failed: 0
Tests skipped: 0

================================================================================

