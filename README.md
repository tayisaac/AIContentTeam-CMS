# AI Content Team for CMS

A multi-agent content team for headless CMS sites, packaged as a **Claude Code plugin marketplace** so many
development teams can use one centrally maintained team. It plans pages, designs them from existing CMS
components, writes and reviews copy, shows an HTML mock-up and saves **unpublished drafts**. Humans publish.

| | |
| --- | --- |
| Marketplace | `aicontentteam` |
| Plugin | `content-team` (see [CHANGELOG.md](CHANGELOG.md) for the current version) |
| CMS today | Storyblok (CMS-swappable by design) |
| Maintainer | @tayisaac |

## What's in this repository

```
.claude-plugin/marketplace.json   the catalogue Claude Code reads
plugins/content-team/             the plugin: 7 agents, 6 skills, the draft-only safety check
workspace-template/               copy this to create a team's own workspace repository
docs/                             onboarding, maintaining, enforcing the guardrails
scripts/validate.py               release checks (also run by GitHub Actions on every pull request)
scripts/build-cowork-plugin.sh    builds a .plugin file for Cowork from the same source
CHANGELOG.md                      one section per release
```

## How it fits together

- **This repository** owns the team: agents, skills, rules, safety check. One version for everyone.
- **Each development team** has its own workspace repository, made from `workspace-template/`. It holds the
  team's projects (one folder per site, each with `project.md`, `extras/`, `learned/`, `cms/`, `runs/`) and
  switches the plugin on. Teams change behaviour through their `project.md` and knowledge files, not by editing
  agents.
- **People** install nothing by hand: opening a workspace in Claude Code registers this marketplace and offers
  the plugin.

## Quick start

- **A new team:** follow [docs/onboarding-a-team.md](docs/onboarding-a-team.md).
- **One person, by hand:** in Claude Code run
  `/plugin marketplace add tayisaac/ai-content-cms`, then `/plugin install content-team@aicontentteam`.
  The repository is public, so no GitHub login is needed to install or update. Only the maintainer can
  change it; everyone else proposes changes through pull requests.
- **Changing the team:** see [docs/maintaining.md](docs/maintaining.md). All changes go through pull requests.

## Guardrails (all teams)

Drafts only (a safety check blocks publish, unpublish, delete, uploads and component changes) · only the CMS
Operator writes, after explicit approval · existing components only · `project.md` is the top authority and
agents never edit it · every story agents touch gets the `ai-draft` tag.
