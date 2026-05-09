Fill the README.md in the application folder `$ARGUMENTS` using the job offer file found there.

If `$ARGUMENTS` is empty, list the folders in `open-applications/` (excluding `_template`) and ask which one to use.

Steps:
1. Read `open-applications/$ARGUMENTS/job-offer.txt`
2. Read `open-applications/$ARGUMENTS/README.md`
3. Fill every empty field and section in the README using only what appears in the job offer — never invent or infer content.

Rules:
- **Details table**: fill any blank cell by scanning the job offer for a match. Only fill what you can find; leave the rest blank. For the `Remote Work` field (if present), derive from the location policy (e.g. "Hybrid – 25% in-office").
- **Named sections** (e.g. `### Key Responsibilities`, `### Logistics`): find the matching block in the job offer by heading name or closest equivalent heading; copy bullet points or lines verbatim. If no match exists, leave the section empty.
- **Unrecognized sections in the README**: apply the same logic — try to find matching content in the job offer; leave empty if not found.
- **Sections in the job offer with no corresponding README section**: ignore them (do not add new sections).
- **Never touch**: Status checkboxes, Contacts table, Company research, Role fit, Follow-ups — leave these exactly as they are.
- Update the top-level heading to `# <Company> — <Role>` using the values you extracted.

4. Write the updated content back to `open-applications/$ARGUMENTS/README.md`.
