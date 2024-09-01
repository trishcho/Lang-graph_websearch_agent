from agent_graph.graph import create_graph, compile_workflow
from langgraph.errors import GraphRecursionError
import sys

# Configuration settings
server = 'openai'
model = 'gpt-4o'
model_endpoint = None
iterations = 40

print("Creating graph and compiling workflow...")
graph = create_graph(server=server, model=model, model_endpoint=model_endpoint)
workflow = compile_workflow(graph)
print("Graph and workflow created.")

if __name__ == "__main__":

    verbose = False

    while True:
        query = input("Please enter your research question: ")
        if query.lower() == "exit":
            break

        dict_inputs = {"research_question": query}
        limit = {"recursion_limit": iterations}

        try:
            for event in workflow.stream(dict_inputs, limit):
                if verbose:
                    print("\nState Dictionary:", event)
                else:
                    print("\n")
        except GraphRecursionError as e:
            print(f"Error: {str(e)}")
            print("Recursion limit reached. Terminating the program.")
            sys.exit(1)
