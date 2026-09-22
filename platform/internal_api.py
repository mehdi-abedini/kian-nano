"""Small stdlib-only control API for the n8n automation plane.
It records proposals/snapshots as JSONL; production deployment should move persistence to Postgres.
"""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import json, os

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "runtime"
DATA.mkdir(exist_ok=True)

def append(name, payload):
    with (DATA / name).open("a", encoding="utf-8") as f:
        f.write(json.dumps(payload, ensure_ascii=False) + "\n")

class Handler(BaseHTTPRequestHandler):
    def _send(self, code, payload):
        body=json.dumps(payload, ensure_ascii=False).encode()
        self.send_response(code); self.send_header("Content-Type","application/json"); self.send_header("Content-Length",str(len(body))); self.end_headers(); self.wfile.write(body)
    def do_GET(self):
        if self.path == "/health": self._send(200, {"status":"ok","service":"knn-agent-control"}); return
        self._send(404, {"error":"not_found"})
    def do_POST(self):
        length=int(self.headers.get("Content-Length","0")); raw=self.rfile.read(length)
        try: payload=json.loads(raw or b"{}")
        except json.JSONDecodeError: self._send(400, {"error":"invalid_json"}); return
        if self.path == "/internal/update-proposals": append("update_proposals.jsonl", payload); self._send(202, {"accepted":True,"mode":"proposal-only"}); return
        if self.path == "/internal/provider-snapshot": append("provider_snapshots.jsonl", payload); self._send(202, {"accepted":True}); return
        self._send(404, {"error":"not_found"})
    def log_message(self, *_): pass

if __name__ == "__main__":
    port=int(os.getenv("KNN_CONTROL_PORT","8090"))
    ThreadingHTTPServer(("127.0.0.1",port), Handler).serve_forever()
