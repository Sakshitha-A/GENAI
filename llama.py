
from clarifai.client.workflow import Workflow

# Your PAT (Personal Access Token) can be found in the Account's Security section

# Initialize the workflow_url
workflow_url = "https://clarifai.com/dkl6r5m9gj82/Llama/workflows/workflow-453908"
text_classfication_workflow = Workflow(
    url= workflow_url , pat="42a01ab970e542979f536e04de5be65d"
)
result = text_classfication_workflow.predict_by_bytes(b"I hate you", input_type="text")
print(result.results[0].outputs[0].data)
