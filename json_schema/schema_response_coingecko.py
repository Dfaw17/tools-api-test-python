ping_server_normal = {
    "type": "object",
    "properties": {
        "gecko_says": {
            "type": "string"
        }
    },
    "required": [
        "gecko_says"
    ]
}

ping_server_error = {
    "type": "object",
    "properties": {
        "error": {
            "type": "string"
        }
    },
    "required": [
        "error"
    ]
}

coin_list_normal = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "array",
    "items": [
        {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string"
                },
                "symbol": {
                    "type": "string"
                },
                "name": {
                    "type": "string"
                }
            },
            "required": [
                "id",
                "symbol",
                "name"
            ]
        }
    ]
}
