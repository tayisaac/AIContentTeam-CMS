# Changelog

Each release bumps `version` in `plugins/<plugin>/.claude-plugin/plugin.json`. Users only receive a release
when that version changes.

## content-team 0.1.8 (2026-10-16)
- Repository renamed to tayisaac/ai-content-cms: links, install commands, the workspace template's
  marketplace source and the managed-settings example now use the new name. No behaviour change.
  The marketplace (aicontentteam) and plugin (content-team) names are unchanged.

## content-team 0.1.7 (2026-10-14)
- First release from this marketplace (aicontentteam). Same behaviour as 0.1.6.
- Wording made host-neutral (Claude Code or Cowork) in the README, folder layout and catalogue format.
- Plugin description now says seven agents.

## content-team 0.1.6 (2026-10-09)
- New agent page-mockup-maker: self-contained HTML mock-up of the proposed page (before/after for updates).
- New skill build-mockup-kit: captures the site's CSS, header, footer and one snippet per component.
- create-page and update-page show the mock-up at the approval step.

## content-team 0.1.5 (2026-10-08)
- Tagging rule: every story agents create or edit gets the ai-draft tag; existing tags are kept.

## content-team 0.1.4 (2026-10-08)
- Knowledge freshness check at the start of every run; Librarian sync mode. Agents never edit project.md.

## content-team 0.1.3 (2026-10-08)
- Safety check also covers connectors whose tools are named by an ID.

## content-team 0.1.0 – 0.1.2 (2026-10-07)
- Initial team: strategist, page architect, copywriter, reviewer, component librarian, CMS operator;
  setup-project, create-page, update-page, refresh-catalogue; draft-only safety check.
