_REQUIRED=('dataset_id','dataset_version','task_type','target','unit','representation','split_strategy','source_id','provenance_id','counts','metric','uncertainty','applicability_domain','leakage_controls')
_ALLOWED_TASKS={'classification','regression'}
_ALLOWED_SPLITS={'random','scaffold','temporal','source_held_out','external'}

def validate_benchmark_record(record):
    errors=[]
    if not isinstance(record,dict): return ['record must be a dict']
    errors += [f'missing required field: {k}' for k in _REQUIRED if k not in record]
    if record.get('task_type') not in _ALLOWED_TASKS: errors.append('invalid task_type')
    if record.get('split_strategy') not in _ALLOWED_SPLITS: errors.append('invalid split_strategy')
    counts=record.get('counts')
    if not isinstance(counts,dict) or not all(isinstance(v,int) and v>=0 for v in counts.values()): errors.append('counts must contain non-negative integers')
    if not record.get('leakage_controls'): errors.append('leakage_controls required')
    if not record.get('uncertainty'): errors.append('uncertainty metadata required')
    if not record.get('applicability_domain'): errors.append('applicability_domain metadata required')
    return errors

def link_molecule_to_benchmark(molecule_id, benchmark_id):
    if not molecule_id or not benchmark_id: raise ValueError('molecule_id and benchmark_id are required')
    return {'molecule_id':molecule_id,'benchmark_id':benchmark_id,'link_type':'molecular_property_benchmark'}
