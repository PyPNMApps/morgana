# Copyright 2026 MORGANA contributors
# SPDX-License-Identifier: Apache-2.0
"""Paired native consumer of the same generic source fixture; no Python science."""
from pathlib import Path
import morgana


def main() -> None:
    """Load idle, discover the actual inventory, run and inspect owned results."""
    fixture = Path(__file__).resolve().parents[1] / "configuration/us-50khz.json"
    document = morgana.ConfigurationDocument.from_json(fixture.read_bytes())
    print("Available presets:", document.inventory())
    simulation = morgana.Simulation()
    simulation.configure_document(document)
    report = simulation.run()
    print(report.to_json())
    if not report.reference_recovered:
        raise RuntimeError("Inspect the retained completed/partial scientific report")


if __name__ == "__main__":
    main()
