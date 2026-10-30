export const meta = {
  name: 'ucompute-growth-draft-review',
  description: 'Fact-check and reader-review the four UCompute Growth content drafts against engineering evidence',
  phases: [
    { title: 'Fact-check', detail: 'each draft checked sentence by sentence against the evidence' },
    { title: 'Reader review', detail: 'clarity, usefulness and hype check for the target developer audience' },
  ],
}
const REPO = '/Users/nasr/repos/ucompute-growth'
const ENG = '/Users/nasr/repos/ucompute'
const DRAFTS = [
  { file: '2026-10-30-pairing-explainer.md', evidence: `${ENG}/docs/decisions/ADR-0003-peer-identity-pairing-transport-discovery.md (section 9, implementation notes; if the file name differs, use the ADR-0003 file in that folder), ${ENG}/docs/security/THREAT_MODEL.md sections 2.13, 3 and 4, ${REPO}/evidence/upstream/capability-snapshot.md sections 3.2, 8 and 9` },
  { file: '2026-10-31-loopback-rpc-vs-authenticated-transport.md', evidence: `https://github.com/ggml-org/llama.cpp/blob/master/tools/rpc/README.md and https://github.com/ggml-org/llama.cpp/blob/master/SECURITY.md (fetch and compare the quotations verbatim), ${ENG}/docs/security/THREAT_MODEL.md section 3 (secure defaults) and 2.13 row M4-01, ${ENG}/docs/decisions/ADR-0002*.md, ${REPO}/evidence/upstream/capability-snapshot.md sections 5, 8 and 9` },
  { file: '2026-11-01-memory-fit-explainer.md', evidence: `${ENG}/crates/ucompute-models/src/feasibility.rs (calibration constants, estimate, check_fit), ${ENG}/docs/VERIFICATION.md (search for F-01-03), ${REPO}/evidence/upstream/capability-snapshot.md section 7 and 8` },
  { file: '2026-11-02-openai-client-base-url.md', evidence: `${ENG}/README.md (serve, port, API), ${ENG}/crates/ucompute-api/src (routes: /v1/models, /openapi.json, /metrics; confirm they exist with grep), ${REPO}/evidence/upstream/capability-snapshot.md section 8 claim 4; the official OpenAI Python and Node client READMEs for the base_url / baseURL parameter names` },
]
const FINDINGS = { type: 'object', properties: { findings: { type: 'array', items: { type: 'object', properties: {
  quote: { type: 'string' }, problem: { type: 'string' }, severity: { type: 'string', enum: ['blocker', 'major', 'minor'] }, fix: { type: 'string' }, evidence: { type: 'string' } }, required: ['quote', 'problem', 'severity', 'fix'] } }, verdict: { type: 'string' } }, required: ['findings', 'verdict'] }

const RULES = `Rules the draft must obey: every product statement must be supported by the evidence files (read them; do not rely on memory); development-build qualifiers must be present; the draft must not imply pooling, model splitting, speed, end-to-end privacy, offline use, platform support, a public release, a download, open-source availability (the source is unpublished) or a waitlist; no person, machine name, tester, IP address other than loopback, university or private repository may appear; quotations from third parties must be verbatim; numbers must match the evidence exactly with model, hardware and build qualifier. The engineering repository at ${ENG} is READ-ONLY: never edit, stage or commit there. Do not edit the draft either; report findings only.`

const results = await pipeline(
  DRAFTS,
  d => agent(`You are a meticulous technical fact-checker for UCompute Growth. Read the draft ${REPO}/content/drafts/${d.file} and then the evidence: ${d.evidence}. ${RULES}\nCheck the draft sentence by sentence. For each factual statement, confirm it against the evidence or report it. Report also any statement that is technically true but overstated, any missing qualifier the capability snapshot section 8 requires next to a claim, and any detail that reveals internal identifiers the website rule forbids while the source is unpublished (commit hashes, requirement ids like F-02-03, test names, file paths). Return findings with exact quotes and a concrete fix, and a one-line verdict (publishable as is / publishable after fixes / not publishable).`,
    { label: `factcheck:${d.file}`, phase: 'Fact-check', schema: FINDINGS }),
  (fc, d) => agent(`You are a senior developer who runs local LLMs and owns two computers, reading ${REPO}/content/drafts/${d.file} for the first time. Judge it as a reader: Is it specific and useful, or marketing? Does it teach something you can verify or apply? Where does it lose you, repeat itself, or hedge so much it says nothing? Is the headline honest? Which sentences read as hype or as AI-generated filler? What would make you trust or share it? Also list anything that reads as a claim you would want proof for. Context: UCompute is an unreleased open-source project; the note must not promise downloads. Return findings (quote, problem, severity, fix) and a verdict. Previous fact-check verdict for context: ${fc ? fc.verdict : 'n/a'}.`,
    { label: `reader:${d.file}`, phase: 'Reader review', schema: FINDINGS, effort: 'medium' })
    .then(rr => ({ file: d.file, factcheck: fc, reader: rr }))
)
return results.filter(Boolean)