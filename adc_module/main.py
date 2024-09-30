from adc_module.adc_module_logic import GhostDetector
from adc_module.hardware import MachineADC, sleep_ms

if __name__ == "__main__":
    adc_module = GhostDetector(adc_class=MachineADC, sleep_ms=sleep_ms)
    adc_module.main()
