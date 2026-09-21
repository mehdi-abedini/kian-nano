_REQ=('cycle_id','candidate_ids','selection_policy','acquisition_budget','observations_added','prior_data_id','posterior_data_id','experiment_linkage','stopping_rule','provenance_id')
def validate_active_learning_record(r):
 e=[]
 if not isinstance(r,dict): return ['record must be dict']
 e += [f'missing required field: {k}' for k in _REQ if k not in r]
 if not isinstance(r.get('candidate_ids'),list) or not r.get('candidate_ids'): e.append('candidate_ids required')
 if not isinstance(r.get('acquisition_budget'),int) or r.get('acquisition_budget')<1: e.append('positive acquisition_budget required')
 if isinstance(r.get('acquisition_budget'),int) and isinstance(r.get('observations_added'),int) and r['observations_added']>r['acquisition_budget']: e.append('observations_added cannot exceed acquisition_budget')
 if not r.get('stopping_rule'): e.append('stopping_rule required')
 return e
