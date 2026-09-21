_REQ=('formulation_id','carrier_class','components','process','cqa','measurement_context','provenance_id')
def validate_formulation_record(r):
 e=[]
 if not isinstance(r,dict): return ['record must be dict']
 e += [f'missing required field: {k}' for k in _REQ if k not in r]
 if not isinstance(r.get('components'),list) or not r.get('components'): e.append('components required')
 if not isinstance(r.get('process'),dict): e.append('process required')
 c=r.get('cqa',{})
 if 'pdi' in c and (not isinstance(c['pdi'],(int,float)) or not 0<=c['pdi']<1): e.append('pdi must be in [0,1)')
 return e
