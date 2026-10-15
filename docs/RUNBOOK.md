# Incident Runbook — proposed, non-operational exercise

This is a proposed response for the synthetic exercise, not an approved institutional procedure. The system is not authorized for operational use with real people. An institutional owner, incident contacts, and due dates have not been assigned.

1. **Detection and classification:** flag a failed configured gate, material change in group metrics, data/schema issue, model drift, or suspected out-of-scope use. Preserve the specific report and model version; classify impact with the institutional owner once assigned.
2. **Containment authority:** suspend model-assisted prioritization immediately when a gate fails or an incident is suspected. The institutional owner must formally designate who can suspend and who can approve resumption; neither role is assigned here.
3. **Evidence preservation:** retain the input-data version, model artifact and version, configuration, run logs, subgroup/intersectional metrics, decision log, and incident timeline, subject to approved retention and privacy rules. Do not collect additional personal data for this synthetic exercise.
4. **Internal and affected-party communication:** notify the designated institutional, technical, privacy/legal, and oversight contacts. If a future real system affects people, define accessible notice, correction, and appeal channels before use; contacts and timelines require institutional approval.
5. **Rollback or safe baseline:** stop model scoring and return to human review without a model score. Do not resume until the cause is investigated, controls are tested, affected-party impacts are assessed where applicable, and the designated owner approves.
6. **Postmortem, owner and due date:** document detection, affected scope, root cause, containment, communications, corrective actions, validation evidence, and approval to close. Assign an institutional owner and due date before this runbook can be treated as operational.
