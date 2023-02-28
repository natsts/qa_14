from voluptuous import PREVENT_EXTRA, Schema

single_user_schema = Schema(
    {"data":
         {"id": int,
          "email": str,
          "first_name": str,
          "last_name": str,
          "avatar": str
          },
     "support":
         {"url": str,
          "text": str
          }
     },
    required=True,
    extra=PREVENT_EXTRA,
)

new_user_schema = Schema(
    {
        "name": str,
        "job": str,
        "id": str,
        "createdAt": str
    },
    required=True,
    extra=PREVENT_EXTRA
)


successful_register_user = Schema(
    {
        "id": int,
        "token": str
    },
    required=True,
    extra=PREVENT_EXTRA
)


login_unsuccessful_user = Schema(
    {
        "error": "Missing password"
    },
    required=True,
    extra=PREVENT_EXTRA
)

update_user = Schema(
    {
        "name": str,
        "job": str,
        "updatedAt": str
    },
    required=True,
    extra=PREVENT_EXTRA
)
