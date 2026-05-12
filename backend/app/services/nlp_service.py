"""
spaCy-based skill extraction from resume/job text.
"""
from __future__ import annotations

import spacy

SKILL_KEYWORDS = frozenset({
    "python",
    "java",
    "javascript",
    "react",
    "nodejs",
    "sql",
    "mongodb",
    "postgresql",
    "docker",
    "kubernetes",
    "aws",
    "azure",
    "gcp",
    "machine learning",
    "deep learning",
    "nlp",
    "tensorflow",
    "pytorch",
    "scikit-learn",
    "fastapi",
    "django",
    "flask",
    "git",
    "linux",
    "data analysis",
    "tableau",
    "power bi",
    "excel",
    "c++",
    "c#",
    "html",
    "css",
    "typescript",
    "redis",
    "kafka",
    "spark",
    "hadoop",
    "devops",
    "ci/cd",
    "agile",
    "scrum",
})

_nlp = None


def _get_nlp():
    global _nlp
    if _nlp is None:
        _nlp = spacy.load("en_core_web_sm")
    return _nlp


def extract_skills(text: str) -> list[str]:
    """
    Tokenize `text` with spaCy; match unigrams and bigrams against SKILL_KEYWORDS.
    Also matches keywords that contain punctuation (e.g. c++, ci/cd) via substring
    checks on the lowercased source text.
    Returns a sorted list of unique matched skills (lowercase).
    """
    if not text or not text.strip():
        return []

    nlp = _get_nlp()
    doc = nlp(text)
    text_lower = text.lower()

    matched: set[str] = set()

    toks: list[str] = []
    for t in doc:
        if t.is_space:
            continue
        toks.append(t.text.lower())

    for w in toks:
        if w in SKILL_KEYWORDS:
            matched.add(w)

    for i in range(len(toks) - 1):
        bigram = f"{toks[i]} {toks[i + 1]}"
        if bigram in SKILL_KEYWORDS:
            matched.add(bigram)

    for kw in SKILL_KEYWORDS:
        if any(c in kw for c in "+#/"):
            if kw in text_lower:
                matched.add(kw)

    # Phrases spaCy may split across punctuation (e.g. "node" "." "js")
    if "node.js" in text_lower or "nodejs" in text_lower:
        matched.add("nodejs")

    return sorted(matched)
