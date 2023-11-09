# autogen-aider-docker

## How to use

- Requires Python and Docker to be installed.
- If using as-is, you will also need an OpenAI API key (but autogen can be configured to use other models).
- Optionally, build the docker image yourself:
  - Run `docker build -t autogen-aider .`.
  - Replace all instances of `danum/autogen-aider` in `docker-compose.yml` with `autogen-aider`.
- Create `.env` and add OpenAI API key: `OPENAI_API_KEY=my-api-key`.
- Copy `my-project` and rename with your project name: `cp -r my-project my-new-project`.
- Specify your new project folder as bind-mount source via env var: `export MOUNT_SOURCE=./my-new-project`.
  - Alternatively, simply include `-e MOUNT_SOURCE=./my-new-project` after `docker compose run`, below.
- Optionally, edit 'main.py' in `my-new-project` to describe the task that you want autogen to work on.
- Run `docker compose run autogen-aider`.
  - Alternatively, run `docker compose run --rm autogen-aider /bin/bash` to prevent auto-run of autogen.
  - Alternatively, run `docker compose run --rm autogen-aider` if you want to dispose the container after autogen completes.
- The code generated by autogen can be found in `generated-content`, in `my-new-project`.
- Optionally, if you haven't exited the docker container yet, run `aider --model gpt-4-1106-preview main.py` (or any other file) to continue coding, with aider as your pair programmer.
