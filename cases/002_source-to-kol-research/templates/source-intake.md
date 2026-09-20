# Source Intake & KOL Extraction

## Input

- source_url:
- source_type: URL / post / thread / video / podcast / article / PDF / image / text / account-list / file
- user_goal:
- fixed_scope: yes / no

## Extraction

| # | Name / Account | Role in source | Organization | Platform | Discovery type | Evidence |
|---:|---|---|---|---|---|---|

Discovery types:

**author / guest / mention / quote / reply / speaker / contributor / collaborator / account**

## Scope control

- Fixed names supplied by user:
- Newly discovered names:
- Added to working set? yes / no
- Reason:

Never silently merge newly discovered people into a fixed user-provided list.

## Verification

For each candidate:

**source → identity evidence → platform account → status → 30D activity**

Status:

**CONFIRMED / PROBABLE / UNVERIFIED / NOT_FOUND / WRONG_PERSON**

## Cross-platform rule

A source on one platform may be used to discover a person, while another platform may provide stronger identity evidence. Do not require the final account to exist on the same platform as the input source.

## Output

1. Discovery & identity table
2. 30D activity table
3. Content signal table
4. Final information-source shortlist