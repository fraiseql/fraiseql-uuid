"""The package says the version it was installed as."""

from importlib.metadata import version

import fraiseql_uuid


def test_version_is_the_installed_distributions() -> None:
    assert fraiseql_uuid.__version__ == version("fraiseql-uuid")
