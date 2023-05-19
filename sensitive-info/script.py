import os
import httpx
import dotenv
import typing as t
from pprint import pprint as print

from regexs import REGEXS


dotenv.load_dotenv()


GITHUB_API_URL: str = "https://api.github.com"

HEADERS: dict = {
    "X-GitHub-Api-Version": "2022-11-28",
    "Accept": "application/vnd.github+json",
    "Authorization": "Bearer {}".format(os.getenv("GITHUB_TOKEN")),
}


class Github:
    """Base class for communicating with github's REST API"""

    def __init__(self, owner: str, repository: str) -> None:
        self.owner = owner
        self.repository = repository
        self.repository_url = f"repos/{self.owner}/{self.repository}"

    def send_request(self, method: str, path: str, body: t.Optional[dict] = {}) -> dict:
        return httpx.request(
            method, f"{GITHUB_API_URL}/{path}", json=body, headers=HEADERS
        ).json()

    # User actions
    def get_current_user(self) -> dict:
        return self.send_request("GET", "user")

    # Issue actions
    def get_issues(self) -> dict:
        return self.send_request("GET", f"{self.repository_url}/issues")

    def get_issue(self, number: int) -> dict:
        return self.send_request("GET", f"{self.repository_url}/issues/{number}")

    def get_issue_comments(self, number: int) -> dict:
        return self.send_request(
            "GET", f"{self.repository_url}/issues/{number}/comments"
        )


def check_content(issue: dict, content: str) -> t.List[t.Dict]:
    """Function that compares content(string) with all available
    regex patterns. Returns resulkt
    """
    results: t.List[t.Dict] = list()

    for regex in REGEXS:
        if value := regex["regex"].search(content):
            results.append(
                {
                    "value": value.group(),
                    "type": regex["type"],
                    "url": issue.get("html_url"),
                }
            )

    return results


if __name__ == "__main__":
    gh = Github("abduazizziyodov", "test-repo")
