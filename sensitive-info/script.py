import os
import httpx
import dotenv
import typing as t
from rich import print

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

    def send_request(
        self, method: str, path: str, body: t.Optional[dict] = {}
    ) -> t.Union[t.Dict, t.List]:
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

    # Pull request actions


def check_content(resource: dict, content: str) -> t.Generator[t.Dict, t.Any, t.Any]:
    """Generator function that compares content(string) with all available
    regex patterns. Returns resulkt
    """
    results: t.List[t.Dict] = list()

    for regex in REGEXS:
        for line in content.split("\n"):
            if value := regex["regex"].search(line):
                yield {
                    "value": value.group(),
                    "type": regex["type"],
                    "url": resource.get("html_url"),
                    "line": line.__str__(),
                }


def create_report(results: t.List[t.Dict]) -> str:
    ...


if __name__ == "__main__":
    github = Github("abduazizziyodov", "test-repo")
