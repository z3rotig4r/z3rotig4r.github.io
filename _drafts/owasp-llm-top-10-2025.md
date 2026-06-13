---
layout: post
title: "[Security for AI] OWASP LLM Top 10 (2025) 완전 정리 — 항목별 공격과 방어"
description: "OWASP Top 10 for LLM Applications 2025를 LLM01~LLM10 항목별 공격 시나리오·방어와 함께 한글로 정리. 2023판 대비 변경점까지."
category: [Security for AI]
tags: [owasp, llm-security, prompt-injection, ai-red-teaming, excessive-agency]
math: false
mermaid: false
toc: true
image:
  path: /assets/img/contents/owasp-llm-top-10-2025/cover.png
  alt: OWASP LLM Top 10 2025 — LLM 애플리케이션 10대 보안 위험
---

> **TL;DR** — OWASP Top 10 for LLM Applications **2025(v2.0)** 는 LLM 앱의 10대 보안 위험을 정리한 사실상의 산업 표준이다. 2023판 대비 **System Prompt Leakage(LLM07)**, **Vector and Embedding Weaknesses(LLM08, RAG 보안)** 가 새로 들어왔다. 항목별로 공격과 방어를 한 번에 본다.
{: .prompt-tip }

## OWASP LLM Top 10이란

[OWASP](https://owasp.org)는 웹 보안의 "Top 10"으로 유명한 비영리 보안 단체다. LLM 도입이 폭발하자 **OWASP GenAI Security Project** 가 LLM 애플리케이션 전용 Top 10을 만들었고, **2024-11-18에 2025판(v2.0)** 을 공개했다. 모델 자체가 아니라 **LLM을 쓰는 애플리케이션**(챗봇, RAG, 에이전트)의 위험에 초점을 둔다.

아래 10개를 먼저 한눈에 본 뒤, 항목별로 들어간다.

| ID | 위험 | 한 줄 요약 |
|----|------|-----------|
| LLM01 | Prompt Injection | 입력에 심은 지시로 모델 행동 탈취 |
| LLM02 | Sensitive Information Disclosure | 학습/맥락 속 민감정보 유출 |
| LLM03 | Supply Chain | 모델·데이터·플러그인 공급망 오염 |
| LLM04 | Data and Model Poisoning | 학습·파인튜닝 데이터 오염 |
| LLM05 | Improper Output Handling | 모델 출력을 검증 없이 실행/렌더 |
| LLM06 | Excessive Agency | 과도한 권한·도구·자율성 |
| LLM07 | System Prompt Leakage | 시스템 프롬프트 내용·비밀 노출 |
| LLM08 | Vector and Embedding Weaknesses | RAG 벡터·임베딩 취약점 |
| LLM09 | Misinformation | 환각·오정보로 인한 피해 |
| LLM10 | Unbounded Consumption | 무제한 자원 소비·DoW(Denial of Wallet) |

## LLM01 — Prompt Injection

공격자가 입력에 악성 지시를 심어 모델이 본래 목표 대신 공격자 의도를 수행하게 만든다. **직접(direct)** 과 데이터에 숨기는 **간접(indirect)** 으로 나뉜다. 근본 원인은 "지시(instruction)와 데이터(data)가 한 컨텍스트에 섞이는" LLM 구조 그 자체.

- **방어:** 입력/출력 분리, 시스템 프롬프트 권한 우선, 신뢰 경계 격리, 출력 검증, HITL. 깊은 내용은 [프롬프트 인젝션 심화](/posts/prompt-injection-deep-dive/) 참고.

## LLM02 — Sensitive Information Disclosure

모델이 학습 데이터·대화 맥락·시스템 설정에 든 PII, 자격증명, 영업비밀을 출력으로 흘린다. RAG가 권한 없는 문서를 끌어오면 더 커진다.

- **방어:** 학습 데이터 정제·익명화, 출력 필터링(DLP), RAG 접근제어(문서 단위 권한), 최소수집 원칙.

## LLM03 — Supply Chain

서드파티 모델·데이터셋·라이브러리·플러그인이 오염되면 앱 전체가 위험하다. 변조된 사전학습 모델, 악성 어댑터(LoRA), 백도어가 포함된다.

- **방어:** 모델·데이터 출처 검증(서명·해시), SBOM, 신뢰 레지스트리만 사용, 의존성 스캔. 에이전트 도구 공급망은 [MCP Tool Poisoning](/posts/mcp-tool-poisoning/) 참고.

## LLM04 — Data and Model Poisoning

학습·파인튜닝·임베딩 단계의 데이터에 공격자가 악성 샘플을 주입해 모델에 편향·백도어·트리거를 심는다. 공개 크롤링 데이터가 주 통로.

- **방어:** 데이터 출처 추적·검증, 이상치 탐지, 견고한 학습(robust training), 트리거 테스트, 데이터 버저닝.

## LLM05 — Improper Output Handling

모델 출력을 **신뢰할 수 없는 입력으로 다루지 않고** 그대로 실행·렌더·전달할 때 발생. 출력이 SQL·셸·HTML로 흘러 XSS, SQLi, RCE로 이어진다.

- **방어:** 출력을 사용자 입력처럼 취급, 컨텍스트별 인코딩/파라미터화, 다운스트림 시스템 권한 최소화.

## LLM06 — Excessive Agency

LLM에 **과도한 기능·권한·자율성**을 줘서, 인젝션이 성공하면 피해가 증폭된다. 불필요한 도구, 광범위한 API 스코프, 무인 자동 실행이 원인. 에이전트 시대의 핵심 위험.

- **방어:** 최소 기능·최소 권한, 비가역 작업 HITL 게이트, 도구별 스코프 제한. [에이전트 권한 상승](/posts/agentic-ai-privilege-escalation/)에서 심화.

## LLM07 — System Prompt Leakage (신규)

2025판 신규. 시스템 프롬프트가 노출되는 것 자체보다, **거기에 비밀(API 키·권한 규칙·필터 로직)을 담는 설계**가 위험이다. 새면 우회·권한상승의 지도가 된다.

- **방어:** 시스템 프롬프트에 비밀 금지(외부 권한제어로), 프롬프트 누출 가정 설계, 민감 로직은 앱 계층에.

## LLM08 — Vector and Embedding Weaknesses (신규)

2025판 신규, **RAG 보안**. 벡터 DB·임베딩의 취약점 — 지식베이스 포이즈닝, 임베딩 역전(원문 복원), 권한 없는 벡터 접근, 교차 테넌트 누출.

- **방어:** 벡터 저장소 접근제어·테넌트 격리, 인덱싱 데이터 출처 검증, 임베딩 민감도 평가.

## LLM09 — Misinformation

모델의 환각·오정보를 사용자가 신뢰해 잘못된 결정을 내린다. 코드 환각(존재하지 않는 패키지 추천 → slopsquatting), 법률·의료 오정보 등.

- **방어:** RAG로 근거 제공, 출처 표기, 불확실성 고지, 고위험 도메인 HITL, 자동 사실검증.

## LLM10 — Unbounded Consumption

무제한 추론 요청으로 비용·자원을 고갈시킨다. **DoW(Denial of Wallet)**, 모델 추출(쿼리 반복으로 모델 복제), 서비스 거부 포함.

- **방어:** rate limit·쿼터, 입력/출력 길이 제한, 비용 모니터링·알람, 추출 탐지.

## 2023 → 2025 무엇이 바뀌었나

- **신규:** LLM07 System Prompt Leakage, LLM08 Vector and Embedding Weaknesses(RAG 확산 반영).
- **확장:** Excessive Agency(LLM06)·Supply Chain(LLM03) 비중↑ — 에이전트·생태계화 반영.
- **재구성:** 기존 "Insecure Output Handling" → LLM05, "Training Data Poisoning" → LLM04(Data and Model Poisoning)로 일반화.

흐름은 분명하다: **단일 모델 위험 → 에이전트·RAG·공급망 등 시스템 위험**으로 무게가 옮겨갔다.

## 정리

OWASP LLM Top 10은 LLM 보안의 공통 언어다. 실무 적용 순서: **(1)** 내 앱이 어느 항목에 노출됐는지 매핑 → **(2)** LLM01·LLM06·LLM08(인젝션·과도권한·RAG)부터 우선 방어 → **(3)** [garak](https://github.com/NVIDIA/garak) 같은 스캐너로 자동 점검. 각 항목 심화글은 시리즈로 이어간다.

## 참고/출처

- [OWASP Top 10 for LLM Applications 2025 (v2.0, PDF)](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf) — OWASP GenAI Security Project, 2024-11-18
- [LLM01:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) — OWASP GenAI
- [OWASP GenAI Security Project](https://genai.owasp.org/) — 프로젝트 홈
