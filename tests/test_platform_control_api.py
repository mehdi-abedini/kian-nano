import json
import os
import subprocess
import sys
import time
import urllib.request
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]

class PlatformControlApiTests(unittest.TestCase):
    def test_health_and_proposal_boundary(self):
        env=os.environ.copy(); env["KNN_CONTROL_PORT"]="18090"
        p=subprocess.Popen([sys.executable, str(ROOT/"platform"/"internal_api.py")], env=env)
        try:
            time.sleep(0.25)
            with urllib.request.urlopen("http://127.0.0.1:18090/health", timeout=2) as r:
                self.assertEqual(r.status, 200)
            req=urllib.request.Request("http://127.0.0.1:18090/internal/update-proposals", data=json.dumps({"candidate":"x"}).encode(), headers={"Content-Type":"application/json"})
            with urllib.request.urlopen(req, timeout=2) as r:
                body=json.load(r); self.assertEqual(r.status, 202); self.assertTrue(body["accepted"]); self.assertEqual(body["mode"],"proposal-only")
        finally:
            p.terminate(); p.wait(timeout=3)

if __name__=="__main__": unittest.main()
