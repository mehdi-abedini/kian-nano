_REQ=('interaction_id','formulation_id','biological_context','exposure','endpoints','controls','method','provenance_id')
def validate_interaction_record(r):
 e=[]
 if not isinstance(r,dict): return ['record must be dict']
 e += [f'missing required field: {k}' for k in _REQ if k not in r]
 if not isinstance(r.get('biological_context'),dict) or not r.get('biological_context'): e.append('biological_context required')
 if not isinstance(r.get('controls'),list) or not r.get('controls'): e.append('controls required')
 return e
