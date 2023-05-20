import re

# Through internet found regexs patterns
# Regexs for email, password, username, SSH API keys ...

REGEXS = [
    {
        "pattern": re.compile(
            r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
        ),
        "type": "Email",
    },
    {"pattern": re.compile(r"password"), "type": "Password"},
    {
        "pattern": re.compile(
            r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3,}"
        ),
        "type": "IP",
    },
    {"pattern": re.compile(r"username"), "type": "Username"},
    {
        "pattern": re.compile(r"api_key=?"),
        "type": "Generic API key",
    },
    {
        "pattern": re.compile(r"^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$"),
        "type": "Some type of phone number",
    },
    {
        "pattern": re.compile(
            r"[a-zA-Z]{3,10}:\/\/[^\/\s:@]{3,20}:[^\/\s:@]{3,20}@.{1,100}\/?.?"
        ),
        "type": "Password in URL",
    },
]
