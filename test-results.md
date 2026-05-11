# Test Execution Results

Generated: 2026-05-11T11:50:54.092Z

## API Request/Response Report

### 1. GET https://f1api.dev/api/circuits

- Status: 200

Response body:

```json
{"api": "https://f1api.dev", "url": "https://f1api.dev/api/circuits", "limit": 30, "offset": 0, "total": 30, "circuits": [{"circuitId": "bahrein", "circuitName": "Bahrein International Circuit", "country": "Bahrein", "city": "Sakhir", "circuitLength": 5412, "lapRecord": "1:31:447", "firstParticipationYear": 2004, "numberOfCorners": 15, "fastestLapDriverId": "de_la_rosa", "fastestLapTeamId": "mclaren", "fastestLapYear": 2005, "url": "https://en.wikipedia.org/wiki/Bahrain_International_Circuit"},
```

### 2. GET https://f1api.dev/api/circuits/nonexistent-xyz-123

- Status: 404

Response body:

```json
{"api": "https://f1api.dev", "url": "https://f1api.dev/api/circuits/nonexistent-xyz-123", "message": "No Circuit found for this id, try with other one.", "status": 404}
```

### 3. GET https://f1api.dev/api/circuits

- Status: 200

Response body:

```json
{"api": "https://f1api.dev", "url": "https://f1api.dev/api/circuits", "limit": 30, "offset": 0, "total": 30, "circuits": [{"circuitId": "bahrein", "circuitName": "Bahrein International Circuit", "country": "Bahrein", "city": "Sakhir", "circuitLength": 5412, "lapRecord": "1:31:447", "firstParticipationYear": 2004, "numberOfCorners": 15, "fastestLapDriverId": "de_la_rosa", "fastestLapTeamId": "mclaren", "fastestLapYear": 2005, "url": "https://en.wikipedia.org/wiki/Bahrain_International_Circuit"},
```

### 4. GET https://f1api.dev/api/drivers-championship

- Status: 404

Response body:

```json
{"api": "https://f1api.dev", "url": "https://f1api.dev/api/drivers-championship", "message": "No seasons found for this year, try with another one.", "status": 404}
```

### 5. GET https://f1api.dev/api/drivers-championship/nonexistent-xyz-123

- Status: 404

Response body:

```json
{"api": "https://f1api.dev", "url": "https://f1api.dev/api/drivers-championship/nonexistent-xyz-123", "message": "No seasons found for this year, try with another one.", "status": 404}
```

### 6. GET https://f1api.dev/api/drivers-championship

- Status: 404

Response body:

```json
{"api": "https://f1api.dev", "url": "https://f1api.dev/api/drivers-championship", "message": "No seasons found for this year, try with another one.", "status": 404}
```

### 7. GET https://f1api.dev/api/constructors-championship

- Status: 404

Response body:

```json
{"api": "https://f1api.dev", "url": "https://f1api.dev/api/constructors-championship", "message": "No seasons found for this year, try with another one.", "status": 404}
```

### 8. GET https://f1api.dev/api/constructors-championship/nonexistent-xyz-123

- Status: 404

Response body:

```json
{"api": "https://f1api.dev", "url": "https://f1api.dev/api/constructors-championship/nonexistent-xyz-123", "message": "No seasons found for this year, try with another one.", "status": 404}
```

### 9. GET https://f1api.dev/api/constructors-championship

- Status: 404

Response body:

```json
{"api": "https://f1api.dev", "url": "https://f1api.dev/api/constructors-championship", "message": "No seasons found for this year, try with another one.", "status": 404}
```

## Raw Output

```text
Command: python test-api-kan-46.py
Exit Code: 1

Output:
    Request: GET https://f1api.dev/api/circuits
    Status: 200
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/circuits", "limit": 30, "offset": 0, "total": 30, "circuits": [{"circuitId": "bahrein", "circuitName": "Bahrein International Circuit", "country": "Bahrein", "city": "Sakhir", "circuitLength": 5412, "lapRecord": "1:31:447", "firstParticipationYear": 2004, "numberOfCorners": 15, "fastestLapDriverId": "de_la_rosa", "fastestLapTeamId": "mclaren", "fastestLapYear": 2005, "url": "https://en.wikipedia.org/wiki/Bahrain_International_Circuit"}, 
    Request: GET https://f1api.dev/api/circuits/nonexistent-xyz-123
    Status: 404
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/circuits/nonexistent-xyz-123", "message": "No Circuit found for this id, try with other one.", "status": 404}
    Request: GET https://f1api.dev/api/circuits
    Status: 200
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/circuits", "limit": 30, "offset": 0, "total": 30, "circuits": [{"circuitId": "bahrein", "circuitName": "Bahrein International Circuit", "country": "Bahrein", "city": "Sakhir", "circuitLength": 5412, "lapRecord": "1:31:447", "firstParticipationYear": 2004, "numberOfCorners": 15, "fastestLapDriverId": "de_la_rosa", "fastestLapTeamId": "mclaren", "fastestLapYear": 2005, "url": "https://en.wikipedia.org/wiki/Bahrain_International_Circuit"}, 
    Request: GET https://f1api.dev/api/drivers-championship
    Status: 404
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/drivers-championship", "message": "No seasons found for this year, try with another one.", "status": 404}
    Request: GET https://f1api.dev/api/drivers-championship/nonexistent-xyz-123
    Status: 404
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/drivers-championship/nonexistent-xyz-123", "message": "No seasons found for this year, try with another one.", "status": 404}
    Request: GET https://f1api.dev/api/drivers-championship
    Status: 404
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/drivers-championship", "message": "No seasons found for this year, try with another one.", "status": 404}
    Request: GET https://f1api.dev/api/constructors-championship
    Status: 404
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/constructors-championship", "message": "No seasons found for this year, try with another one.", "status": 404}
    Request: GET https://f1api.dev/api/constructors-championship/nonexistent-xyz-123
    Status: 404
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/constructors-championship/nonexistent-xyz-123", "message": "No seasons found for this year, try with another one.", "status": 404}
    Request: GET https://f1api.dev/api/constructors-championship
    Status: 404
    Body: {"api": "https://f1api.dev", "url": "https://f1api.dev/api/constructors-championship", "message": "No seasons found for this year, try with another one.", "status": 404}
Passed: 5, Failed: 4, Skipped: 0

================================================================================
```
