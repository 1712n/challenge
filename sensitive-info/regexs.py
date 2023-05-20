import re

# Through internet found regexs for finding sensitive informations
# Regexs for email, password, username, SSH API keys ...

REGEXS = [
    {
        "regex": re.compile(
            r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
        ),
        "type": "Email",
    },
    {"regex": re.compile(r"password"), "type": "Password"},
    {
        "regex": re.compile(
            r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3,}"
        ),
        "type": "IP",
    },
    {"regex": re.compile(r"username"), "type": "Username"},
    {"regex": re.compile(r"\-\-\-\-\-BEGIN PRIVATE KEY\-\-\-\-\-"), "type": "PKCS8"},
    {"regex": re.compile(r"\-\-\-\-\-BEGIN RSA PRIVATE KEY\-\-\-\-\-"), "type": "RSA"},
    {
        "regex": re.compile(r"\-\-\-\-\-BEGIN OPENSSH PRIVATE KEY\-\-\-\-\-"),
        "type": "SSH",
    },
    {
        "regex": re.compile(
            r"(?i)api_key(.{0,20})?[\\'|\\\"][0-9a-zA-Z]{32,45}[\\'|\\\"]"
        ),
        "type": "Generic API key",
    },
    {
        "regex": re.compile(
            r"[a-zA-Z]{3,10}:\/\/[^\/\s:@]{3,20}:[^\/\s:@]{3,20}@.{1,100}\/?.?"
        ),
        "type": "Password in URL",
    },
]
