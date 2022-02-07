import io

import pytest

from main import main


@pytest.mark.parametrize(
    ["test_input", "expected"],
    [
        ("1\n-1\n", "1\n"),
        ("5\n4 -1 4 1 1\n", "3\n"),
        ("5\n-1 0 4 0 3\n", "4\n"),
        ("10\n9 7 5 5 2 9 9 9 2 -1\n", "4\n"),
    ],
)
def test_main(monkeypatch, capsys, test_input, expected):
    monkeypatch.setattr("sys.stdin", io.StringIO(test_input))

    main()

    assert capsys.readouterr().out == expected
