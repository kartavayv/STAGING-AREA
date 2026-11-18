import glob, os
import pandas as pd

DATA_DIR = "DATA/SYMBA - Test Data/SYMBA - Test Data"   # path to the unzipped folder

def load_symba(data_dir, theory="QED"):
    rows = []
    for path in sorted(glob.glob(os.path.join(data_dir, "**", f"{theory}-*.txt"), recursive=True)):
        with open(path, encoding="utf-8") as f:
            for lineno, line in enumerate(f, 1):
                line = line.rstrip("\n")
                if not line.strip():
                    continue
                parts = line.split(" : ")
                assert len(parts) == 4, f"{path}:{lineno} has {len(parts)} fields"
                rows.append({
                    "file": os.path.basename(path),
                    "line": lineno,
                    "interaction": parts[0].removeprefix("Interaction:").strip(),
                    "vertices": parts[1],
                    "amp": parts[2],
                    "sqamp": parts[3],
                })
    return pd.DataFrame(rows)

df = load_symba(DATA_DIR, "QED")
print(df.shape)                       # expect (360, 6)
print(df[["amp", "sqamp"]].describe())

# Goal 1: print 20 raw pairs
for i, r in df.sample(20, random_state=0).iterrows():
    print(f"--- row {i} ({r.file}:{r.line})")
    print("AMP :", r.amp)
    print("SQ  :", r.sqamp)
    print()