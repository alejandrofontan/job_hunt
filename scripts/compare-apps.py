#!/usr/bin/env python3
"""Generate a comparison report of open job applications from their README.md files."""

import re
from pathlib import Path


def parse_details(content: str) -> dict[str, str]:
    details = {}
    in_table = False
    for line in content.splitlines():
        if "| Field" in line and "| Value" in line:
            in_table = True
            continue
        if not in_table:
            continue
        if line.startswith("|---") or line.startswith("| ---"):
            continue
        if not line.startswith("|"):
            break
        parts = [p.strip() for p in line.split("|")]
        if len(parts) >= 3 and parts[1]:
            details[parts[1]] = parts[2]
    return details


def parse_status(content: str) -> str:
    stages = [
        "Applied",
        "Recruiter screen",
        "Technical interview",
        "On-site / final round",
        "Offer",
    ]
    reached = "Not started"
    for line in content.splitlines():
        for stage in stages:
            if re.search(rf"\[[xX]\] {re.escape(stage)}", line):
                reached = stage
    return reached


def parse_section(content: str, heading: str) -> list[str]:
    pattern = rf"### {re.escape(heading)}\n(.*?)(?=\n###|\n##|\Z)"
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        return []
    block = match.group(1).strip()
    return [line.lstrip("- ").strip() for line in block.splitlines() if line.strip().startswith("-")]


def load_apps(apps_dir: Path) -> list[dict]:
    apps = []
    for folder in sorted(apps_dir.iterdir()):
        if not folder.is_dir() or folder.name == "_template":
            continue
        readme = folder / "README.md"
        if not readme.exists():
            continue
        content = readme.read_text()
        apps.append(
            {
                "folder": folder.name,
                "details": parse_details(content),
                "status": parse_status(content),
                "qualifications": parse_section(content, "Qualifications"),
                "preferred": parse_section(content, "Preferred Experience"),
                "responsibilities": parse_section(content, "Key Responsibilities"),
            }
        )
    return apps


def md_table(headers: list[str], rows: list[list[str]]) -> str:
    widths = [max(len(h), max((len(r[i]) for r in rows), default=0)) for i, h in enumerate(headers)]
    sep = "|" + "|".join("-" * (w + 2) for w in widths) + "|"
    fmt_row = lambda cells: "| " + " | ".join(c.ljust(w) for c, w in zip(cells, widths)) + " |"
    lines = [fmt_row(headers), sep] + [fmt_row(row) for row in rows]
    return "\n".join(lines)


def main():
    root = Path(__file__).resolve().parent.parent
    apps_dir = root / "open-applications"
    apps = load_apps(apps_dir)

    if not apps:
        print("No open applications found.")
        return

    print("# Open Applications — Comparison Report\n")

    # Summary table
    summary_fields = ["Company", "Role", "Location", "Salary range", "Remote Work", "Applied"]
    headers = summary_fields + ["Status"]
    rows = []
    for app in apps:
        d = app["details"]
        rows.append([d.get(f, "—") or "—" for f in summary_fields] + [app["status"]])
    print("## Summary\n")
    print(md_table(headers, rows))
    print()

    # Per-application detail
    print("## Per-Application Details\n")
    for app in apps:
        d = app["details"]
        company = d.get("Company", app["folder"])
        role = d.get("Role", "")
        print(f"### {company} — {role}\n")

        detail_fields = ["Location", "Salary range", "Remote Work", "Applied", "Deadline"]
        for f in detail_fields:
            v = d.get(f, "")
            if v:
                print(f"- **{f}:** {v}")
        print(f"- **Status:** {app['status']}")
        print()

        if app["responsibilities"]:
            print("**Key Responsibilities**")
            for item in app["responsibilities"]:
                print(f"- {item}")
            print()

        if app["qualifications"]:
            print("**Qualifications**")
            for item in app["qualifications"]:
                print(f"- {item}")
            print()

        if app["preferred"]:
            print("**Preferred Experience**")
            for item in app["preferred"]:
                print(f"- {item}")
            print()


if __name__ == "__main__":
    main()
