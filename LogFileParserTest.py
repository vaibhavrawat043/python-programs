import re

log_pattern = re.compile(r"([0-9\-]*)T([0-9\-:.+]*)\s*\[([^]]*)\](.*)")

with open(name, "r") as f:
  for line in f:
      match = log_pattern.match(line)
      if not match:
        continue
      grps = match.groups()
      print("Log line:")
      print(f"  date:{grps[0]},\n  time:{grps[1]},\n  type:{grps[2]},\n  text:{grps[3]}")


