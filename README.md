# Awesome AI Evals

> A curated collection of high-quality resources for evaluating AI systems.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

## Start Here

If you are new to AI evaluation, begin with **[Evaluation Fundamentals](#evaluation-fundamentals)**,
then use the methodology and metrics sections to choose an approach that fits
your system and evaluation goals. Each entry should explain what the resource
is and why it is useful.

## Table of Contents

- [Evaluation Fundamentals](#evaluation-fundamentals)
- [Evaluation Methodology](#evaluation-methodology)
- [Metrics](#metrics)
- [Datasets and Benchmarks](#datasets-and-benchmarks)
- [LLM-as-a-Judge](#llm-as-a-judge)
- [Human Evaluation](#human-evaluation)
- [Agent Evaluation](#agent-evaluation)
- [RAG Evaluation](#rag-evaluation)
- [Safety and Red Teaming](#safety-and-red-teaming)
- [Evaluation Frameworks and Tools](#evaluation-frameworks-and-tools)
- [Papers and Surveys](#papers-and-surveys)
- [Courses, Talks, and Guides](#courses-talks-and-guides)
- [Contributing](#contributing)
- [License](#license)

## Evaluation Fundamentals

Resources that explain the goals, scope, and core concepts of evaluating AI
systems.

_Resources will be added here._

## Evaluation Methodology

Resources on designing reliable evaluations, selecting test cases, comparing
systems, and interpreting results.

<!-- markdownlint-disable-next-line MD013 -->
- [A Comprehensive Guide to LLM Evaluations](https://caylent.com/blog/a-comprehensive-guide-to-llm-evaluations) — A vendor-authored overview of reference-based, programmatic, human, and model-based evaluation, with guidance on judge calibration and continuous regression testing. `Article` · `Free to read`

<!-- markdownlint-disable-next-line MD013 -->
- [AI Evals: Everything You Need to Know](https://hamel.dev/blog/posts/evals-faq/#how-to-use-this-faq) — A practical FAQ covering eval fundamentals, error analysis, evaluator design, human annotation, tooling, production use, and domain-specific workflows. `FAQ` · `Free to read`

## Metrics

Definitions and practical guidance for measuring quality, reliability,
efficiency, and other evaluation dimensions.

<!-- markdownlint-disable-next-line MD013 -->
- [LLM Evaluation Metrics: The Ultimate LLM Evaluation Guide](https://www.confident-ai.com/blog/llm-evaluation-metrics-everything-you-need-for-llm-evaluation) — A vendor-authored guide to selecting metrics across programmatic, model-based, RAG, agent, and multi-turn evaluations, with discussions of G-Eval and metric limitations. `Article` · `Free to read`

## Datasets and Benchmarks

Curated datasets and benchmark suites for testing specific capabilities or
comparing model performance.

<!-- markdownlint-disable-next-line MD013 -->
- [30 LLM Evaluation Benchmarks and How They Work](https://www.evidentlyai.com/llm-guide/llm-benchmarks) — An overview of benchmark design and common LLM benchmarks, with links to datasets and papers; notes contamination, narrow coverage, and benchmark staleness as limitations. `Guide` · `Free to read`
<!-- markdownlint-disable-next-line MD013 -->
- [250 LLM Benchmarks and Evaluation Datasets](https://www.evidentlyai.com/llm-evaluation-benchmarks-datasets) — A database of LLM benchmarks and public datasets tagged by capabilities such as reasoning, coding, safety, multimodality, and tool use; useful for discovery, but not a substitute for product-specific evaluations. `Database` · `Free to read`
<!-- markdownlint-disable-next-line MD013 -->
- [Artificial Analysis Evaluations](https://artificialanalysis.ai/evaluations) — A public catalog of independent model evaluations and benchmark leaderboards spanning reasoning, coding, tool use, long context, multimodality, and agentic capabilities. `Evaluation catalog` · `Free to read`
<!-- markdownlint-disable-next-line MD013 -->
- [Google DeepMind Evals](https://deepmind.google/research/evals/) — A catalog of Google DeepMind benchmarks covering robotics safety, factuality, grounding, deep search, reasoning, and long-context tasks, with links to papers, datasets, and leaderboards. `Benchmark catalog` · `Free to read`

## LLM-as-a-Judge

Research and tools for using language models as evaluators, including guidance
on calibration, bias, and limitations.

## Human Evaluation

Resources on rubric design, annotation workflows, evaluator training, quality
control, and agreement.

_Resources will be added here._

## Agent Evaluation

Resources for evaluating systems that plan, use tools, interact with
environments, or complete multi-step tasks.

<!-- markdownlint-disable-next-line MD013 -->
- [Agent Evaluation: A Detailed Guide](https://cameronrwolfe.substack.com/p/agent-evals) — A long-form guide to agent evaluation covering system
  components, evaluation harnesses, graders, and benchmark case studies.
  `Article` · `Free to read`
<!-- markdownlint-disable-next-line MD013 -->
- [The Roadmap to Mastering AI Agent Evaluation](https://machinelearningmastery.com/the-roadmap-to-mastering-ai-agent-evaluation/) — A practical roadmap covering reasoning and action layers,
  deterministic and model-based grading, non-determinism, and production
  monitoring. `Article` · `Free to read`
<!-- markdownlint-disable-next-line MD013 -->
- [Building Closed-Loop Evals for a Multimodal Agent at Scale](https://www.youtube.com/watch?v=31GUkCBD-Uc) — A talk by Uber engineers on designing evaluations for a multimodal food-enhancement agent, including practical pitfalls and lessons learned. `Video` · `Free to watch`
<!-- markdownlint-disable-next-line MD013 -->
- [Stanford CS329A: Agentic Evaluations and Long-Horizon Tasks](https://www.youtube.com/watch?v=8JAqLnTaZu4) — A Stanford lecture covering METR task horizons, GDPval, DeepScholar-Bench, and recurring long-horizon agent failure modes. `Video` · `Free to watch`

## RAG Evaluation

Resources for evaluating retrieval-augmented generation, including retrieval
quality, grounding, attribution, and answer quality.

_Resources will be added here._

## Safety and Red Teaming

Resources for testing harmful behavior, misuse resistance, robustness,
security, and other safety properties.

_Resources will be added here._

## Evaluation Frameworks and Tools

Maintained frameworks, libraries, and utilities that support repeatable AI
evaluation workflows.

- [DeepEval](https://deepeval.com/docs/introduction) — An open-source Python
  framework for LLM application evaluation with unit-test-style assertions,
  ready-to-use metrics, component and end-to-end evaluations, and local
  execution. `Framework` · `Apache-2.0`

## Papers and Surveys

Research papers and surveys that provide useful findings, methods, taxonomies,
or evidence for AI evaluation.

<!-- markdownlint-disable-next-line MD013 -->
- [METR Research](https://metr.org/research/) — A research index from the nonprofit METR covering autonomous capability evaluations, long-horizon tasks, AI R&D benchmarks, evaluation integrity, and frontier AI safety. `Research index` · `Free to read`

## Courses, Talks, and Guides

Educational material that helps practitioners learn how to design, run, and
interpret AI evaluations.

<!-- markdownlint-disable-next-line MD013 -->
- [Evals for AI Engineers](https://www.oreilly.com/library/view/evals-for-ai/9798341660717/) — A forthcoming O'Reilly book page about systematic testing
  and improving AI application reliability; its table of contents is marked
  not yet final and full access may require a subscription. `Book` ·
  `Paid/Subscription`
<!-- markdownlint-disable-next-line MD013 -->
- [AI Evals Advanced Masterclass in Under 57 Minutes](https://www.youtube.com/watch?v=ztN6bE_FuQQ) — A masterclass with Daniel McKinnon on building agentic evals, including offline testing, task-based evaluation, domain expertise, and repeated sampling. `Video` · `Free to watch`

## Contributing

Suggestions and improvements are welcome. See
[CONTRIBUTING.md](CONTRIBUTING.md) for the submission format and review
guidelines.

## License

The curated list content is dedicated to the public domain under [CC0 1.0](LICENSE).
