#!/usr/bin/env python3
"""PreToolUse guard for CMS write tools (content-team plugin).

Allows ONLY draft saves of stories (create/update) without any publish flag.
Blocks everything else: publish, unpublish, delete, components, datasources,
folders, space settings, assets. Fails closed: any parsing problem blocks.
Exit code 2 = block (stderr is shown to Claude). Exit 0 = allow.
"""
import json, re, sys

ALLOWED_OPERATIONS = {"createStory", "updateStory"}
# Options that publish, schedule, overwrite locks, auto-translate or target per-language publishing
PUBLISH_KEYS = re.compile(r"^(publish|release_id|publish_at|unpublish|force_update|ai_translate_language|lang)$", re.I)

def block(msg):
    sys.stderr.write("content-team safety check blocked this CMS call: " + msg +
                     " Only draft saves of stories (createStory/updateStory, no publish) are allowed. "
                     "Publishing, deleting and component or settings changes must be done by a human in the CMS.\n")
    sys.exit(2)

def find_publish(obj):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if PUBLISH_KEYS.match(str(k)) and v not in (None, False, 0, "0", "", "false"):
                return k
            hit = find_publish(v) if k != "content" else None  # story content fields are not flags
            if hit:
                return hit
    elif isinstance(obj, list):
        for v in obj:
            hit = find_publish(v)
            if hit:
                return hit
    return None

try:
    data = json.load(sys.stdin)
except Exception:
    block("could not read the tool call.")

tool = str(data.get("tool_name", ""))
inp = data.get("tool_input") or {}

if tool.endswith("execute_destructive"):
    block("destructive operations are never allowed.")
if "upload_asset" in tool:
    block("asset uploads are not allowed for agents.")
if tool.endswith("execute_mutating"):
    op = str(inp.get("operation", ""))
    if op not in ALLOWED_OPERATIONS:
        block("operation '%s' is not a draft story save." % op)
    key = find_publish(inp.get("parameters") or {})
    if key:
        block("the call sets '%s', which could publish, schedule, overwrite a locked story or auto-translate." % key)
    sys.exit(0)

sys.exit(0)
