# Test Execution Results

Generated: 2026-05-08T12:09:10.444Z

================================================================================

Command: python test-api-kan-45.py
Exit Code: 1

Output:
    Request: GET https://f1api.dev/api/drivers
    Status: 200
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/drivers", "limit": 30, "offset": 0, "total": 30, "drivers": [{"driverId": "Cannoc", "name": "John", "surname": "Cannon", "nationality": "Canada", "birthday": "1933-06-21", "number": null, "shortName": null, "url": "http://en.wikipedia.org/wiki/John_Cannon_(auto_racer)"}, {"driverId": "Changy", "name": "Alain", "surname": "de Changy", "nationality": "Belgium", "birthday": "1922-02-05", "number": null, "shortName": null, "url": "http://en.
    Request: GET https://f1api.dev/api/drivers/nonexistent-xyz-123
    Status: 404
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/drivers/nonexistent-xyz-123", "message": "No driver found for this id, try with other one.", "status": 404}
    Request: GET https://f1api.dev/api/drivers
    Status: 200
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/drivers", "limit": 30, "offset": 0, "total": 30, "drivers": [{"driverId": "Cannoc", "name": "John", "surname": "Cannon", "nationality": "Canada", "birthday": "1933-06-21", "number": null, "shortName": null, "url": "http://en.wikipedia.org/wiki/John_Cannon_(auto_racer)"}, {"driverId": "Changy", "name": "Alain", "surname": "de Changy", "nationality": "Belgium", "birthday": "1922-02-05", "number": null, "shortName": null, "url": "http://en.
    Request: GET https://f1api.dev/api/circuits
    Status: 200
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/circuits", "limit": 30, "offset": 0, "total": 30, "circuits": [{"circuitId": "bahrein", "circuitName": "Bahrein International Circuit", "country": "Bahrein", "city": "Sakhir", "circuitLength": 5412, "lapRecord": "1:31:447", "firstParticipationYear": 2004, "numberOfCorners": 15, "fastestLapDriverId": "de_la_rosa", "fastestLapTeamId": "mclaren", "fastestLapYear": 2005, "url": "https://en.wikipedia.org/wiki/Bahrain_International_Circuit"}, 
    Request: GET https://f1api.dev/api/circuits/nonexistent-xyz-123
    Status: 404
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/circuits/nonexistent-xyz-123", "message": "No Circuit found for this id, try with other one.", "status": 404}
    Request: GET https://f1api.dev/api/circuits
    Status: 200
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/circuits", "limit": 30, "offset": 0, "total": 30, "circuits": [{"circuitId": "bahrein", "circuitName": "Bahrein International Circuit", "country": "Bahrein", "city": "Sakhir", "circuitLength": 5412, "lapRecord": "1:31:447", "firstParticipationYear": 2004, "numberOfCorners": 15, "fastestLapDriverId": "de_la_rosa", "fastestLapTeamId": "mclaren", "fastestLapYear": 2005, "url": "https://en.wikipedia.org/wiki/Bahrain_International_Circuit"}, 
    Request: GET https://f1api.dev/api/constructors-championship
    Status: 404
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/constructors-championship", "message": "No seasons found for this year, try with another one.", "status": 404}
    Request: GET https://f1api.dev/api/constructors-championship/nonexistent-xyz-123
    Status: 404
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/constructors-championship/nonexistent-xyz-123", "message": "No seasons found for this year, try with another one.", "status": 404}
    Request: GET https://f1api.dev/api/constructors-championship
    Status: 404
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/constructors-championship", "message": "No seasons found for this year, try with another one.", "status": 404}
    Request: GET https://f1api.dev/api/drivers-championship
    Status: 404
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/drivers-championship", "message": "No seasons found for this year, try with another one.", "status": 404}
    Request: GET https://f1api.dev/api/drivers-championship/nonexistent-xyz-123
    Status: 404
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/drivers-championship/nonexistent-xyz-123", "message": "No seasons found for this year, try with another one.", "status": 404}
    Request: GET https://f1api.dev/api/drivers-championship
    Status: 404
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/drivers-championship", "message": "No seasons found for this year, try with another one.", "status": 404}
Passed: 8, Failed: 4, Skipped: 0

================================================================================

