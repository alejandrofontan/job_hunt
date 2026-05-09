Suggest targeted CV improvements for the job application in folder `$ARGUMENTS`.

If `$ARGUMENTS` is empty, list the folders in `open-applications/` (excluding `_template`) and ask which one to use.

Steps:
1. Read `open-applications/$ARGUMENTS/README.md` — extract the role, key responsibilities, qualifications, and preferred experience sections.
2. Read `resources/CV_FONTAN_GIT/CV_FONTAN.pdf` — understand the current content, structure, and emphasis of the CV.
3. Compare the two and produce a prioritized list of concrete suggestions.

Output format — use these four sections, in order:

### Keyword gaps
Skills, tools, or terms that appear in the job requirements but are missing or underrepresented in the CV. For each gap: state the keyword, where it appears in the job offer, and whether the CV has adjacent experience that could surface it.

### Emphasis shifts
Existing CV content that is relevant to this role but is buried, understated, or framed in a way that doesn't match the job's language. Suggest specific rewordings or reorderings.

### Missing content
Experiences, projects, or achievements that the job clearly values and that are absent from the CV (only flag if the gap is real — do not invent experience).

### Quick wins
Small, high-impact edits: verb changes, metric additions, reordering bullet points, or section title tweaks that would immediately improve alignment.

Rules:
- Be specific — reference actual lines or sections from the CV and actual requirements from the README.
- Do not suggest fabricating experience.
- Do not suggest changes unrelated to this specific role.
- Do not rewrite the CV; only suggest changes.
