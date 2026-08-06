from backend.app.repositories.company_repository import CompanyRepository


def test_repository_exists():
    assert CompanyRepository is not None