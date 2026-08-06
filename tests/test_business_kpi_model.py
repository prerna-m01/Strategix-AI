from backend.app.models import BusinessKPI


def test_business_kpi_table():
    assert BusinessKPI.__tablename__ == "business_kpis"