# Test Execution Results

Generated: 2026-04-13T16:26:34.028Z

================================================================================

Command: python test-api-kan-44.py
Exit Code: 0

Output:
    Request: GET https://f1api.dev/api/drivers/alonso
    Status: 200
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/drivers/alonso", "total": 1, "driver": [{"driverId": "alonso", "name": "Fernando", "surname": "Alonso", "nationality": "Spain", "birthday": "1981-07-29", "number": 14, "shortName": "ALO", "url": "https://en.wikipedia.org/wiki/Fernando_Alonso"}]}
    Request: GET https://f1api.dev/api/drivers/alonso/nonexistent-xyz-123
    Status: 404
    Body: "<!DOCTYPE html><html><head><meta charSet=\"utf-8\"/><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"/><link rel=\"preload\" as=\"script\" fetchPriority=\"low\" href=\"/_next/static/chunks/webpack-fb1e5a724641dfe2.js\"/><script src=\"/_next/static/chunks/fd9d1056-0adbf876ba8b888d.js\" async=\"\"></script><script src=\"/_next/static/chunks/7023-9ea0c529cce3c474.js\" async=\"\"></script><script src=\"/_next/static/chunks/main-app-881f01dbe13267cd.js\" async=\"\"></script><ti
    Request: GET https://f1api.dev/api/drivers/alonso
    Status: 200
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/drivers/alonso", "total": 1, "driver": [{"driverId": "alonso", "name": "Fernando", "surname": "Alonso", "nationality": "Spain", "birthday": "1981-07-29", "number": 14, "shortName": "ALO", "url": "https://en.wikipedia.org/wiki/Fernando_Alonso"}]}
    Request: GET https://f1api.dev/api/seasons
    Status: 200
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/seasons", "limit": 30, "offset": 0, "total": 30, "championships": [{"championshipId": "f1_2026", "championshipName": "2026 Formula 1 World Championship", "url": "https://en.wikipedia.org/wiki/2026_Formula_One_World_Championship", "year": 2026}, {"championshipId": "f1_2025", "championshipName": "2025 Formula 1 World Championship", "url": "https://en.wikipedia.org/wiki/2025_Formula_One_World_Championship", "year": 2025}, {"championshipId":
    Request: GET https://f1api.dev/api/seasons/nonexistent-xyz-123
    Status: 404
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/seasons/nonexistent-xyz-123", "message": "No seasons found for this year, try with another one.", "status": 404}
    Request: GET https://f1api.dev/api/seasons
    Status: 200
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/seasons", "limit": 30, "offset": 0, "total": 30, "championships": [{"championshipId": "f1_2026", "championshipName": "2026 Formula 1 World Championship", "url": "https://en.wikipedia.org/wiki/2026_Formula_One_World_Championship", "year": 2026}, {"championshipId": "f1_2025", "championshipName": "2025 Formula 1 World Championship", "url": "https://en.wikipedia.org/wiki/2025_Formula_One_World_Championship", "year": 2025}, {"championshipId":
    Request: GET https://f1api.dev/api/circuits
    Status: 200
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/circuits", "limit": 30, "offset": 0, "total": 30, "circuits": [{"circuitId": "bahrein", "circuitName": "Bahrein International Circuit", "country": "Bahrein", "city": "Sakhir", "circuitLength": 5412, "lapRecord": "1:31:447", "firstParticipationYear": 2004, "numberOfCorners": 15, "fastestLapDriverId": "de_la_rosa", "fastestLapTeamId": "mclaren", "fastestLapYear": 2005, "url": "https://en.wikipedia.org/wiki/Bahrain_International_Circuit"}, 
    Request: GET https://f1api.dev/api/circuits/nonexistent-xyz-123
    Status: 404
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/circuits/nonexistent-xyz-123", "message": "No Circuit found for this id, try with other one.", "status": 404}
    Request: GET https://f1api.dev/api/circuits
    Status: 200
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/circuits", "limit": 30, "offset": 0, "total": 30, "circuits": [{"circuitId": "bahrein", "circuitName": "Bahrein International Circuit", "country": "Bahrein", "city": "Sakhir", "circuitLength": 5412, "lapRecord": "1:31:447", "firstParticipationYear": 2004, "numberOfCorners": 15, "fastestLapDriverId": "de_la_rosa", "fastestLapTeamId": "mclaren", "fastestLapYear": 2005, "url": "https://en.wikipedia.org/wiki/Bahrain_International_Circuit"}, 
    Request: GET https://f1api.dev/api/teams
    Status: 200
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/teams", "limit": 30, "offset": 0, "total": 30, "teams": [{"teamId": "adams", "teamName": "Adams", "teamNationality": "American", "firstAppeareance": null, "constructorsChampionships": null, "driversChampionships": null, "url": "http://en.wikipedia.org/wiki/Adams_(constructor)"}, {"teamId": "afm", "teamName": "AFM", "teamNationality": "German", "firstAppeareance": null, "constructorsChampionships": null, "driversChampionships": null, "url
    Request: GET https://f1api.dev/api/teams/nonexistent-xyz-123
    Status: 404
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/teams/nonexistent-xyz-123", "message": "No team found for this id, try with other.", "status": 404}
    Request: GET https://f1api.dev/api/teams
    Status: 200
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/teams", "limit": 30, "offset": 0, "total": 30, "teams": [{"teamId": "adams", "teamName": "Adams", "teamNationality": "American", "firstAppeareance": null, "constructorsChampionships": null, "driversChampionships": null, "url": "http://en.wikipedia.org/wiki/Adams_(constructor)"}, {"teamId": "afm", "teamName": "AFM", "teamNationality": "German", "firstAppeareance": null, "constructorsChampionships": null, "driversChampionships": null, "url
Passed: 12, Failed: 0, Skipped: 0

================================================================================

