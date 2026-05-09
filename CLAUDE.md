# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

Job hunt workspace for tracking applications and maintaining personal resources (CV and website).

## Environment

This project uses [pixi](https://pixi.sh) for environment and dependency management (conda-forge channel, linux-64 platform). Dependencies: `gh` (GitHub CLI) and `tectonic` (LaTeX compiler).

```bash
pixi install          # install/sync the environment
pixi run <task>       # run a named task from pixi.toml
pixi add <pkg>        # add a dependency
pixi shell            # activate the environment interactively
```

## Tasks

```bash
pixi run get-cv          # clone CV repo into resources/
pixi run pdf-cv          # compile CV to PDF (tectonic, outputs resources/CV_FONTAN_GIT/main.pdf)
pixi run get-website     # clone personal website repo into resources/
pixi run serve-website   # serve Jekyll site locally with live reload (resources/alejandrofontan.github.io/)
```

## Repository layout

```
resources/
  CV_FONTAN_GIT/              # LaTeX CV source (main.tex → main.pdf via tectonic)
  alejandrofontan.github.io/  # Jekyll personal website
open-applications/            # one folder per active job application
  _template/                  # copy this folder to start a new application
    README.md                 # tracker: details, status checklist, contacts, notes
    cover-letter.md           # cover letter draft
closed-applications/          # archived applications (accepted, rejected, withdrawn)
```
