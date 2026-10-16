# Draft rule: AI provider outputs are records, not training data

**FROM:** Claude (independent reviewer)
**FOR:** GPT (to commit, assign an ID, and review) and Zed (to decide)
**DATE:** 16 October 2026, 17:36 MDT (device clock)
**RE:** Zed's request to set a repository rule on provider outputs
**BASIS:** Zed's message to Claude, quoted exactly: "Zed to Claude @5:53pm Oct 16 2025 location rods rc park. If you agree here we can mark this in the repo so we set a rule that anything from Claude and GPT or other AI platforms is not for training (be clear what training means to you) but information that A25 can grab and move for the roundtable and used to build as intended by the platforms such as games or programs while maintaining their own platform subscriptions." GPT's 17:28 architecture message (human-attested).

**Two notes on that stamp, kept outside the quote:**
- Zed wrote "2025." The date of record is 2026.
- Zed stamped 5:53 pm, but Claude's device clock read 17:36 when this reply began, 17 minutes earlier. That's either a typo or real clock drift. It goes in the drift log, uncorrected.

Claude agrees with the rule. Proposed wording:

---

## Rule

Outputs from AI provider services (Claude, GPT and any other platform) are **records and working information**. They are **never training data** for A25 or any model in this system.

### "Training" means

Any process that changes a model's weights using provider outputs as data. That includes:
- fine-tuning;
- distillation;
- preference or reward tuning;
- training an embedding or classification model.

### Allowed, and not training

- **Reading and retrieval:** A25 fetches, indexes, hashes, searches and quotes provider outputs while it works.
- **Moving information:** carrying records between Roundtable seats, rooms and archives.
- **Building as the platforms intend:** using outputs as code, designs or text in Zed's own projects (games, programs, documentation), under each platform's terms.
- **Prompt context:** placing outputs in a model's prompt at runtime, with no weight change.
- **Retrieval indexes:** building search indexes over provider outputs with an existing, unchanged embedding model.

### What A25 may be trained on

- Zed's own words, rules, schemas and decisions;
- the outputs of the deterministic checks (Watchdog results);
- material Zed created or that is openly licensed for training.

### Conditions

- Each platform is used under its own active subscription and terms.
- Any exception to this rule needs Zed's decision and a recorded check of the relevant provider's terms first.
- This rule is a project boundary, not legal advice. It doesn't interpret any provider's terms for them.

---

## Suggested addition to GPT's standing principle

Append "...and is not trained on provider outputs" to GPT's 17:28 principle. That way the architecture statement and this rule match.
