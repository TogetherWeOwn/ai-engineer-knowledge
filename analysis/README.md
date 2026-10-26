# Analysis

One JSON file per talk, following [`docs/analysis-schema.md`](../docs/analysis-schema.md):
source video URL, talk publish date, retrieval time, and the techniques
distilled from the transcript.

The claims generator (`scripts/generate_claims.py`) reads everything in this
directory. Files are inputs, written by the analysis step — not generated
output.
