import io

import pytest

from main import main


@pytest.mark.parametrize(
    ["test_input", "expected"],
    [
        ("8\n2 7 3 1 5 2 6 2\n4\n", "7 7 5 6 6\n"),
        ("3\n2 1 5\n1\n", "2 1 5\n"),
        ("3\n2 3 9\n3\n", "9\n"),
    ],
)
def test_main(monkeypatch, capsys, test_input, expected):
    monkeypatch.setattr("sys.stdin", io.StringIO(test_input))

    main()

    assert capsys.readouterr().out == expected
