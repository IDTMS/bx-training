# Session 05 – GPU Awareness

## Objective
Detect GPU capability on the local workstation and document CPU vs GPU expectations using the `scripts/gpu_check.py` helper.

## Why This Matters
- Knowing whether CUDA is available changes how we schedule work.
- GPU checks must fail gracefully without blocking CPU-only contributors.
- Clear messaging prevents hype-driven confusion—either a GPU exists or it does not.

## Prereqs
- Sessions 01–04 complete.
- `.venv` active.
- Optional: PyTorch installed if you want CUDA detection.

## Concepts
- Platform inspection via Python.
- Optional dependency handling.
- Communicating fallback guidance.

## Steps
1. **Run the GPU check**
   ```bash
   python scripts/gpu_check.py
   ```
2. **Interpret the JSON output**
   - `os` and `python_version` confirm runtime.
   - `gpu.torch_installed` indicates whether PyTorch is available.
   - `gpu.cuda_available` reports `torch.cuda.is_available()` when torch exists.
3. **Document findings**
   ```bash
   python scripts/gpu_check.py > logs/gpu_check.json
   ```
4. **Optional: install torch (WSL + Linux)**
   ```bash
   pip install torch --index-url https://download.pytorch.org/whl/cpu
   python scripts/gpu_check.py
   ```
5. **Review next steps**
   - If you have no GPU, note that CPU agents remain supported.
   - If CUDA appears, mark the driver/toolkit version for later tuning.

## Deliverables
- `scripts/gpu_check.py` script in repo.
- Captured output saved to `logs/gpu_check.json` (local evidence).

## Done When
- [ ] Script prints JSON without stack traces.
- [ ] You know whether torch is installed and whether CUDA is available.
- [ ] A log file captures the check for future reference.

## Troubleshooting
- **`ModuleNotFoundError: torch`:** expected if not installed; install only if needed.
- **`ImportError: libcudart`:** indicates missing CUDA runtime—install drivers/toolkit or stick with CPU path.
- **Windows without WSL:** strongly recommended to rerun inside WSL for consistent tooling.
