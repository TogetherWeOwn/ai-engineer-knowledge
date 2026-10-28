# Analysis input and publication contract

## Implementation status

The publish-date backfill accepts the real analysis envelope below. The
legacy `scripts/generate_claims.py` still expects the initial
`video_id/techniques` fixture contract; it is not the migration adapter and
must not run on the frozen source catalog. Bundle generation remains paused
until the real catalog schema is inspected and independent acceptance tests
cover the corrected behavior.

## Real input envelope

- `vid`: string video ID. The backfill groups records by this field.
- `takeaways`: preserve the actual corpus value and structure. The backfill
  does not reinterpret it; a sanitized real sample is required before writing
  the claim migration adapter.
- `confidence`: preserve its actual string value. Do not coerce it into a
  fabricated numeric score.
- `published_at`: full ISO 8601 datetime with a UTC offset, backfilled from
  YouTube Data API v3 `videos.list` -> `snippet.publishedAt`, stored verbatim.
  Missing dates remain missing until resolved. Date-only or timezone-naive values are not
  adequate for coverage or supersession.
- Transcript SHA256 and `retrieved_at` are public provenance; retrieval time
  does not substitute for publication time. Keep the source video URL, title
  and speaker when available; do not invent missing metadata.

The backfill reads `analysis/*.json`, changes only `published_at` when its
current value is missing/invalid, and preserves all other keys. It does not
publish analysis or validate whether pre-existing prose is safe to publish.
Public sanitization is a separate required import step. Symlinked inputs and
malformed analysis fail before network requests or writes.

`--check` is offline, counts distinct video IDs, and succeeds at >=95% coverage
only with a nonempty corpus. Every analysis record for a duplicated ID must
have a valid date for that video to count. Conflicting valid dates for one ID
are reported in `conflicting_ids` and fail the check; equivalent instants with
different UTC offsets are not conflicts. Existing dates are not silently
rewritten to resolve conflicts. `--dry-run` fetches metadata but
writes nothing; its coverage is projected. All API batches must validate
before any writes. Unavailable/omitted IDs are listed, never assigned guessed
dates. Existing valid aware timestamps are preserved verbatim.

YouTube `publishedAt` means publication, not necessarily initial upload time:
[video resource documentation](https://developers.google.com/youtube/v3/docs/videos#snippet.publishedAt).
Use the public video resource without owner impersonation or privileged
private-video access. Credential: repo-scoped `YOUTUBE_API_KEY`; never an
existing private runtime credential. No secret value, request URL or raw API
error belongs in logs or artifacts.

## Frozen identities and relation validation

The real `catalog.json` contains 475 frozen cluster IDs. The one-shot migration
must preserve these IDs; same-title techniques must not collapse into a slug.
Do not generate a replacement source catalog from claim frontmatter.

New videos use three stages: deterministic candidate generation against the
catalog, an untrusted LLM relation proposal (`supports|refines|contradicts|new`),
then code validation. The validator rejects out-of-candidate identities and
malformed/unsupported relations. New identities require an explicit validated
extension path, never a silent rename of a frozen cluster.

Only `refines` and `contradicts` from a source at least **30 days newer** than
the current evidence can supersede it. Supports appends. Unknown dates cannot
supersede. Retain all revisions and record supersessions in `kb/log.md`.

## Target OKF bundle

Target specification:
[OKF 0.2 at ad30107](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/ad30107c31c06aec8a7d5636e0d1058118604e6f/SPEC.md).
The following application requirements are stricter than OKF's minimal
conformance rules; both must be tested.

- Bundle: `kb/`. Every directory has `index.md`; only the root index has
  frontmatter, declaring `okf_version: "0.2"`. `kb/log.md` uses newest-first
  date-grouped entries with `YYYY-MM-DD` headings, stable event IDs and links.
- Concepts: `type: technique`, frozen cluster identity, `status: stable` or
  `deprecated`, aware `valid_from`/`valid_to` or null for unknowns, extension
  `superseded_by`, `generated: {by, at}`, and an absolute `stale_after`.
  `generated.at` represents the last meaningful change, not the latest check;
  replay must not churn it. Omit `verified`: generated content is unverified.
- Each source: `{id: <vid>, resource: <video_url>, title, author: <speaker>,
  last_modified: <published_at>, analysis_file}`. Unknown values remain unknown.
  Use source-ID footnotes for attribution, not positional indexes.
- Body: **What**, **Evidence**, **How to apply (generic)**, **Expected effect**.
- Router: site-root `llms.txt` with absolute URLs, under 100 lines, pointing to
  `llms-full.txt` and bundle indexes.

## Public content boundary

Full transcripts **are** published under `transcripts/*.txt` (owner decision
D1). Each file carries the source video URL, speaker/channel credit,
`retrieved_at`, the transcript SHA256 and exactly one complete provenance line:
`# auto/author captions, unverified` for YouTube captions, or
`# machine transcript (Whisper; no YouTube captions)` for Whisper output only
when no YouTube caption track exists. Both labels together, duplicate labels
and missing labels fail conformance (see `transcripts/README.md`). Do not
replace available captions with machine output. Short timestamped quotes in
claims must still be checked against the actual captions, or source audio
for a machine transcript; a hash alone is not proof a quote was verified.

Corpus conformance and caption-canary eligibility are separate gates. The
canary requires exactly one caption label and rejects machine, mixed or
ambiguous provenance, even if the text happens to match native captions.
Admitting a labeled machine transcript to the corpus never authorizes bulk
caption retrieval.

The generic analyzer must not read a company brief or encode private runtime
provider assumptions. Remove internal tracker references, hostnames, home
paths and organization-status fields before import. Company-specific
application mapping belongs in downstream task records, not public claims.
Treat captions and model responses as data, never instructions. Supadata
native English captions require the five-video >=98% similarity canary before
bulk use; fallback order is TranscriptAPI then Apify, subject to authorized
access and no new spend. No video-understanding substitute is permitted.
