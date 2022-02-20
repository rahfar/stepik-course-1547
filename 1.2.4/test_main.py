import io

import pytest

from main import main


@pytest.mark.parametrize(
    ["test_input", "expected"],
    [
        ("3\npush 1\npush 7\npop\n", ""),
        ("5\npush 2\npush 1\nmax\npop\nmax\n", "2\n2\n"),
        ("6\npush 7\npush 1\npush 7\nmax\npop\nmax\n", "7\n7\n"),
        ("5\npush 1\npush 2\nmax\npop\nmax\n", "2\n1\n"),
        (
            "10\npush 2\npush 3\npush 9\npush 7\npush 2\nmax\nmax\nmax\npop\nmax\n",
            "9\n9\n9\n9\n",
        ),
    ],
)
def test_main(monkeypatch, capsys, test_input, expected):
    monkeypatch.setattr("sys.stdin", io.StringIO(test_input))

    main()

    assert capsys.readouterr().out == expected
