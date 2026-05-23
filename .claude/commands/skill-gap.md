Produce a skills gap analysis across all job applications.

## Step 1 — Discover applications

Find all README.md files in:
- `open-applications/*/README.md` (exclude `_template`)
- `closed-applications/*/README.md`

List each application as `<Company> — <Role>` (read from the top-level heading of each README). If a README heading is still the default `# Company — Role`, use the folder name instead.

## Step 2 — Extract requirements

For each README, extract every bullet point from:
- `### Qualifications`
- `### Preferred Experience`

Tag each extracted item with the application it came from and whether it is a Qualification (required) or Preferred.

## Step 3 — Normalize and deduplicate into a skills list

Collapse near-duplicate entries across applications into a single canonical skill name. Group them into these categories (add a row per skill, not per mention):

- **Programming Languages** (e.g. C++, Python, CUDA)
- **Frameworks & Libraries** (e.g. PyTorch, TensorFlow, OpenCV, ROS)
- **Domain Knowledge** (e.g. Visual SLAM, Pose Estimation, Deep Learning, 3D Computer Vision)
- **Methods & Architectures** (e.g. Transformer, NeRF, Gaussian Splatting, VAE, GAN)
- **Platforms & Tools** (e.g. Android, Isaac Sim, SNPE, Git)
- **Soft Skills** (e.g. Mentoring, Communication, Publication record)

## Step 4 — Read proficiency sources

Read both:
- `resources/CV_FONTAN_GIT/CV_FONTAN.pdf`
- `resources/on-going-learning.md`

## Step 5 — Rate proficiency

For each canonical skill, assign one of four levels based solely on what you observe in the CV and on-going-learning.md:

| Level | Meaning |
|-------|---------|
| ★★★ Strong | Clearly demonstrated: listed in programming, used in published work, or described in a role |
| ★★☆ Familiar | Mentioned but not central: appears in one role/project or as an interest |
| ★☆☆ Learning | Present in on-going-learning.md but not yet in CV |
| ☆☆☆ Gap | Not found in CV or learning list |

## Output format

Print a summary header first:

> **Applications scanned:** N open, M closed  
> **Skills identified:** K across all applications

Then print the full skills table, grouped by category:

```
## <Category name>

| Skill | Required by | Preferred by | Proficiency | Notes |
|-------|-------------|--------------|-------------|-------|
| ...   | App1, App2  | App3         | ★★★ Strong  | Brief evidence from CV |
```

- **Required by**: applications where this skill appears under Qualifications
- **Preferred by**: applications where it appears under Preferred Experience only
- **Notes**: one short phrase of evidence (e.g. "PyTorch listed in programming bar", "CVPR 20 Oral on RGB-D odometry", "not found in CV")

End with a **Priority gaps** section: list the ☆☆☆ Gap and ★☆☆ Learning skills that appear as *required* (not just preferred) in at least one application, ordered by number of applications that require them.
