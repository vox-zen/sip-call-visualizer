# SIP Call Visualizer Architecture

The visualizer reads a simplified SIP trace format and transforms it into a readable sequence.

## Flow

Input Trace File
↓
Parser
↓
Structured SIP Events
↓
Text Call Flow Output
↓
Mermaid Sequence Diagram Output

## Current Input Format

The current implementation supports simple trace lines like:

Alice -> Proxy: INVITE

## Future Improvements

- raw SIP packet parsing
- Wireshark export support
- HTML rendering
- image export
- web interface
