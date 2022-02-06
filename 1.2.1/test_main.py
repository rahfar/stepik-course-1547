import io

import pytest

from main import main


@pytest.mark.parametrize(
    ["test_input", "expected"],
    [
        ("[]\n", "Success\n"),
        ("{}[]\n", "Success\n"),
        ("[()]\n", "Success\n"),
        ("(())\n", "Success\n"),
        ("{[]}()\n", "Success\n"),
        ("{\n", "1\n"),
        ("{[}\n", "3\n"),
        ("foo(bar);\n", "Success\n"),
        ("foo(bar[i);\n", "10\n"),
        ("([](){([])})\n", "Success\n"),
        ("()[]}\n", "5\n"),
        ("{{[()]]\n", "7\n"),
        ("{{{**[][][]\n", "3\n"),
    ],
)
def test_main(monkeypatch, capsys, test_input, expected):
    monkeypatch.setattr("sys.stdin", io.StringIO(test_input))

    main()

    assert capsys.readouterr().out == expected
