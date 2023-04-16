login_normal = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "status_code": {
            "type": "integer"
        },
        "msg": {
            "type": "string"
        },
        "token": {
            "type": "object",
            "properties": {
                "access_token": {
                    "type": "string"
                },
                "token_type": {
                    "type": "string"
                }
            },
            "required": [
                "access_token",
                "token_type"
            ]
        },
        "data": {
            "type": "object",
            "properties": {
                "akun": {
                    "type": "object",
                    "properties": {
                        "key_ecd": {
                            "type": "string"
                        },
                        "photo_norek": {
                            "type": "null"
                        },
                        "phone": {
                            "type": "string"
                        },
                        "photo_norek_url": {
                            "type": "null"
                        },
                        "address": {
                            "type": "null"
                        },
                        "account_type": {
                            "type": "integer"
                        },
                        "id": {
                            "type": "integer"
                        },
                        "no_rekening": {
                            "type": "null"
                        },
                        "OTP": {
                            "type": "null"
                        },
                        "name": {
                            "type": "string"
                        },
                        "jenis_bank": {
                            "type": "null"
                        },
                        "createdAt": {
                            "type": "string"
                        },
                        "email": {
                            "type": "string"
                        },
                        "photo_profile": {
                            "type": "null"
                        },
                        "is_deleted": {
                            "type": "boolean"
                        },
                        "pwd": {
                            "type": "string"
                        },
                        "photo_profile_url": {
                            "type": "null"
                        },
                        "is_subs": {
                            "type": "null"
                        },
                        "ecd": {
                            "type": "string"
                        },
                        "subs_date": {
                            "type": "null"
                        }
                    },
                    "required": [
                        "key_ecd",
                        "photo_norek",
                        "phone",
                        "photo_norek_url",
                        "address",
                        "account_type",
                        "id",
                        "no_rekening",
                        "OTP",
                        "name",
                        "jenis_bank",
                        "createdAt",
                        "email",
                        "photo_profile",
                        "is_deleted",
                        "pwd",
                        "photo_profile_url",
                        "is_subs",
                        "ecd",
                        "subs_date"
                    ]
                },
                "list_toko": {
                    "type": "array",
                    "items": {}
                }
            },
            "required": [
                "akun",
                "list_toko"
            ]
        }
    },
    "required": [
        "status_code",
        "msg",
        "token",
        "data"
    ]
}

login_error = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "status_code": {
            "type": "integer"
        },
        "msg": {
            "type": "string"
        },
        "token": {
            "type": "object",
            "properties": {
                "access_token": {
                    "type": "null"
                },
                "token_type": {
                    "type": "string"
                }
            },
            "required": [
                "access_token",
                "token_type"
            ]
        },
        "data": {
            "type": "null"
        }
    },
    "required": [
        "status_code",
        "msg",
        "token",
        "data"
    ]
}
