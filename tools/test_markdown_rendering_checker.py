#!/usr/bin/env python3
"""Self-test the Markdown rendering checker against known-good and known-bad fixtures.

Purpose: a checker that merely exists is not evidence that it still catches the failure classes
it is supposed to block. This file makes the rendering guard test itself before the repository
audit runs.
"""

from pathlib import Path
import tempfile

import check_markdown_rendering as checker


def run_fixture(text: str):
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "fixture.md"
        path.write_text(text, encoding="utf-8")
        return checker.audit(path)


def require_failure(name: str, text: str, expected_fragment: str):
    problems = run_fixture(text)
    if not problems:
        raise AssertionError(f"{name}: checker failed open; expected a rendering violation")
    if not any(expected_fragment in problem for problem in problems):
        raise AssertionError(
            f"{name}: checker failed for the wrong reason. Problems were: {problems!r}"
        )


def require_pass(name: str, text: str):
    problems = run_fixture(text)
    if problems:
        raise AssertionError(f"{name}: known-good fixture was rejected: {problems!r}")


def main():
    require_failure(
        "unsupported operatorname",
        """# Bad\n\n```math\n\\operatorname{Address}(x)\n```\n""",
        "unsupported GitHub math macro",
    )

    require_failure(
        "unclosed TeX grouping brace",
        """# Bad\n\n```math\n\\boxed{\\mathcal F(x)\n```\n""",
        "unclosed TeX grouping brace",
    )

    require_failure(
        "unbalanced aligned environment",
        """# Bad\n\n```math\n\\begin{aligned}\nx &= 1\n```\n""",
        "unbalanced aligned environment",
    )

    require_failure(
        "legacy display delimiter",
        """# Bad\n\n$$\nx=1\n$$\n""",
        "legacy display-math delimiter",
    )

    require_failure(
        "raw TeX outside carrier",
        """# Bad\n\nThe object is \\mathcal F and should have been rendered.\n""",
        "TeX-like command is outside an explicit GitHub math carrier",
    )

    require_pass(
        "current TVT-safe constructions",
        r"""# Good

```math
\boxed{
a_t=\mathrm{Address}\!\left(x_t,\mathrm{context}_t\right)
}
```

```math
\mathcal L(x,a)
=
\mathrm{ParetoMin}_{\tau\in\mathcal F_{\kappa}(x,a)}
\mathbf D_a(\tau).
```

```math
\tau^{*}
\in
\underset{\tau\in\mathcal L(x,a)}{\mathrm{argmax}}
\;U_{\mathrm{soft}}(\tau\mid x,a).
```
""",
    )

    print("PASS: Markdown rendering checker self-tests passed.")


if __name__ == "__main__":
    main()
