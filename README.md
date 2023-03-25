# EskomDeviceToggle

Turns a TCL TV back on (via a Tuya IR blaster) after load shedding ends, using the EskomSePush API.

## Setup

1. Install dependencies:

   ```
   pip install requests tinytuya python-dotenv
   ```

2. Copy `.env.example` to `.env` and fill in your values:

   ```
   cp .env.example .env
   ```

3. Run `python -m tinytuya wizard` to create `tinytuya.json` with your Tuya Cloud API credentials.

`.env` and `tinytuya.json` are listed in `.gitignore` and must never be committed.

## Usage

- `get_sepush_sch.py` checks the current load-shedding stage and, if it has changed, saves your area's schedule to `json_data.json`.
- `process_sepush.py` reads that schedule and calls `tv_toggle()` once a load-shedding slot has ended.

Both scripts expect `Stage.txt`, `Time.txt` and `Date.txt` to exist in the working directory.
