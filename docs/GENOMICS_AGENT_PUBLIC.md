# Kian Nano Karno Genomics & NGS Research Agent

## Purpose
A benchmark-first, provenance-controlled research workflow for WGS/WES, RNA-seq, long-read sequencing, single-cell/spatial omics, population genomics, variant interpretation, and genomic AI.

## Core execution chain
**Question / estimand -> governance -> sample/data identity -> raw-data integrity -> reference/annotation lock -> QC -> reproducible workflow -> benchmark -> statistical inference -> biological validation -> replication -> translational/IP gate**

The agent does not treat a model prediction, automated annotation, generated code, or pipeline completion as biological evidence.

## Reproducibility and interoperability
The architecture uses version-pinned workflows, containers, checksums, machine-readable manifests and provenance. Nextflow/nf-core, Snakemake and Galaxy are evaluated as complementary workflow ecosystems. GA4GH WES/TES/TRS/DRS/VRS/Phenopackets are tracked as interoperability and governance standards.

## Current data layer
The registry tracks NCBI SRA/ClinVar, Ensembl/GENCODE, gnomAD, GDC, GWAS Catalog, CELLxGENE and benchmark resources such as GIAB. Exact releases are pinned per analysis; “latest” is never accepted as a reproducibility identifier.

## Agentic genomics
External agent implementations are treated as untrusted until audited. Current references include BioMaster, bioinformatics-mcp, bioinformatics-agent-skills, Agentic Genomics, BIA, and execution-grounded single-cell agent benchmarks. They inform architecture and evaluation; they are not automatically adopted.

## Benchmark-first policy
Public truth sets and task-specific benchmarks precede confidential data where appropriate. Variant pipelines are benchmarked against scope-matched truth sets. Single-cell/spatial agents are evaluated with executable tasks and deterministic or expert-defined graders. Foundation models are compared by task, modality, preprocessing, domain shift, leakage/homology controls and uncertainty—not by a universal leaderboard.

## Data protection
Human genomic data, unpublished company datasets, credentials and trade secrets remain outside the public repository unless explicitly authorized.

## Scientific boundary
The module supports research. It does not by itself establish diagnosis, pathogenicity, causality, clinical performance or therapeutic efficacy.
