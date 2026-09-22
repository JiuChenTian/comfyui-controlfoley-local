"""Check local model files without importing GPU libraries or accessing the network."""
from controlfoley.local_models import check_models, model_dir

if __name__ == '__main__':
    files = check_models()
    print(f'OK: {len(files)} required model files found in {model_dir()}')
