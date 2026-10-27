# Supadata canary procedure

The canary authorizes bulk verbatim-caption retrieval. It runs only from a
GitHub-hosted runner (`ubuntu-latest`), never from local machines, so the
egress path matches future automation.

## Gate (all must hold)

- Exactly 5 videos, each with a conforming `transcripts/<vid>.txt` reference
  (D1 header rules in `transcripts/README.md`).
- Each fetch is `GET /v1/youtube/transcript` with `videoId`, `lang=en`,
  `mode=native`, `text=true` and the repo secret `SUPADATA_API_KEY` in the
  `x-api-key` header.
- Each fetch returns **HTTP 200** with a JSON string `content`. A 206, a 202
  job, any other status, or a chunk/malformed body fails that video.
- Each video reaches **>= 0.98 word similarity** against its reference.

Word similarity is `word_sequence_ratio.v1`: the difflib SequenceMatcher
ratio over normalized word sequences. Normalization drops `#` header lines,
drops timestamp/`-->` tokens, lowercases, strips punctuation and splits on
whitespace. The report records the metric, the normalization, word counts
and the per-video score.

## Dispatch

1. Pick 5 video IDs that already have conforming reference transcripts
   (imported host captions under D1). Prefer varied lengths and speakers.
2. Actions -> `canary` -> Run workflow -> enter the IDs comma-separated.
3. Read the `canary-report` artifact and the job log (exit 0 = pass).

A pass authorizes bulk retrieval with the same request shape. A fail keeps
bulk retrieval disabled: fix the cause (bad reference, fetch shape, or a
real caption mismatch) and re-dispatch. Never print the key, request URLs
or caption bodies into logs or cards; the script reports fixed detail
tokens only.
