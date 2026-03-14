## Commit

```bash
git add .
git commit -m "add initial sip call visualizer"
git push
```

---

# SIP Call Visualizer

SIP Call Visualizer is a simple tool that parses SIP traces and converts them into readable call flow sequences.

It is useful for VoIP engineers, telecom developers, and support teams who need to understand SIP signaling faster.

The tool can help visualize common SIP call flows such as:

- INVITE
- 100 Trying
- 180 Ringing
- 200 OK
- ACK
- BYE

It can also generate Mermaid sequence diagrams for documentation and debugging.

---

# Features

- parse simple SIP traces
- extract sender and receiver flow
- generate readable call sequence
- generate Mermaid sequence diagram
- useful for SIP troubleshooting and documentation

---

# Example Input

```text
Alice -> Proxy: INVITE
Proxy -> Bob: INVITE
Bob -> Proxy: 100 Trying
Proxy -> Alice: 100 Trying
Bob -> Proxy: 180 Ringing
Proxy -> Alice: 180 Ringing
Bob -> Proxy: 200 OK
Proxy -> Alice: 200 OK
Alice -> Proxy: ACK
Proxy -> Bob: ACK
Bob -> Proxy: BYE
Proxy -> Alice: BYE
Alice -> Proxy: 200 OK
Proxy -> Bob: 200 OK
```

---

# Example Output

Parsed Call Flow

```text
Alice -> Proxy : INVITE.
Proxy -> Bob : INVITE.
Bob -> Proxy : 100 Trying.
Proxy -> Alice : 100 Trying
Bob -> Proxy : 180 Ringing
Proxy -> Alice : 180 Ringing
Bob -> Proxy : 200 OK
Proxy -> Alice : 200 OK
Alice -> Proxy : ACK
Proxy -> Bob : ACK
Bob -> Proxy : BYE
Proxy -> Alice : BYE
Alice -> Proxy : 200 OK
Proxy -> Bob : 200 OK
```

---

# Mermaid Diagram

```text
sequenceDiagram
    participant Alice
    participant Proxy
    participant Bob

    Alice->>Proxy: INVITE
    Proxy->>Bob: INVITE
    Bob->>Proxy: 100 Trying
    Proxy->>Alice: 100 Trying
    Bob->>Proxy: 180 Ringing
    Proxy->>Alice: 180 Ringing
    Bob->>Proxy: 200 OK
    Proxy->>Alice: 200 OK
    Alice->>Proxy: ACK
    Proxy->>Bob: ACK
    Bob->>Proxy: BYE
    Proxy->>Alice: BYE
    Alice->>Proxy: 200 OK
    Proxy->>Bob: 200 OK
```
---

# Project Structure

```text
visualizer/
main parser and sample data

docs/
architecture notes

scripts/
helper script to run parser
```

---

# Run

```bash
python visualizer/sip_visualizer.py
```

---

# Use Cases

- SIP troubleshooting
- VoIP support analysis
- call flow documentation
- debugging SIP interactions
- telecom training

---

# Roadmap

- support raw SIP log parsing
- export PNG or SVG diagrams
- web UI
- ladder diagram output
- Wireshark text export support

# License

MIT
