import autogen
import os

# Import OpenAI API key
# When config_list gets more complicated, should start using OAI_CONFIG_LIST
#config_list = autogen.config_list_from_json(env_or_file="OAI_CONFIG_LIST")

# Create the assistant agent
assistant = autogen.AssistantAgent(
  name="assistant",
  llm_config={
    #"cache_seed": 100,
    #"config_list": config_list, # A list of OpenAI API configurations
    "config_list": [{"model": "gpt-4-1106-preview", "api_key": os.environ["OPENAI_API_KEY"]}],
    "temperature": 0, # Temperature for sampling
  }, # Configuration for autogen's enhanced inference API which is compatible with OpenAI API
)

# Create the user proxy agent
user_proxy = autogen.UserProxyAgent(
  name="UserProxy",
  human_input_mode="NEVER", # Never prompt user for feedback
  max_consecutive_auto_reply=10,
  is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
  code_execution_config={
    "work_dir": "generated-content",
    "use_docker": False, # Set to True or image name (e.g. "python:3") to use.
  },
)

# Start the conversation
user_proxy.initiate_chat(
  assistant,
  message="Create a python script that lists the first 5 prime numbers.",
)
