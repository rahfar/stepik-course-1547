import subprocess
import pathlib
from typing import ByteString


def run_module(input: ByteString, output: ByteString):
    res = subprocess.run(
        ["python", "main.py"],
        input=input,
        capture_output=True,
        cwd=pathlib.Path(__file__).parent,
        check=True,
    )
    assert output.decode("utf-8").strip() == res.stdout.decode("utf-8").strip()


def test_1():
    input = b"""([](){([])})
"""
    output = b"""Success
"""
    run_module(input, output)

def test_2():
    input = b"""()[]}
"""
    output = b"""5
"""
    run_module(input, output)

def test_3():
    input = b"""{{[()]]
"""
    output = b"""7
"""
    run_module(input, output)

def test_4():
    input = b"""{{{**[][][]
"""
    output = b"""3
"""
    run_module(input, output)
