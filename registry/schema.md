# Machine-readable genomics registry schema

Each registry record should expose the same audit fields where applicable:
- id
- category
- organization
- region
- url
- repository
- version
- release_date
- license
- access
- modality
- task
- reference_build
- annotation_dependency
- benchmark_evidence
- maintenance
- reproducibility
- compute
- privacy
- failure_modes
- kian_suitability
- confidence
- last_verified

Rules:
1. Never infer a current version when it was not verified.
2. Separate availability from scientific validity.
3. Record benchmark evidence as evidence, not as a ranking.
4. Human genomic data must remain outside public benchmark artifacts.
5. Reference/annotation versions must be locked per analysis.
6. last_verified is the date the record was checked against a primary source.
