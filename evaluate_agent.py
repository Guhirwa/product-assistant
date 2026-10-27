from deepeval.metrics import AnswerRelevancyMetric, FaithfulnessMetric
from deepeval.models import AnthropicModel
from deepeval.test_case import LLMTestCase
from agent import ask_agent

judge = AnthropicModel(model="claude-haiku-4-5")

questions = [
    "What is the price of P002?",
    "Find the laptop",
    "What is the price of P999?",
]

for question in questions:
    reply, tool_results = ask_agent(question)  # real answer from my agent

    test_case = LLMTestCase(
        input=question,
        actual_output=reply,
        retrieval_context=tool_results or ["No product information was found."],
    )

    print(f"\nQuestion: {question}\nAnswer: {reply}")
    for metric in [AnswerRelevancyMetric(threshold=0.7, model=judge),
                   FaithfulnessMetric(threshold=0.7, model=judge)]:
        metric.measure(test_case)
        result = "PASS" if metric.is_successful() else "FAIL"
        print(f"  {metric.__name__}: {metric.score:.2f} {result} - {metric.reason}")