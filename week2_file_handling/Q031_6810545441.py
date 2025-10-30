# Name: Krittitee Chaisang  # Student ID: 6810545441
from pathlib import Path

def read_source():
    mode = input("Load from 'file' or 'manual' input? ").strip()
    if mode == "file":
        fname = input("Enter filename: ").strip()
        p = Path(fname)
        if not p.exists():
            print(f"Error: File '{fname}' not found.")
            return None
        return [ln.rstrip("\n") for ln in p.read_text(encoding="utf-8").splitlines()]
    elif mode == "manual":
        print("Enter configuration (type 'DONE' to finish):")
        lines = []
        while True:
            ln = input()
            if ln == "DONE":
                break
            lines.append(ln)
        return lines
    else:
        return None

def parse_value(raw):
    raw = raw.strip()
    if raw.startswith("{") and raw.endswith("}"):
        inner = raw[1:-1]
        parts = [s for s in inner.split(";") if s != ""]
        d = {}
        for p in parts:
            if "=" not in p:
                raise ValueError
            k,v = p.split("=",1)
            d[k.strip()] = v.strip()
        return d
    if "," in raw:
        return [x.strip() for x in raw.split(",")]
    return raw

def parse_lines(lines):
    cfg = {}
    for ln in lines:
        s = ln.strip()
        if not s or s.startswith("#"):
            continue
        if "=" not in s:
            continue
        k,v = s.split("=",1)
        k = k.strip()
        try:
            cfg[k] = parse_value(v)
        except Exception:
            cfg[k] = v.strip()
    return cfg

def validate(cfg):
    if "port" not in cfg:
        return "Validation Error: Port must be an integer between 1 and 65535."
    try:
        port = int(str(cfg["port"]))
        if not (1 <= port <= 65535):
            return "Validation Error: Port must be an integer between 1 and 65535."
    except Exception:
        return "Validation Error: Port must be an integer between 1 and 65535."

    if "allowed_users" not in cfg:
        return "Validation Error: Allowed users list must not be empty."
    users = cfg["allowed_users"]
    if isinstance(users, list):
        if len(users) == 0 or (len(users)==1 and users[0]==""):
            return "Validation Error: Allowed users list must not be empty."
    else:
        if str(users).strip() == "":
            return "Validation Error: Allowed users list must not be empty."

    if "database" not in cfg or not isinstance(cfg["database"], dict):
        return "Validation Error: Database dictionary must contain both 'user' and 'password' keys."
    db = cfg["database"]
    if "user" not in db or "password" not in db:
        return "Validation Error: Database dictionary must contain both 'user' and 'password' keys."
    if "timeout" not in db:
        return "Validation Error: Database timeout must be a positive integer."
    try:
        tout = int(str(db["timeout"]))
        if tout <= 0:
            return "Validation Error: Database timeout must be a positive integer."
    except Exception:
        return "Validation Error: Database timeout must be a positive integer."
    return None

def show(cfg):
    port = int(str(cfg["port"]))
    users = cfg["allowed_users"]
    if isinstance(users, list):
        users_str = ",".join(users)
    else:
        users_str = str(users)
    db = cfg["database"]
    print("Configuration file is valid.")
    print("Parsed Data:")
    print(f"port: {port}")
    print(f"allowed_users: {users_str}")
    print("database:")
    print(f"  user: {db['user']}")
    print(f"  password: {db['password']}")
    print(f"  timeout: {int(str(db['timeout']))}")

lines = read_source()
if lines is not None:
    cfg = parse_lines(lines)
    err = validate(cfg)
    if err:
        print(err)
    else:
        show(cfg)
