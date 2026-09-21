_REQ=('design_id','target_id','representation','model','training_data_id','split_strategy','uncertainty','applicability_domain','synthesis_feasibility','objective_terms','provenance_id')
def validate_design_record(r):
 e=[]
 if not isinstance(r,dict): return ['record must be dict']
 e += [f'missing required field: {k}' for k in _REQ if k not in r]
 if r.get('split_strategy') not in {'scaffold','temporal','source_held_out','external'}: e.append('robust split strategy required')
 if not r.get('uncertainty'): e.append('uncertainty required')
 if not r.get('applicability_domain'): e.append('applicability_domain required')
 if not r.get('synthesis_feasibility'): e.append('synthesis_feasibility required')
 return e
