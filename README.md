# प्राचीन कश्मीर · Prācīna Kashmira

Ancient Kashmiri Knowledge Portal — Streamlit Application

## Setup & Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Files
- `app.py` — Main Streamlit application
- `astro_engine.py` — Vedic astrology computation engine (panchang, marriage matching, mangalik)
- `kashmir_data.py` — Kashmiri cultural, geographic, and astrological data

## Tab 1: Ritual & Panchang
- Live Vedic Panchang: Tithi, Vara, Nakshatra, Yoga, Karana
- Location-aware (state + district → lat/lon auto-resolved)
- Muhurats: Brahma Muhurta, Abhijit, Rahu Kaal, Gulika, Yamaganda
- All planetary positions (sidereal/Lahiri ayanamsa)
- Birthday Panchang for current & next year
- Kashmiri festival information
- AI-powered Pandit query (asks Claude via API)

## Tab 2: Marriage Matching
- 36 Gunas (Kundali Milan) — all 8 kootas calculated from nakshatra
- Nakshatra auto-detected from date of birth and location
- Mangalik Dosha from D1 (Lagna), Moon chart, and D9 (Navamsha)
- Gotra compatibility check
- AI marriage compatibility report

## Notes
- Uses Swiss Ephemeris (swisseph) with Lahiri ayanamsa for accuracy
- All calculations are sidereal (Nirayana system)
- Time zone defaults to IST (UTC+5:30)
- AI features require network access to api.anthropic.com
