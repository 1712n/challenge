import re
import httpx
import typing as t
from rich import print

from regexs import REGEXS
from constants import (
    GITHUB_API_URL,
    HEADERS,
    TEST_REPO_OWNER,
    TEST_REPO,
    REPORT_SAVE_PATH,
)


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
        """Fetch list of all issues. Somehow, github rest API
        includes pull requests also. I mean, this function returns
        issues + pull requests. We don't need to write another function
        for pull requests.
        """
        return self.send_request("GET", f"{self.repository_url}/issues")

    def get_issue(self, number: int) -> dict:
        return self.send_request("GET", f"{self.repository_url}/issues/{number}")

    def get_issue_comments(self, number: int) -> dict:
        return self.send_request(
            "GET", f"{self.repository_url}/issues/{number}/comments"
        )


def check_content(resource: dict, content: str) -> t.Generator[t.Dict, t.Any, t.Any]:
    """Generator function that compares content(string) with all available
    regex patterns.
    """
    for regex in REGEXS:
        for line in re.split(r"\n|,|!|;", content):
            if value := regex.get("pattern").search(line):
                yield {
                    "value": value.group(),
                    "type": regex["type"],
                    "url": resource.get("html_url"),
                    "part": line.__str__(),
                }


def report_generator(results: t.List[t.Dict]) -> t.Generator[str, t.Any, t.Any]:
    # Terminal text - with colored output :D
    report: str = "[bold red]\n[ Sensitive Informations ][/ bold red]\n"

    for result in results:
        report += (
            f"[bold medium_purple1]Type[/ bold medium_purple1]: {result['type']}\n"
        )
        report += f"[bold medium_purple1]Info value[/ bold medium_purple1]: {result['value']}\n"
        report += f"[bold medium_purple1]Part of the information[/ bold medium_purple1]: {result['part']}\n"
        report += f"[bold medium_purple1]Link(source)[/ bold medium_purple1]: {result['url']}\n\n"

    yield report

    colors: str = [
        "[bold red]",
        "[/ bold red]",
        "[bold medium_purple1]",
        "[/ bold medium_purple1]",
    ]

    for piece_to_remove in colors:
        report = report.replace(piece_to_remove, "")

    yield report


def main() -> None:
    """Main function for our script.
    Performs search, reports about results (+save).
    """
    github = Github(TEST_REPO_OWNER, TEST_REPO)

    issue_results: t.List[dict] = [
        result
        for issue in github.get_issues()
        for result in check_content(issue, issue["body"])
    ]

    comment_results: t.List[dict] = [
        result
        for issue in github.get_issues()
        for comment in github.get_issue_comments(issue["number"])
        for result in check_content(issue, comment["body"])
    ]

    generator = report_generator(issue_results + comment_results)

    print(next(generator))  # first time it yields terminal output

    with open(REPORT_SAVE_PATH, "w") as file:
        file.write(next(generator))  # then raw text


if __name__ == "__main__":
    main()
