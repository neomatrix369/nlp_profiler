from nlp_profiler.constants import NOT_APPLICABLE, NaN
import language_tool_python


### Grammar check: this is a very slow process
### take a lot of time per text it analysis
def grammar_check_score(text: str) -> int:
    if (not isinstance(text, str)) or (len(text.strip()) == 0):
        return NaN

    tool = language_tool_python.LanguageTool('en-GB')
    matches = tool.check(text)
    return len(matches)


def grammar_quality(score: float) -> str:
    if score is NaN:
        return NOT_APPLICABLE

    if score == 1:
        return "1 issue"
    elif score > 1:
        return f"{score} issues"

    return "No issues"
