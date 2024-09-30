from adc_module_logic import GhostDetector  # type: ignore[import-untyped]
from hardware import MachineADC, sleep_ms  # type: ignore[import-untyped]

if __name__ == "__main__":
    adc_module = GhostDetector(adc_class=MachineADC, sleep_ms=sleep_ms)
    adc_module.main()
