# GridPrint MVP
Smart‑grid‑aware 3D printing scheduler MVP for Vice3D production validation.

## What this is
GridPrint is a lightweight scheduling tool that recommends the cheapest time to start a 3D print based on electricity prices. It is designed and validated using real production prints from Vice3D (21h crimps, 10h callous balls, 3h inserts).

This MVP focuses on:
- Loading a price curve (manual JSON for now)
- Accepting a print duration + deadline
- Recommending the cheapest start time
- Logging real energy usage from a smart plug

## Roadmap
### Phase 1 — Baseline data collection
- Log energy usage for real Vice3D prints
- Build baseline energy model for Bambu P1S + PLA

### Phase 2 — MVP Scheduler
- Load price curve
- Compute cheapest start time
- Estimate cost savings

### Phase 3 — Validation
- Compare “start now” vs “scheduled start”
- Document real savings

### Phase 4 — Dynamic Profiles (Eco/Turbo)
- G‑code post‑processing
- Speed/temperature modulation

## Status
Repo initialized. Baseline data collection begins as soon as smart plug arrives.
