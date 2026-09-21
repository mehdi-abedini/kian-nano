_REQ=('candidate_id','development_stage','intended_use','manufacturing_status','regulatory_jurisdiction','ip_status','fto_status','claim_boundaries','evidence_ledger_id','confidentiality')
def validate_translation_record(r):
 e=[]
 if not isinstance(r,dict): return ['record must be dict']
 e += [f'missing required field: {k}' for k in _REQ if k not in r]
 if not r.get('confidentiality'): e.append('confidentiality required')
 if r.get('intended_use')=='commercial_product' and r.get('fto_status')!='assessed': e.append('commercial product intent requires assessed FTO')
 if r.get('intended_use')=='commercial_product' and r.get('regulatory_jurisdiction')=='unspecified': e.append('commercial product intent requires jurisdiction')
 return e
