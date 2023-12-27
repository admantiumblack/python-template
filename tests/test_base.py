import pytest
import src

def test_base():
    assert hasattr(src, "main")