import json
from pathlib import Path
from urllib.request import Request, urlopen

class SchemaFetchError(ValueError):
    pass

def schema_url(repository, version, filename):
    if not repository or "/" not in repository: raise SchemaFetchError("repository must be owner/name")
    if not version or version in {"latest","main","master"}: raise SchemaFetchError("schema fetch requires pinned version")
    if filename not in {"nextflow_schema.json","assets/schema_input.json"}: raise SchemaFetchError("unsupported schema")
    return f"https://raw.githubusercontent.com/{repository}/{version}/{filename}"

def fetch_schema(repository, version, filename, opener=urlopen):
    url=schema_url(repository,version,filename)
    req=Request(url,headers={"User-Agent":"KNN-Genomics-Agent/1.0"})
    with opener(req, timeout=20) as response:
        data=json.loads(response.read().decode("utf-8"))
    if not isinstance(data,dict): raise SchemaFetchError("schema root must be object")
    return {"url":url,"schema":data}
