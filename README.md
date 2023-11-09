# autogen-aider-docker

### How to use

- Requires Python and Docker to be installed.
- If using as-is, you will also need an OpenAI API key (but autogen can be configured to use other models).
- Build the docker image: `docker build -t autogen-aider-docker .`.
- Create `.env` and add OpenAI API key: `OPENAI_API_KEY=my-api-key`.
- Copy `my-project` and rename with your project name: `cp -r my-project my-new-project`.
- Specify your new project folder as bind-mount source via env var: `export MOUNT_SOURCE=./my-new-project`.
  - Alternatively, simply include `-e MOUNT_SOURCE=./my-new-project` after `docker compose run`, below.
- Run `docker compose run --rm poc-autogen`.
- Optionally, edit `main.py` therein to describe the task that autogen needs to work on.
- Run `python main.py` to have autogen complete the specified task.
- Optionally, run `aider --model gpt-4-1106-preview main.py` (or any other file) to dev with aider.

### Scratch pad, refreshers

- `docker compose run --rm -e MOUNT_SOURCE=./my-project autogen-aider-docker`
- `docker build -t autogen-aider-docker .` or `docker build -t autogen-aider-docker:1.0.0 .`
- `docker compose run autogen-aider-docker`
- `docker run -it --rm --mount type=bind,source=.,target=/app autogen-aider-docker /bin/bash`
- `docker attach <container-id>`
- `docker exec -it <container-id> /bin/bash`
- ctrl+p, ctrl+q
- `exit` or ctrl+d
