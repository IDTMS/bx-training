# Session 04 – Agents Basics

## Objective
Understand agents as long-running local processes by running a watcher that moves jobs from `jobs/inbox` to `jobs/outbox`.

## Why This Matters
- Agents underpin everything else we build: they sit idle until work arrives.
- File-based job queues keep workflows observable and debuggable locally.
- Watching folders mirrors real runtime behavior without cloud services.

## Prereqs
- Sessions 01–03 complete.
- `.venv` active.
- `jobs/inbox` and `jobs/outbox` directories exist (created automatically by the agent).

## Concepts
- Long-running Python loop with polling.
- File-based message passing.
- Graceful shutdown (CTRL+C).

## Steps
1. **Review the agent code**
   ```bash
   sed -n '1,120p' projects/agent_basic/agent.py
   ```
2. **Start the agent**
   ```bash
   python projects/agent_basic/agent.py
   ```
   Leave it running in one terminal.
3. **Submit a job from another terminal**
   ```bash
   echo '{"job_id":"demo","payload":"agent basics"}' > jobs/inbox/demo.json
   ```
4. **Observe output**
   ```bash
   ls jobs/outbox
   cat jobs/outbox/demo.result.json
   ```
5. **Stop the agent**
   - Press `CTRL+C` in the agent terminal.

## Deliverables
- `projects/agent_basic/agent.py` in repo.
- `projects/agent_basic/README.md` describing how to run the agent.
- `jobs/outbox/<job>.result.json` artifact generated locally.

## Done When
- [ ] Agent logs show files being processed.
- [ ] Input files disappear from `jobs/inbox` after processing.
- [ ] Result files appear in `jobs/outbox` with JSON payloads.

## Troubleshooting
- **Agent exits immediately:** confirm `.venv` is active and Python can find dependencies.
- **Unicode decode errors:** ensure job files are UTF-8 encoded (`iconv -f UTF-8 -t UTF-8`).
- **No output generated:** verify file permissions on `jobs/` and that filenames end in `.json`.
