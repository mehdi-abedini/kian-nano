_REQ=('validation_id','claim_type','evidence_class','dataset_ids','split_strategy','external_validation','replicates','metrics','uncertainty_reported','failure_cases_recorded','provenance_id')
def validate_validation_record(r):
 e=[]
 if not isinstance(r,dict): return ['record must be dict']
 e += [f'missing required field: {k}' for k in _REQ if k not in r]
 if not isinstance(r.get('replicates'),int) or r.get('replicates')<1: e.append('replicates must be >=1')
 if not r.get('uncertainty_reported'): e.append('uncertainty must be reported')
 if not r.get('failure_cases_recorded'): e.append('failure cases must be recorded')
 return e
