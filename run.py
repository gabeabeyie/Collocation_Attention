import os
import subprocess

def run_notebook(notebook_path):
    """Executes a Jupyter notebook programmatically."""
    command = f"jupyter nbconvert --to notebook --execute {notebook_path}"
    subprocess.run(command, shell=True, check=True)

def main():
    notebooks = [
        "notebooks/main_results.ipynb",
        "notebooks/Appendix.ipynb"
    ]
    
    for notebook in notebooks:
        print(f"Running {notebook}...")
        run_notebook(notebook)
    
    print("All notebooks executed successfully.")

if __name__ == "__main__":
    main()