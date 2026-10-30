#!/usr/bin/env python3
"""One runnable check: the lint catches what it must and passes what it must."""
import subprocess, sys, tempfile, pathlib
HERE = pathlib.Path(__file__).resolve().parent
def run(text, strict=False):
    with tempfile.TemporaryDirectory() as d:
        p = pathlib.Path(d) / "x.md"; p.write_text(text)
        args = [sys.executable, str(HERE / "claims_lint.py"), str(p)] + (["--strict"] if strict else [])
        return subprocess.run(args, capture_output=True, text=True).returncode
good = "---\nclaims: [run-local, mesh-pair-choose]\n---\nUCompute does not split a model across devices.\n\n122.7 tok/s on qwen2.5-0.5b, Apple M2, development build (path check, not performance).\n"
assert run(good, strict=True) == 0, "clean file must pass"
assert run("Pool your devices into an AI supercomputer!") == 1, "prohibited phrase must fail"
assert run("Contact nasr for details") == 1, "identity leak must fail"
assert run("---\nclaims: [bogus]\n---\nx") == 1, "unknown claim id must fail"
assert run("No front matter here") == 0 and run("No front matter here", strict=True) == 1, "strict needs claims"
assert run("It ran at 500 tok/s on the fixture.") == 1, "tok/s without path check must fail"
print("test_claims_lint: ok")
