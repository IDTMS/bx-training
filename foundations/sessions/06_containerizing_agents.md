# Session 06 – Containerizing Agents

## Objective
Package the basic agent into a Docker container that mounts `jobs/` as volumes for reproducible execution.

## Why This Matters
- Containers keep runtime dependencies pinned.
- Mounting shared folders lets host tools inspect artifacts mid-run.
- Container discipline now sets the stage for GPU-enabled workloads later.

## Prereqs
- Sessions 01–05 complete.
- Docker Desktop (macOS) or Docker Engine (Linux/WSL) installed.
- `projects/agent_basic/agent.py` present.

## Concepts
- Docker build contexts.
- Volume mounts for shared job folders.
- Running long-lived containers interactively.

## Steps
1. **Inspect the Dockerfile**
   ```bash
   cat projects/agent_basic/Dockerfile
   ```
2. **Build the image**
   ```bash
   cd projects/agent_basic
   docker build -t agent_basic:latest .
   cd -
   ```
3. **Prepare shared folders**
   ```bash
   mkdir -p jobs/inbox jobs/outbox
   ```
4. **Run the container**
   ```bash
   docker run --rm -it \
     -v "$(pwd)/jobs/inbox:/jobs/inbox" \
     -v "$(pwd)/jobs/outbox:/jobs/outbox" \
     agent_basic:latest
   ```
   On Windows (WSL recommended): run from WSL shell to avoid path conversion problems.
5. **Submit a job**
   ```bash
   echo '{"job_id":"docker-demo","payload":"container"}' > jobs/inbox/docker-demo.json
   ```
6. **Observe artifact**
   ```bash
   cat jobs/outbox/docker-demo.result.json
   ```
7. **Stop the container**
   - Press `CTRL+C` in the Docker terminal.

## Deliverables
- `projects/agent_basic/Dockerfile` stored in repo.
- `projects/agent_basic/README.md` updated with Docker run instructions.
- Verified container run that writes to `jobs/outbox/`.

## Done When
- [ ] Docker image builds successfully.
- [ ] Container run processes sample jobs using mounted volumes.
- [ ] Agent stop leaves log/output files accessible on the host.

## Troubleshooting
- **Docker cannot access host path:** ensure the repo directory is shared with Docker Desktop (Settings → Resources → File Sharing on macOS).
- **`Permission denied` writing jobs:** adjust mount options or run `chmod -R 775 jobs` before starting container.
- **Clock skew errors inside container:** rely on host `date`; containers inherit host time when started.
