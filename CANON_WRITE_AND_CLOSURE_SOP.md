# MKUFT Canon Write and Closure SOP

**Status:** Mandatory working procedure for changes to the live public MKUFT canon.  
**Purpose:** prevent rendering faults, partial propagation, stale dependencies, truncation, and false completion during writes, moves, renames, deletions, and cleanups.

## 1. Governing rule

> A canon change is not complete when the target file has been edited. It is complete only when the changed object, every load-bearing reference to it, every rendered mathematical expression affected by the change, and every public route that depends on it have been checked and closed.

The write method is therefore **object → dependency surface → write → propagation → readback → closure proof**.

No change may be called complete merely because one file saved successfully.

## 2. Human-readable mathematics is the default

Human-facing Markdown must use GitHub-rendered mathematics.

Inline mathematics uses dollar delimiters, for example $E=mc^2$.

Display mathematics uses double-dollar delimiters, for example:

$$
P(B\mid A)=\frac{1}{Z_A}\sum_{\gamma\in\Gamma(A\to B)}e^{-\beta C[\gamma]}.
$$

Rules:

- mathematical expressions are not written as ASCII or pseudo-math inside fenced `text` blocks when they are intended to be read as equations;
- legacy LaTeX bracket or parenthesis delimiters that GitHub may expose literally are not permitted in live human-facing Markdown;
- fenced blocks are reserved for literal code, terminal material, file trees, or genuine process/architecture diagrams;
- mathematical meaning must survive transfer between source, GitHub, reading copy, and publication copy;
- notation is checked after rendering, not only in source text;
- an equation is never accepted because the source code "looks right" if the human reading surface renders it incorrectly.

Existing legacy fenced equations are presentation debt and are not a template for future writing. When such an equation is materially revised, it must be promoted to rendered mathematics in the same change.

## 3. Mandatory pre-write pass

Before changing a canonical object:

1. Identify the exact file, version, layer address, and role.
2. Fetch the complete current object before replacement.
3. Record its current blob or commit identity.
4. Identify direct references: exact path, filename, module number, title, aliases, and architecture-route labels.
5. Identify semantic dependencies: documents that describe the object as a parent, child, route, recovery handle, source, limit, or required support.
6. Separate frozen publications and historical records from live working-canon objects. Frozen material is not silently rewritten.
7. Define the intended post-change state before writing.

If the dependency surface is unknown, the change is not ready to execute.

## 4. Write pass

During the write:

1. Change only the declared object and required propagation set.
2. Preserve unrelated text exactly.
3. Use rendered mathematics for every new or materially revised equation.
4. Do not reuse a truncated fetch as a complete file.
5. Do not infer that a rename or deletion propagated merely because the primary object changed.
6. Keep public, private, frozen, and live objects typed separately.

For structural changes, work on a branch and expose the completed set to `main` only after closure checks.

## 5. Deletion, rename, move, and cleanup closure

A deletion, rename, move, or public-cleanup task has a stricter burden.

Before it can be called complete:

1. Remove or update the primary object.
2. Search for the exact old path.
3. Search for the old filename.
4. Search for the module number or canonical label where distinctive.
5. Search for the old title and meaningful aliases.
6. Inspect architecture maps, registries, entry routes, dependency tables, and support footers.
7. Inspect neighbouring modules that previously depended on the object.
8. Remove semantic dependency language even where no literal path remains.
9. Preserve deliberate historical references only when they are clearly historical and cannot be mistaken for a live route.
10. Add retired live identifiers to `CANON_RETIRED_IDENTIFIERS.txt` when they must never re-enter the live canon.
11. Re-run the search after all edits. **Zero unexplained live matches is the closure condition.**

A cleanup that removes the object but leaves a route, parent relation, registry row, or recovery instruction pointing to it has failed.

## 6. Propagation test

Every changed invariant or object must be tested in both directions:

**Forward:** what does this object support, route to, constrain, or explain?

**Reverse:** what points to, names, depends on, limits, or reconstructs through this object?

The change is closed only when both directions agree with the intended post-change architecture.

## 7. Readback and diff gate

After writing:

1. Fetch every changed file from the branch again.
2. Read the changed region.
3. Read the final section of every replaced file.
4. Confirm expected headings, architecture routes, and terminal content still exist.
5. Compare against the pre-change state.
6. Treat disproportionate unexplained deletion as a blocking fault.
7. Confirm rendered equations use the required Markdown math form.
8. Run the repository integrity guard.
9. Do not merge while any closure check is unresolved.

## 8. Canon integrity guard

`tools/validate_canon_integrity.py` is the machine check for the minimum non-negotiable invariants.

It checks the live Markdown canon for:

- forbidden retired identifiers;
- legacy math delimiters that can survive transfer as raw source;
- newly introduced equation-like `text` fences in changed Markdown.

The GitHub workflow `.github/workflows/canon-integrity.yml` runs the guard on pull requests and pushes.

This guard is a floor, not the whole audit. It does not replace semantic dependency inspection, readback, scientific checking, or human review.

## 9. Failure rule

If any step fails:

- stop the propagation chain;
- identify the last verified closed state;
- repair from that state;
- do not describe the task as complete;
- do not compensate by broad rewriting unrelated files.

## 10. Completion statement

A structural canon change may be reported complete only when all four statements are true:

1. **Object closed:** the intended file state is correct.
2. **Dependency closed:** no unexplained live dependency points to the old state.
3. **Presentation closed:** human-facing mathematics and links render correctly.
4. **Readback closed:** changed files and endings have been re-fetched and compared.

Compressed rule:

> **Write the object. Propagate the object. Render the object. Re-read the object. Prove closure. Then call it done.**
