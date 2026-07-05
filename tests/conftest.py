"""Test configuration for SOAR Automation Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "soar-automation-agent", "category": "Security AI"}
