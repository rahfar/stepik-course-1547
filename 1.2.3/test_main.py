import io

import pytest

from main import main


@pytest.mark.parametrize(
    ["test_input", "expected"],
    [
        ("1 0\n", ""),
        ("1 1\n0 0\n", "0\n"),
        ("1 2\n0 1\n0 1\n", "0\n-1\n"),
        ("1 2\n0 1\n1 1\n", "0\n1\n"),
        ("2 8\n0 0\n0 0\n0 0\n1 0\n1 0\n1 1\n1 2\n1 3\n", "0\n0\n0\n1\n1\n1\n2\n-1\n"),
        ("2 8\n0 0\n0 0\n0 0\n1 1\n1 0\n1 0\n1 2\n1 3\n", "0\n0\n0\n1\n2\n-1\n-1\n-1\n"),
        ("2 5\n2 9\n4 8\n10 9\n15 2\n19 1\n", "2\n11\n-1\n19\n21\n"),
    ],
)
def test_main(monkeypatch, capsys, test_input, expected):
    monkeypatch.setattr("sys.stdin", io.StringIO(test_input))

    main()

    assert capsys.readouterr().out == expected
