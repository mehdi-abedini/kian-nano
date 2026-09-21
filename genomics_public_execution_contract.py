_REQUIRED=('benchmark_id','access','input_manifest_hash','reference','workflow','container_digest','parameters_hash','truth_set','metrics','outputs','claim_gate')
def validate_public_execution(record):
    errors=[]
    if not isinstance(record,dict): return ['record']
    errors += [x for x in _REQUIRED if x not in record]
    if record.get('access') != 'public': errors.append('access')
    ref=record.get('reference',{})
    if not all(ref.get(x) for x in ('assembly','reference_id','annotation')): errors.append('reference')
    wf=record.get('workflow',{})
    if not all(wf.get(x) for x in ('engine','pipeline','version')) or wf.get('version') == 'latest': errors.append('workflow')
    if not str(record.get('container_digest','')).startswith('sha256:'): errors.append('container_digest')
    if not str(record.get('parameters_hash','')).startswith('sha256:'): errors.append('parameters_hash')
    truth=record.get('truth_set',{})
    if not truth.get('id') or not truth.get('scope'): errors.append('truth_set')
    if not record.get('metrics'): errors.append('metrics')
    if not record.get('outputs'): errors.append('outputs')
    if record.get('claim_gate') != 'benchmark-only': errors.append('claim_gate')
    return sorted(set(errors))
