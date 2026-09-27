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
        "unsupported operatorname in display math",
        """# Bad\n\n```math\n\\operatorname{Address}(x)\n```\n""",
        "unsupported GitHub math macro",
    )

    require_failure(
        "unsupported operatorname in inline math",
        r"""# Bad

The object is $\operatorname{Address}(x)$.
""",
        "unsupported GitHub math macro",
    )

    require_failure(
        "unsupported operatorname naked in prose",
        r"""# Bad

The object is \operatorname{Address}(x) and should have been rendered.
""",
        "unsupported GitHub math macro",
    )

    require_pass(
        "literal banned macro documentation",
        r"""# Good

The historical failure used the literal command `\operatorname` inside a math carrier.
""",
    )

    require_pass(
        "literal TeX notation explicitly typed as literal source",
        r"""# Good

The literal source token `D_{\mathrm{irr}}(\gamma)` is quoted here as source syntax, not used as the mathematical carrier.
""",
    )

    require_failure(
        "semantic TeX notation wrongly carried as inline code",
        r"""# Bad

Let `D_{\mathrm{irr}}(\gamma)` denote the irreversible-loss vector.
""",
        "mathematical notation is in a literal inline-code carrier",
    )

    require_failure(
        "single-letter mathematical variable wrongly carried as inline code",
        r"""# Bad

Fix target `q` before testing.
""",
        "mathematical notation is in a literal inline-code carrier",
    )

    require_pass(
        "semantic inline mathematics uses the math carrier",
        r"""# Good

Let $D_{\mathrm{irr}}(\gamma)$ denote the irreversible-loss vector and fix target $q$ before testing.
""",
    )

    require_failure(
        "inline mapping wrongly carried as code",
        r"""# Bad

The projection is `P -> E`.
""",
        "mathematical notation is in a literal inline-code carrier",
    )

    require_failure(
        "starred mathematical coordinate wrongly carried as code",
        r"""# Bad

Recruit candidate `c*` before confirmation.
""",
        "mathematical notation is in a literal inline-code carrier",
    )

    require_failure(
        "bare Unicode Greek symbol wrongly carried as code",
        """# Bad

Fix horizon `Δ` before testing.
""",
        "mathematical notation is in a literal inline-code carrier",
    )

    require_failure(
        "math span is not shielded by ordinary prose word path",
        """# Bad

Let `X⁺` denote the future path object after `t`.
""",
        "mathematical notation is in a literal inline-code carrier",
    )

    require_failure(
        "unicode Greek with subscript is semantic mathematics",
        """# Bad

Let `Π_adm` be the admissible policy family.
""",
        "mathematical notation is in a literal inline-code carrier",
    )

    require_failure(
        "simple mathematical fraction wrongly carried as code",
        """# Bad

The Euclidean volume is `8/3`.
""",
        "mathematical notation is in a literal inline-code carrier",
    )

    require_failure(
        "simple mathematical equality wrongly carried as code",
        """# Bad

On the facet `nu=0`.
""",
        "mathematical notation is in a literal inline-code carrier",
    )

    require_failure(
        "TeX fraction expression is not mistaken for a file path",
        r"""# Bad

Choose `\eta=1/2`.
""",
        "mathematical notation is in a literal inline-code carrier",
    )

    require_failure(
        "numeric interval is semantic mathematics",
        """# Bad

All probabilities lie in `[1/8,3/8]`.
""",
        "mathematical notation is in a literal inline-code carrier",
    )

    require_failure(
        "standalone ASCII Greek name inside display math",
        """# Bad

```math
K_q(r\mid a,E,U,Delta)
```
""",
        "ASCII Greek-name token Delta",
    )

    require_failure(
        "unbraced multi-letter display subscript",
        """# Bad

```math
u_PI = 1
```
""",
        "unbraced multi-letter subscript",
    )

    require_failure(
        "unbraced multi-letter inline subscript",
        """# Bad

The comparator is $u_PI$.
""",
        "unbraced multi-letter subscript",
    )

    require_failure(
        "ASCII Greek-name token inside display math",
        """# Bad

```math
x^T Sigma_0^{-1} x
```
""",
        "ASCII Greek-name token",
    )

    require_pass(
        "TeX Greek token inside display math",
        """# Good

```math
x^T \\Sigma_0^{-1} x
```
""",
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
        "tilde math fence",
        r"""# Bad

~~~math
\mathcal F(x)
~~~
""",
        "unsupported tilde math fence",
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
