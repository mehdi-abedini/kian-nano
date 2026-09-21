# Genomics / NGS / Bioinformatics Module

## Purpose
Use this module for WGS/WES, bulk and single-cell RNA-seq, long-read DNA/RNA, spatial omics, GWAS/PheWAS, population genomics, variant interpretation, and AI/foundation-model-assisted genomics.

## Mandatory research contract
1. Define the biological question and estimand before choosing a pipeline.
2. Lock sample identity, metadata, consent/data-use constraints, reference genome/assembly, annotation release, coordinate convention, and analysis endpoint.
3. Preserve raw-data integrity with immutable inputs, checksums, sample manifests, and provenance.
4. Run sample identity/swap, contamination, library, sequencing, coverage, mapping, strandness, UMI, batch, and modality-specific QC before inference.
5. Prefer benchmark-first validation using authoritative truth sets and public challenge datasets before confidential/company data.
6. Record software, versions, parameters, reference resources, containers, and compute environment.
7. Predefine contrasts, covariates, inclusion/exclusion, missing-data handling, and multiple-testing control where statistical inference is used.
8. Separate association, prediction, mechanism, causality, pathogenicity, and clinical interpretation; none may be inferred from a model score alone.
9. Require orthogonal validation and/or independent replication for material biological claims when feasible.
10. Maintain a claim-evidence ledger through final report, publication, or IP release.

## Reference and benchmark registry
Maintain a versioned registry for: NIST Genome in a Bottle, Human Pangenome Reference Consortium, T2T assemblies, GENCODE, ClinGen, ClinVar, gnomAD, dbSNP, dbVar/DGV, COSMIC, GTEx, ENA/SRA, GEO, Expression Atlas, CELLxGENE, Human Cell Atlas, HuBMAP, spatial resources, Gene Ontology, Reactome, STRING, GWAS Catalog, Open Targets, cBioPortal, DepMap, and other task-specific authoritative resources.

The registry must record: resource name, release/version, release date, genome build/assembly, scope, provenance, license/access restrictions, update cadence, intended use, known limitations, and checksum or immutable identifier when available.

Current benchmark priority includes GIAB HG002 v5.0q and T2T-linked resources, including difficult small variants and structural variants. NIST also provides public tumor/normal benchmarking resources through the Cancer GIAB program. These are benchmarks, not universal biological truth for arbitrary samples or populations.

## Pipeline registry
Evaluate tools and workflows by scientific validity, reproducibility, maintenance, license, provenance, compute requirements, benchmark evidence, and failure modes. Prefer reproducible workflow systems such as Nextflow/nf-core or Snakemake when appropriate.

Maintain explicit candidates for:
- germline/somatic variant workflows
- long-read variant/SV/phasing workflows
- bulk RNA-seq
- single-cell RNA-seq and multi-omics
- spatial transcriptomics/spatial multi-omics
- methylation/epigenomics
- GWAS/PheWAS/population genomics

Do not select a pipeline from popularity alone.

## Agent and tool registry
Third-party genomics agents are untrusted until audited. Record repository, organization, license, maintenance/activity, dependencies, model/API requirements, tool permissions, data handling, reproducibility, benchmark evidence, and security/privacy risks.

A current reference architecture is Genentech SpatialAgent: an autonomous spatial-biology agent with plan-act-conclude execution, specialized tools, skills, and multimodel support. Treat it as an external research reference, not a dependency, until independently audited.

Agentic analysis must execute the required computational work rather than answer from prior knowledge. Benchmark against task-specific graders where available. Current examples include SpatialBench for verifiable spatial-analysis tasks and the 2026 single-cell-omics agent benchmark covering 50 real-world tasks.

## Foundation-model registry
For genomic foundation models, compare models by task, species, sequence context, training data, architecture, parameter count, licensing, compute, leakage/homology controls, and downstream benchmark protocol.

Do not use aggregate leaderboard position as a universal quality claim. Prefer task- and regime-specific metrics, held-out/OOD tests, calibration, uncertainty, ablation, and external validation.

Current benchmark infrastructure includes GENEB, which evaluates genomic foundation models across 100 DNA classification tasks and 13 functional categories using a controlled frozen-embedding protocol. OmniGenBench is another reproducibility-oriented benchmarking framework for genomic foundation models.

## Modality-specific controls
### WGS/WES and variants
FASTQ/CRAM → QC → alignment or assembly → post-processing → calling → normalization → annotation → evidence interpretation → orthogonal validation. Track allele balance, depth, mapping quality, strand/orientation, duplicate/UMI handling, difficult regions, and reference/annotation versions.

### Bulk RNA-seq
QC → preprocessing → alignment/pseudoalignment → quantification → normalization/model → differential analysis → pathway analysis → validation. Check batch, library strandedness, transcript annotation, dispersion/model assumptions, and multiple testing.

### Long-read DNA/RNA
Use when phasing, structural variation, repeats, methylation, or full-length isoforms materially affect the biological question. Record chemistry/basecaller/version, read N50/quality, coverage, alignment/assembly, phasing, SV/isoform metrics, and platform-specific failure modes.

### Single-cell and spatial
QC → ambient RNA/doublets → normalization → integration/batch assessment → clustering/annotation → differential analysis → spatial registration/segmentation → multimodal integration → validation. Treat cell-type annotation as an evidence-backed inference, not a marker-only label.

## AI safety and scientific validity
For LLM agents and foundation models require: prompt/tool provenance, dataset provenance, train/test leakage controls, homology/scaffold split controls where relevant, deterministic configuration where possible, uncertainty/calibration, ablation/sensitivity, failure-case logging, and external validation.

Never convert generated code, a model score, a predicted expression value, or an automated annotation into experimental evidence without validation.

## Data governance
Human genomic data require appropriate consent, data-use agreements, access controls, encryption/pseudonymization, auditability, and jurisdiction-specific governance. No patient-level or confidential company genomic data belongs in a public repository or public AI workflow unless explicitly authorized.

## Validation ladder
G0 question/design → G1 identity/data integrity → G2 sequencing/QC → G3 computational validity → G4 statistical validity → G5 biological/orthogonal validation → G6 independent replication → G7 translational/clinical interpretation → G8 publication/IP release.

## Output requirements
Every genomics report should contain: question/estimand, dataset and access status, reference lock, methods, benchmark evidence, QC, results, uncertainty, failure modes, reproducibility manifest, claim-evidence ledger, limitations, and next validation gate.
