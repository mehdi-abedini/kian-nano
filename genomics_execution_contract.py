_REQUIRED = (
    'project_id','modality','question_id','estimand','data_access',
    'sample_manifest_id','raw_input_checksums','reference_lock','workflow',
    'qc_requirements','benchmark_plan','provenance','governance','claim_gate'
)
_ALLOWED_CLAIM_GATES = {'research-only','publication-ready','clinical'}

def validate_execution_record(record):
    errors=[]
    if not isinstance(record, dict):
        return ['record must be a dict']
    errors += [f for f in _REQUIRED if f not in record]
    if not record.get('raw_input_checksums'):
        errors.append('raw_input_checksums')
    ref=record.get('reference_lock')
    if not isinstance(ref,dict) or not ref.get('assembly') or not ref.get('reference_id') or not ref.get('annotation'):
        errors.append('reference_lock')
    wf=record.get('workflow')
    if not isinstance(wf,dict) or not wf.get('engine') or not wf.get('workflow_id') or not wf.get('version'):
        errors.append('workflow')
    if not record.get('qc_requirements'):
        errors.append('qc_requirements')
    bench=record.get('benchmark_plan')
    if not isinstance(bench,dict) or not bench.get('dataset_id') or not bench.get('version') or not bench.get('truth_set'):
        errors.append('benchmark_plan')
    prov=record.get('provenance')
    if not isinstance(prov,dict) or not prov.get('container_digest') or not prov.get('parameters_hash'):
        errors.append('provenance')
    gov=record.get('governance')
    if not isinstance(gov,dict) or not gov.get('human_genomic_data') or not gov.get('consent_status'):
        errors.append('governance')
    gate=record.get('claim_gate')
    if gate not in _ALLOWED_CLAIM_GATES:
        errors.append('claim_gate')
    if gate == 'clinical':
        errors.append('claim_gate')
    return sorted(set(errors))
