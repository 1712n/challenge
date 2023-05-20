import os
from dotenv import load_dotenv

load_dotenv()


REPORT_SAVE_PATH: str = "report_file.txt"
TEST_REPO_OWNER: str = "abduazizziyodov"
TEST_REPO: str = "sensitive-test-repository"

GITHUB_API_URL: str = "https://api.github.com"

HEADERS: dict = {
    "X-GitHub-Api-Version": "2022-11-28",
    "Accept": "application/vnd.github+json",
    "Authorization": "Bearer {}".format(os.getenv("GITHUB_TOKEN")),
}
