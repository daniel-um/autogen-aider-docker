# poc-autogen

### How to use

- Requires Python and Docker to be installed.
- If using as-is, you will also need an OpenAI API key (but autogen can be configured to use other models).
- Create `.env` and add OpenAI API key: `OPENAI_API_KEY=my-api-key`.
- Copy `my-project` and rename with your project name.
- Specify your new project folder as bind-mount source via env var: `export MOUNT_SOURCE=./my-new-project`.
  - Alternatively, simply include `-e MOUNT_SOURCE=./my-new-project` after `docker compose run`, below.
- Run `docker compose run --rm poc-autogen`.
- Edit `main.py` therein to describe the task that autogen needs to work on.
- Optionally, execute `aider main.py` (or on any other file) to pair program with aider.

### Scratch pad, refreshers

- `docker compose run --rm -e MOUNT_SOURCE=./my-project poc-autogen`
- `docker build -t poc-autogen .` or `docker build -t poc-autogen:1.0.0 .`
- `docker compose run poc-autogen`
- `docker run -it --rm --mount type=bind,source=.,target=/app poc-autogen /bin/bash`
- `docker attach <container-id>`
- `docker exec -it <container-id> /bin/bash`
- ctrl+p, ctrl+q
- `exit` or ctrl+d
