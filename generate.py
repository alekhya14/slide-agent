import sys
from orchestration.graph import run_pipeline

if __name__ == "__main__":
    prompt = " ".join(sys.argv[1:])
    # prompt = "Create a 3 slide investor deck with revenue chart"
    output = run_pipeline(prompt)
    print(f"Generated: {output}")