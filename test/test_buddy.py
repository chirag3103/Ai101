# tests/test_buddy.py
import pytest
from src.apps.tech_buddy.generate import Generate


def test_buddy_initialization():
    buddy = Generate()
    assert buddy.client is not None
