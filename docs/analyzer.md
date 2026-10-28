# Generic caption analyzer (offline-ready, live disabled)

`scripts/analyze_transcript.py` validates the imported public corpus and implements
the extraction → deterministic candidates → untrusted relation proposal → code
validation pipeline. It never changes frozen identities or the knowledge bundle.

## Current provider contract: unavailable

There is **no approved public LLM provider, endpoint, model, free allowance, or
repository secret contract**. `APPROVED_LLM_CONFIG` is `None`, and `request_model`
is an intentionally non-networking transport that returns `provider_unavailable`.
A secret or environment variable cannot select a provider or enable live calls.
The workflow's `ANALYZER_LLM_API_KEY` reference is a disconnected placeholder,
not evidence of an installed key or an authorized secret name. Do not install a
key under that name on the strength of this documentation.

Live activation requires a separately reviewed change implementing exactly the
approved public provider/endpoint/model/secret-name contract and its free-allowance,
request/token and timeout caps. Never use ambient SDK credentials, a host key,
a private proxy, automatic retries, paid fallback, or a different provider.
There is no provider SDK dependency in this offline implementation. Synthetic
transport substitutions in the acceptance suite are not production authorization.

## Offline usage

```sh
python3 scripts/analyze_transcript.py --root . --vid qZj7sqmidqA --check
```

`--check` is read-only and needs no credentials or network. It validates:

- An exact 11-character video ID and real, nonsymlinked corpus/input/output paths.
- The published provenance header: exact source watch URL, speaker or channel
  credit, aware `retrieved_at`, caption track and `auto/author captions, unverified`
  label. Machine transcripts are not caption evidence for this slice.
- SHA256 over the **original body bytes**, not normalized line endings or text.
- Nonempty, individually valid timestamped captions (minutes:seconds or
  hours:minutes:seconds). Evidence timestamps address one caption span exactly.
- Existing analysis provenance, preserving a valid aware `published_at` verbatim;
  missing dates remain missing and retrieval time never substitutes for them.
- Unique frozen catalog IDs, declared record count and sorted-ID digest.

Normal invocation without `--check` currently returns nonzero with sanitized JSON
`{"ok": false, "error": "provider_unavailable"}` after validating its inputs.
It makes zero provider requests and writes nothing. No working live analyzer,
provider similarity result or successful workflow is claimed.

## Untrusted proposal boundary

Extraction permits only `talk_summary`, `takeaways` and `truncated=false`.
Takeaways use `area`, nullable `technique`, `what_they_do` and `numbers`, string
`confidence` (`low|medium|high`), `evidence_quote` and `evidence_timestamp`.
There are at most 20 takeaways. Quotes are bounded to 40 words / 280 characters
and must match a contiguous whole-word sequence at that exact caption timestamp.
Case and punctuation are normalized for word comparison; words cannot be omitted,
borrowed from a different timestamp, or joined across spans. Code alone supplies
`evidence_quote_verification=normalized-exact`; a model cannot bless its own quote.

Candidates are ranked in deterministic code using lexical Jaccard overlap between
takeaway technique/explanation and catalog title/mechanism text. Zero-overlap IDs
are excluded; ties sort by frozen ID; at most eight IDs are offered per takeaway.
Null projected prose is supported. Area labels are not a hard filter because the
analysis and catalog use different taxonomies. This is a bounded lexical shortlist,
not a semantic recall guarantee.

The second request receives the frozen per-takeaway candidate lists. Its only
allowed proposal is exactly one `{takeaway_index, relation, catalog_id}` per
extracted takeaway. `supports`, `refines`, and `contradicts` must name an ID offered
for **that** takeaway. `new` has `catalog_id=null` and remains unassigned; it does
not mint a catalog identity. Duplicate keys/indexes, missing proposals, extra
fields, truncation and out-of-candidate IDs reject the entire response.

The analyzer emits relations only. The generator alone owns `kb/`, stable/deprecated
state, revisions, and `kb/log.md`. Supports only appends. Only validated refines or
contradicts from a source at least 30 days newer may supersede; unknown dates never
do, and no revision is deleted. This analyzer does not implement those mutations.

## Writes and failure behavior

All inputs are bounded to 16 MiB, model text responses to 128 KiB. No intermediate
analysis is written. After both responses validate, input bytes are rechecked,
then only `analysis/<validated-vid>.json` is atomically replaced. Rejected responses,
changed inputs and failed replacements preserve the previous analysis and clean
up temporary files. Other videos, `data/catalog.json`, root `catalog.json`, state
and `kb/` are never publication targets. Raw provider exceptions, key-bearing URLs
and model error bodies are not logged. Public text guards reject the active key,
private addresses/home paths and internal identifiers; they are conservative
checks, not a promise to discover every possible private string in arbitrary prose.

## Manual workflow and activation prerequisites

`.github/workflows/analyze.yml` has one required string input, `vid`, no schedule,
no matrix and no caption fetch. Inputs enter shell via environment variables, not
executable expression text. It runs on `ubuntu-latest` and only from the default
branch. The read-only analysis job checks out the dispatch SHA with
`persist-credentials:false`, runs `backfill_publish_dates.py --check` first
(>=95% distinct-video publication-date coverage), and validates captions before
analysis. Failure stops artifact upload and publication.

The currently disabled transport prevents a live run regardless of installed
secrets. Before any later activation or successful real-data acceptance:

1. Land the prerequisite workflow/corpus/generator changes through their existing
   review and CI gates; verify default-branch workflow presence.
2. Complete `videos.list` backfill first and retain >=95% coverage evidence.
3. Retain a passing five-video Supadata **native/en**, HTTP 200 canary with every
   score >=98% against the existing reference transcripts: exact video IDs,
   normalization/metric, reference/provider word counts and per-video scores.
   A key or five prepared reference files is not a passing canary. No bulk
   ingestion before a pass; HTTP 206 is not accepted.
4. Obtain and implement the reviewed public, repo-scoped, no-new-spend provider
   contract, including runtime verification of those live prerequisite receipts.
5. Run the merged workflow on one real existing caption video; independently
   verify output provenance, quotes, frozen-ID digest and unchanged `kb/`.

Caption acquisition stays outside this workflow. Supadata native/en remains
primary; TranscriptAPI then Apify may be used only with their separately explicit
access/free-allowance contracts. No borrowed credentials, video-understanding
substitute, bulk fetch, or refresh-publication activation is added here.

After successful analysis only, a separate contents-write job downloads one
short-lived named artifact into an isolated directory. It checks out the same SHA
without persisted credentials and revalidates the artifact's entire allowlisted
schema, provenance, dates, quotes, candidate relations and sole filename against
that pinned corpus, with no model secret or model request. It stages only
`analysis/$VIDEO_ID.json` using `git add --`; credentials are supplied to the push
process environment, never stored in git configuration or an artifact. A concurrent
default-branch update makes the non-forced push fail rather than overwrite work.
Branch protection remains authoritative; a rejected push is not bypassed.

Undo: revert the analyzer/workflow additions or leave the unavailable contract in
place. No credentials were provisioned and no catalog/data migration is needed.
