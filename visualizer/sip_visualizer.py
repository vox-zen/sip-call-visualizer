import re
from pathlib import Path


TRACE_FILE = Path("visualizer/sample_trace.txt")
OUTPUT_FILE = Path("visualizer/output_example.md")


def parse_trace_line(line: str):
    pattern = r"^\s*(.+?)\s*->\s*(.+?)\s*:\s*(.+?)\s*$"
    match = re.match(pattern, line)
    if not match:
        return None
    sender, receiver, message = match.groups()
    return sender.strip(), receiver.strip(), message.strip()


def load_trace(file_path: Path):
    entries = []
    for raw_line in file_path.read_text(encoding="utf-8").splitlines():
        if not raw_line.strip():
            continue
        parsed = parse_trace_line(raw_line)
        if parsed:
            entries.append(parsed)
    return entries


def collect_participants(entries):
    participants = []
    seen = set()

    for sender, receiver, _ in entries:
        if sender not in seen:
            seen.add(sender)
            participants.append(sender)
        if receiver not in seen:
            seen.add(receiver)
            participants.append(receiver)

    return participants


def generate_plain_flow(entries):
    lines = ["## Parsed Call Flow", "", "```text"]
    for sender, receiver, message in entries:
        lines.append(f"{sender} -> {receiver} : {message}")
    lines.append("```")
    return "\n".join(lines)


def generate_mermaid(entries, participants):
    lines = ["## Mermaid Diagram", "", "```mermaid", "sequenceDiagram"]

    for participant in participants:
        lines.append(f"    participant {participant}")

    lines.append("")

    for sender, receiver, message in entries:
        lines.append(f"    {sender}->>{receiver}: {message}")

    lines.append("```")
    return "\n".join(lines)


def main():
    entries = load_trace(TRACE_FILE)

    if not entries:
        print("No valid SIP trace entries found.")
        return

    participants = collect_participants(entries)

    print("Parsed SIP Call Flow:\n")
    for sender, receiver, message in entries:
        print(f"{sender} -> {receiver} : {message}")

    plain_flow = generate_plain_flow(entries)
    mermaid = generate_mermaid(entries, participants)

    output = "# Output Example\n\n" + plain_flow + "\n\n" + mermaid + "\n"
    OUTPUT_FILE.write_text(output, encoding="utf-8")

    print("\nMermaid output written to visualizer/output_example.md")


if __name__ == "__main__":
    main()
