# Transit Crime Risk Streamlit App

## Overview
Interactive Streamlit app to link TPS Major Crime Indicators to TTC stops, map crimes, compute stop risk scores, compare event vs normal days, and explore hourly patterns per stop.

## Project structure
```
RBAC_TPS/
├─ app.py                 # Entrypoint (bootstraps deps, runs app_streamlit)
├─ app_streamlit.py       # Streamlit UI
├─ crime_around_stops.py  # Data loading, linking, scoring, mapping helpers
├─ requirements.txt       # Python dependencies
├─ data/
│  ├─ Complete GTFS/      # GTFS files (stops.txt, routes.txt, calendar*.txt, etc.)
│  ├─ Festivals and events json feed.json
│  ├─ Major_Crime_Indicators.csv
│  └─ processed/stop_times_with_stops.csv.gz (optional)
└─ venv/                  # (optional) local virtualenv, not needed in prod
```

## Run locally
```bash
cd RBAC_TPS
python -m venv venv && venv/Scripts/activate       # optional
pip install -r requirements.txt
streamlit run app.py
```

## Deploy (Streamlit Community Cloud)
1. Push this repo to GitHub (keep large files out or use Git LFS).
2. In Streamlit Cloud, create an app pointing to `app.py`.
3. Dependencies come from `requirements.txt`.
4. Add any secrets (e.g., data URLs) in the Cloud “Secrets” panel.

## Data notes
- Default paths expect GTFS and crime data under `data/` (see structure above).
- Large files (e.g., `stop_times.txt` >100 MB) should be kept out of git or tracked with Git LFS; otherwise host externally and point the app to the URL.
