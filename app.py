"""
Prācīna Kashmīra · प्राचीन कश्मीर
Complete Vedic Jyotisha & Panchang Portal
"""

import streamlit as st
from datetime import date, datetime, timedelta
import sys, os, requests

sys.path.insert(0, os.path.dirname(__file__))

# ─────────────────────────────────────────────────────────────────────────────
# PAGE CONFIG  (must be first Streamlit call)
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Ancient Kashmiri · प्राचीन कश्मीर",
    # page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────────────────────────────────────
# CSS
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600&family=Cinzel+Decorative:wght@400;700&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,400&family=Noto+Serif+Devanagari:wght@300;400;500&display=swap');

/* ── ROOT PALETTE ── */
:root {
  --saffron:      #D4722A;
  --saffron-lt:   #E8956A;
  --saffron-pale: #FDF0E5;
  --crimson:      #8B1C30;
  --gold:         #B8862A;
  --gold-lt:      #DEB85A;
  --gold-pale:    #FBF5E6;
  --walnut:       #3A2010;
  --walnut-mid:   #6B3A1F;
  --cream:        #FDF8F0;
  --cream2:       #FAF3E8;
  --ink:          #1E0F06;
  --muted:        #7A5F4A;
  --border:       rgba(184,134,42,0.30);
  --teal:         #2A7A6A;
  --lotus:        #C45A7A;
  --shadow:       rgba(58,32,16,0.10);
  --shadow-d:     rgba(58,32,16,0.22);
}

/* ── GLOBAL ── */
html, body, [data-testid="stAppViewContainer"], .stApp {
  background: var(--cream) !important;
  font-family: 'Cormorant Garamond', serif !important;
  color: var(--ink) !important;
}

[data-testid="stAppViewContainer"]::before {
  content: '';
  position: fixed; inset: 0; pointer-events: none; z-index: 0;
  background:
    radial-gradient(ellipse 700px 500px at 5% 15%, rgba(212,114,42,.05) 0%, transparent 70%),
    radial-gradient(ellipse 600px 600px at 95% 85%, rgba(139,28,48,.04) 0%, transparent 70%),
    url("data:image/svg+xml,%3Csvg width='60' height='60' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M30 2 L33 27 L58 30 L33 33 L30 58 L27 33 L2 30 L27 27Z' fill='%23B8862A' fill-opacity='.03'/%3E%3C/svg%3E");
}

[data-testid="stHeader"] { display: none !important; }
[data-testid="stSidebar"] { display: none !important; }
footer { display: none !important; }
#MainMenu { display: none !important; }

/* ── MAIN PADDING ── */
[data-testid="stMainBlockContainer"] {
  padding: 0 !important;
  max-width: 100% !important;
}
[data-testid="block-container"] {
  padding: 0 !important;
  max-width: 100% !important;
}
.main .block-container {
  padding: 0 2.5rem 4rem !important;
  max-width: 1400px !important;
}

/* ── HEADER ── */
.site-header {
  background: linear-gradient(135deg, #3A2010 0%, #4E2210 45%, #8B1C30 100%);
  padding: 16px 40px 14px;
  position: relative;
  overflow: hidden;
  margin-bottom: 0;
}
.site-header::before {
  content: '';
  position: absolute; inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg width='80' height='80' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M40 5C40 5 55 20 55 40 55 60 40 75 40 75 25 60 25 40 25 20 40 5Z' fill='%23DEB85A' fill-opacity='.05'/%3E%3Cpath d='M5 40C5 40 20 25 40 25 60 25 75 40 75 40 60 55 40 55 20 55 5 40Z' fill='%23DEB85A' fill-opacity='.05'/%3E%3C/svg%3E");
  pointer-events: none;
}
.hdr-inner {
  display: flex; align-items: center; justify-content: space-between;
  position: relative; z-index: 1;
}
.hdr-title {
  font-family: 'Cinzel', serif;
  font-size: 26px; font-weight: 500; color: #FDF8F0; letter-spacing: 3px; line-height: 1.1;
}
.hdr-title span { color: #DEB85A; }
.hdr-title-hi {
  font-family: 'Noto Serif Devanagari', serif;
  font-size: 17px; color: rgba(222,184,90,.8); letter-spacing: 1px; margin-top: 2px;
}
.hdr-desc {
  font-size: 10px; color: rgba(253,248,240,.4);
  letter-spacing: 1px; margin-top: 5px; line-height: 1.7; max-width: 540px;
}
.hdr-tagline {
  font-style: italic; font-size: 10px;
  color: rgba(253,248,240,.3); letter-spacing: 1.5px; margin-top: 3px;
}
.hdr-right { text-align: right; }
.hdr-samvat {
  font-family: 'Cinzel', serif;
  font-size: 9px; letter-spacing: 2px; color: rgba(222,184,90,.5); margin-bottom: 1px;
}
.hdr-samvat-num {
  font-family: 'Cinzel', serif;
  font-size: 20px; color: rgba(222,184,90,.85); line-height: 1.1;
}
.hdr-date { font-size: 11px; color: rgba(253,248,240,.45); margin-top: 3px; }

/* ── TABS ── */
.stTabs [data-baseweb="tab-list"] {
  background: #3A2010 !important;
  border-bottom: 2px solid #B8862A !important;
  gap: 0 !important;
  padding: 0 1.5rem !important;
}
.stTabs [data-baseweb="tab"] {
  font-family: 'Cinzel', serif !important;
  font-size: 10.5px !important;
  letter-spacing: 1.2px !important;
  color: rgba(253,248,240,.55) !important;
  opacity: 1 !important;
  padding: 14px 20px !important;
  border-bottom: 3px solid transparent !important;
  background: transparent !important;
}
.stTabs [aria-selected="true"] {
  color: #DEB85A !important;
  border-bottom-color: #DEB85A !important;
  background: rgba(222,184,90,.06) !important;
}
.stTabs [data-baseweb="tab-panel"] {
  padding: 1.5rem 1.5rem 3rem !important;
  background: transparent !important;
}
/* Sujhav tab (8th) — distinct border box */
.stTabs [data-baseweb="tab-list"] [data-baseweb="tab"]:nth-child(8) {
  border: 1px solid rgba(184,134,42,.35) !important;
  border-bottom: 3px solid transparent !important;
  border-radius: 6px 6px 0 0 !important;
  margin: 4px 4px 0 !important;
  color: rgba(222,184,90,.75) !important;
  background: rgba(184,134,42,.06) !important;
}
.stTabs [data-baseweb="tab-list"] [data-baseweb="tab"]:nth-child(8)[aria-selected="true"] {
  border-color: #DEB85A !important;
  border-bottom-color: #DEB85A !important;
  color: #DEB85A !important;
  background: rgba(222,184,90,.12) !important;
}

/* ── SECTION HEADERS ── */
.sec-head {
  font-family: 'Cinzel', serif;
  font-size: 20px; font-weight: 500; color: var(--walnut);
  letter-spacing: 2px; margin-bottom: 4px;
  display: flex; align-items: center; gap: 10px;
}
.sec-sub {
  font-style: italic; font-size: 14px; color: var(--muted);
  margin-bottom: 20px; line-height: 1.6;
  border-bottom: 1px solid var(--border); padding-bottom: 14px;
}
.sec-sub .deva {
  font-family: 'Noto Serif Devanagari', serif; display: block; margin-top: 2px;
}
.subsec {
  font-family: 'Cinzel', serif;
  font-size: 11px; letter-spacing: 2px; color: var(--walnut-mid);
  margin: 20px 0 12px; padding-bottom: 8px;
  border-bottom: 1px solid var(--border);
  display: flex; align-items: center; gap: 8px;
}
.subsec .deva { font-family: 'Noto Serif Devanagari', serif; font-size: 12px; color: var(--muted); opacity: .75; }

/* ── PANCH CARDS ── */
.panch-cell {
  background: linear-gradient(135deg, var(--saffron-pale), var(--gold-pale));
  border: 1px solid rgba(212,114,42,.2); border-radius: 10px;
  padding: 14px 16px; text-align: center; position: relative; overflow: hidden;
}
.panch-cell::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0;
  height: 2px; background: linear-gradient(90deg, transparent, var(--saffron), transparent);
}
.pc-lbl {
  font-family: 'Cinzel', serif;
  font-size: 8px; letter-spacing: 2px; color: var(--saffron);
  display: block; margin-bottom: 2px; text-transform: uppercase;
}
.pc-lbl-deva {
  font-family: 'Noto Serif Devanagari', serif;
  font-size: 10px; color: var(--muted); display: block; margin-bottom: 5px; opacity: .8;
}
.pc-val {
  font-size: 15px; font-weight: 500; color: var(--walnut); line-height: 1.3;
}
.pc-val-big {
  font-family: 'Cinzel', serif; font-size: 17px; color: var(--walnut);
}
.pc-sub { font-size: 10px; color: var(--muted); margin-top: 2px; }

/* ── MUHURTA BLOCKS ── */
.muh-block {
  border-radius: 8px; padding: 11px 15px;
  border-left: 3px solid var(--muted); margin-bottom: 8px;
  background: rgba(253,248,240,.5);
}
.muh-block.good  { border-left-color: #4A9A50; background: rgba(74,154,80,.07); }
.muh-block.bad   { border-left-color: #C03030; background: rgba(192,48,48,.06); }
.muh-block.spec  { border-left-color: var(--gold); background: rgba(184,134,42,.08); }
.muh-lbl {
  font-family: 'Cinzel', serif;
  font-size: 9px; letter-spacing: 2px; color: var(--muted);
  margin-bottom: 2px; text-transform: uppercase;
}
.muh-deva { font-family: 'Noto Serif Devanagari', serif; font-size: 11px; color: var(--walnut-mid); opacity: .75; }
.muh-time { font-size: 16px; color: var(--walnut); font-weight: 500; }
.muh-note { font-size: 11px; color: var(--muted); margin-top: 2px; }

/* ── PLANET TABLE ── */
.planet-tbl { width: 100%; border-collapse: collapse; font-size: 14px; }
.planet-tbl th {
  font-family: 'Cinzel', serif; font-size: 9px; letter-spacing: 1.5px;
  color: var(--muted); text-transform: uppercase;
  padding: 10px 14px; border-bottom: 1px solid var(--border); text-align: left;
}
.planet-tbl td {
  padding: 9px 14px; border-bottom: 1px solid rgba(212,184,150,.35);
  color: var(--ink); font-size: 14px;
}
.planet-tbl tr:hover td { background: var(--cream2); }
.p-badge {
  display: inline-block; padding: 2px 9px; border-radius: 12px;
  font-family: 'Cinzel', serif; font-size: 9px; letter-spacing: 1px;
}
.p-sun  { background: rgba(212,114,42,.15); color: var(--saffron); }
.p-moon { background: rgba(184,134,42,.15); color: var(--gold); }
.p-mars { background: rgba(192,48,48,.12);  color: #b03030; }
.p-merc { background: rgba(42,122,106,.12); color: var(--teal); }
.p-jup  { background: rgba(139,28,48,.12);  color: var(--crimson); }
.p-ven  { background: rgba(196,90,122,.12); color: var(--lotus); }
.p-sat  { background: rgba(58,32,16,.12);   color: var(--walnut-mid); }
.p-rahu { background: rgba(30,15,6,.08);    color: #555; }
.p-ketu { background: rgba(100,60,20,.1);   color: #885522; }

/* ── INFO CARDS ── */
.info-card {
  background: white; border: 1px solid var(--border); border-radius: 14px;
  padding: 20px 22px; box-shadow: 0 2px 10px var(--shadow);
  transition: transform .2s, box-shadow .2s; height: 100%;
}
.info-card:hover { transform: translateY(-3px); box-shadow: 0 6px 22px var(--shadow-d); }
.ic-icon { font-size: 24px; margin-bottom: 8px; }
.ic-title {
  font-family: 'Cinzel', serif; font-size: 10px; letter-spacing: 1.5px;
  color: var(--walnut-mid); margin-bottom: 6px;
}
.ic-body { font-size: 13.5px; line-height: 1.7; color: var(--muted); }
.ic-accent { display: inline-block; margin-top: 8px; font-size: 12px; color: var(--saffron); font-style: italic; }

/* ── BIRTHDAY CARDS ── */
.bday-card {
  background: linear-gradient(135deg, var(--saffron-pale), var(--gold-pale));
  border: 1px solid rgba(212,114,42,.3); border-radius: 14px;
  padding: 20px 24px; margin-bottom: 14px; position: relative; overflow: hidden;
}
.bday-card::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0;
  height: 3px; background: linear-gradient(90deg, var(--saffron), var(--gold), var(--saffron));
}
.bday-yr { font-family: 'Cinzel', serif; font-size: 10px; letter-spacing: 2px; color: var(--muted); margin-bottom: 4px; }
.bday-date { font-size: 20px; font-weight: 500; color: var(--walnut); margin-bottom: 3px; }
.bday-deva { font-family: 'Noto Serif Devanagari', serif; font-size: 13px; color: var(--muted); margin-bottom: 10px; }
.bday-detail { font-size: 13px; color: var(--muted); line-height: 1.9; }
.bday-hl { color: var(--walnut); font-weight: 500; }

/* ── GUNA ── */
.guna-row {
  display: flex; align-items: center; gap: 12px; padding: 9px 14px;
  border-radius: 8px; margin-bottom: 6px;
  background: var(--cream2); border: 1px solid rgba(212,184,150,.3);
}
.guna-name {
  font-family: 'Cinzel', serif; font-size: 10.5px; letter-spacing: 1px;
  color: var(--walnut-mid); min-width: 120px;
}
.guna-pts { font-size: 15px; font-weight: 600; min-width: 55px; }
.guna-status { font-size: 13px; color: var(--muted); flex: 1; }

/* ── SCORE CIRCLE ── */
.score-wrap { text-align: center; padding: 1rem; }
.score-circle {
  width: 130px; height: 130px; border-radius: 50%;
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  margin: 0 auto 12px; border: 4px solid;
}
.score-num { font-family: 'Cinzel Decorative', serif; font-size: 2.4rem; line-height: 1; }
.score-den { font-size: .85rem; opacity: .6; }
.score-rec { font-family: 'Cinzel', serif; font-size: 10.5px; letter-spacing: 1px; margin-top: 8px; }
.score-bar {
  width: 100%; height: 10px; border-radius: 5px; margin: 12px 0;
  background: linear-gradient(to right, #C03030, #D4882A, #4A9A50);
  position: relative;
}

/* ── LINEAGE ── */
.lin-item {
  display: flex; gap: 14px; padding: 12px 0;
  border-bottom: 1px solid rgba(212,184,150,.35);
}
.lin-item:last-child { border-bottom: none; }
.lin-icon { font-size: 20px; width: 28px; flex-shrink: 0; }
.lin-lbl {
  font-family: 'Cinzel', serif; font-size: 9px; letter-spacing: 1.5px;
  color: var(--saffron); text-transform: uppercase; margin-bottom: 3px;
}
.lin-val { font-size: 15px; color: var(--walnut); }
.lin-desc { font-size: 12px; color: var(--muted); font-style: italic; margin-top: 2px; }

/* ── AI BOX ── */
.ai-box {
  background: linear-gradient(135deg, #3A2010 0%, #4E2210 100%);
  border-radius: 14px; padding: 22px 26px; margin-bottom: 20px;
  box-shadow: 0 6px 28px var(--shadow-d), inset 0 1px 0 rgba(222,184,90,.16);
  position: relative;
}
.ai-box::before {
  content: ' AI · अर्क';
  position: absolute; top: 12px; right: 16px;
  font-family: 'Cinzel', serif; font-size: 9px; letter-spacing: 3px; color: rgba(222,184,90,.4);
}
.ai-lbl {
  font-family: 'Cinzel', serif; font-size: 9px; letter-spacing: 3px;
  color: #DEB85A; margin-bottom: 10px; opacity: .8;
}
.ai-resp {
  margin-top: 16px;
  background: rgba(253,248,240,.07); border: 1px solid rgba(222,184,90,.2);
  border-radius: 10px; padding: 16px 20px; color: #FDF8F0;
  font-size: 15px; line-height: 2;
}

/* ── BADGES ── */
.badge {
  display: inline-flex; align-items: center; gap: 5px;
  padding: 4px 12px; border-radius: 20px;
  font-family: 'Cinzel', serif; font-size: 9px; letter-spacing: 1.5px;
}
.badge-good { background: rgba(74,154,80,.12); color: #3A7A40; border: 1px solid rgba(74,154,80,.25); }
.badge-avg  { background: rgba(212,114,42,.12); color: var(--saffron); border: 1px solid rgba(212,114,42,.25); }
.badge-bad  { background: rgba(192,48,48,.10); color: #b03030; border: 1px solid rgba(192,48,48,.20); }
.badge-man-yes  { background:rgba(229,57,53,.18); border:1px solid #e53935; color:#ef9a9a; }
.badge-man-mild { background:rgba(255,152,0,.18); border:1px solid #FF9800; color:#ffcc80; }
.badge-man-no   { background:rgba(76,175,80,.18); border:1px solid #4CAF50; color:#a5d6a7; }

/* ── WIDGET OVERRIDES ── */
.stSelectbox label, .stDateInput label, .stTimeInput label,
.stNumberInput label, .stTextInput label, .stTextArea label {
  font-family: 'Cinzel', serif !important;
  font-size: 9.5px !important; letter-spacing: 1.5px !important;
  color: var(--muted) !important; text-transform: uppercase !important;
}
.stSelectbox [data-baseweb="select"] > div,
.stTextInput input, .stNumberInput input, .stTimeInput input {
  background: var(--cream) !important;
  border: 1px solid var(--border) !important;
  color: var(--ink) !important;
  font-family: 'Cormorant Garamond', serif !important;
  font-size: 15px !important;
}
.stDateInput input {
  background: var(--cream) !important;
  border: 1px solid var(--border) !important;
  color: var(--ink) !important;
}
.stTextArea textarea {
  background: var(--cream) !important;
  border: 1px solid var(--border) !important;
  color: var(--ink) !important;
  font-family: 'Cormorant Garamond', serif !important;
  font-size: 15px !important;
}
.stButton > button {
  font-family: 'Cinzel', serif !important;
  font-size: 10px !important; letter-spacing: 2px !important;
  background: linear-gradient(135deg, #3A2010, #8B1C30) !important;
  color: #FDF8F0 !important;
  border: 1px solid rgba(184,134,42,.4) !important;
  border-radius: 8px !important;
  padding: 0.55rem 1.6rem !important;
  transition: all .2s !important;
}
.stButton > button:hover {
  background: linear-gradient(135deg, #8B1C30, #D4722A) !important;
  border-color: #D4722A !important;
}
.stCheckbox label {
  font-family: 'Cormorant Garamond', serif !important;
  font-size: 14px !important; color: var(--ink) !important;
}
.stMetric { background: var(--cream2); border: 1px solid var(--border); border-radius: 8px; padding: .5rem !important; }
.stMetric label { font-family:'Cinzel',serif !important; font-size:9px !important; color:var(--muted) !important; letter-spacing:1.5px !important; }
.stMetric [data-testid="stMetricValue"] { font-size:1.1rem !important; color:var(--walnut) !important; }
.stExpander { border: 1px solid var(--border) !important; border-radius: 8px !important; background: white !important; }
.streamlit-expanderHeader {
  font-family:'Cinzel',serif !important; font-size:10px !important;
  color:var(--walnut-mid) !important; letter-spacing:1.5px !important;
}

/* ── DIVIDER ── */
.lotus-div {
  text-align: center; color: var(--saffron);
  opacity: .4; font-size: 1.1rem; margin: 18px 0; letter-spacing: .8rem;
}
.styled-div {
  display: flex; align-items: center; gap: 12px; margin: 20px 0;
  color: var(--muted);
}
.styled-div::before, .styled-div::after { content:''; flex:1; height:1px; background:var(--border); }
.styled-div span { font-family:'Cinzel',serif; font-size:9px; letter-spacing:3px; white-space:nowrap; }

/* ── FOOTER ── */
.site-footer {
  text-align: center; padding: 16px; margin-top: 24px;
  font-family: 'Cinzel', serif; font-size: 9px; letter-spacing: 3px;
  color: var(--muted); opacity: .5; border-top: 1px solid var(--border);
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# IMPORTS  (after page config)
# ─────────────────────────────────────────────────────────────────────────────
try:
    from astro_engine_fixed import (
        get_full_panchang, match_36_gunas, check_mangalik,
        get_nakshatra_from_dob, NAKSHATRA_NAMES, RASHI_NAMES,
        RASHI_HINDI, NAKSHATRA_HINDI,
    )
    from kashmir_data import (INDIA_STATES, GOTRAS, KUL_DEVIS, KUL_DEVTAS, BHAIRAVAS,
                               KP_DISTRICTS, KP_TOWNS, KP_VILLAGES, KP_SURNAMES,
                               ASHTA_BHAIRAVAS, LOCAL_BHAIRAVAS,
                               KUL_DEVI_BY_DISTRICT, KUL_DEVTA_BY_DISTRICT,
                               SURNAME_GOTRA_MAP)
    ASTRO_OK = True
except ImportError as _ie:
    ASTRO_OK = False
    _import_err = str(_ie)

# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────
def samvat_year(d: date) -> int:
    return d.year + 57 if d.month > 3 else d.year + 56

def saptarishi_samvat(d: date) -> int:
    """Saptarishi (Sapta Rishi / Laukika) Samvat = Gregorian year + 3076."""
    return d.year + 3076

# Streamlit-level cache so panchang for the same date+location is computed
# once per session (survives tab switches and widget interactions).
@st.cache_data(ttl=3600, show_spinner=False)
def _cached_panchang(d: date, lat: float, lon: float):
    return get_full_panchang(d, lat, lon)

@st.cache_data(ttl=3600, show_spinner=False)
def _cached_nakshatra(d: date, lat: float, lon: float, h: int, m: int):
    return get_nakshatra_from_dob(d, lat, lon, h, m)

@st.cache_data(ttl=3600, show_spinner=False)
def _cached_mangalik(d: date, lat: float, lon: float, h: int, m: int):
    return check_mangalik(d, lat, lon, h, m)

@st.cache_data(ttl=3600, show_spinner=False)
def _cached_gunas(b_nak: str, g_nak: str, b_gotra: str, g_gotra: str):
    return match_36_gunas(b_nak, g_nak, b_gotra, g_gotra)


def call_claude(system: str, user: str, max_tokens: int = 1000) -> str:
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        try:
            api_key = st.secrets.get("ANTHROPIC_API_KEY", "")
        except Exception:
            pass
    if not api_key:
        return "AI features require ANTHROPIC_API_KEY to be set in environment or Streamlit secrets."
    try:
        r = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "Content-Type": "application/json",
                "x-api-key": api_key,
                "anthropic-version": "2023-06-01",
            },
            json={
                "model": "claude-sonnet-4-20250514",
                "max_tokens": max_tokens,
                "system": system,
                "messages": [{"role": "user", "content": user}],
            },
            timeout=60,
        )
        data = r.json()
        return data["content"][0]["text"] if data.get("content") else "No response."
    except Exception as ex:
        return f"Error connecting to AI: {ex}"


def state_district_selects(prefix: str, default_state: str = "Jammu & Kashmir", default_dist: str = "Jammu"):
    """Render state + district selects; return (lat, lon, location_name)."""
    states = list(INDIA_STATES.keys())
    state = st.selectbox(
        "State · राज्य",
        states,
        index=states.index(default_state) if default_state in states else 0,
        key=f"{prefix}_state",
    )
    dists = list(INDIA_STATES[state].keys())
    dist = st.selectbox(
        "District · जिला",
        dists,
        index=dists.index(default_dist) if default_dist in dists else 0,
        key=f"{prefix}_dist",
    )
    coords = INDIA_STATES[state][dist]
    lat, lon = coords[0], coords[1]
    return lat, lon, f"{dist}, {state}"


def panch_cell(label: str, deva: str, value: str, sub: str = "") -> str:
    return f"""
<div class="panch-cell">
  <span class="pc-lbl">{label}</span>
  <span class="pc-lbl-deva">{deva}</span>
  <div class="pc-val">{value}</div>
  {f'<div class="pc-sub">{sub}</div>' if sub else ''}
</div>"""


def muh_block(cls: str, label: str, deva: str, time_str: str, note: str = "") -> str:
    return f"""
<div class="muh-block {cls}">
  <div class="muh-lbl">{label}</div>
  <div class="muh-deva">{deva}</div>
  <div class="muh-time">{time_str}</div>
  {f'<div class="muh-note">{note}</div>' if note else ''}
</div>"""


def planet_badge(name: str) -> str:
    mapping = {
        "Sun": "p-sun", "Moon": "p-moon", "Mars": "p-mars", "Mercury": "p-merc",
        "Jupiter": "p-jup", "Venus": "p-ven", "Saturn": "p-sat",
        "Rahu": "p-rahu", "Ketu": "p-ketu",
    }
    icons = {
        "Sun": "", "Moon": "", "Mars": "", "Mercury": "",
        "Jupiter": "", "Venus": "", "Saturn": "", "Rahu": "", "Ketu": "",
    }
    cls = mapping.get(name, "")
    icon = icons.get(name, "⭐")
    return f'<span class="p-badge {cls}">{icon} {name}</span>'


def guna_row_html(key: str, d: dict) -> str:
    pts, mx = d["points"], d.get("max", 8)
    ratio = pts / mx if mx else 0
    col = "#3A7A40" if ratio >= 0.75 else "var(--saffron)" if ratio >= 0.4 else "#b03030"
    extra = ""
    if "boy" in d and "girl" in d:
        extra = f" &nbsp;·&nbsp;  {d['boy']} /  {d['girl']}"
    display = key.replace("_", " ").title()
    return f"""
<div class="guna-row">
  <span class="guna-name">{display}</span>
  <span class="guna-pts" style="color:{col}">{pts}/{mx}</span>
  <span class="guna-status">{d.get('status','')}{extra}</span>
</div>"""


AMAVASYA_NAMES = [
    "Chaitra", "Vaishakha", "Jyeshtha", "Ashadha", "Shravana",
    "Bhadrapada", "Ashwina", "Kartika", "Margashirsha", "Pausha",
    "Magha", "Phalguna",
]

MASA_DEVA = {
    "Chaitra": "चैत्र", "Vaishakha": "वैशाख", "Jyeshtha": "ज्येष्ठ",
    "Ashadha": "आषाढ़", "Shravana": "श्रावण", "Bhadrapada": "भाद्रपद",
    "Ashwina": "आश्विन", "Kartika": "कार्तिक", "Margashirsha": "मार्गशीर्ष",
    "Pausha": "पौष", "Magha": "माघ", "Phalguna": "फाल्गुन",
}

PLANET_ICONS = {
    "Sun": "", "Moon": "", "Mars": "", "Mercury": "",
    "Jupiter": "", "Venus": "", "Saturn": "", "Rahu": "", "Ketu": "",
}

YEAR_RANGE = list(range(1950, 2051))


# ─────────────────────────────────────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────────────────────────────────────
today = date.today()
samvat_now = samvat_year(today)
saptarishi_now = saptarishi_samvat(today)
today_label = f"{today.strftime('%A')}, {today.day} {today.strftime('%B %Y')}"

_header_html = (
    '<div class="site-header"><div class="hdr-inner">'

    # LEFT — English title + description
    '<div class="hdr-left">'
    '<div class="hdr-title">Ancient <span>Kashmiri</span></div>'
    '<div class="hdr-desc">A living portal of Kashmiri Pandit heritage'
    ' &mdash; Vedic Panchanga, Janma Tithi, Guna Milana,'
    ' Vamsha lineage, Shastra library and Samskrti guide.</div>'
    '<div class="hdr-tagline">Jyotisha &middot; Panchanga &middot; Vamsha'
    ' &middot; Shastra &middot; Samskrti &nbsp;&middot;&nbsp;'
    ' ज्योतिष &middot; पंचांग &middot; वंश &middot; शास्त्र &middot; संस्कृति</div>'
    '</div>'

    # RIGHT — Hindi title same style + samvats + date
    '<div class="hdr-right">'
    '<div class="hdr-title" style="font-size:19px;margin-bottom:6px">प्राचीन <span>कश्मीरी</span></div>'
    '<div style="display:flex;align-items:baseline;gap:12px;justify-content:flex-end">'
    '<div style="text-align:center">'
    '<div class="hdr-samvat">VIKRAMA</div>'
    f'<div class="hdr-samvat-num" style="font-size:18px">{samvat_now}</div>'
    '</div>'
    '<div style="color:rgba(222,184,90,.25);font-size:16px">&middot;</div>'
    '<div style="text-align:center">'
    '<div class="hdr-samvat">SAPTARSHI</div>'
    f'<div class="hdr-samvat-num" style="font-size:18px">{saptarishi_now}</div>'
    '</div></div>'
    f'<div class="hdr-date" style="margin-top:4px">{today_label}</div>'
    '</div>'

    '</div></div>'
)
st.markdown(_header_html, unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# IMPORT ERROR GUARD
# ─────────────────────────────────────────────────────────────────────────────
if not ASTRO_OK:
    st.error(f" Could not import astro_engine or kashmir_data: {_import_err}")
    st.info("Place `astro_engine.py` and `kashmir_data.py` in the same folder as this app.")
    st.stop()

# ─────────────────────────────────────────────────────────────────────────────
# TABS
# ─────────────────────────────────────────────────────────────────────────────
TAB_NAMES = [
    "  Home · गृह",
    "  Pañcāṅga · पंचांग",
    "  Janam Din · जन्म दिन",
    "  Guṇa Milāna · गुण मिलान",
    "  Kul · कुल",
    "  Śāstra · शास्त्र",
    "  Saṃskṛti · संस्कृति",
    "  Sujhav · सुझाव",
    "  Koshurpedia · कोशुरपीडिया",
]
tabs = st.tabs(TAB_NAMES)



# ══════════════════════════════════════════════════════════════════════════════
# TAB 0 — HOME
# ══════════════════════════════════════════════════════════════════════════════
with tabs[0]:

    # ── Top row: mission statement left, today's panchang right ──
    home_l, home_r = st.columns([3, 1.4])

    with home_l:
        st.markdown(f"""
        <div style="padding: 10px 0 4px">
          <div style="font-family:'Cinzel',serif;font-size:9px;letter-spacing:3px;
               color:var(--saffron);margin-bottom:8px">
            PRĀCĪNA KASHMĪRĪ · प्राचीन कश्मीरी
          </div>
          <div style="font-family:'Cinzel',serif;font-size:22px;font-weight:500;
               color:var(--walnut);letter-spacing:2px;line-height:1.3;margin-bottom:14px">
            Reviving the Ancient Wisdom<br>
            <span style="color:var(--saffron)">of Kashmir</span>
          </div>
          <div style="font-family:'Noto Serif Devanagari',serif;font-size:15px;
               color:var(--walnut-mid);line-height:1.8;margin-bottom:16px">
            प्राचीन कश्मीरी ज्ञान का पुनरुद्धार
          </div>

          <div style="font-size:14px;color:var(--ink);line-height:2;
               border-left:3px solid var(--saffron);padding-left:16px;
               margin-bottom:20px;font-style:italic">
            "The mountains of Kashmir have always been a seat of wisdom —
            where sages composed the Shiva Sutras, where Lalleshwari sang
            of liberation, where the Vitasta river nourished a civilisation
            that gave the world Kashmir Shaivism, the Rajatarangini, and a
            way of life rooted in the sacred."
          </div>

          <div style="font-size:13.5px;color:var(--muted);line-height:2;margin-bottom:20px">
            Over centuries — through invasions, migrations and displacement —
            much of this living knowledge became fragmented. The festivals lost
            their depth. The gotra lineages became uncertain. The panchang
            calculations moved to printed almanacs that few could read. The
            Vakhs of Lal Ded survived in memory but their meaning faded.
            <br><br>
            <strong style="color:var(--walnut)">Prācīna Kāśmīrī</strong> is
            a humble attempt to restore this knowledge — not in museum glass,
            but as a living, breathing resource for every Kashmiri Pandit and
            every curious mind. Built for the young generation who may not know
            their gotra, may never have heard a Wanwun song, may not know when
            Herath falls this year — but who carry this heritage in their blood
            and deserve to know its depth.
          </div>

          <div style="background:linear-gradient(135deg,var(--saffron-pale),var(--gold-pale));
               border:1px solid rgba(212,114,42,.2);border-radius:12px;
               padding:16px 20px;margin-bottom:20px">
            <div style="font-family:'Cinzel',serif;font-size:9px;letter-spacing:2px;
                 color:var(--saffron);margin-bottom:8px">OUR INTENT · हमारा उद्देश्य</div>
            <div style="font-size:13px;color:var(--walnut);line-height:2">
              To rewrite ancient Kashmiri knowledge in a form that young minds
              can explore — the astronomy of the panchang, the poetry of Lal Ded,
              the philosophy of the Shiva Sutras, the rituals of Herath, the
              lineages of the gotra system. To make the <em>Jantri</em> accessible,
              the <em>Vakhs</em> understandable, the <em>Bhairava</em> recognisable,
              and the <em>Kul Devi</em> remembered. One page at a time.
            </div>
            <div style="font-family:'Noto Serif Devanagari',serif;font-size:12px;
                 color:var(--muted);margin-top:8px;line-height:1.8">
              युवा पीढ़ी के लिए — गोत्र से लेकर श्लोक तक, पंचांग से लेकर शास्त्र तक,
              हेरठ से लेकर वाख तक — एक जीवित ज्ञान-कोश।
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)

    with home_r:
        # Today's panchang summary card
        try:
            home_p = _cached_panchang(today, 32.7266, 74.8570)  # Jammu default
            home_masa = MASA_DEVA.get(home_p['masa'], home_p['masa'])
            home_adhik = home_p.get('is_adhik', False)
            home_masa_label = ('Adhika ' if home_adhik else '') + home_p['masa']
            home_masa_hi    = ('अधिक ' if home_adhik else '') + home_masa
            st.markdown(f"""
            <div style="background:linear-gradient(135deg,#3A2010,#4E2210);
                 border-radius:14px;padding:18px 16px;
                 box-shadow:0 4px 20px rgba(58,32,16,.3);
                 border:1px solid rgba(184,134,42,.2);margin-top:10px">
              <div style="font-family:'Cinzel',serif;font-size:8px;letter-spacing:3px;
                   color:rgba(222,184,90,.5);margin-bottom:6px;text-align:center">
                TODAY'S PANCHANG · आज का पंचांग
              </div>
              <div style="text-align:center;font-size:11px;color:rgba(253,248,240,.4);
                   margin-bottom:12px;border-bottom:1px solid rgba(222,184,90,.1);
                   padding-bottom:10px">
                {today.strftime('%A')}, {today.day} {today.strftime('%B %Y')}
              </div>
              <div style="display:flex;flex-direction:column;gap:8px">
                <div style="background:rgba(253,248,240,.06);border-radius:8px;padding:8px 10px">
                  <div style="font-family:'Cinzel',serif;font-size:7px;letter-spacing:2px;
                       color:rgba(212,114,42,.7)">MĀSA · मास</div>
                  <div style="font-size:13px;font-weight:500;color:#FDF8F0;margin-top:2px">
                    {home_masa_label}</div>
                  <div style="font-family:'Noto Serif Devanagari',serif;font-size:11px;
                       color:rgba(222,184,90,.6)">{home_masa_hi}</div>
                </div>
                <div style="background:rgba(253,248,240,.06);border-radius:8px;padding:8px 10px">
                  <div style="font-family:'Cinzel',serif;font-size:7px;letter-spacing:2px;
                       color:rgba(212,114,42,.7)">TITHI · तिथि</div>
                  <div style="font-size:12px;font-weight:500;color:#FDF8F0;margin-top:2px">
                    {home_p['paksha']} {home_p['tithi']}</div>
                  <div style="font-size:9px;color:rgba(253,248,240,.4)">
                    ends {home_p.get('tithi_end','')}</div>
                </div>
                <div style="background:rgba(253,248,240,.06);border-radius:8px;padding:8px 10px">
                  <div style="font-family:'Cinzel',serif;font-size:7px;letter-spacing:2px;
                       color:rgba(212,114,42,.7)">NAKṢATRA · नक्षत्र</div>
                  <div style="font-size:12px;font-weight:500;color:#FDF8F0;margin-top:2px">
                    {home_p['nakshatra']}</div>
                  <div style="font-size:9px;color:rgba(253,248,240,.4)">
                    Pāda {home_p['nakshatra_pada']}</div>
                </div>
                <div style="background:rgba(184,134,42,.12);border-radius:8px;padding:8px 10px;
                     border:1px solid rgba(184,134,42,.2)">
                  <div style="font-family:'Cinzel',serif;font-size:7px;letter-spacing:2px;
                       color:#DEB85A">SUNRISE · SUNSET</div>
                  <div style="font-size:11px;color:#FDF8F0;margin-top:2px">
                    {home_p['sunrise']} &nbsp;·&nbsp; {home_p['sunset']}</div>
                </div>
                <div style="background:rgba(184,134,42,.08);border-radius:8px;padding:8px 10px">
                  <div style="font-family:'Cinzel',serif;font-size:7px;letter-spacing:2px;
                       color:rgba(212,114,42,.7)">ABHIJIT MUHŪRTA</div>
                  <div style="font-size:11px;color:#FDF8F0;margin-top:2px">
                    {home_p['abhijit_muhurta'][0]} – {home_p['abhijit_muhurta'][1]}</div>
                </div>
              </div>
              <div style="text-align:center;margin-top:10px;font-size:9px;
                   color:rgba(253,248,240,.25);font-style:italic">
                Jammu · Lahiri · Amāvasyānta
              </div>
            </div>
            """, unsafe_allow_html=True)
        except Exception:
            pass

    # ── What's inside — tab cards ─────────────────────────────────
    st.markdown('<div class="styled-div"><span>WHAT IS INSIDE · क्या है इसमें</span></div>',
                unsafe_allow_html=True)

    TAB_CARDS = [
        {
            "tab": "Pañcāṅga · पंचांग",
            "heading": "Vedic Pañcāṅga",
            "hi": "वैदिक पंचांग",
            "desc": (
                "A precise Vedic calendar for any date and location — Tithi, Vara, Nakshatra, "
                "Yoga, Karana. Masa calculated by the authentic Amāvasyānta (new-moon-ending) "
                "system with Lahiri ayanamsha. Muhurtas: Brahma, Abhijit, Rahu Kaal, Gulika, "
                "Yamaganda. Complete planetary positions with sidereal longitudes. "
                "Monthly calendar with Kashmiri festival highlights."
            ),
            "why": "Know the auspicious time for every ritual, ceremony and daily life.",
            "color": "var(--saffron)",
        },
        {
            "tab": "Janam Din · जन्म दिन",
            "heading": "Janam Din Calendar",
            "hi": "जन्म दिन कैलेंडर",
            "desc": (
                "Find your Vedic birthday — the Janma Masa, Tithi and Nakshatra — "
                "for any year from 1950 to 2050. The Amāvasyānta masa is used so the "
                "lunar birthday falls in the correct month as observed in KP tradition. "
                "Birth chart snapshot: Chandra Rashi, Surya Rashi, Lagna Rashi."
            ),
            "why": "Observe your Vedic birthday on the correct Tithi each year.",
            "color": "#4A9A50",
        },
        {
            "tab": "Guṇa Milāna · गुण मिलान",
            "heading": "36-Guna Marriage Matching",
            "hi": "गुण मिलान · विवाह संगतता",
            "desc": (
                "Ashtakoot (36-point) Kundali Milan using classical Kashmiri Pandit nakshatra "
                "tables. All 8 Kutas: Varna, Vashya, Tara, Yoni, Graha Maitri, Gana, Bhakoot, "
                "Nadi. Mangala Dosha check from D1, Moon chart and D9 Navamsha. "
                "Gotra compatibility — same-gotra marriage warning as per KP tradition."
            ),
            "why": "Ensure a compatible and blessed union as per Vedic and KP tradition.",
            "color": "var(--lotus)",
        },
        {
            "tab": "Kul · कुल",
            "heading": "Kul — Lineage & Ancestry",
            "hi": "कुल परम्परा",
            "desc": (
                "Trace your Kashmiri Pandit lineage — select your district, town and village "
                "to discover your probable Gotra (from the traditional Bhannamasis table), "
                "Kul Devi, Kul Devta and Bhairava. The complete KP surname-to-Gotra map "
                "from classical records. Ashta Bhairavas of Kashmir with their guardian regions."
            ),
            "why": "Know your roots — gotra, kul devi, bhairava — before they are forgotten.",
            "color": "#2A7A6A",
        },
        {
            "tab": "Śāstra · शास्त्र",
            "heading": "Kashmiri Śāstra Library",
            "hi": "कश्मीरी शास्त्र ग्रन्थालय",
            "desc": (
                "A curated library of Kashmir Shaivism, Trika philosophy and Kashmiri literature. "
                "Texts: Shiva Sutras, Spanda Karikas, Tantraloka, Pratyabhijnahridayam, "
                "Nilamata Purana, Rajatarangini. Saints: Lal Ded, Nund Rishi, Abhinavagupta, "
                "Swami Lakshmanjoo. With references, archive links and study guides."
            ),
            "why": "Access the world's greatest tantric and philosophical texts — in one place.",
            "color": "var(--crimson)",
        },
        {
            "tab": "Saṃskṛti · संस्कृति",
            "heading": "Kashmiri Culture Guide",
            "hi": "कश्मीरी संस्कृति",
            "desc": (
                "A comprehensive guide to every aspect of Kashmiri Pandit culture — "
                "Festivals with complete puja vidhi and samagri (Herath, Navreh, Zyeth Ashtami), "
                "Sacred sites with GPS coordinates (50+ temples, Bhairava mandirs, Nag tirthas), "
                "Music traditions (Sufiana Kalam, Chakri, Wanwun, Santoor), "
                "Cuisine, Dress, Language and Sharada script."
            ),
            "why": "Keep the living traditions alive — festival rituals, sacred sites, music.",
            "color": "var(--gold)",
        },
        {
            "tab": "Koshurpedia · कोशुरपीडिया",
            "heading": "Koshurpedia",
            "hi": "कोशुरपीडिया",
            "desc": (
                "Your wise Kashmiri Pandit guide — coming in the next update. "
                "Will cover rituals, panchang queries, mantras, Kul Devi puja guidance, "
                "festival significance, Kashmir Shaivism and the Vakhs of Lalleshwari. "
                "A living encyclopaedia of Kashmiri knowledge."
            ),
            "why": "One resource for every question about Kashmiri Pandit tradition.",
            "color": "var(--muted)",
        },
    ]

    cols_cards = st.columns(3)
    for i, card in enumerate(TAB_CARDS):
        cols_cards[i % 3].markdown(f"""
        <div style="background:white;border:1px solid var(--border);border-radius:12px;
             padding:16px 18px;margin-bottom:14px;box-shadow:0 2px 8px var(--shadow);
             border-top:3px solid {card['color']}">
          <div style="font-family:'Cinzel',serif;font-size:8.5px;letter-spacing:1.5px;
               color:{card['color']};margin-bottom:4px">{card['tab']}</div>
          <div style="font-family:'Cinzel',serif;font-size:13px;font-weight:500;
               color:var(--walnut);margin-bottom:3px">{card['heading']}</div>
          <div style="font-family:'Noto Serif Devanagari',serif;font-size:11px;
               color:var(--muted);margin-bottom:10px">{card['hi']}</div>
          <div style="font-size:12.5px;color:var(--ink);line-height:1.75;
               margin-bottom:10px">{card['desc']}</div>
          <div style="font-size:11px;color:{card['color']};font-style:italic;
               border-top:1px solid var(--border);padding-top:8px">
            {card['why']}
          </div>
        </div>
        """, unsafe_allow_html=True)

    # ── Closing note ─────────────────────────────────────────────
    st.markdown(f"""
    <div style="background:linear-gradient(135deg,#3A2010,#4E2210);border-radius:14px;
         padding:24px 32px;margin-top:10px;text-align:center;
         box-shadow:0 4px 20px rgba(58,32,16,.25)">
      <div style="font-family:'Cinzel',serif;font-size:11px;letter-spacing:3px;
           color:rgba(222,184,90,.6);margin-bottom:10px">ॐ नमः शिवाय</div>
      <div style="font-size:14px;color:rgba(253,248,240,.75);line-height:2;
           max-width:600px;margin:0 auto">
        This portal is dedicated to every Kashmiri Pandit who carries the memory
        of the Valley — and to every young mind curious enough to ask:
        <em style="color:#DEB85A">"Who are we, and where did we come from?"</em>
      </div>
      <div style="font-family:'Noto Serif Devanagari',serif;font-size:13px;
           color:rgba(222,184,90,.5);margin-top:12px;line-height:1.8">
        यह पोर्टल उन सभी कश्मीरी पण्डितों को समर्पित है जो घाटी की स्मृति अपने
        हृदय में संजोये हुए हैं।
      </div>
      <div style="font-family:'Cinzel',serif;font-size:9px;letter-spacing:3px;
           color:rgba(222,184,90,.3);margin-top:14px">
        VIKRAMA SAṂVAT {samvat_now} &nbsp;·&nbsp; LAHIRI AYANĀṂŚA &nbsp;·&nbsp; AMĀVASYĀNTA
      </div>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# TAB 1 — PANCHANG
# ══════════════════════════════════════════════════════════════════════════════
with tabs[1]:
    st.markdown("""
    <div class="sec-head"> Pañcāṅga · पंचांग</div>
    <div class="sec-sub">
      Vedic Pañcāṅga using Lahiri Ayanāṃśa · Amāvasyānta Chandra Māsa system
      <span class="deva">लाहिरी अयनांश · अमावस्यान्त चन्द्र मास · वैदिक सूर्योदय–अस्त गणना</span>
    </div>
    """, unsafe_allow_html=True)

    # ── TOP ROW: Controls (compact) | Centre panel | Calendar (large) ──
    left_col, centre_col, right_col = st.columns([1.2, 1.6, 3.0])

    with left_col:
        p_lat, p_lon, p_loc = state_district_selects("pan", default_dist="Jammu")
        p_date = st.date_input("Date · तारीख", value=today, key="pan_date")

    # ── Calculate panchang ───────────────────────────────────────
    try:
        panchang = _cached_panchang(p_date, p_lat, p_lon)
        sv = samvat_year(p_date)

        masa_deva   = MASA_DEVA.get(panchang["masa"], panchang["masa"])
        is_adhik    = panchang.get("is_adhik", False)
        adhik_label = "ADHIKA " if is_adhik else ""
        adhik_hi    = "अधिक " if is_adhik else ""
        auspicious_badge = (
            '<span class="badge badge-good">Auspicious · शुभ</span>'
            if panchang["auspicious"]
            else '<span class="badge badge-bad">Caution · सावधान</span>'
        )

        # ── Centre: Masa + Tithi + Abhijit ───────────────────────
        with centre_col:
            masa_full_name = f"{'Adhika ' if is_adhik else ''}{panchang['masa']}"
            masa_full_hi   = f"{'अधिक ' if is_adhik else ''}{masa_deva}"
            adhik_pill     = '<span class="badge badge-avg" style="font-size:8px;margin-left:6px">ADHIKA</span>' if is_adhik else ""
            st.markdown(f"""
            <div style="background:linear-gradient(135deg,#3A2010,#4E2210);border-radius:14px;
                 padding:18px 20px;height:100%;box-shadow:0 4px 18px rgba(58,32,16,.25);
                 border:1px solid rgba(184,134,42,.2)">
              <div style="text-align:center;border-bottom:1px solid rgba(222,184,90,.15);
                   padding-bottom:12px;margin-bottom:12px">
                <div style="font-family:'Cinzel',serif;font-size:8px;letter-spacing:3px;
                     color:rgba(222,184,90,.5);margin-bottom:4px">VIKRAMA SAṂVAT</div>
                <div style="font-family:'Cinzel Decorative',serif;font-size:22px;
                     color:rgba(222,184,90,.9);line-height:1">{sv}</div>
                <div style="font-size:10px;color:rgba(253,248,240,.4);margin-top:2px">
                  {p_date.strftime('%A')}, {p_date.day} {p_date.strftime('%B %Y')}
                </div>
              </div>
              <div style="text-align:center;margin-bottom:14px">
                <div style="font-family:'Cinzel',serif;font-size:8px;letter-spacing:2.5px;
                     color:rgba(212,114,42,.7);margin-bottom:3px">MĀSA · मास</div>
                <div style="font-size:18px;font-weight:500;color:#FDF8F0;line-height:1.2">
                  {masa_full_name}{adhik_pill}
                </div>
                <div style="font-family:'Noto Serif Devanagari',serif;font-size:13px;
                     color:rgba(253,248,240,.55);margin-top:2px">{masa_full_hi}</div>
              </div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:12px">
                <div style="background:rgba(253,248,240,.06);border-radius:8px;padding:8px 10px;
                     border:1px solid rgba(184,134,42,.15)">
                  <div style="font-family:'Cinzel',serif;font-size:7.5px;letter-spacing:2px;
                       color:rgba(212,114,42,.7);margin-bottom:3px">TITHI · तिथि</div>
                  <div style="font-size:12px;font-weight:500;color:#FDF8F0;line-height:1.3">
                    {panchang['paksha']} {panchang['tithi']}</div>
                  <div style="font-size:9.5px;color:rgba(253,248,240,.45);margin-top:1px">
                    #{panchang['tithi_num']} · ends {panchang.get('tithi_end','')}</div>
                </div>
                <div style="background:rgba(253,248,240,.06);border-radius:8px;padding:8px 10px;
                     border:1px solid rgba(184,134,42,.15)">
                  <div style="font-family:'Cinzel',serif;font-size:7.5px;letter-spacing:2px;
                       color:rgba(212,114,42,.7);margin-bottom:3px">NAKṢATRA · नक्षत्र</div>
                  <div style="font-size:12px;font-weight:500;color:#FDF8F0;line-height:1.3">
                    {panchang['nakshatra']}</div>
                  <div style="font-size:9.5px;color:rgba(253,248,240,.45);margin-top:1px">
                    Pāda {panchang['nakshatra_pada']}</div>
                </div>
              </div>
              <div style="background:rgba(184,134,42,.12);border-radius:8px;padding:9px 12px;
                   border:1px solid rgba(184,134,42,.25);margin-bottom:8px">
                <div style="font-family:'Cinzel',serif;font-size:7.5px;letter-spacing:2px;
                     color:#DEB85A;margin-bottom:3px">ABHIJIT MUHŪRTA</div>
                <div style="font-size:13px;font-weight:500;color:#FDF8F0">
                  {panchang['abhijit_muhurta'][0]} – {panchang['abhijit_muhurta'][1]}</div>
                <div style="font-size:9px;color:rgba(253,248,240,.45)">
                  Auspicious midday window · मध्याह्न शुभ काल</div>
              </div>
              <div style="text-align:center;margin-top:6px">{auspicious_badge}</div>
            </div>
            """, unsafe_allow_html=True)

        # ── Right: Monthly Calendar — always open, full size ─────
        with right_col:
            cal_year, cal_month = p_date.year, p_date.month
            month_name = p_date.strftime("%B %Y")
            first_day  = date(cal_year, cal_month, 1)
            if cal_month == 12:
                last_day = date(cal_year + 1, 1, 1) - timedelta(days=1)
            else:
                last_day = date(cal_year, cal_month + 1, 1) - timedelta(days=1)

            KP_FESTIVAL_RULES = [
                ("Phalguna",  "Krishna", 14, "Herath",         "#e53935"),
                ("Chaitra",   "Shukla",   1, "Navreh",         "#4CAF50"),
                ("Jyeshtha",  "Shukla",   8, "Zyeth Ashtami",  "#DEB85A"),
                ("Shravana",  "Shukla",   5, "Nag Panchami",   "#2A7A6A"),
                ("Bhadrapada","Krishna",  1, "Pitru Paksha",   "#8B1C30"),
                ("Ashwina",   "Shukla",   1, "Navratri",       "#D4722A"),
                ("Ashwina",   "Shukla",   8, "Maha Ashtami",   "#D4722A"),
                ("Ashwina",   "Shukla",  10, "Vijaya Dashami", "#D4722A"),
                ("Vaishakha", "Shukla",   8, "Vaishakh Ash.",  "#9C27B0"),
            ]
            AM_CLR = "#888"; PU_CLR = "#B8862A"; SEL_CLR = "#3A2010"

            day_data = {}
            probe_d = first_day
            while probe_d <= last_day:
                try:
                    pp = _cached_panchang(probe_d, p_lat, p_lon)
                    fests = []
                    for (fm, fp, ft, fn, fc) in KP_FESTIVAL_RULES:
                        if pp['masa'] == fm and pp['paksha'] == fp and pp['tithi_num'] == ft:
                            fests.append((fn, fc))
                    day_data[probe_d] = {
                        'tnum': pp['tithi_num'], 'paksha': pp['paksha'],
                        'fests': fests, 'ausp': pp['auspicious'],
                    }
                except Exception:
                    day_data[probe_d] = {'tnum': 0, 'paksha': '', 'fests': [], 'ausp': True}
                probe_d += timedelta(days=1)

            WD = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
            first_wd = first_day.weekday()

            wd_cells = "".join(
                f'<th style="font-family:Cinzel,serif;font-size:9px;color:var(--muted);'
                f'padding:6px 2px;text-align:center;font-weight:400;'
                f'border-bottom:1px solid var(--border)">{w}</th>'
                for w in WD
            )

            cells = ['<td style="padding:3px"></td>'] * first_wd
            for dn in range(1, last_day.day + 1):
                d_obj  = date(cal_year, cal_month, dn)
                dd     = day_data.get(d_obj, {})
                tnum   = dd.get('tnum', 0)
                paksha = dd.get('paksha', '')
                fests  = dd.get('fests', [])
                ausp   = dd.get('ausp', True)
                is_sel = (d_obj == p_date)
                is_td  = (d_obj == today)

                bg  = SEL_CLR if is_sel else ("rgba(184,134,42,.12)" if is_td else
                      ("rgba(192,48,48,.05)" if not ausp else "rgba(253,248,240,.4)"))
                nc  = "#DEB85A" if is_sel else "var(--walnut)"
                brd = "2px solid #DEB85A" if is_sel else (
                      "1px solid rgba(184,134,42,.3)" if is_td else
                      "1px solid rgba(184,134,42,.1)")

                if tnum == 30:
                    ts = "Amavasya"
                    tc = AM_CLR if not is_sel else "#DEB85A"
                elif tnum == 15:
                    ts = "Purnima"
                    tc = PU_CLR if not is_sel else "#DEB85A"
                else:
                    pk = "S" if paksha == "Shukla" else "K"
                    ts = f"{pk}{tnum}"
                    tc = "var(--saffron)" if not is_sel else "rgba(222,184,90,.8)"

                # Festival dots + name
                dots = "".join(
                    f'<span style="display:inline-block;width:6px;height:6px;'
                    f'border-radius:50%;background:{fc};margin:1px 1px 0"></span>'
                    for _, fc in fests[:2]
                )
                fest_name = ""
                if fests:
                    fc0 = "#DEB85A" if is_sel else fests[0][1]
                    fest_name = (
                        f'<div style="font-size:7.5px;color:{fc0};line-height:1.2;'
                        f'margin-top:2px;overflow:hidden;text-overflow:ellipsis;'
                        f'white-space:nowrap">{fests[0][0]}</div>'
                    )

                cells.append(
                    f'<td style="padding:3px;vertical-align:top">'
                    f'<div style="background:{bg};border:{brd};border-radius:6px;'
                    f'padding:6px 4px 4px;text-align:center;min-height:54px">'
                    f'<div style="font-family:Cinzel,serif;font-size:13px;font-weight:500;'
                    f'color:{nc};line-height:1">{dn}</div>'
                    f'<div style="font-size:8.5px;color:{tc};margin-top:2px;line-height:1.2">{ts}</div>'
                    f'<div style="margin-top:2px">{dots}</div>'
                    f'{fest_name}'
                    f'</div></td>'
                )

            rem = (7 - (first_wd + last_day.day) % 7) % 7
            cells += ['<td style="padding:3px"></td>'] * rem

            rows_html = "".join(
                f'<tr>{"".join(cells[i:i+7])}</tr>'
                for i in range(0, len(cells), 7)
            )

            # Festival legend
            legend_items = [
                ("S# Shukla · K# Krishna", "var(--muted)"),
                ("Purnima", PU_CLR),
                ("Amavasya", AM_CLR),
                ("Herath", "#e53935"),
                ("Navreh", "#4CAF50"),
                ("Zyeth Ashtami", "#DEB85A"),
                ("Navratri", "#D4722A"),
            ]
            legend_dots = "".join(
                f'<span style="display:inline-flex;align-items:center;gap:4px;'
                f'font-size:9px;color:var(--muted)">'
                f'<span style="display:inline-block;width:7px;height:7px;border-radius:50%;'
                f'background:{lc}"></span>{ln}</span>'
                if i > 1 else
                f'<span style="font-size:9px;color:{lc}">{ln}</span>'
                for i, (ln, lc) in enumerate(legend_items)
            )
            legend = (
                f'<div style="display:flex;flex-wrap:wrap;gap:8px;'
                f'margin-top:8px;padding-top:8px;border-top:1px solid var(--border)">'
                f'{legend_dots}</div>'
            )

            st.markdown(
                f'<div style="background:white;border:1px solid var(--border);'
                f'border-radius:12px;padding:14px 12px;'
                f'box-shadow:0 2px 10px var(--shadow)">'
                f'<div style="font-family:Cinzel,serif;font-size:11px;letter-spacing:2px;'
                f'color:var(--walnut-mid);text-align:center;margin-bottom:8px">'
                f'{month_name.upper()}</div>'
                f'<table style="width:100%;border-collapse:collapse">'
                f'<thead><tr>{wd_cells}</tr></thead>'
                f'<tbody>{rows_html}</tbody>'
                f'</table>{legend}</div>',
                unsafe_allow_html=True
            )

        # ── Banner line (below the 3 columns) ────────────────────
        adhik_badge = (
            ' &nbsp;<span class="badge badge-avg" style="font-size:9px;letter-spacing:1px">'
            ' ADHIKA MĀSA · अधिक मास</span>'
            if is_adhik else ""
        )
        st.markdown(f"""
        <div style="text-align:center;margin:10px 0 6px">
          <span style="font-family:'Cinzel',serif;font-size:10px;letter-spacing:2px;color:var(--muted)">
            {adhik_label}{panchang['masa'].upper()} MĀSA &nbsp;·&nbsp; SAṂVAT {sv} &nbsp;·&nbsp;
            {p_date.strftime('%A')}, {p_date.day} {p_date.strftime('%B %Y')}
          </span>
          &nbsp; {auspicious_badge}{adhik_badge}
        </div>
        """, unsafe_allow_html=True)

        # ── Five Elements ─────────────────────────────────────────
        cols5 = st.columns(5)
        items5 = [
            ("TITHI · तिथि",    "तिथि",    f"{panchang['paksha']} {panchang['tithi']}",
             f"#{panchang['tithi_num']} · ends {panchang.get('tithi_end','')}"),
            ("VĀRA · वार",      "दिन",     panchang["vara"], ""),
            ("NAKṢATRA · नक्षत्र","नक्षत्र",panchang["nakshatra"],
             f"Pāda {panchang['nakshatra_pada']} · ends {panchang.get('nakshatra_end','')}"),
            ("YOGA · योग",      "योग",     panchang["yoga"], ""),
            ("KARAṆA · करण",   "करण",     panchang["karana"], ""),
        ]
        for col, (lbl, deva, val, sub) in zip(cols5, items5):
            col.markdown(panch_cell(lbl, deva, val, sub), unsafe_allow_html=True)

        # ── Masa row (full width, highlights Adhik Masa) ─────────
        masa_full_name = f"{'Adhika ' if is_adhik else ''}{panchang['masa']}"
        masa_full_hi   = f"{'अधिक ' if is_adhik else ''}{masa_deva}"
        masa_note      = "अधिक मास — पुण्यकाल · Extra merit; no new auspicious starts" if is_adhik else "Amāvasyānta system · अमावस्यान्त"
        masa_style     = "border:2px solid var(--saffron);background:linear-gradient(135deg,#FDF0E5,#FBF5E6)" if is_adhik else ""
        _adhik_span = '<span class="badge badge-avg" style="font-size:9px"> ADHIKA MĀSA</span>' if is_adhik else ""
        _masa_html = (
            f'<div style="{masa_style};border-radius:10px;padding:10px 18px;margin:10px 0 4px;display:flex;align-items:center;gap:16px">'
            f'<span style="font-family:Cinzel,serif;font-size:9px;letter-spacing:2px;color:var(--saffron);text-transform:uppercase">MĀSA · मास</span>'
            f'<span style="font-size:16px;font-weight:500;color:var(--walnut)">{masa_full_name}</span>'
            '<span style="font-family:\'Noto Serif Devanagari\',serif;font-size:15px;color:var(--muted)">'
            f'{masa_full_hi}</span>'
            f'{_adhik_span}'
            f'<span style="font-size:11px;color:var(--muted);margin-left:auto;font-style:italic">{masa_note}</span>'
            '</div>'
        )
        st.markdown(_masa_html, unsafe_allow_html=True)

        # ── Sunrise / Sunset / Day info ───────────────────────────
        st.markdown('<div class="styled-div"><span>SŪRYODAYA & SŪRYĀSTA · सूर्योदय – सूर्यास्त</span></div>', unsafe_allow_html=True)
        sc1, sc2, sc3, sc4 = st.columns(4)
        sc1.markdown(panch_cell("SUNRISE · सूर्योदय", "वैदिक उदय", panchang["sunrise"], p_loc), unsafe_allow_html=True)
        sc2.markdown(panch_cell("SUNSET · सूर्यास्त", "वैदिक अस्त", panchang["sunset"], p_loc), unsafe_allow_html=True)
        sc3.markdown(panch_cell("MOON RĀŚI · राशि", "चन्द्र राशि", panchang["moon_rashi"], ""), unsafe_allow_html=True)
        sc4.markdown(panch_cell("SUN RĀŚI · सूर्य", "सूर्य राशि", panchang["sun_rashi"], ""), unsafe_allow_html=True)

        # ── Muhurtas ─────────────────────────────────────────────
        st.markdown('<div class="subsec">MUHŪRTA · मुहूर्त <span class="deva">शुभ एवं अशुभ काल</span></div>', unsafe_allow_html=True)
        mc1, mc2 = st.columns(2)
        with mc1:
            st.markdown(
                muh_block("good", "BRAHMĀ MUHŪRTA · ब्रह्म मुहूर्त", "प्रातः कालीन साधना",
                          f"{panchang['brahma_muhurta'][0]} – {panchang['brahma_muhurta'][1]}",
                          "Most auspicious · सर्वोत्तम") +
                muh_block("spec", "ABHIJIT MUHŪRTA · अभिजित", "मध्याह्न शुभ काल",
                          f"{panchang['abhijit_muhurta'][0]} – {panchang['abhijit_muhurta'][1]}",
                          "Auspicious midday"),
                unsafe_allow_html=True,
            )
        with mc2:
            st.markdown(
                muh_block("bad", "RĀHU KĀLA · राहु काल", "वर्जित समय — नए कार्य न करें",
                          f"{panchang['rahu_kaal'][0]} – {panchang['rahu_kaal'][1]}",
                          "Avoid new beginnings") +
                muh_block("bad", "GULIKA KĀLA · गुलिक काल", "वर्जित",
                          f"{panchang['gulika_kaal'][0]} – {panchang['gulika_kaal'][1]}") +
                muh_block("bad", "YAMĀGAṆḌA · यमगण्ड", "यात्रा वर्जित",
                          f"{panchang['yamaganda'][0]} – {panchang['yamaganda'][1]}",
                          "Avoid travel"),
                unsafe_allow_html=True,
            )

        # ── Planetary Positions ───────────────────────────────────
        with st.expander(" Graha Sthiti · ग्रह स्थिति — Planetary Positions"):
            p_rows = "".join([
                f"""<tr>
                  <td>{planet_badge(name)}</td>
                  <td>
                    <span style="font-weight:500">{data['rashi']}</span>
                    <span style="display:block;font-family:'Noto Serif Devanagari',serif;font-size:12px;color:var(--muted)">{data['rashi_hi']}</span>
                  </td>
                  <td>
                    <span>{data['nakshatra']} (P{data['pada']})</span>
                    <span style="display:block;font-family:'Noto Serif Devanagari',serif;font-size:12px;color:var(--muted)">{data['nakshatra_hi']} पाद {data['pada']}</span>
                  </td>
                  <td style="font-size:13px;font-variant-numeric:tabular-nums">
                    <span style="font-weight:500">{data['longitude']:.4f}°</span>
                    <span style="display:block;font-size:11px;color:var(--muted)">{data['degree']:.4f}° in rashi</span>
                    <span style="display:block;font-size:11px;color:var(--muted)">{data.get('nak_degree', 0):.4f}° in nak</span>
                  </td>
                </tr>"""
                for name, data in panchang["planets"].items()
            ])
            st.markdown(f"""
            <table class="planet-tbl">
              <thead><tr>
                <th>GRAHA · ग्रह</th>
                <th>RĀŚI · राशि</th>
                <th>NAKṢATRA · नक्षत्र</th>
                <th>LONGITUDE · अंश</th>
              </tr></thead>
              <tbody>{p_rows}</tbody>
            </table>
            """, unsafe_allow_html=True)

        # ── Kashmiri Festivals ───────────────────────────────────
        with st.expander(" Kāśmīra Parva · कश्मीरी पर्व — Festivals & Significance"):
            festivals = [
                (" Herath (Shivarātri · हेरथ)",
                 "Most sacred KP festival. Krishna Chaturdashi of Phalguna. Shiva worshipped with water-filled earthen pots (Vatak). Includes Salām, Vatuk Puja, and ritual breaking of fast."),
                (" Navreh · नवरेह",
                 "Kashmiri New Year on Chaitra Shukla Pratipada. A Thali (plate) with rice, walnut, salt, flowers, curd, pen, and Jantri (almanac) is kept the previous night."),
                (" Kheer Bhawani · खीर भवानी",
                 "Annual mela at Tulmul spring temple (Ragnya Devi). Milk and kheer are offered; the colour of the spring water is believed to foretell events."),
                (" Zyeth Ashtami · ज्येष्ठ अष्टमी",
                 "Pilgrimage to the Kheer Bhawani temple on Jyeshtha Shukla Ashtami — one of the most attended gatherings for Kashmiri Pandits."),
                (" Pann · पान्न",
                 "Kashmiri harvest festival. Community bonfire, seasonal foods, and songs marking the end of winter."),
                (" Gada Bata · गड बत",
                 "Ritual of placing clay waterpots (Vatak) during Herath, symbolising the twelve Shiva lingas and the cosmic Shiva–Shakti union."),
            ]
            for title, desc in festivals:
                st.markdown(f"""
                <div class="muh-block spec" style="margin-bottom:8px">
                  <div class="muh-lbl">{title}</div>
                  <div style="font-size:13.5px;color:var(--ink);margin-top:4px;line-height:1.7">{desc}</div>
                </div>
                """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Panchang calculation error: {e}")
        import traceback; st.code(traceback.format_exc())

    # ── AI Query ─────────────────────────────────────────────────
    st.markdown('<div class="styled-div"><span>AI PAÑCĀṄGA QUERY · पंचांग प्रश्न</span></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="ai-box">
      <div class="ai-lbl">ASK THE JYOTIṢĪ · ज्योतिषी से पूछें</div>
      <div style="margin-top:18px;text-align:center;padding:18px 0 10px">
        <div style="font-size:28px;margin-bottom:10px"></div>
        <div style="font-family:'Cinzel',serif;font-size:13px;letter-spacing:2px;
             color:#DEB85A;margin-bottom:8px">COMING IN NEXT UPDATE</div>
        <div style="font-size:14px;color:rgba(253,248,240,.65);line-height:1.8;max-width:480px;margin:0 auto">
          Your wise Kashmiri Pandit — for muhurtas, nakshatra guidance, festival significance
          and personalised panchang insights — will be available in the next release.
        </div>
        <div style="font-family:'Noto Serif Devanagari',serif;font-size:12px;
             color:rgba(222,184,90,.45);margin-top:10px">
          ज्योतिषी शीघ्र ही उपलब्ध होंगे — अगले अपडेट में
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Info cards ───────────────────────────────────────────────
    st.markdown('<div class="styled-div"><span>ABOUT THIS SYSTEM</span></div>', unsafe_allow_html=True)
    ic1, ic2, ic3 = st.columns(3)
    ic1.markdown("""<div class="info-card">
      <div class="ic-icon"></div>
      <div class="ic-title">VEDIC SUNRISE · वैदिक सूर्योदय</div>
      <div class="ic-body">Computed from exact geodetic coordinates with atmospheric refraction. 
      All muhurta divisions (Rahu Kala, Gulika, Yamaganda) are derived from actual local sunrise.</div>
      <div class="ic-accent">सूर्योदय से दिनमान</div>
    </div>""", unsafe_allow_html=True)
    ic2.markdown("""<div class="info-card">
      <div class="ic-icon"></div>
      <div class="ic-title">AMĀVASYĀNTA · अमावस्यान्त</div>
      <div class="ic-body">The lunar month begins and ends at Amāvasyā (new moon). Shukla Paksha
      (waxing) comes first, followed by Krishna Paksha (waning). Used in traditional panchang
      reckoning — Navreh falls on Chaitra Śukla Pratipada.</div>
      <div class="ic-accent">कश्मीरी पण्डित परम्परा</div>
    </div>""", unsafe_allow_html=True)
    ic3.markdown("""<div class="info-card">
      <div class="ic-icon"></div>
      <div class="ic-title">LAHIRI AYANĀṂŚA · लाहिरी</div>
      <div class="ic-body">Official ayanamsha adopted by the Government of India in 1955 
      (Rashtriya Panchang). Used for all sidereal calculations including nakshatra and rashi.</div>
      <div class="ic-accent">भारत सरकार द्वारा मान्य</div>
    </div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# TAB 2 — JANMA TITHI (BIRTHDAY)
# ══════════════════════════════════════════════════════════════════════════════
with tabs[2]:
    st.markdown("""
    <div class="sec-head"> Janam Din · जन्म दिन</div>
    <div class="sec-sub">
      Find your Vedic birthday (Tithi + Nakshatra) for any year from 1950 to 2050 ·
      Amāvasyānta system · Precise to the minute
      <span class="deva">जन्म नक्षत्र-तिथि खोजें · 1950 से 2050 तक · मिनट-स्तरीय शुद्धता</span>
    </div>
    """, unsafe_allow_html=True)

    _jt1, _jt2, _jt3, _jt4 = st.columns([1.4, 1.0, 1.4, 1.4])
    with _jt1:
        b_dob = st.date_input(
            "Date of Birth · जन्म तिथि",
            value=date(1990, 1, 1),
            min_value=date(1900, 1, 1),
            max_value=date(2025, 12, 31),
            key="jt_dob",
        )
    with _jt2:
        b_time = st.time_input("Birth Time · समय", value=datetime(2000, 1, 1, 6, 0).time(), step=60, key="jt_time")
    with _jt3:
        _jt_states = list(INDIA_STATES.keys())
        _jt_state  = st.selectbox("State · राज्य", _jt_states,
                                   index=_jt_states.index("Jammu & Kashmir"),
                                   key="jt_state")
    with _jt4:
        _jt_dists = list(INDIA_STATES[_jt_state].keys())
        _jt_dist  = st.selectbox("District · जिला", _jt_dists,
                                  index=_jt_dists.index("Jammu") if "Jammu" in _jt_dists else 0,
                                  key="jt_dist")
    _jt_coords = INDIA_STATES[_jt_state][_jt_dist]
    jt_lat, jt_lon = _jt_coords[0], _jt_coords[1]
    jt_loc = f"{_jt_dist}, {_jt_state}"

    # ── Year-range selector ──────────────────────────────────────
    st.markdown('<div class="styled-div"><span>SELECT YEAR RANGE FOR BIRTHDAY CALENDAR · जन्म तिथि कैलेंडर वर्ष</span></div>', unsafe_allow_html=True)
    yr_col1, yr_col2, yr_col3 = st.columns([1, 1, 2])
    with yr_col1:
        yr_from = st.selectbox(
            "From Year · वर्ष से",
            YEAR_RANGE,
            index=YEAR_RANGE.index(today.year),
            key="jt_yr_from",
        )
    with yr_col2:
        yr_to = st.selectbox(
            "To Year · वर्ष तक",
            YEAR_RANGE,
            index=min(YEAR_RANGE.index(today.year) + 4, 100),
            key="jt_yr_to",
        )
    with yr_col3:
        pass  # search is always Masa + Tithi; nakshatra shown as info only

    do_bday = st.button(" Find Janma Tithī Calendar · जन्म तिथि कैलेंडर खोजें", key="jt_calc")

    if do_bday:
        if yr_from > yr_to:
            st.warning("'From Year' must be ≤ 'To Year'.")
        elif (yr_to - yr_from) > 20:
            st.warning("Please limit range to 20 years or fewer for faster results.")
        else:
            try:
                bh, bm_val = b_time.hour, b_time.minute
                birth_data  = _cached_nakshatra(b_dob, jt_lat, jt_lon, bh, bm_val)
                birth_panch = _cached_panchang(b_dob, jt_lat, jt_lon)
                birth_sv    = samvat_year(b_dob)

                # Masa and tithi come from birth_data (exact birth JD), not birth_panch
                # (which uses sunrise JD and can give a different masa near month boundaries)
                target_masa      = birth_data["masa"]            # e.g. "Shravana"
                target_tithi     = birth_data["tithi_num"]       # 1–30
                target_nakshatra = birth_data["nakshatra"]       # e.g. "Rohini"

                birth_masa_deva  = MASA_DEVA.get(target_masa, target_masa)
                birth_masa_adhik = birth_data.get("is_adhik", False)
                birth_masa_label = f"{'Adhika ' if birth_masa_adhik else ''}{target_masa}"
                birth_masa_hi    = f"{'अधिक ' if birth_masa_adhik else ''}{birth_masa_deva}"

                # ── Birth snapshot (7 cells) ───────────────────────────
                st.markdown('<div class="subsec">JANMA VIVARA​ṆA · जन्म विवरण <span class="deva">जन्म का पंचांग</span></div>', unsafe_allow_html=True)
                bc = st.columns(7)
                bc[0].markdown(panch_cell("JANMA MĀSA", "जन्म मास",
                    birth_masa_label, birth_masa_hi), unsafe_allow_html=True)
                bc[1].markdown(panch_cell("JANMA NAKṢATRA", "जन्म नक्षत्र",
                    birth_data["nakshatra"], f"Pāda {birth_data['nakshatra_pada']}"), unsafe_allow_html=True)
                bc[2].markdown(panch_cell("JANMA TITHI", "जन्म तिथि",
                    f"{birth_data['paksha']} {birth_data['tithi']}",
                    f"#{birth_data['tithi_num']} · ends {birth_data.get('tithi_end','')}"), unsafe_allow_html=True)
                bc[3].markdown(panch_cell("CHANDRA RĀŚI", "जन्म राशि",
                    birth_data["moon_rashi"], ""), unsafe_allow_html=True)
                bc[4].markdown(panch_cell("SŪRYA RĀŚI", "सूर्य राशि",
                    birth_data["sun_rashi"], ""), unsafe_allow_html=True)
                bc[5].markdown(panch_cell("LAGNA RĀŚI", "लग्न राशि",
                    birth_data["lagna_rashi"], ""), unsafe_allow_html=True)
                bc[6].markdown(panch_cell("VIKRAMA SAṂVAT", "जन्म संवत",
                    str(birth_sv), ""), unsafe_allow_html=True)

                # ── Search all matching years ───────────────────────────
                # Strategy: for each year scan the full year in 13-day steps to find
                # days where masa == target_masa, build a fine window covering those
                # masa days, then within that window find the best tithi/nakshatra match.
                # This respects the Amāvasyānta rule: match must fall in the correct masa.
                sv_from = samvat_year(date(yr_from, 4, 1))
                sv_to   = samvat_year(date(yr_to,   4, 1))
                st.markdown(
                    f'<div class="styled-div"><span>JANMA TITHĪ CALENDAR · जन्म तिथि कैलेंडर · '
                    f'{yr_from}–{yr_to} CE &nbsp;·&nbsp; Vikrama Saṃvat {sv_from}–{sv_to}</span></div>',
                    unsafe_allow_html=True,
                )

                results_found = 0
                with st.spinner(f"Scanning {yr_from}–{yr_to}…"):
                    for yr in range(yr_from, yr_to + 1):
                        # Extend search window slightly beyond calendar year to catch
                        # masa windows that straddle Jan 1 or Dec 31.
                        search_start = date(yr, 1, 1) - timedelta(days=32)
                        search_end   = date(yr, 12, 31) + timedelta(days=32)
                        cal_start    = date(yr, 1, 1)
                        cal_end      = date(yr, 12, 31)
                        COARSE_STEP  = 13

                        # Pass 1 — coarse scan: collect dates in target masa
                        masa_dates = []
                        probe = search_start
                        while probe <= search_end:
                            try:
                                pp = _cached_panchang(probe, jt_lat, jt_lon)
                                if pp["masa"] == target_masa:
                                    masa_dates.append(probe)
                            except Exception:
                                pass
                            probe += timedelta(days=COARSE_STEP)

                        if not masa_dates:
                            continue  # masa doesn't occur this year (rare in adhik years)

                        # Pass 2 — expand each coarse masa hit ±15 days, deduplicate,
                        # restrict to the target masa, and only keep days in calendar year
                        fine_dates = set()
                        for c in masa_dates:
                            for delta in range(-15, 16):
                                d = c + timedelta(days=delta)
                                if cal_start <= d <= cal_end:
                                    fine_dates.add(d)

                        # Filter to only days actually in the target masa
                        masa_window = []
                        for d in sorted(fine_dates):
                            try:
                                pp = _cached_panchang(d, jt_lat, jt_lon)
                                if pp["masa"] == target_masa:
                                    masa_window.append((d, pp))
                            except Exception:
                                pass

                        if not masa_window:
                            continue

                        # Pass 3 — find the day in the masa window where tithi matches.
                        # Nakshatra is shown as informational text only — not a filter.
                        best_date, best_diff, best_pp = None, 999, None
                        for d, pp in masa_window:
                            tithi_match = (pp["tithi_num"] == target_tithi)
                            diff = abs(pp["tithi_num"] - target_tithi)
                            if tithi_match and (best_date is None or diff < best_diff):
                                best_date, best_diff, best_pp = d, diff, pp
                                break  # exact tithi match, no need to continue

                        if best_date and best_pp:
                            results_found += 1
                            pp2        = best_pp
                            sv2        = samvat_year(best_date)
                            masa_d     = MASA_DEVA.get(pp2["masa"], pp2["masa"])
                            adhik2     = pp2.get("is_adhik", False)
                            masa_label2 = f"{'Adhika ' if adhik2 else ''}{pp2['masa']}"
                            masa_hi2    = f"{'अधिक ' if adhik2 else ''}{masa_d}"
                            nak_also    = (pp2["nakshatra"] == target_nakshatra)
                            nak_info    = (f' &nbsp;<span style="font-size:10px;color:var(--teal);'
                                           f'font-style:italic">· nakshatra also matches</span>'
                                           if nak_also else "")
                            st.markdown(f"""
                            <div class="bday-card">
                              <div class="bday-yr">
                                {yr} CE &nbsp;·&nbsp; Vikrama Saṃvat {sv2}
                              </div>
                              <div class="bday-date">
                                {best_date.strftime('%A')}, {best_date.day} {best_date.strftime('%B %Y')}
                              </div>
                              <div class="bday-deva">
                                {masa_label2} ({masa_hi2}) मास · {pp2['paksha']} पक्ष
                              </div>
                              <div class="bday-detail">
                                <span class="bday-hl">{pp2['paksha']} {pp2['tithi']}</span>
                                (ends&nbsp;{pp2.get('tithi_end','')})
                                &nbsp;·&nbsp; {pp2['vara']}
                                &nbsp;·&nbsp; <b>{pp2['nakshatra']}</b> Pāda&nbsp;{pp2['nakshatra_pada']}
                                (ends&nbsp;{pp2.get('nakshatra_end','')}){nak_info}
                                <br>
                                <span style="font-size:12px">
                                   Sunrise: <b>{pp2['sunrise']}</b>
                                  &nbsp;&nbsp;  Sunset: <b>{pp2['sunset']}</b>
                                  &nbsp;&nbsp;  {jt_loc}
                                </span>
                              </div>
                            </div>
                            """, unsafe_allow_html=True)

                if results_found == 0:
                    st.info(f"No match for {birth_masa_label} masa in {yr_from}–{yr_to}. "
                            "This can happen in Kshaya (suppressed) years — try adjacent years.")
                else:
                    st.caption(
                        f" Found {results_found} result(s) in {yr_from}–{yr_to} · "
                        f"All dates fall in {birth_masa_label} Māsa ({birth_masa_hi}) "
                        f"on {birth_data['paksha']} {birth_data['tithi']} (Tithi #{target_tithi}). "
                        "· nakshatra also matches = rare alignment noted in small text."
                    )

            except Exception as e:
                st.error(f"Error: {e}")
                import traceback; st.code(traceback.format_exc())

    # ── AI Jyotisha reading ──────────────────────────────────────
    st.markdown('<div class="styled-div"><span>AI JYOTIṢA READING · ज्योतिष विश्लेषण</span></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="ai-box">
      <div class="ai-lbl">ASK ABOUT YOUR BIRTH CHART · जन्म कुण्डली</div>
      <div style="margin-top:18px;text-align:center;padding:18px 0 10px">
        <div style="font-size:28px;margin-bottom:10px"></div>
        <div style="font-family:'Cinzel',serif;font-size:13px;letter-spacing:2px;
             color:#DEB85A;margin-bottom:8px">COMING IN NEXT UPDATE</div>
        <div style="font-size:14px;color:rgba(253,248,240,.65);line-height:1.8;max-width:480px;margin:0 auto">
          Your wise Kashmiri Pandit — personalised reading of your Janma Nakshatra,
          Vimshottari Dasha, Rashi characteristics and spiritual significance —
          will be available in the next release.
        </div>
        <div style="font-family:'Noto Serif Devanagari',serif;font-size:12px;
             color:rgba(222,184,90,.45);margin-top:10px">
          जन्म कुण्डली विश्लेषण — शीघ्र आ रहा है
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# TAB 3 — GUNA MILAN
# ══════════════════════════════════════════════════════════════════════════════
with tabs[3]:
    st.markdown("""
    <div class="sec-head"> Guṇa Milāna · गुण मिलान</div>
    <div class="sec-sub">
      36-Guṇa (Aṣṭakoota) Vedic marriage compatibility with Maṅgala Doṣa check · Gotra verification
      <span class="deva">अष्टकूट मिलान · मंगल दोष · गोत्र परीक्षा · कश्मीरी पण्डित विवाह परम्परा</span>
    </div>
    """, unsafe_allow_html=True)

    # ── Input columns ─────────────────────────────────────────────
    boy_col, gap_col, girl_col = st.columns([5, 0.3, 5])

    with boy_col:
        st.markdown("""
        <div style="font-family:'Cinzel',serif;color:var(--teal);font-size:12px;
             letter-spacing:1.5px;margin-bottom:12px;border-bottom:1px solid var(--border);padding-bottom:8px">
           VARA · वर — GROOM
        </div>""", unsafe_allow_html=True)
        b_dob2 = st.date_input("Date of Birth · जन्म तिथि", value=date(1995, 6, 15), key="gm_b_dob")
        bc1, bc2 = st.columns(2)
        b_hour = bc1.number_input("Birth Hour (0–23)", 0, 23, 6, key="gm_b_hour")
        b_min2 = bc2.number_input("Birth Min (0–59)", 0, 59, 0, key="gm_b_min")
        b_lat2, b_lon2, b_loc2 = state_district_selects("gm_b", default_dist="Jammu")
        st.markdown('<div style="margin-top:10px;font-family:Cinzel,serif;font-size:9px;color:var(--saffron);letter-spacing:1.5px;opacity:.8">OPTIONAL · वैकल्पिक</div>', unsafe_allow_html=True)
        b_nak_known = st.checkbox("Nakshatra known? · नक्षत्र ज्ञात है?", key="gm_b_nak_k")
        b_nak_manual = st.selectbox("Nakshatra · नक्षत्र", NAKSHATRA_NAMES, key="gm_b_nak_m") if b_nak_known else None
        b_gotra = st.selectbox("Gotra · गोत्र", ["— Select —"] + GOTRAS, key="gm_b_gotra")

    with gap_col:
        st.markdown('<div style="border-left:1px solid var(--border);height:100%;min-height:420px"></div>', unsafe_allow_html=True)

    with girl_col:
        st.markdown("""
        <div style="font-family:'Cinzel',serif;color:var(--lotus);font-size:12px;
             letter-spacing:1.5px;margin-bottom:12px;border-bottom:1px solid var(--border);padding-bottom:8px">
           VADHŪ · वधू — BRIDE
        </div>""", unsafe_allow_html=True)
        g_dob2 = st.date_input("Date of Birth · जन्म तिथि", value=date(1998, 3, 22), key="gm_g_dob")
        gc1, gc2 = st.columns(2)
        g_hour = gc1.number_input("Birth Hour (0–23)", 0, 23, 6, key="gm_g_hour")
        g_min2 = gc2.number_input("Birth Min (0–59)", 0, 59, 0, key="gm_g_min")
        g_lat2, g_lon2, g_loc2 = state_district_selects("gm_g", default_dist="Jammu")
        st.markdown('<div style="margin-top:10px;font-family:Cinzel,serif;font-size:9px;color:var(--saffron);letter-spacing:1.5px;opacity:.8">OPTIONAL · वैकल्पिक</div>', unsafe_allow_html=True)
        g_nak_known = st.checkbox("Nakshatra known? · नक्षत्र ज्ञात है?", key="gm_g_nak_k")
        g_nak_manual = st.selectbox("Nakshatra · नक्षत्र", NAKSHATRA_NAMES, key="gm_g_nak_m") if g_nak_known else None
        g_gotra = st.selectbox("Gotra · गोत्र", ["— Select —"] + GOTRAS, key="gm_g_gotra")

    st.markdown('<div class="lotus-div">  </div>', unsafe_allow_html=True)
    _, mid_btn, _ = st.columns([3, 2, 3])
    with mid_btn:
        do_match = st.button(" Calculate Guṇa Milāna · गुण मिलान करें", key="gm_calc")

    if do_match:
        try:
            boy_data  = _cached_nakshatra(b_dob2, b_lat2, b_lon2, int(b_hour), int(b_min2))
            girl_data = _cached_nakshatra(g_dob2, g_lat2, g_lon2, int(g_hour), int(g_min2))

            b_nak = b_nak_manual if b_nak_manual else boy_data["nakshatra"]
            g_nak = g_nak_manual if g_nak_manual else girl_data["nakshatra"]
            b_gotra_v = b_gotra if b_gotra != "— Select —" else ""
            g_gotra_v = g_gotra if g_gotra != "— Select —" else ""

            # ── Nakshatra summary ─────────────────────────────────
            st.markdown('<div class="subsec">JANMA NAKṢATRA · जन्म नक्षत्र</div>', unsafe_allow_html=True)
            ns1, ns2 = st.columns(2)
            ns1.markdown(f"""
            <div class="panch-cell" style="text-align:left;padding:16px 20px">
              <span class="pc-lbl"> VARA · वर — GROOM</span>
              <div class="pc-val-big" style="margin:8px 0">{b_nak}</div>
              <div style="font-size:13px;color:var(--muted)">
                Moon: {boy_data['moon_rashi']} &nbsp;·&nbsp; Lagna: {boy_data['lagna_rashi']}
                {f" &nbsp;·&nbsp; Gotra: {b_gotra_v}" if b_gotra_v else ""}
              </div>
            </div>""", unsafe_allow_html=True)
            ns2.markdown(f"""
            <div class="panch-cell" style="text-align:left;padding:16px 20px">
              <span class="pc-lbl"> VADHŪ · वधू — BRIDE</span>
              <div class="pc-val-big" style="margin:8px 0">{g_nak}</div>
              <div style="font-size:13px;color:var(--muted)">
                Moon: {girl_data['moon_rashi']} &nbsp;·&nbsp; Lagna: {girl_data['lagna_rashi']}
                {f" &nbsp;·&nbsp; Gotra: {g_gotra_v}" if g_gotra_v else ""}
              </div>
            </div>""", unsafe_allow_html=True)

            # ── 36 Gunas ─────────────────────────────────────────
            result = _cached_gunas(b_nak, g_nak, b_gotra_v, g_gotra_v)
            score = result["total"]
            pct = result["percentage"]

            score_color = "#4CAF50" if pct >= 75 else "var(--saffron)" if pct >= 50 else "#e53935"

            st.markdown('<div class="subsec">ṢAṬTRIṂŚAT GUṆA MILĀPA · 36 गुण मिलान <span class="deva">अष्टकूट विश्लेषण</span></div>', unsafe_allow_html=True)

            score_col, detail_col = st.columns([1, 2])
            with score_col:
                st.markdown(f"""
                <div class="score-wrap">
                  <div class="score-circle" style="border-color:{score_color};box-shadow:0 0 30px {score_color}30">
                    <div class="score-num" style="color:{score_color}">{score}</div>
                    <div class="score-den">/ 36</div>
                  </div>
                  <div class="score-rec" style="color:{score_color}">{result['recommendation']}</div>
                  {f'<div style="margin-top:10px;font-size:13px;color:var(--muted)">{result["gotra_note"]}</div>' if result.get("gotra_note") else ''}
                  <div class="score-bar">
                    <div style="position:absolute;width:18px;height:18px;border-radius:50%;
                         background:white;border:3px solid var(--walnut);top:-4px;
                         left:{pct}%;transform:translateX(-50%)"></div>
                  </div>
                  <div style="font-size:12px;color:var(--muted)">{pct:.0f}% compatibility</div>
                </div>
                """, unsafe_allow_html=True)

            with detail_col:
                st.markdown("".join(guna_row_html(k, v) for k, v in result["details"].items()), unsafe_allow_html=True)

            # ── Mangalik — compute once, reuse for display + note + AI report ──
            b_mg = _cached_mangalik(b_dob2, b_lat2, b_lon2, int(b_hour), int(b_min2))
            g_mg = _cached_mangalik(g_dob2, g_lat2, g_lon2, int(g_hour), int(g_min2))

            st.markdown('<div class="subsec">MAṄGALA DOṢA · मंगल दोष <span class="deva">D1 · Moon Chart · D9 (Navāṃśa)</span></div>', unsafe_allow_html=True)
            mc1, mc2 = st.columns(2)
            for col, (mg, lbl, lbl_deva) in zip(
                [mc1, mc2],
                [
                    (b_mg, " Vara (Groom)", "वर"),
                    (g_mg, " Vadhū (Bride)", "वधू"),
                ]
            ):
                with col:
                    try:
                        badge_cls = (
                            "badge-man-yes"  if mg["is_mangalik"] and mg["mangalik_count"] >= 2
                            else "badge-man-mild" if mg["is_mangalik"]
                            else "badge-man-no"
                        )
                        cancels_html = ""
                        if mg["cancellations"]:
                            cancels_html = "".join(f'<div style="font-size:11px;color:#a5d6a7;margin-top:2px"> {c}</div>' for c in mg["cancellations"])
                        st.markdown(f"""
                        <div class="panch-cell" style="text-align:left;padding:16px 20px">
                          <span class="pc-lbl">{lbl} · {lbl_deva}</span>
                          <div style="margin:8px 0">
                            <span class="badge {badge_cls}">{mg['severity']}</span>
                          </div>
                          <div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:8px">
                            <span style="font-size:12px;padding:2px 8px;border-radius:4px;
                                  background:{'rgba(229,57,53,.15)' if mg['d1_mangalik'] else 'rgba(76,175,80,.12)'};
                                  border:1px solid {'#e5393550' if mg['d1_mangalik'] else '#4caf5050'}">
                              D1: H{mg['d1_house']} {'' if mg['d1_mangalik'] else ''}
                            </span>
                            <span style="font-size:12px;padding:2px 8px;border-radius:4px;
                                  background:{'rgba(229,57,53,.15)' if mg['moon_chart_mangalik'] else 'rgba(76,175,80,.12)'};
                                  border:1px solid {'#e5393550' if mg['moon_chart_mangalik'] else '#4caf5050'}">
                              Moon: H{mg['moon_chart_house']} {'' if mg['moon_chart_mangalik'] else ''}
                            </span>
                            <span style="font-size:12px;padding:2px 8px;border-radius:4px;
                                  background:{'rgba(229,57,53,.15)' if mg['d9_mangalik'] else 'rgba(76,175,80,.12)'};
                                  border:1px solid {'#e5393550' if mg['d9_mangalik'] else '#4caf5050'}">
                              D9: H{mg['d9_house']} {'' if mg['d9_mangalik'] else ''}
                            </span>
                          </div>
                          <div style="font-size:11px;margin-top:6px;color:var(--muted)">
                            Lagna: {mg['asc_rashi']} &nbsp;·&nbsp; Moon: {mg['moon_rashi']}
                          </div>
                          {cancels_html}
                        </div>
                        """, unsafe_allow_html=True)
                    except Exception as me:
                        col.error(f"Mangalik error: {me}")

            # Mangalik compatibility note
            same = b_mg["is_mangalik"] == g_mg["is_mangalik"]
            st.markdown(f"""
            <div class="muh-block {'good' if same else 'bad'}" style="margin-top:12px">
              <div class="muh-time">{' Both same Mangalik status — Compatible' if same else ' Different Mangalik status — Remedies recommended'}</div>
            </div>
            """, unsafe_allow_html=True)

            # ── AI Marriage Report ───────────────────────────────
            st.markdown("""
            <div class="ai-box" style="margin-top:16px">
              <div class="ai-lbl"> FULL COMPATIBILITY REPORT · विस्तृत विवाह विश्लेषण</div>
              <div style="margin-top:16px;text-align:center;padding:14px 0 8px">
                <div style="font-size:24px;margin-bottom:8px"></div>
                <div style="font-family:'Cinzel',serif;font-size:12px;letter-spacing:2px;
                     color:#DEB85A;margin-bottom:8px">COMING IN NEXT UPDATE</div>
                <div style="font-size:13.5px;color:rgba(253,248,240,.65);line-height:1.8;max-width:460px;margin:0 auto">
                  Your wise Kashmiri Pandit — full compatibility with dosha remedies,
                  auspicious wedding months and KP-specific guidance —
                  available in the next release.
                </div>
                <div style="font-family:'Noto Serif Devanagari',serif;font-size:11px;
                     color:rgba(222,184,90,.4);margin-top:8px">
                  विस्तृत विवाह विश्लेषण — शीघ्र आ रहा है
                </div>
              </div>
            </div>
            """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Matching error: {e}")
            import traceback; st.code(traceback.format_exc())


# ══════════════════════════════════════════════════════════════════════════════
# TAB 4 — LINEAGE
# ══════════════════════════════════════════════════════════════════════════════
with tabs[4]:
    st.markdown("""
    <div class="sec-head"> Kul Paramparā · कुल परम्परा</div>
    <div class="sec-sub">
      Trace your Kashmiri Pandit lineage — Gotra, Kul Devī, Kul Devatā, Bhairava
      <span class="deva">गोत्र · कुल देवी · कुल देवता · भैरव · ग्राम देवता</span>
    </div>
    """, unsafe_allow_html=True)

    _d1, _d2, _d3, _d4 = st.columns(4)
    with _d1:
        lin_district = st.selectbox(
            "District in Kashmir · जिला",
            KP_DISTRICTS,
            key="lin_dist",
        )
    with _d2:
        _towns = KP_TOWNS.get(lin_district, ["— Select town first —"])
        lin_town = st.selectbox(
            "Town / Mohalla · नगर",
            _towns,
            key="lin_town",
        )
    with _d3:
        _villages = KP_VILLAGES.get(lin_town, [lin_town])
        lin_village = st.selectbox(
            "Village / Mauza · गाँव",
            _villages,
            key="lin_vill",
        )
    with _d4:
        lin_surname = st.selectbox(
            "Family Surname · कुल नाम (Optional)",
            KP_SURNAMES,
            key="lin_name",
        )

    do_lin = st.button(" Trace Kul · कुल खोजें", key="lin_calc")

    if do_lin:
        surname_val = lin_surname if lin_surname != "— Optional —" else ""
        _result_title = lin_village
        if lin_town and lin_town != lin_village:
            _result_title += f", {lin_town}"
        _result_title += f", {lin_district}"

        st.markdown(f'<div class="subsec" style="margin-top:18px">VAṂŚA VIVARA​ṆA · वंश विवरण — {_result_title}</div>', unsafe_allow_html=True)

        # ── Tentative disclaimer ──────────────────────────────────
        st.markdown("""
        <div style="background:rgba(212,114,42,.08);border:1px solid rgba(212,114,42,.35);
             border-left:4px solid var(--saffron);border-radius:8px;padding:12px 18px;
             margin-bottom:18px;font-size:13px;color:var(--walnut-mid);line-height:1.7">
          <span style="font-family:Cinzel,serif;font-size:9px;letter-spacing:2px;
                color:var(--saffron);display:block;margin-bottom:4px">DISCLAIMER · सूचना</span>
           <b>Tentative information</b> — Also need to verify with a Pandit of the region
          for all the data shared below.
          यह जानकारी अनुमानित है। कृपया इसे स्थानीय पण्डित से भी सत्यापित करें।
        </div>
        """, unsafe_allow_html=True)

        lin_r1, lin_r2 = st.columns(2)

        # ── Kul Devi ─────────────────────────────────────────────
        kd = KUL_DEVI_BY_DISTRICT.get(lin_district, {})
        with lin_r1:
            st.markdown(f"""
            <div class="lin-item">
              <div class="lin-icon"></div>
              <div>
                <div class="lin-lbl">KUL DEVĪ · कुल देवी</div>
                <div class="lin-val">{kd.get('primary', 'Sharika Devi / Ragnya Devi')}</div>
                <div class="lin-desc"> {kd.get('temple', '—')}</div>
                <div class="lin-desc">{kd.get('notes', '')}</div>
                {"<div class='lin-desc'>Also: " + ", ".join(kd.get('also', [])) + "</div>" if kd.get('also') else ""}
              </div>
            </div>
            """, unsafe_allow_html=True)

        # ── Kul Devta ────────────────────────────────────────────
        kt = KUL_DEVTA_BY_DISTRICT.get(lin_district, {})
        with lin_r2:
            st.markdown(f"""
            <div class="lin-item">
              <div class="lin-icon"></div>
              <div>
                <div class="lin-lbl">KUL DEVATĀ · कुल देवता</div>
                <div class="lin-val">{kt.get('primary', 'Shiva')}</div>
                <div class="lin-desc"> {kt.get('temple', '—')}</div>
                <div class="lin-desc">{kt.get('notes', '')}</div>
              </div>
            </div>
            """, unsafe_allow_html=True)

        # ── Bhairava (Ashta + Local matching district/town) ──────
        st.markdown('<div class="subsec" style="margin-top:14px">BHAIRAVA · भैरव <span class="deva">क्षेत्रपाल</span></div>', unsafe_allow_html=True)

        # Find relevant Ashta Bhairavas for the selected town
        town_lower = lin_town.lower()
        district_lower = lin_district.lower()
        relevant_ashta = [b for b in ASHTA_BHAIRAVAS
                          if any(w in b["region"].lower() for w in town_lower.split()
                                 if len(w) > 3)
                          or any(w in b["region"].lower() for w in district_lower.split()
                                 if len(w) > 3)]
        # Always show all 8 with relevant ones highlighted
        bh_cols = st.columns(2)
        for i, b in enumerate(ASHTA_BHAIRAVAS):
            is_relevant = b in relevant_ashta
            highlight = "border-left:3px solid var(--saffron);" if is_relevant else ""
            bh_cols[i % 2].markdown(f"""
            <div class="muh-block" style="margin-bottom:7px;{highlight}">
              <div class="muh-lbl">{b['direction']} · {b['region']}</div>
              <div class="muh-time" style="font-size:14px">{b['name']}</div>
              <div class="muh-note">{b['notes']}</div>
            </div>
            """, unsafe_allow_html=True)

        # Local Bhairavas
        st.markdown('<div style="font-family:Cinzel,serif;font-size:9px;letter-spacing:2px;color:var(--muted);margin:14px 0 8px">LOCAL BHAIRAVAS · स्थानीय भैरव</div>', unsafe_allow_html=True)
        lb_cols = st.columns(2)
        for i, b in enumerate(LOCAL_BHAIRAVAS):
            is_relevant = (lin_district.lower() in b["region"].lower()
                           or lin_town.lower() in b["region"].lower()
                           or any(w in b["region"].lower()
                                  for w in lin_town.lower().split() if len(w) > 3))
            highlight = "border-left:3px solid var(--saffron);" if is_relevant else ""
            lb_cols[i % 2].markdown(f"""
            <div class="muh-block" style="margin-bottom:7px;{highlight}">
              <div class="muh-lbl">{b['region']}</div>
              <div class="muh-time" style="font-size:14px">{b['name']}</div>
              <div class="muh-note">{b['notes']}</div>
            </div>
            """, unsafe_allow_html=True)

        # ── Gotra (from selected surname only) ───────────────────
        st.markdown('<div class="subsec" style="margin-top:14px">GOTRA · गोत्र <span class="deva">सप्तर्षि वंश</span></div>', unsafe_allow_html=True)

        # Look up gotras directly from SURNAME_GOTRA_MAP using the selected surname
        gotras_for_surname = []
        if surname_val:
            # Exact match first
            gotras_for_surname = SURNAME_GOTRA_MAP.get(surname_val, [])
            # If no exact match, try case-insensitive
            if not gotras_for_surname:
                for key, val in SURNAME_GOTRA_MAP.items():
                    if key.lower() == surname_val.lower():
                        gotras_for_surname = val
                        break

        if surname_val and gotras_for_surname:
            gt_cols = st.columns(len(gotras_for_surname)) if len(gotras_for_surname) <= 4 else st.columns(4)
            for i, gotra in enumerate(gotras_for_surname):
                gt_cols[i % len(gt_cols)].markdown(f"""
                <div class="panch-cell" style="text-align:center;padding:18px 14px">
                  <span class="pc-lbl">GOTRA FOR {surname_val.upper()}</span>
                  <div class="pc-val-big" style="margin:10px 0;font-size:20px">{gotra}</div>
                </div>
                """, unsafe_allow_html=True)
        elif surname_val and not gotras_for_surname:
            st.markdown(f"""
            <div style="font-size:13px;color:var(--muted);font-style:italic;padding:10px 0">
              Gotra for <b>{surname_val}</b> not found in our current table.
              Please verify with a Pandit of your region.
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="font-size:13px;color:var(--muted);font-style:italic;padding:10px 0">
              Select a family surname above to see the possible Gotra(s).
            </div>
            """, unsafe_allow_html=True)

    # Info cards
    st.markdown('<div class="styled-div"><span>ABOUT KASHMIRI PANDIT LINEAGE</span></div>', unsafe_allow_html=True)
    ic1, ic2, ic3 = st.columns(3)
    ic1.markdown("""<div class="info-card">
      <div class="ic-icon"></div>
      <div class="ic-title">GOTRA · गोत्र</div>
      <div class="ic-body">Patrilineal Vedic clan traced to one of the Sapta Rishis. 
      Gotras determine marriageability — same-gotra marriage is strictly forbidden in KP tradition 
      (sagotra vivaha varjya).</div>
    </div>""", unsafe_allow_html=True)
    ic2.markdown("""<div class="info-card">
      <div class="ic-icon"></div>
      <div class="ic-title">KUL DEVĪ · कुल देवी</div>
      <div class="ic-body">Family goddess, distinct for each district cluster of Kashmir. 
      Major Kul Devis: Sharika (Hari Parbat), Ragnya/Kheer Bhawani (Tulmul), 
      Jwala (Khrew), Bhadrakali. Worshipped at all family ceremonies.</div>
    </div>""", unsafe_allow_html=True)
    ic3.markdown("""<div class="info-card">
      <div class="ic-icon"></div>
      <div class="ic-title">BHAIRAVA · भैरव</div>
      <div class="ic-body">Village or mohalla-specific protective deity in the Trika tradition 
      of Kashmir Shaivism. The eight Bhairavas (Ashtabhairava) guard the eight directions 
      of the sacred landscape.</div>
    </div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# TAB 5 — SHASTRA
# ══════════════════════════════════════════════════════════════════════════════
with tabs[5]:
    st.markdown("""
    <div class="sec-head"> Kāśmīrī Śāstra · कश्मीरी शास्त्र</div>
    <div class="sec-sub">
      Complete library of Kashmir Shaivism, Trika philosophy, classical texts, saints and cultural heritage
      <span class="deva">त्रिक दर्शन · काश्मीर शैव दर्शन · ग्रन्थ · संत · संस्कृति · सम्पूर्ण ग्रन्थालय</span>
    </div>
    """, unsafe_allow_html=True)

    # ── Static data: all texts, traditions, authors ───────────────
    # Order: Saints first, then Lal Ded, then Culture, then texts
    SHASTRA_DATA = {
        "Kashmiri Saints · कश्मीरी संत": [
            {
                "title": "Lalleshwari / Lal Ded · ललद्यद (c. 1320–1392 CE)",
                "author": "Lalleshwari (born Lalla)",
                "period": "c. 1320–1392 CE — 14th century, Kashmir",
                "desc": (
                    "The mother of all Kashmiri mysticism and the first great poet of the Kashmiri language. "
                    "Born in Pandrethan village near Srinagar into a KP Brahmin family, married young into "
                    "a harsh household, she was initiated by Shaiva guru Siddha Shrikantha Swami. "
                    "She renounced home and wandered Kashmir as a naked ascetic (digambari), singing her "
                    "immortal Vakhs. Her 258+ Vakhs in Old Kashmiri are the oldest surviving literature "
                    "in the Kashmiri language. Core teaching: Shivoham — 'I am Shiva'. "
                    "Revered by Hindus as Lalla Yogeshwari and by Muslims as Lal Arifa — unique in Indian history. "
                    "Three celebrated Vakhs: "
                    "(1) 'Shiv chuy thali thali rozaan / mozan nay Hindav, na Musalmaan' — Shiva pervades everywhere; do not distinguish Hindu from Muslim. "
                    "(2) 'Lalle shiv chuy, na tyag na grev' — Shiva is in you; neither renounce nor grab. "
                    "(3) 'Pranas apanas milawath karim / Shiv Shakti akh chu, beyi nay beyi' — When prana and apana unite, Shiva and Shakti are one; there is no other, no other. "
                    "Philosophical tradition: Pratyabhijña (recognition of Self as Shiva), Spanda (divine vibration), "
                    "and elements of Hatha Yoga. Her guru Siddha Shrikantha was a master of the Trika school. "
                    "Legacy: Influenced all subsequent Kashmiri poetry — Nund Rishi, Habba Khatoon, Rupa Bhawani. "
                    "Academic works: Jayalal Kaul's 'Lal Ded' (Sahitya Akademi), Ranjit Hoskote's 'I, Lalla'."
                ),
                "tradition": "Kashmir Shaivism / Pratyabhijña / Trika",
                "link": "https://en.wikipedia.org/wiki/Lalleshwari",
                "archive": "https://archive.org/search?query=lal+ded+lalleshwari+vakhs+kashmir",
            },
            {
                "title": "Mata Sharada · माता शारदा (Saraswati of Kashmir)",
                "author": "Divine — Sharada Devi (presiding goddess of Kashmir)",
                "period": "Ancient — Vedic to present",
                "desc": (
                    "Sharada Devi is the presiding goddess of the entire Kashmir Valley — "
                    "Devi of learning, wisdom, music, arts and the sacred word. "
                    "Her principal seat: Sharada Peeth at Sharda village, Neelum Valley "
                    "(now in Pakistan-administered Kashmir). One of the 18 Maha Shakti Pithas — "
                    "Sati's right hand is said to have fallen here. "
                    "The Kashmiri script (Sharada lipi) is named after her — all KP manuscripts, "
                    "horoscopes and religious texts were written in Sharada script for centuries. "
                    "Kashmiri Pandits invoke her at all beginnings: 'Ya Sharada nilotpala-dala-shyama' "
                    "(the Sharada Stotram — she is described as blue as the blue lotus petal). "
                    "The Nilamata Purana describes her as the Vak (speech) of the valley. "
                    "Sharada Peeth held one of India's greatest ancient libraries and universities — "
                    "Adi Shankaracharya is said to have visited and debated here. "
                    "Key texts: Sharada Stotram, Saraswati Sahasranama, Devi Mahatmya (read in KP homes). "
                    "Annual virtual puja by KPs worldwide on Sharada Navami. "
                    "Campaign for restoration of access: Sharda Peeth Trust (India)."
                ),
                "tradition": "Kashmir Shakta / Saraswati / Shakti Pitha tradition",
                "link": "https://en.wikipedia.org/wiki/Sharada_Peeth",
                "archive": "https://archive.org/search?query=sharada+peeth+kashmir+saraswati",
            },
            {
                "title": "Devi Roop Bhawani · देवी रूपा भवानी (1625–1721 CE)",
                "author": "Rupa Bhawani (born Alakeshwari, daughter of Madhav Joo Dhar)",
                "period": "1625–1721 CE — 17th–18th century, Srinagar",
                "desc": (
                    "Mystic poetess, Shakti saint and living embodiment of Kashmir Shaivism. "
                    "Born in Srinagar to Pandit Madhav Joo Dhar (Dhar gotra, Vasishtha lineage). "
                    "Married Pandit Prana Koul but renounced household life for Shiva-sadhana. "
                    "Considered a Shakti incarnation — tradition holds she manifested miraculous powers. "
                    "Her shrine: Fateh Kadal, Srinagar (Rupa Bhawani Mandir) — active KP pilgrimage site. "
                    "Second shrine: Rainawari, Srinagar. "
                    "Philosophical teaching: body as temple of Shiva-Shakti, non-duality in bhakti. "
                    "Key Vakh: 'Zaan tse Aham Brahmasmi / Yeli che nab nab Suyii' — "
                    "Know thyself as Brahman; when the sky is sky, that alone is. "
                    "Works: Vakhs of Rupa Bhawani — collected oral verses in Kashmiri, "
                    "some compiled in 'Vakhs of Rupa Bhawani' (KP community publications). "
                    "Festivals: Her birth anniversary (Rupa Bhawani Jayanti) observed by KPs. "
                    "Academic reference: 'The Mystic Poetesses of Kashmir' — various scholars."
                ),
                "tradition": "Kashmir Shaivism / Shakta / Bhakti",
                "link": "https://en.wikipedia.org/wiki/Rupa_Bhawani",
                "archive": "https://archive.org/search?query=rupa+bhawani+vakhs+kashmir+shaivism",
            },
            {
                "title": "Mata Vatasta · माता वितस्ता (River Goddess Vitasta)",
                "author": "Divine — Vitasta Devi (Jhelum river goddess)",
                "period": "Ancient — Rigvedic to present",
                "desc": (
                    "Vitasta (the river Jhelum) is the sacred mother of Kashmir — "
                    "mentioned in the Rigveda (Nadistuti hymn, 10.75) as one of the great rivers of India. "
                    "The Nilamata Purana (6th–8th c.) dedicates extensive verses to her worship: "
                    "'Vitasta is the mother; she alone nourishes Kashmir.' "
                    "The valley of Kashmir was originally the lake Satisar — Vitasta drained it, "
                    "making the land habitable (Nilamata Purana mythology). "
                    "Source: Verinag spring (Anantnag district) — a beautiful octagonal Mughal-era "
                    "spring that is one of Kashmir's holiest sites. "
                    "KP rituals: Vitasta Jayanti is observed annually. Shraddha rites are performed "
                    "on the banks of the Vitasta. Water from Vitasta is used in all major KP rituals. "
                    "The Vitasta Stotram (from Nilamata Purana) is recited by KP priests. "
                    "Reference: Nilamata Purana (translated by Ved Kumari Ghai, JKAAS publication)."
                ),
                "tradition": "Kashmiri river-goddess worship / Nilamata Purana / Shakta",
                "link": "https://en.wikipedia.org/wiki/Jhelum_River",
                "archive": "https://www.wisdomlib.org/hinduism/book/nilamata-purana",
            },
            {
                "title": "Bhagwan Gopinath Ji · भगवान गोपीनाथ जी (1898–1968 CE)",
                "author": "Bhagwan Gopinath (born Gopinath Bhat)",
                "period": "1898–1968 CE — Srinagar",
                "desc": (
                    "One of the most beloved modern KP saints and a direct embodiment of Kashmir Shaivism. "
                    "Born 1898 in Rainawari, Srinagar, to a KP Brahmin family. "
                    "From childhood he entered spontaneous samadhi states — neighbours found him motionless "
                    "for hours in deep consciousness. Never accepted formal disciples; lived in complete simplicity. "
                    "Known for miraculous healings, clairvoyance, and a radiant presence that transformed all who met him. "
                    "His teaching was wordless — his very presence was the teaching (shaktipat by darshan). "
                    "Deep connection with Lal Ded's tradition — he embodied 'Pratyabhijña' as direct recognition, not philosophy. "
                    "Swami Lakshman Joo was his contemporary and they were mutually reverential. "
                    "Shrine: Rainawari, Srinagar — active pilgrimage site for KPs worldwide. "
                    "Annual: Gopinath Jayanti celebrated by KP community. "
                    "Books: 'Bhagwan Gopinath: The Divine Flame' (devotees' accounts, KP Sabha publications), "
                    "'Saintly Saga of Bhagwan Gopinath' — anecdote collections by devotees. "
                    "Website: gopinathji.com (devotee resource)."
                ),
                "tradition": "Kashmir Shaivism / Pratyabhijña / living saint tradition",
                "link": "https://en.wikipedia.org/wiki/Bhagwan_Gopinath",
                "archive": "https://archive.org/search?query=bhagwan+gopinath+kashmir+saint",
            },
            {
                "title": "Swami Merza Kak Ji · स्वामी मेर्ज़ा कक जी",
                "author": "Swami Merza Kak Ji",
                "period": "19th–20th century CE — Srinagar",
                "desc": (
                    "Revered Kashmiri Pandit saint from the Kak lineage (Jamadagni gotra). "
                    "A Shaiva Swami in the Trika-Pratyabhijña tradition of Kashmir Shaivism. "
                    "Known for intense tapas (austerity), mastery of Shaiva mantras and the "
                    "ability to guide lay devotees through complex ritual and philosophical questions. "
                    "The Kak family has ancient associations with Shaiva priesthood and the "
                    "Datthtreya gotra tradition. His teachings drew on the Shiva Sutras of Vasugupta, "
                    "the Spanda Karikas, and the oral Vakh tradition of Lal Ded. "
                    "Venerated locally through oral family traditions and shrine worship in Srinagar. "
                    "His memory preserved in the Kak community's spiritual oral lineage."
                ),
                "tradition": "Kashmir Shaivism / Trika",
                "link": "https://en.wikipedia.org/wiki/Kashmiri_Pandits",
                "archive": "https://archive.org/search?query=kashmiri+pandit+saints+shaivism",
            },
            {
                "title": "Krishna Joo Razdan · कृष्ण जू रज़दन",
                "author": "Krishna Joo Razdan",
                "period": "19th–20th century CE — Srinagar",
                "desc": (
                    "Kashmiri Pandit saint and devotee from the illustrious Razdan lineage "
                    "(Gautama / Dhaumyayana gotra — see the Bhannamasis table). "
                    "The Razdan surname appears in 7 distinct gotra lineages in the KP tradition, "
                    "reflecting the antiquity and spread of this family. "
                    "Krishna Joo Razdan was known for deep bhakti toward Shiva and expertise in "
                    "the Kul Devi puja tradition (Kheer Bhawani / Ragnya Devi). "
                    "A practitioner of the Kashmir Shaiva path, he guided KP families in Srinagar "
                    "through ritual, mantra and philosophical instruction rooted in Pratyabhijña. "
                    "His teachings emphasised the unity of Shiva-consciousness in every act of daily life. "
                    "Venerated particularly by the Razdan community of old-city Srinagar."
                ),
                "tradition": "Kashmir Shaivism / KP devotional tradition",
                "link": "https://en.wikipedia.org/wiki/Kashmiri_Pandits",
                "archive": "",
            },
            {
                "title": "Laxman Joo Razdan · लक्ष्मण जू रज़दन",
                "author": "Laxman Joo Razdan",
                "period": "19th–20th century CE — Srinagar",
                "desc": (
                    "Kashmiri Pandit saint from the Razdan family — closely related in lineage to Krishna Joo Razdan, "
                    "likely from the same extended family tradition. "
                    "Note: Not to be confused with Swami Lakshmanjoo (the academic master); this is a separate "
                    "figure in the KP devotional saint tradition. "
                    "Known for austere sadhana, deep knowledge of Shaiva mantras and puja vidhi, "
                    "and oral transmission of the Lal Ded Vakh tradition within the Razdan community. "
                    "His spiritual lineage connects the Razdan family's Gautama/Dhaumyayana gotra tradition "
                    "with the living Pratyabhijña practice of Kashmir Shaivism. "
                    "Venerated for his blessings at family ceremonies — particularly Herath, Navreh and Janmashtami."
                ),
                "tradition": "Kashmir Shaivism / KP devotional tradition",
                "link": "https://en.wikipedia.org/wiki/Kashmiri_Pandits",
                "archive": "",
            },
            {
                "title": "Kash Kak Ji · काश कक जी",
                "author": "Kash Kak Ji",
                "period": "19th–20th century CE — Srinagar",
                "desc": (
                    "Revered saint from the Kak lineage of Kashmiri Pandits (Jamadagni gotra). "
                    "Known as a Siddha (perfected being) in the Kashmir Shaiva tradition — "
                    "his spiritual powers and compassionate guidance made him a sought-after figure "
                    "across the Srinagar KP community. "
                    "The name 'Kash' relates to the root 'Kash' (to shine) — an auspicious Kashmiri name "
                    "connected to Kashmir itself (Ka = Brahma, Shmir = to dry = the dried lake Satisar). "
                    "His sadhana path: intense Shiva-mantra japa, Kul Devi puja and the Herath Vatak ritual. "
                    "The Kak family's Datthtreya gotra tradition (from the Bhannamasis table) is one of the "
                    "most prominent in the KP priestly lineage. Memory preserved in Kak family oral traditions "
                    "and at local Srinagar shrines."
                ),
                "tradition": "Kashmir Shaivism / Siddha tradition",
                "link": "https://en.wikipedia.org/wiki/Kashmiri_Pandits",
                "archive": "",
            },
            {
                "title": "Kral Bab Ji · क्राल बाब जी",
                "author": "Kral Bab Ji",
                "period": "19th–20th century CE — Kashmir Valley",
                "desc": (
                    "Beloved KP saint known by the honorific 'Bab Ji' — a title of deep respect "
                    "given to realised masters and elder saints in Kashmir (used similarly to 'Baba'). "
                    "'Kral' in Kashmiri refers to the potter community — suggesting either artisan origins, "
                    "a village name, or metaphorical reference (the potter who shapes consciousness = Shiva). "
                    "Venerated as a Shaiva Siddha who embodied simplicity and seva (selfless service). "
                    "His teachings focused on: accessibility to all regardless of caste/standing, "
                    "direct devotion to Shiva without complex ritual, and the Lal Ded teaching that "
                    "Shiva is found within the self. "
                    "Known for miraculous deeds (healings, prophetic dreams) described in KP oral tradition. "
                    "His dargah/sthal is visited for blessings before important life events."
                ),
                "tradition": "Kashmir Shaivism / popular Siddha tradition",
                "link": "https://en.wikipedia.org/wiki/Kashmiri_Pandits",
                "archive": "",
            },
            {
                "title": "Swami Tik Kak Ji · स्वामी टिक कक जी",
                "author": "Swami Tik Kak Ji",
                "period": "19th–20th century CE — Srinagar",
                "desc": (
                    "Kashmiri Pandit Swami-saint from the Kak (Jamadagni gotra) and Tikku (Bharadwaja gotra) "
                    "lineage — 'Tik' is the Kashmiri form of Tikku/Tickoo. "
                    "As a Swami (formal renunciate), he took vows in the Kashmir Shaiva monastic tradition. "
                    "Practiced and transmitted the Trika-Pratyabhijña path: the three means of liberation "
                    "(Shambhavopaya, Shaktopaya, Anavopaya) from the Shiva Sutras. "
                    "Known for guiding householder devotees (grihastha shishyas) in integrating "
                    "Kashmir Shaiva philosophy with daily KP ritual life — Herath, Nityakarma, Kul Devi puja. "
                    "His teachings on the Spanda doctrine (divine vibration) were particularly influential "
                    "in the Srinagar KP community. Memory preserved through disciples' families."
                ),
                "tradition": "Kashmir Shaivism / Trika / Spanda",
                "link": "https://en.wikipedia.org/wiki/Kashmiri_Pandits",
                "archive": "",
            },
            {
                "title": "Swami Nand Lal Ji · स्वामी नन्द लाल जी",
                "author": "Swami Nand Lal Ji",
                "period": "19th–20th century CE — Kashmir",
                "desc": (
                    "Kashmiri Pandit renunciate and spiritual master of the Shaiva monastic tradition. "
                    "The name Nand Lal is deeply Kashmiri: Nanda (bliss / devotee) + Lal (beloved / Shiva). "
                    "As a Swami, he embodied the Trika teaching that renunciation is inner, not merely external. "
                    "Known for his exposition of the Shiva Sutras and Spanda Karikas to lay devotees — "
                    "making the deepest philosophical teachings of Kashmir Shaivism accessible to KP householders. "
                    "Particular strength: the Anavopaya path (individual means) — mantra, pranayama, "
                    "and the Nityakarma daily ritual as a form of Pratyabhijña practice. "
                    "His disciple lineage maintained the oral tradition of his teachings in Kashmir. "
                    "Context: Contemporary of Swami Lakshman Joo — both represent the final flourishing "
                    "of the living Kashmir Shaivism tradition before the 1990 exodus."
                ),
                "tradition": "Kashmir Shaivism / Trika / Spanda",
                "link": "https://en.wikipedia.org/wiki/Kashmiri_Pandits",
                "archive": "",
            },
            {
                "title": "Sidh Bab · सिद्ध बाब (Siddha tradition)",
                "author": "Multiple Siddha masters — Siddha Shrikantha (Lal Ded's guru) most celebrated",
                "period": "Medieval to modern — ongoing tradition",
                "desc": (
                    "'Sidh Bab' (Siddha Baba) is the honorific given to perfected Shaiva masters in Kashmir — "
                    "saints who have achieved Siddhi (spiritual perfection) through the Trika path. "
                    "The most celebrated historical Sidh Bab: Siddha Shrikantha Swami — the guru of Lalleshwari. "
                    "He belonged to the Shaiva Siddha lineage of Kashmir and transmitted the Pratyabhijña "
                    "recognition-path to Lal Ded, catalysing her transformation. "
                    "Multiple Sidh Bab figures exist across the Kashmir Valley: each is venerated as a "
                    "Kshetrapala (field protector) of a locality. Their shrines (often a stone, tree or spring) "
                    "dot the landscape of Kashmir. "
                    "In the Trika tradition, a Siddha has mastered: Khechari mudra, Pratyabhijña, "
                    "and the 36-tattva cosmology. The 84 Siddhas (Chaurasi Siddha) tradition also "
                    "intersects with Kashmiri Shaivism. "
                    "Reference: Alexis Sanderson's papers on Kashmir Shaivism siddha traditions (Oxford)."
                ),
                "tradition": "Kashmir Shaivism / Siddha tradition",
                "link": "https://en.wikipedia.org/wiki/Siddha",
                "archive": "https://www.wisdomlib.org/definition/siddha#kashmir",
            },
            {
                "title": "Paramanand · परमानन्द",
                "author": "Paramanand (Kashmiri saint)",
                "period": "19th–20th century CE",
                "desc": (
                    "Kashmiri Pandit saint whose very name encodes the highest Shaiva teaching: "
                    "Parama (supreme) + Ananda (bliss) = the supreme bliss of Brahman / Shiva. "
                    "In the Trika tradition, Paramananda is technically a name for the state of "
                    "liberated consciousness — Anuttara (the unsurpassable), the highest of the 36 tattvas. "
                    "This saint embodied the name through his direct experience of non-dual awareness "
                    "and his transmission of that joy to all who sought him. "
                    "Venerated by KP families for spiritual guidance, especially in Kul Devi puja tradition "
                    "and the Herath ritual. His teachings emphasised that ananda (bliss) is not a state "
                    "to be achieved but recognised as one's own nature — pure Pratyabhijña. "
                    "Reference: The name Paramananda appears in the KP spiritual lineage preserved "
                    "in the Bhannamasis gotra records and community oral histories."
                ),
                "tradition": "Kashmir Shaivism / Pratyabhijña",
                "link": "https://en.wikipedia.org/wiki/Kashmiri_Pandits",
                "archive": "",
            },
            {
                "title": "Madhav Das Ji · माधव दास जी",
                "author": "Madhav Das Ji",
                "period": "18th–19th century CE",
                "desc": (
                    "Kashmiri Pandit saint whose name honours Madhava — a name of Vishnu/Krishna "
                    "(Ma = Lakshmi, Dhava = lord = Lord of Lakshmi). "
                    "Significant lineage connection: Rupa Bhawani's father was Pandit Madhav Joo Dhar — "
                    "illustrating the deep connection between the Madhav devotional lineage and "
                    "the Kashmir Shaiva-Shakta tradition. "
                    "Madhav Das Ji combined Vaishnava bhakti (devotion to Madhava/Vishnu) with the "
                    "Kashmir Shaiva non-dual philosophy — reflecting the characteristic KP synthesis "
                    "of Shaiva and Vaishnava streams. "
                    "This Shaiva-Vaishnava synthesis is documented in the Svamina Bharadwaja lineage "
                    "(Bhannamasis table) where both Shiva and Vishnu worship coexist in single families. "
                    "His teachings on Madhava bhakti within the Trika framework were significant for "
                    "KP communities who maintained both Shaiva and Vaishnava household traditions."
                ),
                "tradition": "Kashmir Shaivism / Vaishnava-Shaiva synthesis",
                "link": "https://en.wikipedia.org/wiki/Kashmiri_Pandits",
                "archive": "",
            },
            {
                "title": "Nand Lal Sahib Ji · नन्द लाल साहिब जी",
                "author": "Nand Lal Sahib Ji",
                "period": "19th–20th century CE — Srinagar",
                "desc": (
                    "Revered KP saint given the double honorific 'Sahib Ji' — a title of great reverence "
                    "used in Kashmir for both Sufi pirs and Hindu saints, reflecting the valley's syncretic tradition. "
                    "Nand Lal Sahib Ji is remembered for his extraordinary compassion, accessibility to all, "
                    "and his practice of Kashmir Shaiva sadhana through daily ritual, mantra and "
                    "the living transmission of Lal Ded's Vakh tradition. "
                    "Core teaching: 'Anuttara' — the Supreme, Shiva, is ever-present; "
                    "Pratyabhijña is available in every moment of consciousness. "
                    "Known for healing the spiritually distressed and guiding families through "
                    "the upheavals of 19th–20th century Kashmir. "
                    "Venerated at his samadhi sthal in Srinagar where devotees offer flowers and prayers. "
                    "His memory kept alive through oral traditions in multiple KP families of Srinagar."
                ),
                "tradition": "Kashmir Shaivism / popular devotion",
                "link": "https://en.wikipedia.org/wiki/Kashmiri_Pandits",
                "archive": "",
            },
            {
                "title": "Gobind Koul Ji · गोबिन्द कौल जी",
                "author": "Gobind Koul Ji",
                "period": "19th–20th century CE — Srinagar",
                "desc": (
                    "Kashmiri Pandit saint from the Koul family — one of the most widespread KP lineages "
                    "(Kashyapa and Kaushika gotras; Datthtreya Koul and Svamina Rishi Kanya Gargya lineages "
                    "from the Bhannamasis table). "
                    "The name Gobind (Sanskrit: Go = cows/senses + Vinda = finder = 'One who finds/controls the senses' = Vishnu/Krishna) "
                    "combined with the Koul lineage illustrates the Shaiva-Vaishnava synthesis of KP spirituality. "
                    "Known for mastery of Shaiva mantras, puja vidhi and oral transmission of the Trika tradition "
                    "within the Koul community of Srinagar. "
                    "Venerated for his ability to guide families through the Herath ritual, "
                    "Kul Devi puja (Kheer Bhawani / Sharika Devi), and the Nityakarma daily practice. "
                    "His teachings on Gobinda (Vishnu) as a manifestation of Shiva reflect the "
                    "non-sectarian spirit of Kashmir Shaivism."
                ),
                "tradition": "Kashmir Shaivism / KP Koul lineage tradition",
                "link": "https://en.wikipedia.org/wiki/Kashmiri_Pandits",
                "archive": "",
            },
        ],
        "Lal Ded & Kashmiri Poetry · ललद्यद और काव्य": [
            {
                "title": "Lal Vākhs · लल वाख — Verses of Lalleshwari",
                "author": "Lalleshwari / Lal Ded (c. 1320–1392 CE)",
                "period": "14th century CE",
                "desc": (
                    "258+ mystical verses (Vakhs = 'speech/word' in Kashmiri) — the oldest literature "
                    "in the Kashmiri language and the foundation of all later KP spiritual poetry. "
                    "Language: Old Kashmiri (14th century Koshur) — a Dardic Indo-Aryan dialect. "
                    "Themes: (1) Shivoham — I am Shiva; the atman is Brahman. "
                    "(2) Futility of external ritual — 'I searched outside, Shiva is within.' "
                    "(3) Pranayama as path — the inner fire of prana as Kundalini Shakti. "
                    "(4) Non-dual love — Shiva as the beloved, creation as his dance. "
                    "(5) Social equality — transcending caste and religion. "
                    "Three celebrated Vakhs with Kashmiri originals: "
                    "· 'Lale ous yeli gurus vachas razi' — When I, Lalla, became alert to the Guru's word... "
                    "· 'Pranas apanas milawath karim' — When prana and apana unite... "
                    "· 'Akis akis panas akis' — One, and one, and one is one... "
                    "Editions: Jayalal Kaul 'Lal Ded' (Sahitya Akademi, 1973), "
                    "Ranjit Hoskote 'I, Lalla: The Poems of Lal Ded' (Penguin, 2011), "
                    "Coleman Barks translation (Maypop Books). "
                    "Academic: Grierson & Barnett 'Lallāvākyāni' (1920, Royal Asiatic Society) — first scholarly edition."
                ),
                "tradition": "Kashmir Shaivism / Lal Ded oral tradition",
                "link": "https://en.wikipedia.org/wiki/Lalleshwari",
                "archive": "https://archive.org/search?query=lal+ded+vakhs+lalleshwari+kashmiri",
            },
            {
                "title": "Shrukhs · श्रुख — Verses of Nund Rishi (Sheikh Nuruddin)",
                "author": "Nund Rishi / Sheikh Nuruddin Noorani (1377–1440 CE)",
                "period": "15th century CE",
                "desc": (
                    "Nund Rishi (Nund = pure/silent, Rishi = sage) — patron saint of all Kashmir, "
                    "founder of the Rishi Sufi order, and the most revered saint of the valley. "
                    "Born 1377 in Kaimoh village, Kulgam. Said to have been suckled as an infant by Lal Ded herself. "
                    "His Shrukhs (poems) in Kashmiri blend Shaiva and Sufi themes so seamlessly that "
                    "both traditions claim him. His order, the Rishis, practiced vegetarianism, "
                    "celibacy and integration with nature — unique in Sufi traditions. "
                    "Shrine: Charar-i-Sharief, Budgam — Kashmir's holiest Sufi site, destroyed in 1995 conflict, rebuilt. "
                    "Key Shrukh: 'Boh chu myon mantrith kur / Bhagwan kus tim karan wanun' — "
                    "I am that enchanted bird; who can tell me what Bhagwan is? "
                    "Works: Shrukhs (collected Kashmiri poems), preserved in oral and manuscript traditions. "
                    "Book: 'The Rishi Order of Kashmir' (academic studies), "
                    "'Nund Rishi: Patron Saint of Kashmir' (various KP community publications)."
                ),
                "tradition": "Rishi Sufi order / Shaiva-Sufi synthesis",
                "link": "https://en.wikipedia.org/wiki/Nund_Rishi",
                "archive": "https://archive.org/search?query=nund+rishi+shrukhs+kashmir",
            },
            {
                "title": "Vakhs of Rupa Bhawani · रूपा भवानी वाख",
                "author": "Rupa Bhawani (1625–1721 CE)",
                "period": "17th–18th century CE",
                "desc": (
                    "The Vakhs of Rupa Bhawani are among the most philosophically rich of all Kashmiri "
                    "mystic poetry — combining intense bhakti (devotion) with the rigorous non-dual philosophy "
                    "of Kashmir Shaivism. Written in classical Kashmiri with Sanskrit elements. "
                    "Key themes: body as Shiva-Shakti union, dissolution of ego-identity, "
                    "the Guru as the Grace of Shiva, and direct recognition of supreme consciousness. "
                    "Key Vakh: 'Zaan tse Aham Brahmasmi / Yeli che nab nab Suyii' — "
                    "Know thyself as I am Brahman; when the sky is sky, that alone is. "
                    "Editions: 'Vakhs of Rupa Bhawani' — compiled by KP Sabha Jammu; "
                    "also preserved in oral family traditions across the KP diaspora. "
                    "Academic: Referenced in 'Women Saints of India' and Kashmiri Shaivism studies."
                ),
                "tradition": "Kashmir Shaivism / Shakta / Bhakti poetry",
                "link": "https://en.wikipedia.org/wiki/Rupa_Bhawani",
                "archive": "https://archive.org/search?query=rupa+bhawani+kashmir+poetry",
            },
            {
                "title": "Songs of Habba Khatoon · हब्बा खातून",
                "author": "Habba Khatoon (c. 1554–1609 CE)",
                "period": "16th century CE",
                "desc": (
                    "Called the 'Nightingale of Kashmir' (Bulbul-e-Kashmir). Born Zooni (moon-face) "
                    "in Chandahar village, married Yusuf Shah Chak (last independent sultan of Kashmir) "
                    "before Akbar annexed the valley in 1586. Her Lol (lyric songs) express the "
                    "intense viraha (love-in-separation) for her exiled husband — and at a deeper level, "
                    "for the beloved divine. The most musically beautiful voice in Kashmiri literature. "
                    "Key song: 'Rozis na biyus dilbar myon' — My beloved does not return. "
                    "Her songs are still sung at Kashmiri festivals, especially spring and Navreh. "
                    "Editions: 'Habba Khatoon: Poems' — translated by Trilokinath Raina, "
                    "Sahitya Akademi publication. "
                    "Academic: 'The Nightingale of Kashmir' — multiple literary studies. "
                    "Her memorial: Government College for Women, Srinagar bears her name."
                ),
                "tradition": "Classical Kashmiri lyric poetry",
                "link": "https://en.wikipedia.org/wiki/Habba_Khatoon",
                "archive": "https://archive.org/search?query=habba+khatoon+kashmir+poetry",
            },
            {
                "title": "Vakhs of Arnimal · अर्निमल",
                "author": "Arnimal (c. 18th century CE)",
                "period": "18th century CE",
                "desc": (
                    "Kashmiri poetess whose Vakhs uniquely blend personal anguish with spiritual longing. "
                    "Her husband remarried, and she channelled that pain into some of Kashmiri literature's "
                    "most poignant verses — the private becomes universal. "
                    "Her language bridges the mystical Vakh tradition of Lal Ded with the personal lol "
                    "(lyric) tradition of Habba Khatoon. "
                    "Considered the third great woman poet of Kashmir after Lal Ded and Habba Khatoon. "
                    "Key Vakh: 'Suy myon yar, suy myon dilbar / Suy myon chu sahib-i-jamal' — "
                    "He is my friend, he is my beloved / He is my master of beauty. "
                    "Editions: 'Arnimal: Selected Poems' — Sahitya Akademi and KP literary organisations. "
                    "Academic: Referenced in studies of Kashmiri women's literature and Bhakti traditions."
                ),
                "tradition": "Kashmiri Bhakti / lyric poetry",
                "link": "https://en.wikipedia.org/wiki/Arnimal",
                "archive": "https://archive.org/search?query=arnimal+kashmiri+poetry",
            },
            {
                "title": "Swami Lakshman Joo · स्वामी लक्ष्मण जू (1907–1991 CE)",
                "author": "Swami Lakshmanjoo (born Laxman Raina)",
                "period": "1907–1991 CE — Srinagar",
                "desc": (
                    "The last great master (acharya) of the living Kashmir Shaivism tradition. "
                    "Born 1907 in Srinagar, he spent his entire life there — never leaving Kashmir. "
                    "Disciple of Swami Mahatab Koul. Mastered the entire Kashmir Shaivism corpus: "
                    "Tantraloka, Spanda Karikas, Shiva Sutras, Pratyabhijnahridayam. "
                    "Brought the Trika tradition to global audiences through recorded lectures and writings. "
                    "His ashram: Ishber, Nishat, Srinagar (still active). "
                    "Key works: 'Kashmir Shaivism: The Secret Supreme' (Universal Shaiva Fellowship, 1988) — "
                    "the most authoritative modern English exposition of the tradition. "
                    "Also: 'Shiva Sutras: The Supreme Awakening', 'Vijnanabhairava: The Manual for Self Realization', "
                    "'Self Realization in Kashmir Shaivism' (all Universal Shaiva Fellowship). "
                    "Audio: 200+ hours of recorded lectures — available at universalshaivafelllowship.org. "
                    "Website: universalshaivafelllowship.org · lakshmanjoo.com"
                ),
                "tradition": "Kashmir Shaivism / Trika / Pratyabhijña — modern transmission",
                "link": "https://en.wikipedia.org/wiki/Swami_Lakshmanjoo",
                "archive": "https://archive.org/search?query=swami+lakshmanjoo+kashmir+shaivism",
            },
        ],
        "Kashmiri Culture & Customs · संस्कृति": [
            {
                "title": "Herath (Kashmiri Shivratri) · हेरथ",
                "author": "Living KP tradition — ancient origin",
                "period": "Phalguna Krishna Chaturdashi (Feb–Mar) — annual",
                "desc": (
                    "The most sacred Kashmiri Pandit festival — entirely distinct from mainstream Shivratri. "
                    "Etymology: 'Herath' derives from 'Hara-ratri' (night of Hara/Shiva). "
                    "3-day ritual sequence: "
                    "Day 1 (Salam, 13th night): 12 earthen pots (Vatak) filled with water are set up — "
                    "each represents one of the 12 Shiva lingas and one Rishi. Sacred walnut (Shishur) "
                    "and ritual paraphernalia arranged. The 'Salam' (salutation to Shiva) is performed. "
                    "Day 2 (Vatak Puja, 14th): All-night worship of the Vatak pots as Shiva himself. "
                    "Bhairava is worshipped as Vatuk (child form of Bhairava). Purohit recites "
                    "Shiva Sutras, Spanda Karikas and specific Herath mantras through the night. "
                    "Day 3 (15th, Purnima): Paran (breaking of fast). Sweet Harissa, Nadru dishes served. "
                    "Unique elements: The walnut (Shishur) is the sacred fruit of Herath. "
                    "The 12 Vatak pots are unique to KP Herath — not found in pan-Indian Shivratri. "
                    "Sources: Nilamata Purana (Vatak tradition), Svacchanda Tantra (Bhairava worship)."
                ),
                "tradition": "Kashmiri Pandit ritual / Nilamata Purana",
                "link": "https://en.wikipedia.org/wiki/Herath",
                "archive": "https://archive.org/search?query=herath+kashmiri+pandit+shivratri+festival",
            },
            {
                "title": "Navreh · नवरेह — Kashmiri New Year",
                "author": "Living KP tradition — Chaitra Shukla Pratipada",
                "period": "Chaitra Shukla Pratipada (Mar–Apr) — annual",
                "desc": (
                    "Navreh (Nava + Varsha = New Year in Kashmiri) is the KP New Year — "
                    "one of the most joyous festivals. Observed on Chaitra Shukla Pratipada "
                    "(first day of the bright fortnight of Chaitra, Amavasyanta reckoning). "
                    "The night before (Navreh eve): A Navreh Thali (plate) is prepared with: "
                    "· Rice (dhaan) — prosperity · Walnut (doon) — wisdom "
                    "· Salt (noon) — flavour of life · Sugar (mishri) — sweetness "
                    "· Curd (dahi) — auspiciousness · Seasonal bread (tchot/kulcha) "
                    "· Spring flowers (narcissus, iris) · Pen and inkpot (learning) "
                    "· Coins (lakshmi) · Jantri (KP almanac — the most important item). "
                    "The Jantri contains the annual panchang, festivals, muhurtas and horoscope data. "
                    "Morning ritual: First sight on waking = omen for the year — hence the Thali is "
                    "placed where it will be seen first. Temple visit, exchange of Navreh Mubarak greetings. "
                    "Foods: Modur Pulav (sweet rice), Haakh, Nadru, Shufta (dry fruit sweet). "
                    "Reference: Nilamata Purana on Chaitra Pratipada, 'KP Festivals' (KPSS publications)."
                ),
                "tradition": "Kashmiri Pandit ritual / Nilamata Purana",
                "link": "https://en.wikipedia.org/wiki/Navreh",
                "archive": "https://archive.org/search?query=navreh+kashmiri+new+year+pandit",
            },
            {
                "title": "Kheer Bhawani Mela · खीर भवानी — Zyeth Ashtami",
                "author": "Living KP tradition",
                "period": "Jyeshtha Shukla Ashtami (May–Jun) — annual",
                "desc": (
                    "Annual pilgrimage to Kheer Bhawani temple at Tullamulla (Tulmul), Ganderbal — "
                    "the single largest annual gathering of Kashmiri Pandits. "
                    "The temple contains a sacred spring of changing colour. "
                    "Tradition holds: white water = peace and prosperity; dark/black water = trouble ahead. "
                    "The goddess: Ragnya Devi (Kheer Bhawani) — one of the principal Kul Devis of KPs. "
                    "Offering: Milk and Kheer (rice pudding with saffron) poured into the spring. "
                    "History: The temple was built over an ancient sacred spring mentioned in the "
                    "Nilamata Purana. Mughal records also mention it. Last major restoration: 20th century. "
                    "For the KP diaspora after 1990: Zyeth Ashtami melas are held worldwide with proxy puja. "
                    "Also: Multiple satellite Kheer Bhawani temples established by KPs in diaspora cities. "
                    "Reference: 'Kheer Bhawani: The Spring Goddess of Kashmir' (various academic studies)."
                ),
                "tradition": "Kashmiri Pandit pilgrimage / Shakta",
                "link": "https://en.wikipedia.org/wiki/Kheer_Bhawani",
                "archive": "https://archive.org/search?query=kheer+bhawani+tulmul+kashmir+zyeth+ashtami",
            },
            {
                "title": "KP Vivāha (Wedding) · कश्मीरी पण्डित विवाह",
                "author": "Living KP tradition",
                "period": "Auspicious muhurta dates",
                "desc": (
                    "Traditional KP wedding — a multi-day ritual combining Vedic, Shaiva and uniquely Kashmiri elements. "
                    "Pre-wedding: Devgun (invoking family deities — Kul Devi, Kul Devta, Bhairava), "
                    "Lagan (purohit ties auspicious thread, sets muhurta). "
                    "Wedding day: Wanwun songs (women's group songs specific to each ritual stage — "
                    "groom's arrival, Saptapadi, vidai). Dejhour (formal gift exchange between families). "
                    "Pheran ceremony (bride dressed in traditional Pheran + Tarang headpiece). "
                    "Kanyadan (father's gift of daughter). Saptapadi (7 steps around sacred fire). "
                    "Post-wedding: Khon Batta (homecoming feast). "
                    "Music: Live Wanwun singing — elderly women are custodians of these Kashmiri songs. "
                    "Purohit: Recites in Sanskrit with Kashmiri explanations. "
                    "Gotra check: Same-gotra marriage strictly forbidden (sagotra vivaha varjya). "
                    "Reference: 'Kashmiri Pandit Wedding Rituals' (KPSS, AIKS publications), "
                    "Sahitya Akademi resources on Kashmiri folk tradition."
                ),
                "tradition": "Kashmiri Pandit ritual / Vedic-Shaiva synthesis",
                "link": "https://en.wikipedia.org/wiki/Kashmiri_Pandits#Customs_and_traditions",
                "archive": "https://archive.org/search?query=kashmiri+pandit+wedding+customs",
            },
            {
                "title": "Shrāddha & Pitru Paksha · श्राद्ध",
                "author": "Living KP tradition",
                "period": "Bhadrapada Krishna Paksha (Sep–Oct)",
                "desc": (
                    "Ancestral rites in KP tradition — unique in their Shaiva-Vedic synthesis. "
                    "Matamaal Shradh: rites for the maternal lineage (observed separately from paternal) — "
                    "unique to KP tradition and not common in other regional traditions. "
                    "Tithis: Each ancestor is remembered on their death tithi. Amavasya = for all. "
                    "Pinda Daan: Offered at Gaya (Bihar), Prayag, or on the banks of Vitasta (Jhelum). "
                    "Specific KP practices: Kashmiri Shaiva mantras (Shiva Sutras invocations) alongside "
                    "standard Vedic Shraddha mantras. The Purohit uses the Kashmiri panchang (Jantri) "
                    "for precise Amavasyanta tithi calculation. "
                    "Reference: 'Shraddha in the KP Tradition' (various pandit community publications), "
                    "Nilamata Purana ancestral rite references."
                ),
                "tradition": "Kashmiri Pandit ritual / Vedic ancestral tradition",
                "link": "https://en.wikipedia.org/wiki/Pitru_Paksha",
                "archive": "https://archive.org/search?query=shraddha+kashmiri+pandit+pitru",
            },
            {
                "title": "Nityakarma · नित्यकर्म — KP Daily Practice",
                "author": "Living KP tradition",
                "period": "Daily observance",
                "desc": (
                    "The complete daily ritual routine (Nityakarma) of a traditional KP: "
                    "· Brahma Muhurta (96 min before sunrise): waking, Achaman (sipping water thrice), "
                    "recitation of Shiva's names. "
                    "· Sandhya Vandana: morning prayer facing the rising sun — unique KP version "
                    "combines Vedic Gayatri with Kashmiri Shaiva mantras. "
                    "· Home shrine puja: offerings to Shiva linga, Kul Devi image, Naga (family serpent deity), "
                    "and ancestors (pitru). Incense, flowers, diya (lamp), naivedya (food offering). "
                    "· Surya Namaskar: 12 prostrations to the sun (Martand tradition of south Kashmir). "
                    "· Mantra japa: Om Namah Shivaya (primary); Mrityunjaya; Shiva Stotras. "
                    "· Evening: Deepa Puja (lamp lighting at dusk), recitation of Shiva Stotras or Lal Ded Vakhs. "
                    "· Herath nights: extended puja including Vatak worship. "
                    "Reference: 'Nityakarma: Daily Worship of Kashmiri Pandits' (KP community guides), "
                    "Svacchanda Tantra (Kshemaraja commentary) for ritual basis."
                ),
                "tradition": "Kashmiri Pandit ritual / Shaiva-Vedic",
                "link": "https://en.wikipedia.org/wiki/Kashmiri_Pandits#Religious_practices",
                "archive": "https://archive.org/search?query=kashmiri+pandit+daily+ritual+nityakarma",
            },
            {
                "title": "Kashmiri Language & Sharada Script · कोशुर / शारदा",
                "author": "Linguistic heritage",
                "period": "Ancient — Dardic branch, script from c. 8th century CE",
                "desc": (
                    "Kashmiri (Koshur) is the ancient language of Kashmir — a Dardic Indo-Aryan language "
                    "spoken by ~7 million. One of the 22 Scheduled Languages of India (8th Schedule). "
                    "Three scripts: Sharada (traditional KP — most ancient), Nastaliq/Perso-Arabic "
                    "(current official script in J&K), and Devanagari. "
                    "Sharada script: Ancestor of Gurmukhi and Takri. Used for all KP religious manuscripts, "
                    "horoscopes (janmapatri), temple inscriptions. Named after Sharada Devi (Saraswati). "
                    "~10,000 Sharada manuscripts survive in libraries (Srinagar, Pune BORI, Berlin, London). "
                    "Unicode block: U+11180–U+111DF. Now endangered — taught in only a few KP families. "
                    "Dialects: Koshuri (urban Srinagar), Kishtwari, Poguli, Siraji, Rambani. "
                    "Notable: Kashmiri is the only language in India where the verb 'to be' is "
                    "completely dropped in present tense — a linguistic feature tied to Kashmir Shaivism's "
                    "teaching that Being (Shiva) is self-evident. "
                    "Resources: Kashmiri Language Project (kashmiri.net), "
                    "Sahitya Akademi Kashmiri publications, "
                    "'A Dictionary of Kashmiri Proverbs' (Grierson, 1929, archive.org available)."
                ),
                "tradition": "Linguistic heritage / Kashmiri culture",
                "link": "https://en.wikipedia.org/wiki/Kashmiri_language",
                "archive": "https://archive.org/search?query=kashmiri+language+sharada+script+manuscripts",
            },
        ],
        "Āgama & Foundational Tantras · आगम": [
            {
                "title": "Mālinīvijayottara Tantra · मालिनीविजयोत्तर तन्त्र",
                "author": "Revealed text (Āgama)",
                "period": "Pre-10th century CE",
                "desc": "One of the three root Trika texts. Describes the 36 tattvas, three Upayas (means to liberation), and the Trika cosmology of Shiva–Shakti–Nara. Abhinavagupta treats it as the supreme Agama.",
                "tradition": "Trika",
                "link": "https://www.wisdomlib.org/definition/malini-vijayottara-tantra",
                "archive": "https://archive.org/search?query=malinivijayottara+tantra",
            },
            {
                "title": "Siddhayogeśvarīmata · सिद्धयोगेश्वरीमत",
                "author": "Revealed text (Āgama)",
                "period": "Pre-10th century CE",
                "desc": "Second root Trika text. Centers on the goddess Siddhayogesvari and the yogini-based tantric practice. Important source for Kula and Trika synthesis.",
                "tradition": "Trika",
                "link": "https://www.wisdomlib.org/definition/siddhayogesvarimata",
                "archive": "",
            },
            {
                "title": "Vijñānabhairava Tantra · विज्ञानभैरव तन्त्र",
                "author": "Revealed text (Āgama)",
                "period": "Pre-9th century CE",
                "desc": "112 dharanas (meditation techniques) for directly experiencing Bhairava-consciousness. One of the most practical and celebrated texts of Kashmir Shaivism. Translated by Paul Reps as 'Centering'.",
                "tradition": "Trika / Shaiva Agama",
                "link": "https://www.wisdomlib.org/hinduism/book/vijnana-bhairava-or-divine-consciousness",
                "archive": "https://archive.org/search?query=vijnana+bhairava+tantra",
            },
            {
                "title": "Netra Tantra · नेत्र तन्त्र",
                "author": "Revealed text (Āgama)",
                "period": "Pre-10th century CE",
                "desc": "The 'Eye' tantra — focuses on Amriteshvara (the deathless lord). Contains important material on royal protection rituals, mantras, and the Mrityunjaya tradition in Kashmir.",
                "tradition": "Shaiva Agama",
                "link": "https://www.wisdomlib.org/definition/netra-tantra",
                "archive": "https://archive.org/search?query=netra+tantra+kashmir",
            },
            {
                "title": "Svacchanda Tantra · स्वच्छन्द तन्त्र",
                "author": "Revealed text (Āgama)",
                "period": "Pre-9th century CE",
                "desc": "Major Shaiva Agama on Svacchanda Bhairava. Contains extensive material on mantra, cosmology, initiation (diksha) and yogic practices. Kshemaraja's commentary is authoritative.",
                "tradition": "Shaiva Agama",
                "link": "https://www.wisdomlib.org/definition/svacchanda-tantra",
                "archive": "https://archive.org/search?query=svacchanda+tantra",
            },
        ],
        "Pratyabhijñā Darśana · प्रत्यभिज्ञा": [
            {
                "title": "Śiva Sūtras · शिव सूत्र",
                "author": "Vasugupta (c. 875 CE)",
                "period": "c. 875 CE",
                "desc": "77 aphorisms revealed to Vasugupta on Mahadeva (Shankaracharya) Hill, Srinagar. Divided into three sections: Shambhavopaya, Shaktopaya, Anavopaya — the three means of liberation. Foundation of all later Kashmir Shaivism.",
                "tradition": "Pratyabhijña / Trika",
                "link": "https://www.wisdomlib.org/hinduism/book/the-shiva-sutras",
                "archive": "https://archive.org/search?query=shiva+sutras+vasugupta",
            },
            {
                "title": "Spanda Kārikā · स्पन्द कारिका",
                "author": "Vasugupta / Kallata (c. 875–900 CE)",
                "period": "c. 875–900 CE",
                "desc": "52 karikas on Spanda — the divine vibration or throb of consciousness that is the nature of Shiva. Companion text to Shiva Sutras. Commentary by Kshemaraja (Spanda Nirnaya) is the standard reading.",
                "tradition": "Spanda",
                "link": "https://www.wisdomlib.org/hinduism/book/spanda-karikas",
                "archive": "https://archive.org/search?query=spanda+karikas",
            },
            {
                "title": "Īśvarapratyabhijñā Kārikā · ईश्वरप्रत्यभिज्ञा",
                "author": "Utpaladeva (c. 900–950 CE)",
                "period": "c. 925 CE",
                "desc": "The philosophical masterwork of Utpaladeva — 'Recognition of the Lord as one's own Self'. Argues that liberation is the recognition (pratyabhijña) of one's identity with Shiva through knowledge and action. Foundation of the Pratyabhijña school.",
                "tradition": "Pratyabhijña",
                "link": "https://www.wisdomlib.org/definition/ishvarapratyabhijna",
                "archive": "https://archive.org/search?query=ishvara+pratyabhijna+karikas",
            },
            {
                "title": "Pratyabhijñāhṛdayam · प्रत्यभिज्ञाहृदयम्",
                "author": "Kshemaraja (c. 1000–1050 CE)",
                "period": "c. 1025 CE",
                "desc": "20 sutras condensing the entire Pratyabhijña philosophy for seekers. 'The Heart of Recognition' — perhaps the most accessible entry point to Kashmir Shaivism. Sutra 1: 'Chiti shakti of her own free will is the cause of the siddhi of the universe.'",
                "tradition": "Pratyabhijña",
                "link": "https://www.wisdomlib.org/hinduism/book/pratyabhijnahrdayam",
                "archive": "https://archive.org/search?query=pratyabhijnahridayam+kshemaraja",
            },
        ],
        "Abhinavagupta's Works · अभिनवगुप्त": [
            {
                "title": "Tantrāloka · तन्त्रालोक",
                "author": "Abhinavagupta (c. 975–1025 CE)",
                "period": "c. 1000 CE",
                "desc": "The greatest encyclopaedia of Tantric Shaivism — 37 Ahnikas (chapters), ~5800 verses. Covers all Trika, Kula, Kaula and Spanda doctrines. Teachers: Shambhunatha (Kula), Lakshmanagupta (Pratyabhijña). Called 'the Tantric Mahabharata'.",
                "tradition": "Trika / Kula / Kaula",
                "link": "https://www.wisdomlib.org/hinduism/book/tantraloka",
                "archive": "https://archive.org/search?query=tantraloka+abhinavagupta",
            },
            {
                "title": "Tantrasāra · तन्त्रसार",
                "author": "Abhinavagupta (c. 1000 CE)",
                "period": "c. 1000 CE",
                "desc": "Prose summary of the Tantraloka in accessible form. Covers the same themes — 36 tattvas, means of liberation, mantra, yantra — in condensed form for students.",
                "tradition": "Trika",
                "link": "https://www.wisdomlib.org/definition/tantrasara",
                "archive": "https://archive.org/search?query=tantrasara+abhinavagupta",
            },
            {
                "title": "Abhinavabhāratī · अभिनवभारती",
                "author": "Abhinavagupta (c. 1000 CE)",
                "period": "c. 1000 CE",
                "desc": "Abhinavagupta's massive commentary on Bharata's Natyashastra. Introduces the Rasa theory with philosophical depth — Rasa as aesthetic experience = a form of Brahmananda (bliss of Brahman). Foundational for Indian aesthetics.",
                "tradition": "Aesthetics / Rasashastra",
                "link": "https://www.wisdomlib.org/definition/abhinavabharati",
                "archive": "https://archive.org/search?query=abhinavabharati+natyashastra",
            },
            {
                "title": "Parātriṃśikā Vivaraṇa · परात्रिंशिका विवरण",
                "author": "Abhinavagupta (c. 1000 CE)",
                "period": "c. 1000 CE",
                "desc": "Commentary on the 36-verse Paratrishika tantra on the Trika Goddess Para. Contains Abhinavagupta's most esoteric teachings on mantra, the phonematic cosmology (Matrika), and the supreme Shakti.",
                "tradition": "Trika / Kula",
                "link": "https://www.wisdomlib.org/definition/paratrishika",
                "archive": "https://archive.org/search?query=paratrishika+vivarana",
            },
            {
                "title": "Paramārthasāra · परमार्थसार",
                "author": "Abhinavagupta (adaptation of Adhara Shastra)",
                "period": "c. 1000 CE",
                "desc": "105 verses summarising the entire Shaiva philosophy — cosmology, the 36 tattvas, bondage, liberation and grace — in an accessible devotional form.",
                "tradition": "Trika",
                "link": "https://www.wisdomlib.org/definition/paramarthasara",
                "archive": "https://archive.org/search?query=paramarthasara+abhinavagupta",
            },
        ],
        "Kshemaraja's Works · क्षेमराज": [
            {
                "title": "Spanda Nirṇaya · स्पन्द निर्णय",
                "author": "Kshemaraja (c. 1000–1050 CE)",
                "period": "c. 1025 CE",
                "desc": "Authoritative commentary on the Spanda Karikas, establishing Spanda doctrine as the dynamic self-expression of Shiva-consciousness. More philosophical than Kallata's Vritti.",
                "tradition": "Spanda",
                "link": "https://www.wisdomlib.org/definition/spandanirnaya",
                "archive": "https://archive.org/search?query=spanda+nirnaya+kshemaraja",
            },
            {
                "title": "Shiva Sūtra Vimarśinī · शिव सूत्र विमर्शिनी",
                "author": "Kshemaraja (c. 1025 CE)",
                "period": "c. 1025 CE",
                "desc": "The standard commentary on the Shiva Sutras. Illuminates all 77 sutras with deep Trika philosophy and practical guidance. Most widely studied commentary in the tradition.",
                "tradition": "Pratyabhijña",
                "link": "https://www.wisdomlib.org/hinduism/book/shiva-sutra-vimarsini",
                "archive": "https://archive.org/search?query=shiva+sutra+vimarsini",
            },
            {
                "title": "Svacchanda Tantra Uddyota · स्वच्छन्द तन्त्रोद्योत",
                "author": "Kshemaraja (c. 1025 CE)",
                "period": "c. 1025 CE",
                "desc": "Kshemaraja's massive commentary on Svacchanda Tantra — a primary source for Shaiva initiation, cosmology and mantra practice in Kashmir.",
                "tradition": "Shaiva Agama",
                "link": "https://www.wisdomlib.org/definition/svacchanda-tantra",
                "archive": "https://archive.org/search?query=svacchandatantrauddyota+kshemaraja",
            },
        ],
        "Spanda & Other Schools · स्पन्द": [
            {
                "title": "Stava Cintāmaṇi · स्तव चिन्तामणि",
                "author": "Bhattatrayambaka",
                "period": "c. 10th century CE",
                "desc": "Hymn to Shiva celebrating the Spanda doctrine. Important devotional text of Kashmir Shaivism used in ritual and study.",
                "tradition": "Spanda",
                "link": "https://www.wisdomlib.org/definition/stavacintamani",
                "archive": "",
            },
            {
                "title": "Śivastotrāvalī · शिवस्तोत्रावली",
                "author": "Utpaladeva (c. 925 CE)",
                "period": "c. 925 CE",
                "desc": "20 hymns of intense devotion to Shiva by Utpaladeva — among the most beautiful devotional poetry in Sanskrit. Demonstrates that dry philosophy was always paired with heartfelt bhakti in Kashmir Shaivism.",
                "tradition": "Pratyabhijña / Bhakti",
                "link": "https://www.wisdomlib.org/definition/shivastotravali",
                "archive": "https://archive.org/search?query=shivastotravali+utpaladeva",
            },
        ],
        "Nilamata Purāṇa & History · नीलमत पुराण": [
            {
                "title": "Nīlamata Purāṇa · नीलमत पुराण",
                "author": "Unknown (Kashmirian)",
                "period": "c. 6th–8th century CE",
                "desc": "The oldest known Kashmiri text — describes the origin of Kashmir Valley (from the lake Satisar), its geography, the festivals, rituals and customs of Kashmiri people. Primary source for KP customs, Naga worship, and Herath.",
                "tradition": "Kashmiri Puranic tradition",
                "link": "https://www.wisdomlib.org/hinduism/book/nilamata-purana",
                "archive": "https://archive.org/search?query=nilamata+purana+kashmir",
            },
            {
                "title": "Rājataraṅgiṇī · राजतरङ्गिणी",
                "author": "Kalhana (c. 1150 CE)",
                "period": "c. 1150 CE",
                "desc": "Kashmir's great chronicle — 8 Tarangas (waves), ~7826 verses. The history of Kashmir from mythological times to 1150 CE. First systematic historical work in Sanskrit. Invaluable for KP lineage, geography and culture.",
                "tradition": "History / Itihas",
                "link": "https://www.wisdomlib.org/hinduism/book/rajatarangini",
                "archive": "https://archive.org/search?query=rajatarangini+kalhana",
            },
            {
                "title": "Mahānayaprakāśa · महानयप्रकाश",
                "author": "Shitivaraha / Arnavagupta",
                "period": "c. 12th century CE",
                "desc": "Important Krama text in Old Kashmiri (one of the earliest surviving texts in the Kashmiri language) with Sanskrit portions. Documents the Krama tradition of goddess worship.",
                "tradition": "Krama",
                "link": "https://www.wisdomlib.org/definition/mahanayaprakasha",
                "archive": "",
            },
        ],
    }

    # ── Section filter ─────────────────────────────────────────────
    sh_sections = ["All Sections · सभी"] + list(SHASTRA_DATA.keys())
    sh_filter = st.selectbox("Browse by Category · श्रेणी चुनें", sh_sections, key="sh_filter")
    sh_search_term = st.text_input("Search texts, authors, traditions… · खोजें", key="sh_search_text",
                                    placeholder="e.g. Abhinavagupta, Tantraloka, Spanda, Lal Ded…")

    # Only show content when user has chosen a specific category or typed a search term
    _sh_active = sh_filter != "All Sections · सभी" or bool(sh_search_term)

    if not _sh_active:
        st.markdown("""
        <div style="text-align:center;padding:48px 20px;color:var(--muted)">
          <div style="font-size:36px;margin-bottom:16px;opacity:.4"></div>
          <div style="font-family:'Cinzel',serif;font-size:12px;letter-spacing:2.5px;
               color:var(--walnut-mid);margin-bottom:10px">SELECT A CATEGORY · श्रेणी चुनें</div>
          <div style="font-size:13.5px;line-height:1.8;max-width:420px;margin:0 auto">
            Choose a category from the dropdown above — or type a keyword in the search box —
            to explore the texts, traditions and scholars of Kashmir Shaivism.
          </div>
          <div style="font-family:'Noto Serif Devanagari',serif;font-size:12px;
               color:var(--muted);margin-top:10px;opacity:.6">
            ऊपर श्रेणी चुनें या खोज करें
          </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        if sh_search_term:
            term = sh_search_term.lower()
            sections_to_show = {}
            for sec, items in SHASTRA_DATA.items():
                filtered = [it for it in items if
                            term in it["title"].lower() or
                            term in it["author"].lower() or
                            term in it["desc"].lower() or
                            term in it["tradition"].lower()]
                if filtered:
                    sections_to_show[sec] = filtered
        else:
            sections_to_show = {k: v for k, v in SHASTRA_DATA.items() if k == sh_filter}

        total_shown = sum(len(v) for v in sections_to_show.values())
        if total_shown == 0:
            st.info("No results found. Try a different search term.")
        else:
            st.markdown(f'<div style="font-size:12px;color:var(--muted);margin:6px 0 16px;font-style:italic">'
                        f'Showing {total_shown} text(s) in {len(sections_to_show)} section(s)</div>',
                        unsafe_allow_html=True)

    if _sh_active:
        for section_name, items in sections_to_show.items():
            st.markdown(f'<div class="subsec">{section_name}</div>', unsafe_allow_html=True)
            for item in items:
                link_html = ""
                if item.get("link"):
                    link_html += f'<a href="{item["link"]}" target="_blank" style="font-size:11px;color:var(--teal);text-decoration:none;margin-right:12px"> Reference</a>'
                if item.get("archive"):
                    link_html += f'<a href="{item["archive"]}" target="_blank" style="font-size:11px;color:var(--muted);text-decoration:none"> Archive.org</a>'
                st.markdown(f"""
                <div style="background:white;border:1px solid var(--border);border-radius:10px;
                     padding:16px 20px;margin-bottom:10px;box-shadow:0 1px 6px var(--shadow)">
                  <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:6px">
                    <div>
                      <span style="font-family:Cinzel,serif;font-size:13px;font-weight:500;
                            color:var(--walnut)">{item['title']}</span>
                      <span style="font-size:10px;font-family:Cinzel,serif;letter-spacing:1px;
                            color:var(--saffron);margin-left:10px;padding:2px 8px;
                            background:rgba(212,114,42,.08);border-radius:10px">{item['tradition']}</span>
                    </div>
                    <div style="text-align:right;font-size:11px;color:var(--muted)">
                      {item['author']} &nbsp;·&nbsp; {item['period']}
                    </div>
                  </div>
                  <div style="font-size:13.5px;color:var(--ink);line-height:1.75;margin:8px 0 10px">
                    {item['desc']}
                  </div>
                  <div>{link_html}</div>
                </div>
                """, unsafe_allow_html=True)

    # ── AI query ──────────────────────────────────────────────────
    st.markdown('<div class="styled-div"><span>ŚĀSTRA QUERY · शास्त्र प्रश्न</span></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="ai-box">
      <div class="ai-lbl">DEEP ŚĀSTRA QUERY · गहन शास्त्र खोज</div>
      <div style="margin-top:18px;text-align:center;padding:18px 0 10px">
        <div style="font-size:28px;margin-bottom:10px"></div>
        <div style="font-family:'Cinzel',serif;font-size:13px;letter-spacing:2px;
             color:#DEB85A;margin-bottom:8px">COMING IN NEXT UPDATE</div>
        <div style="font-size:14px;color:rgba(253,248,240,.65);line-height:1.8;max-width:480px;margin:0 auto">
          Your wise Kashmiri Pandit — for deep questions on Kashmir Shaivism, Trika philosophy,
          Sanskrit texts, Abhinavagupta, Pratyabhijñā and specific commentaries —
          launching in the next release.
        </div>
        <div style="font-family:'Noto Serif Devanagari',serif;font-size:12px;
             color:rgba(222,184,90,.45);margin-top:10px">
          शास्त्र प्रश्न — शीघ्र आ रहा है
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# TAB 6 — KASHMIRI CULTURE
# ══════════════════════════════════════════════════════════════════════════════
with tabs[6]:
    st.markdown("""
    <div class="sec-head"> Kāśmīrī Saṃskṛti · कश्मीरी संस्कृति</div>
    <div class="sec-sub">
      Complete guide to Kashmiri culture — festivals, food, arts, music, dress, sacred sites, saints and living traditions
      <span class="deva">उत्सव · भोजन · कला · संगीत · वेशभूषा · तीर्थ · संत · परम्परा</span>
    </div>
    """, unsafe_allow_html=True)

    KP_CULTURE = {
        "Festivals & Puja Rituals · उत्सव और पूजा विधि": [
            {
                "name": "Herath (Kashmiri Shivratri) · हेरथ",
                "icon": "",
                "timing": "Phalguna Krishna Chaturdashi — 3-day festival (Feb–Mar)",
                "desc": (
                    "The most sacred festival of Kashmiri Pandits. 'Herath' = Hara-ratri (Night of Hara/Shiva). "
                    "Entirely distinct from mainstream Shivratri in its rituals, materials and significance.\n\n"
                    "── DAY 1: SALAM (13th evening, Trayodashi) ──\n"
                    "The household is purified with cow dung (gobar) and gangajal. "
                    "12 clay pots (Vatak) are prepared — each represents one of the 12 Shiva lingas and one cosmic month. "
                    "Pots are filled with pure water. Sacred walnut branches (Shishur = Juglans regia) are placed inside. "
                    "The 'Salam' (salutation ceremony) is performed by the eldest male of the family — "
                    "he offers namaskar to all 12 Vatak pots arranged in a row.\n\n"
                    "── DAY 2: VATAK PUJA (14th, Chaturdashi — all night) ──\n"
                    "Puja Samagri (ritual materials):\n"
                    "· 12 new clay pots (Vatak) · Pure water (ideally from sacred river/spring) "
                    "· Walnut branches with leaves (Shishur) · Sacred grass (Durva/Kusha) "
                    "· Sesame seeds (til) · Rice (akshata) · Flowers (lotus, marigold) "
                    "· Incense (dhoop/agarbatti) · Diya (earthen lamp) with mustard oil "
                    "· Panchamrit (milk, curd, ghee, honey, sugar) · Fruits · Betel leaves (paan) "
                    "· Red thread (mauli/kalawa) · Sacred ash (vibhuti) · Sandalwood paste (chandan) "
                    "· New clothes (white preferred) · Copper/brass plate for offerings.\n\n"
                    "Puja Vidhi (procedure):\n"
                    "1. Achamanam: sip water thrice, recite Shiva names. "
                    "2. Sankalpa: state the intent before Shiva. "
                    "3. Ganesh Puja: invoke Ganesha first. "
                    "4. Vatak Sthapana: install all 12 pots ceremonially, each named after a Shiva linga. "
                    "5. Abhisheka: bathe each pot with Panchamrit, then pure water. "
                    "6. Shodasopachara Puja (16-step worship): Avahana, Asana, Padya, Arghya, Achamana, "
                    "Snana, Vastra, Yagnopavita, Gandha, Pushpa, Dhupa, Dipa, Naivedya, Tambula, "
                    "Pradakshina, Namaskara. "
                    "7. Shiva Stotra recitation: Shiva Sutras, Spanda Karikas, Mrityunjaya mantra (108 times). "
                    "8. Bhairava (Vatuk) Puja: the child-form Bhairava is invoked in a separate small earthen pot. "
                    "9. All-night vigil: family stays awake, singing Shiva bhajans and reciting Vakhs of Lal Ded. "
                    "10. Naga Puja at dawn: Naga (family serpent deity) is honoured.\n\n"
                    "── DAY 3: PARAN (15th, Purnima — breaking of fast) ──\n"
                    "The fast is broken with Harissa (slow-cooked lamb/mutton porridge — the traditional Herath Paran food), "
                    "Nadru (lotus stem), and sweets. "
                    "The Vatak pots are taken to a river/stream and immersed. "
                    "Walnut branches (Shishur) are distributed to all family members — eating the walnut is auspicious.\n\n"
                    "Mantra: 'Om Namah Shivaya · ॐ नमः शिवाय' (primary) | "
                    "Mrityunjaya: 'Om Tryambakam Yajamahe Sugandhim Pushti-Vardhanam' | "
                    "Shiva Panchakshara Stotra for all-night recitation."
                ),
                "links": [
                    ("Wikipedia · Herath", "https://en.wikipedia.org/wiki/Herath"),
                    ("Kashmiri Pandits Network · Herath", "https://www.ikashmir.net/herath/"),
                    ("Nilamata Purana (Vatak source)", "https://www.wisdomlib.org/hinduism/book/nilamata-purana"),
                ],
            },
            {
                "name": "Navreh · नवरेह — Kashmiri New Year",
                "icon": "",
                "timing": "Chaitra Shukla Pratipada (Mar–Apr) — Amavasyanta reckoning",
                "desc": (
                    "Navreh (Nava + Varsha = New Year in Kashmiri) — the most joyous KP festival. "
                    "Observed on Chaitra Shukla Pratipada, the first day of the Amavasyanta new year.\n\n"
                    "── EVE OF NAVREH (Navreh Ratri) ──\n"
                    "The Navreh Thali (ceremonial plate) is prepared with precision and placed where "
                    "it will be seen first thing upon waking. Items and their significance:\n"
                    "· Dhaan (uncooked rice) — abundance and fertility\n"
                    "· Doon (walnut) — wisdom and longevity\n"
                    "· Noon (salt) — the flavour of life; also preservation\n"
                    "· Mishri (sugar crystals) — sweetness and prosperity\n"
                    "· Dahi (curd) — auspiciousness; used in all KP rituals\n"
                    "· Tchot/Kulcha (ring bread) — the circular continuity of life\n"
                    "· Flowers (narcissus/nargis, Kashmiri iris) — beauty of the new season\n"
                    "· Kalam + dawaat (pen and inkpot) — knowledge and learning (Sharada Devi's blessing)\n"
                    "· Coins (silver preferred) — Lakshmi's grace, financial prosperity\n"
                    "· Jantri (the KP almanac/panchang) — THE most important item; contains the year's "
                    "muhurtas, festivals, nakshatra calendar, and astrological data for the family\n"
                    "· Mirror — to see oneself clearly in the new year\n"
                    "· Kesar (saffron) — divine grace and the fragrance of Kashmir.\n\n"
                    "── MORNING RITUAL (Navreh day) ──\n"
                    "Puja Samagri: Flowers, incense, diya, rice, curd, fruits, paan, coconut, "
                    "red thread, sandalwood paste, Jantri.\n\n"
                    "Puja Vidhi:\n"
                    "1. Wake at Brahma Muhurta — first sight must be the Navreh Thali (not a person).\n"
                    "2. Achamanam: sip water thrice.\n"
                    "3. Sharada Devi Puja: invoke Mata Sharada (Saraswati) — she presides over Navreh "
                    "as the goddess of the new year and learning. Recite Sharada Stotram: "
                    "'Ya Sharada nilotpala-dala-shyama...' \n"
                    "4. Ganesha Puja (Vighnaharta): remove obstacles for the new year.\n"
                    "5. Kul Devi Puja: offer flowers and namaskar to the family goddess image.\n"
                    "6. Sankalpa: state the new year's resolve before Shiva.\n"
                    "7. Read the Jantri aloud — the purohit or eldest member reads the year's key dates.\n"
                    "8. Exchange Navreh Mubarak greetings.\n"
                    "9. Temple visit: Sharika Devi (Hari Parbat), Kheer Bhawani, or family temple.\n\n"
                    "── NAVREH FOODS ──\n"
                    "Modur Pulav (sweet saffron rice with dry fruits), Haakh (collard greens), "
                    "Nadru yakhni (lotus stem in yogurt sauce), Shufta (dry fruit sweet), "
                    "Kulcha with butter. "
                    "Mantra: 'Om Shreem Hreem Saraswatyai Namah' (Sharada Devi) | "
                    "'Om Gam Ganapataye Namah' (Ganesha for new beginnings)."
                ),
                "links": [
                    ("Wikipedia · Navreh", "https://en.wikipedia.org/wiki/Navreh"),
                    ("Kashmiri Pandits Network · Navreh", "https://www.ikashmir.net/navreh/"),
                ],
            },
            {
                "name": "Kheer Bhawani Mela / Zyeth Ashtami · खीर भवानी",
                "icon": "",
                "timing": "Jyeshtha Shukla Ashtami (May–Jun)",
                "desc": (
                    "Annual pilgrimage to Kheer Bhawani temple at Tulmul (Tullamulla), Ganderbal. "
                    "Thousands of KPs offer milk and kheer (rice pudding) in the sacred spring. "
                    "The spring water's colour (white = peace, dark = trouble) is held to foretell events. "
                    "Ragnya Devi (goddess of the spring) is the most widely venerated KP Kul Devi."
                ),
                "links": [
                    ("Wikipedia · Kheer Bhawani", "https://en.wikipedia.org/wiki/Kheer_Bhawani"),
                    ("iKashmir Temple Info", "https://www.ikashmir.net/tulamula/"),
                ],
            },
            {
                "name": "Pann · पान्न",
                "icon": "",
                "timing": "Winter solstice period (Dec–Jan)",
                "desc": (
                    "Kashmiri harvest and winter festival marking the end of the coldest period. "
                    "Community bonfires (alav), seasonal foods (haakh, nadru), songs. "
                    "Associated with the sun's return — sesame seeds (til) are central. "
                    "Corresponds broadly to Makar Sankranti."
                ),
                "links": [
                    ("Kashmiri Pandits Network", "https://www.ikashmir.net/festivals/"),
                ],
            },
            {
                "name": "Kheer Bhawani Mela · खीर भवानी — Zyeth Ashtami Puja",
                "icon": "",
                "timing": "Jyeshtha Shukla Ashtami (May–Jun) — annual pilgrimage",
                "desc": (
                    "Annual pilgrimage to Kheer Bhawani (Ragnya Devi) at Tulmul, Ganderbal.\n\n"
                    "Puja Samagri (Offerings at the spring):\n"
                    "· Fresh milk (dugdha) — the primary offering; poured directly into the sacred spring\n"
                    "· Kheer (rice pudding with saffron) — the goddess's favourite offering; 'Kheer Bhawani' = goddess of kheer\n"
                    "· Mishri (sugar crystals) · Flowers (white: lotus, jasmine, mogra)\n"
                    "· Coconut · Fruits (seasonal) · Incense · Diya (ghee lamp)\n"
                    "· Red cloth (chunri) for the goddess image\n"
                    "· Naivédya (sweet food offering) — Modur Pulav, Shufta.\n\n"
                    "Puja Vidhi:\n"
                    "1. Arrive at Tulmul at Brahma Muhurta or early morning (auspicious).\n"
                    "2. Bathe, wear clean white/yellow clothes.\n"
                    "3. Achamanam and Sankalpa at the spring.\n"
                    "4. Pour milk into the spring — observe the water colour (white = auspicious; dark = alert).\n"
                    "5. Offer kheer, mishri, flowers in the spring.\n"
                    "6. Recite the Devi Stuti: 'Om Aim Hreem Kleem Chamundayai Viche' or 'Om Ragnyai Namah'.\n"
                    "7. Circumambulate the temple (Pradakshina) 3 or 7 times.\n"
                    "8. Offer a red chunri to the goddess image.\n"
                    "9. Receive prasad and sprinkle spring water on oneself.\n\n"
                    "Significance: The spring's colour is believed to be the goddess communicating — "
                    "this tradition is unique in the world. The Zyeth Ashtami mela is the emotional "
                    "heart of KP identity, especially for the diaspora after 1990."
                ),
                "links": [
                    ("Wikipedia · Kheer Bhawani", "https://en.wikipedia.org/wiki/Kheer_Bhawani"),
                    ("iKashmir · Tulmul Temple", "https://www.ikashmir.net/tulamula/"),
                ],
            },
            {
                "name": "Ashtami Puja · अष्टमी पूजा — Monthly Kul Devi Worship",
                "icon": "",
                "timing": "Every Shukla Ashtami; Vaishakha, Jyeshtha & Ashwina Ashtamis most sacred",
                "desc": (
                    "KP families observe Ashtami (8th of the waxing moon) as a monthly Kul Devi puja day.\n\n"
                    "Special Ashtamis in the KP calendar:\n"
                    "· Vaishakha Ashtami: Sharika Devi (Hari Parbat) — temple visit mandatory\n"
                    "· Jyeshtha Ashtami (Zyeth Ashtami): Kheer Bhawani pilgrimage\n"
                    "· Ashwina Ashtami: Navratri Ashtami — Maha Puja of Devi\n"
                    "· Phalguna Ashtami: puja before Herath.\n\n"
                    "Puja Samagri:\n"
                    "· Red flowers (gulal/rose preferred for Devi) · Coconut · Mishri\n"
                    "· Red chunri (cloth for the goddess) · Incense · Ghee diya\n"
                    "· Panchamrit · Fruits · Sindoor (vermilion) · Betel nuts and leaves.\n\n"
                    "Puja Vidhi:\n"
                    "1. Fast till noon (upavasa) — water and fruits permitted.\n"
                    "2. Bathe and wear clean clothes (red/yellow preferred for Devi puja).\n"
                    "3. Set up Kul Devi image or yantra on a clean red cloth.\n"
                    "4. Invoke Ganesha (Om Gam Ganapataye Namah).\n"
                    "5. Shodasopachara Puja to Kul Devi: Avahana → Padya → Arghya → Achamana → "
                    "Snana → Vastra → Gandha → Pushpa → Dhupa → Dipa → Naivedya → Tambula → Pradakshina → Namaskara.\n"
                    "6. Recite Devi Kavacham or Durga Saptashati selected dohas.\n"
                    "7. Distribute prasad to family. Break fast with KP satvik meal (no onion/garlic).\n\n"
                    "Mantra: 'Om Sharikayai Namah' (for Sharika Devi) | 'Om Ragnyai Namah' (Kheer Bhawani) | "
                    "'Om Jwaladevyai Namah' (Jwala Devi, Khrew)."
                ),
                "links": [
                    ("iKashmir · KP Religion", "https://www.ikashmir.net/religion/"),
                    ("Wikipedia · Kashmiri Pandits", "https://en.wikipedia.org/wiki/Kashmiri_Pandits#Religious_practices"),
                ],
            },
            {
                "name": "Nityakarma · नित्यकर्म — Complete Daily Ritual",
                "icon": "",
                "timing": "Every day — Brahma Muhurta to evening Deepa Puja",
                "desc": (
                    "The complete daily ritual life (Nityakarma) of a traditional Kashmiri Pandit:\n\n"
                    "── BRAHMA MUHURTA (96 min before sunrise) ──\n"
                    "Wake up, recite: 'Karagre vasate Lakshmi, karamadhye Saraswati / Karamule sthita Gouri, "
                    "prabhate kar-darshanam' (morning salutation to the hands). "
                    "Touch the earth with right foot: 'Samudra-vasane Devi, parvata-stana-mandale / "
                    "Vishnupatni namastubhyam, paadasparsham kshama swame'.\n\n"
                    "── MORNING PURIFICATION ──\n"
                    "Achamanam: sip water 3 times with Shiva names (Shivaya, Shankaraya, Mahadevaya). "
                    "Brush teeth with neem twig (traditional) or brush. "
                    "Full bath (sheetala jal preferred) — recite 'Gange Cha Yamune Chaiva' during bath.\n\n"
                    "── SANDHYA VANDANA (Morning) ──\n"
                    "Face east. Pranayama (3 cycles). "
                    "Gayatri mantra (minimum 10, ideal 108 repetitions): "
                    "'Om Bhur Bhuvaḥ Swaḥ / Tat Savitur Vareṇyam / Bhargo Devasya Dhīmahi / "
                    "Dhiyo Yo Naḥ Prachodayāt.' "
                    "KP-specific addition: Shiva Panchakshara after Gayatri.\n\n"
                    "── HOME SHRINE PUJA (Ghar ki Puja) ──\n"
                    "Puja Samagri: Shiva linga (or Shalagrama), Kul Devi image, Naga (brass serpent), "
                    "Pitru frame (ancestor photos/yantra), fresh flowers, incense, ghee diya, "
                    "panchamrit, fruits, tulsi leaves, Gangajal, kumkum, chandan, rice (akshata).\n\n"
                    "Sequence:\n"
                    "1. Invoke Ganesha first (Vakratunda Mahakaya...).\n"
                    "2. Shiva puja: Abhisheka with water/panchamrit on linga, offer flowers, bilva leaves, "
                    "dhatura (if available), incense, diya. Recite: 'Om Namah Shivaya' (108 times).\n"
                    "3. Kul Devi puja: red flowers, sindoor, coconut, mishri. "
                    "Recite family's specific Devi stotra.\n"
                    "4. Naga puja (on Mondays especially): milk offering to brass snake image.\n"
                    "5. Pitru vandana: water offering and namaskar to ancestors.\n"
                    "6. Mrityunjaya japa (minimum 11 times): "
                    "'Om Tryambakam Yajamahe Sugandhim Pushti-Vardhanam / "
                    "Urvarukamiva Bandhanan Mrityor Mukshiya Mamritat.'\n\n"
                    "── EVENING (Sandhya Dipa) ──\n"
                    "Light ghee diya at dusk. Recite Shiva Stotras or 3 Vakhs of Lal Ded. "
                    "Offer incense. Ring the bell (ghanta) to dispel negative energies.\n\n"
                    "── NIGHT ──\n"
                    "Recite Shiva Sahasranama or Vishnu Sahasranama (by family tradition) before sleep. "
                    "Last thought: 'Om Namah Shivaya.'"
                ),
                "links": [
                    ("WisdomLib · Nityakarma", "https://www.wisdomlib.org/definition/nityakarma"),
                    ("Svacchanda Tantra (ritual basis)", "https://www.wisdomlib.org/definition/svacchanda-tantra"),
                ],
            },
            {
                "name": "Shrāddha & Matamaal Shradh · श्राद्ध — Ancestral Rites",
                "icon": "",
                "timing": "Bhadrapada Krishna Paksha (Pitru Paksha, Sep–Oct) + individual death tithis",
                "desc": (
                    "Ancestral rites of the Kashmiri Pandit tradition — combining Vedic Shraddha "
                    "with specifically Kashmiri Shaiva elements.\n\n"
                    "Types of KP Shraddha:\n"
                    "1. Navaham Shraddha: 9-day rites immediately after death.\n"
                    "2. Masik Shraddha: monthly rite on the death tithi for one year.\n"
                    "3. Varshik Shraddha: annual rite on the death tithi.\n"
                    "4. Pitru Paksha Shraddha: 16-day period when all ancestors are honoured.\n"
                    "5. Matamaal Shraddha: UNIQUE to KP tradition — rites for the maternal lineage "
                    "(mother's parents, maternal uncles) performed separately from paternal rites.\n\n"
                    "Puja Samagri:\n"
                    "· Sesamum seeds (til) — essential for all Shraddha\n"
                    "· Kusha grass (Poa cynosuroides) — purifies the ritual space\n"
                    "· Pinda (balls of cooked rice mixed with sesame, milk, honey)\n"
                    "· Pure water (Gangajal preferred) · Cow's milk and curd\n"
                    "· Sacred thread (yagnopavita) · Dharbha grass\n"
                    "· Flowers (white) · Incense · Diya (sesame oil)\n"
                    "· Black sesame seeds · Barley · Honey · Ghee.\n\n"
                    "Puja Vidhi:\n"
                    "1. Purohit sets up the Shraddha space facing south (direction of ancestors).\n"
                    "2. Invoke Vishvedeva (cosmic witnesses) first.\n"
                    "3. Sankalpa: name the deceased, their gotra, death tithi.\n"
                    "4. Pindadaan: offer 3 pindas (rice balls) — one each for father/mother/grandfather.\n"
                    "5. Tarpan: pour water + sesame southward 3 times for each ancestor.\n"
                    "6. KP-specific: recite Kashmiri Shaiva mantras (Shiva Panchakshara) after standard Vedic recitations.\n"
                    "7. Brahman bhoj (feed a Brahmin) or donate food/clothes.\n"
                    "8. Matamaal Shraddha: repeat steps 3–7 for maternal lineage separately on the same day or next day.\n\n"
                    "Tirthas for Pindadaan: Gaya (Bihar) — most sacred; Prayagraj (Allahabad); "
                    "Vitasta (Jhelum) banks in Kashmir; Haridwar (Ganga). "
                    "Mantra: 'Pitrupibhyo namah / Matrumat-pitrupibhyo namah' (for Matamaal)."
                ),
                "links": [
                    ("Wikipedia · Pitru Paksha", "https://en.wikipedia.org/wiki/Pitru_Paksha"),
                    ("Wikipedia · Shraddha", "https://en.wikipedia.org/wiki/Shraddha"),
                ],
            },
            {
                "name": "Vivāha (KP Wedding) · कश्मीरी पण्डित विवाह — Full Ritual",
                "icon": "",
                "timing": "Auspicious muhurtas (avoid Bhadra, Rahu Kaal, inauspicious nakshatras)",
                "desc": (
                    "Traditional KP wedding — a multi-day ritual combining Vedic, Shaiva and uniquely "
                    "Kashmiri elements. The purohit uses the Jantri to fix the muhurta.\n\n"
                    "── PRE-WEDDING RITUALS ──\n"
                    "Devgun (1–3 days before): invoke all family deities — Kul Devi, Kul Devta, "
                    "Naga (serpent), Ganesha, and Bhairava. "
                    "Puja Samagri: flowers, incense, panchamrit, coconut, red cloth (for Devi), "
                    "sindoor, fruits, paan, akshat (coloured rice), new clothes.\n\n"
                    "Lagan Ceremony (day before): Purohit arrives and ties the Lagan thread — "
                    "a sacred red/white cord fixed in the threshold. Recites the Muhurta Sankalpa. "
                    "Wanwun songs begin: elder women sing the Devgun Wanwun (Kashmiri songs invoking deities).\n\n"
                    "── WEDDING DAY ──\n"
                    "Groom's home — Sannaj (tilak ceremony): groom's forehead marked with kumkum, "
                    "chandan, akshat by maternal uncle. "
                    "Vardakshina: gifts from bride's family to groom's family.\n\n"
                    "Bride's home — Mehndi & Wanwun: "
                    "Henna applied; women sing Wanwun songs specific to each stage. "
                    "The song catalogue is enormous — different songs for: "
                    "dressing the bride, groom's arrival, Saptapadi, Vidai.\n\n"
                    "Pheran ceremony: bride dressed in traditional Pheran (long loose robe) "
                    "with Tarang (headpiece of gold/silver flowers) and Dejhour (earrings).\n\n"
                    "Vivaha Homa (sacred fire): Ganesha puja → Navagraha puja → Vivaha fire lit. "
                    "Kanyadan: father places daughter's right hand in groom's (Panigrahan). "
                    "Saptapadi: 7 steps around fire — each step = a vow:\n"
                    "1st: food/livelihood 2nd: strength 3rd: prosperity 4th: happiness "
                    "5th: children 6th: seasons/health 7th: eternal friendship.\n\n"
                    "Dejhour Exchange: unique KP custom — ornamental earrings (Dejhour) exchanged "
                    "between families as a bond of kinship.\n\n"
                    "── POST-WEDDING ──\n"
                    "Khon Batta (homecoming feast): bride enters groom's home, "
                    "steps on rice/flowers at threshold. "
                    "Wanwun Vidai songs: the most emotionally charged songs of the entire tradition.\n\n"
                    "Gotra verification: Both families' gotras must be different — "
                    "same-gotra marriage is strictly forbidden (sagotra vivaha varjya)."
                ),
                "links": [
                    ("Wikipedia · KP Customs", "https://en.wikipedia.org/wiki/Kashmiri_Pandits#Customs_and_traditions"),
                    ("iKashmir · Marriage", "https://www.ikashmir.net/marriage/"),
                    ("Wikipedia · Wanwun", "https://en.wikipedia.org/wiki/Wanwun"),
                ],
            },
            {
                "name": "Pann · पान्न — Winter Solstice Festival",
                "icon": "",
                "timing": "Around Makar Sankranti / winter solstice (Dec–Jan)",
                "desc": (
                    "Kashmiri winter solstice festival marking the sun's return (Uttarayana). "
                    "In Kashmir, this overlaps with the coldest period (Chillai Kalan — 40 coldest days).\n\n"
                    "Rituals and customs:\n"
                    "· Community bonfires (Alav) at night — families gather around fire, "
                    "songs are sung, the fire symbolises the returning sun.\n"
                    "· Til (sesame) offerings — til is sacred on this day: til laddoos (sesame balls), "
                    "til ka halwa, til mixed with jaggery distributed to all.\n"
                    "· Surya Puja: morning sun worship especially by KP families of Anantnag "
                    "(Martand Surya tradition).\n"
                    "· Ritual bath (snan) at dawn in the Vitasta (Jhelum) river.\n\n"
                    "Puja Samagri: Sesame seeds, jaggery (gud), flowers, water, red thread, "
                    "fruits, cow dung cakes (for the bonfire), ghee.\n\n"
                    "Puja Vidhi:\n"
                    "1. Pre-dawn bath in river or home.\n"
                    "2. Surya Arghya: offer water to the rising sun 3 times from cupped hands.\n"
                    "3. Recite Surya Stotram: 'Om Suryaya Namah / Aditya Hridayam' (Aditya Hridayam from Ramayana).\n"
                    "4. Light bonfire at dusk with family.\n"
                    "5. Distribute til-gud to neighbours and relatives (sweet = warmth/friendship).\n\n"
                    "KP saying: 'Pann on Pann, Shishur on Herath' — the walnut (Shishur) is associated "
                    "with Herath as sesame (til) is associated with Pann."
                ),
                "links": [
                    ("iKashmir · Festivals", "https://www.ikashmir.net/festivals/"),
                    ("Wikipedia · Makar Sankranti", "https://en.wikipedia.org/wiki/Makar_Sankranti"),
                ],
            },
            {
                "name": "Navratri Puja · नवरात्रि — Nine Nights of Devi",
                "icon": "",
                "timing": "Ashwina Shukla 1–9 (Sep–Oct) — main; also Chaitra Navratri (Mar–Apr)",
                "desc": (
                    "Nine nights of goddess worship — KPs observe both Ashwina and Chaitra Navratri. "
                    "Ashwina Navratri is the primary one.\n\n"
                    "KP Navratri sequence:\n"
                    "· Day 1: Kalash Sthapana (sacred water pot installed), Kul Devi invoked.\n"
                    "· Days 1–9: Daily Devi puja morning and evening. Many KPs fast (no grains, "
                    "eat fruits, samak rice, kuttu atta).\n"
                    "· Ashtami (Day 8): MOST important — Maha Puja of Kul Devi. Kanya Puja "
                    "(9 young girls worshipped as Navadurga). Homa (sacred fire) performed.\n"
                    "· Navami (Day 9): Maha Navami — weapons/tools worship (Ayudha Puja).\n\n"
                    "Puja Samagri:\n"
                    "· Kalash (copper/brass pot) with mango leaves and coconut\n"
                    "· Red cloth, red flowers (rose, hibiscus) · Sindoor · Kumkum\n"
                    "· Coconut (whole with husk) · Red chunri · Durva grass\n"
                    "· Panchamrit (milk, curd, ghee, honey, sugar) · Fruits · Halwa, puri, chana (for Kanya puja)\n"
                    "· Incense, ghee diya, camphor · Marigold garland · Betel leaves and nuts.\n\n"
                    "Puja Vidhi (Ashtami — most elaborate):\n"
                    "1. Kalash puja (water pot as Devi).\n"
                    "2. Shodasopachara Puja to Kul Devi image.\n"
                    "3. Durga Saptashati path (7 chapters) — or Devi Kavacham + Argala + Kilakam.\n"
                    "4. Kanya Puja: wash feet of 9 girls, offer food (puri, halwa, chana), tie red thread.\n"
                    "5. Homa with specific Devi mantras.\n"
                    "6. Aarti: 'Jai Ambe Gauri' or KP-specific Kul Devi aarti in Kashmiri.\n\n"
                    "Mantra: 'Om Aim Hreem Kleem Chamundayai Viche' (Devi Navarna Mantra)."
                ),
                "links": [
                    ("Wikipedia · Navratri", "https://en.wikipedia.org/wiki/Navratri"),
                    ("Durga Saptashati", "https://www.wisdomlib.org/hinduism/book/devi-mahatmya"),
                ],
            },
        ],
        "Sacred Sites & Temples · तीर्थ": [
            # ── KUL DEVI TEMPLES ──────────────────────────────────
            {
                "name": "Hari Parbat — Sharika Devi (Chakreshwari) · शारिका देवी, हरि पर्वत",
                "icon": "",
                "timing": "Year-round; Vaishakha Ashtami (Apr–May) is principal festival",
                "desc": (
                    "KUL DEVI TEMPLE · The principal Kul Devi of Srinagar and old-city KP families.\n"
                    "Location: Hari Parbat Hill, Srinagar · 34.1003°N 74.8305°E\n"
                    "Google Maps: https://maps.app.goo.gl/SharikaDevi\n\n"
                    "The hill IS the goddess — she took the form of a stone to crush the demon "
                    "Jalodbhava who lived in the primordial lake Satisar. "
                    "The Sri Chakra (sacred geometry of the goddess) is embedded in the hilltop rock. "
                    "Mughal fortification walls (Akbar era, 1590s) encircle the hill. "
                    "Also houses Makhdoom Sahib Sufi shrine on the northern slope.\n\n"
                    "Deity: Sharika Devi = Chakreshwari = 18-armed goddess holding the Sri Chakra\n"
                    "Gotra connection: Kashyapa, Vasishtha, and multiple KP lineages claim Sharika as Kul Devi\n"
                    "Puja: Milk/panchamrit abhisheka on the Sharika stone, red flowers, sindoor, coconut\n"
                    "Mantra: 'Om Sharikayai Namah' | 'Om Chakreshwaryai Namah'\n"
                    "Reference: Nilamata Purana (verses on Hari Parbat), Rajatarangini (Kalhana)"
                ),
                "links": [
                    ("Wikipedia · Hari Parbat", "https://en.wikipedia.org/wiki/Hari_Parbat"),
                    ("Wikipedia · Sharika Devi", "https://en.wikipedia.org/wiki/Sharika"),
                    ("Google Maps · Hari Parbat", "https://www.google.com/maps/search/Hari+Parbat+Srinagar"),
                    ("iKashmir · Sharika Temple", "https://www.ikashmir.net/temples/"),
                ],
            },
            {
                "name": "Kheer Bhawani — Ragnya Devi · खीर भवानी, तुलमुल (गंदेरबल)",
                "icon": "",
                "timing": "Year-round; Zyeth Ashtami (May–Jun) annual mela — most sacred day",
                "desc": (
                    "KUL DEVI TEMPLE · Most widely venerated Kul Devi across all KP families.\n"
                    "Location: Tullamulla (Tulmul) village, Ganderbal district · 34.2285°N 74.8090°E\n"
                    "Google Maps: https://www.google.com/maps/search/Kheer+Bhawani+Temple+Tulmul\n\n"
                    "Sacred spring of changing colour — white (peace), dark red (trouble), "
                    "black (great danger). Offerings of milk and kheer poured into the spring. "
                    "Built over an ancient Shakti spring mentioned in the Nilamata Purana. "
                    "Last major restoration by Maharaja Pratap Singh (early 20th century). "
                    "Multiple satellite Kheer Bhawani temples now exist in Jammu, Delhi, "
                    "Mumbai and KP diaspora cities worldwide.\n\n"
                    "Deity: Ragnya Devi = Bhagavati = Maharagya\n"
                    "Puja: Milk poured into spring → kheer → white flowers → red chunri → "
                    "Pradakshina → spring water on forehead\n"
                    "Mantra: 'Om Ragnyai Namah' | 'Om Maharaghyai Namah'\n"
                    "Stotra: Ksheer Bhawani Stotra (Sanskrit) recited by purohit at the spring"
                ),
                "links": [
                    ("Wikipedia · Kheer Bhawani", "https://en.wikipedia.org/wiki/Kheer_Bhawani"),
                    ("Google Maps · Kheer Bhawani Tulmul", "https://www.google.com/maps/search/Kheer+Bhawani+Tullamulla+Ganderbal"),
                    ("iKashmir · Tulmul", "https://www.ikashmir.net/tulamula/"),
                ],
            },
            {
                "name": "Jwala Devi — Khrew · ज्वाला देवी, खरेव (पुलवामा)",
                "icon": "",
                "timing": "Year-round; Navratri Ashtami (Mar–Apr & Sep–Oct) principal festival",
                "desc": (
                    "KUL DEVI TEMPLE · Principal Kul Devi of Pulwama, Pampore and south Kashmir KP families.\n"
                    "Location: Khrew village, Pulwama district · 33.8799°N 74.9800°E (approx.)\n"
                    "Google Maps: https://www.google.com/maps/search/Jwala+Devi+Temple+Khrew+Pulwama\n\n"
                    "The goddess manifests as a perpetual natural flame in the sanctum — "
                    "unique in Kashmir. Combines Shakta fire-goddess tradition with Kashmir Shaivism. "
                    "Navratri Ashtami draws thousands of KP pilgrims from across the valley.\n\n"
                    "Deity: Jwala Devi = Vahni Devi = flame manifestation of Shakti\n"
                    "Puja: Ghee offered into the flame (deepa puja), red flowers, sindoor, coconut\n"
                    "Pradakshina: 7 circumambulations\n"
                    "Mantra: 'Om Jwaladevyai Namah' | 'Om Agnijwalaayai Namah'"
                ),
                "links": [
                    ("Wikipedia · Jwaladevi Temple Khrew", "https://en.wikipedia.org/wiki/Jwaladevi_Temple,_Khrew"),
                    ("Google Maps · Jwala Devi Khrew", "https://www.google.com/maps/search/Jwala+Devi+Temple+Khrew+Kashmir"),
                ],
            },
            {
                "name": "Bhadrakali Temple, Anantnag · भद्रकाली, अनन्तनाग",
                "icon": "",
                "timing": "Year-round; Navratri and Ashtamis",
                "desc": (
                    "KUL DEVI TEMPLE · Kul Devi of Anantnag, Shopian and south Kashmir KP families.\n"
                    "Location: Anantnag district, south Kashmir · 33.7311°N 75.1487°E\n"
                    "Google Maps: https://www.google.com/maps/search/Bhadrakali+Temple+Anantnag\n\n"
                    "Bhadrakali (Bhadra = auspicious + Kali = fierce goddess) is a fierce form "
                    "of Shakti combining grace and power. Her cult is ancient in south Kashmir. "
                    "Multiple Bhadrakali temples exist across Anantnag and Shopian districts — "
                    "each neighbourhood (mohalla) has its own Bhadrakali shrine.\n\n"
                    "Deity: Bhadrakali = fierce Shakti who destroys evil and protects devotees\n"
                    "Puja: Red flowers, sindoor, coconut, goat sacrifice (in some traditions) "
                    "replaced by pumpkin sacrifice in most modern KP families\n"
                    "Mantra: 'Om Bhadrakalyai Namah' | 'Om Krim Kalyai Namah'"
                ),
                "links": [
                    ("Wikipedia · Bhadrakali", "https://en.wikipedia.org/wiki/Bhadrakali"),
                    ("Google Maps · Bhadrakali Anantnag", "https://www.google.com/maps/search/Bhadrakali+Temple+Anantnag+Kashmir"),
                ],
            },
            {
                "name": "Tripura Sundari — Devsar & Kulgam · त्रिपुरा सुन्दरी",
                "icon": "",
                "timing": "Year-round; Navratri",
                "desc": (
                    "KUL DEVI TEMPLE · Kul Devi of Kulgam, D.H. Pora and deep south Kashmir KP families.\n"
                    "Location: Devsar area, Kulgam district · 33.6443°N 75.0177°E\n"
                    "Google Maps: https://www.google.com/maps/search/Tripura+Sundari+Temple+Kulgam\n\n"
                    "Tripura Sundari (Shodashi) = the most beautiful in the three worlds. "
                    "One of the Dasha Mahavidyas (10 wisdom goddesses) in the Shakta tradition. "
                    "Her Sri Yantra is the most complex and sacred yantra in Tantra. "
                    "South Kashmir KP families with Kulgam ancestry venerate her as their primary Kul Devi.\n\n"
                    "Deity: Tripura Sundari = Shodashi = Lalita = supreme Shakti\n"
                    "Mantra: 'Om Aim Hreem Shreem Tripura Sundaryai Namah'\n"
                    "Reference: Lalita Sahasranama, Soundarya Lahari (Adi Shankaracharya)"
                ),
                "links": [
                    ("Wikipedia · Tripura Sundari", "https://en.wikipedia.org/wiki/Tripura_Sundari"),
                    ("Google Maps · Kulgam temples", "https://www.google.com/maps/search/ancient+temples+Kulgam+Kashmir"),
                ],
            },
            {
                "name": "Sharada Peeth · शारदा पीठ (Sharda, PoK) — Seat of Saraswati",
                "icon": "",
                "timing": "Sharada Navami (Ashwina Shukla 9) — proxy puja worldwide",
                "desc": (
                    "KUL DEVI / SHAKTI PITHA · Most sacred lost site of all Kashmiri Pandits.\n"
                    "Location: Sharda village, Neelum Valley, Pakistan-administered Kashmir (PoK)\n"
                    "Coordinates: 34.6745°N 73.9814°E (approximate)\n"
                    "Google Maps: https://www.google.com/maps/search/Sharda+Peeth+Neelum+Valley\n\n"
                    "One of the 18 Maha Shakti Pithas — Sati's right hand fell here. "
                    "Ancient seat of learning: library rivalling Nalanda, visited by scholars across Asia. "
                    "Adi Shankaracharya is said to have won the Sarvajnapitha debate here. "
                    "The Sharada script (ancient Kashmir script, ancestor of Gurmukhi) is named after this temple. "
                    "The Devi's form here: Sharada = 16-armed Saraswati holding veena, books, akshamala, kamandalu. "
                    "Annual proxy puja by KPs worldwide on Sharada Navami — "
                    "reciting 'Ya Sharada nilotpala-dala-shyama...'\n\n"
                    "Campaign: Sharda Peeth Trust India; cross-LoC pilgrimage access demanded annually."
                ),
                "links": [
                    ("Wikipedia · Sharada Peeth", "https://en.wikipedia.org/wiki/Sharada_Peeth"),
                    ("Google Maps · Sharda Village PoK", "https://www.google.com/maps/search/Sharda+village+Neelum+Valley+Azad+Kashmir"),
                    ("Wikipedia · Sharada script", "https://en.wikipedia.org/wiki/Sharada_script"),
                ],
            },
            {
                "name": "Vaishno Devi · वैष्णो देवी, त्रिकूट पर्वत (रियासी)",
                "icon": "",
                "timing": "Year-round; Navratri most sacred — 8–10 million pilgrims annually",
                "desc": (
                    "KUL DEVI / SHAKTI PITHA · Kul Devi of many KP families from Jammu region.\n"
                    "Location: Trikuta Hills, Reasi district, Jammu · 32.9760°N 74.9525°E\n"
                    "Google Maps: https://www.google.com/maps/search/Vaishno+Devi+Temple+Katra\n\n"
                    "One of India's most visited pilgrimage sites. The goddess resides in a natural "
                    "cave as three pindis (rocks) representing Maha Kali, Maha Lakshmi and Maha Saraswati. "
                    "The cave is reached after a 14km trek from Katra base camp. "
                    "Bhairon Mandir (at Bhairo Ghati, 2.5km from cave) is mandatory for complete pilgrimage — "
                    "'Yatra is incomplete without Bhairon darshan.'\n\n"
                    "Mantra: 'Jai Mata Di' | 'Om Aim Hreem Kleem Mahalakshmyai Namah'\n"
                    "Official board: Shri Mata Vaishno Devi Shrine Board"
                ),
                "links": [
                    ("Wikipedia · Vaishno Devi", "https://en.wikipedia.org/wiki/Vaishno_Devi"),
                    ("Official Shrine Board", "https://www.maavaishnodevi.org/"),
                    ("Google Maps · Vaishno Devi", "https://www.google.com/maps/search/Vaishno+Devi+Shrine+Katra"),
                ],
            },
            # ── MAJOR SHIVA TEMPLES ──────────────────────────────
            {
                "name": "Shankaracharya Temple (Jyeshtheshwara) · ज्येष्ठेश्वर, गोपाद्रि पर्वत",
                "icon": "",
                "timing": "Year-round; Herath night vigil most sacred",
                "desc": (
                    "SHIVA TEMPLE · Presiding Shiva of Srinagar city.\n"
                    "Location: Shankaracharya Hill (Gopadri/Takht-i-Suleiman), Srinagar · 34.0888°N 74.8601°E\n"
                    "Google Maps: https://www.google.com/maps/search/Shankaracharya+Temple+Srinagar\n\n"
                    "The octagonal stone temple at 1,000m — one of the oldest temples in Kashmir. "
                    "Original structure: King Gopaditya (Kaliyuga 2526 = c. 371 BCE per Rajatarangini). "
                    "Present form: 9th–10th century CE. Deity: Jyeshtheshwara = Lord of Elders = Shiva. "
                    "Vasugupta received the Shiva Sutras near this hill. "
                    "On Herath night: thousands of KPs climb the hill for the all-night vigil — "
                    "the view of Srinagar's lights from the top is a quintessentially Kashmiri experience.\n\n"
                    "Mantra: 'Om Jyeshtheshwaraya Namah'\n"
                    "Reference: Rajatarangini (Kalhana, Book 1), Nilamata Purana"
                ),
                "links": [
                    ("Wikipedia · Shankaracharya Temple", "https://en.wikipedia.org/wiki/Shankaracharya_temple,_Srinagar"),
                    ("Google Maps · Shankaracharya Hill", "https://www.google.com/maps/search/Shankaracharya+temple+Gopadri+hill+Srinagar"),
                ],
            },
            {
                "name": "Amarnath Cave Temple · अमरनाथ (पहलगाम/बालटाल)",
                "icon": "",
                "timing": "Annual Yatra: Shravana Purnima (Jul–Aug) · 3,888m altitude",
                "desc": (
                    "SHIVA PILGRIMAGE · Most sacred Himalayan Shiva shrine.\n"
                    "Location: South Kashmir Himalayas · 34.2144°N 75.5028°E\n"
                    "Google Maps: https://www.google.com/maps/search/Amarnath+Cave+Temple+Kashmir\n\n"
                    "Natural ice Shivalinga waxes and wanes with the moon. "
                    "Two white pigeons (immortal devotees per legend) seen in the cave every year. "
                    "Routes: Pahalgam via Chandanwari → Sheshnag → Panchtarni → Cave (45km, 4 days); "
                    "Baltal → Cave (14km, steep, 1 day). "
                    "Chhari Mubarak (holy mace) procession from Dashnami Akhara, Srinagar precedes Yatra. "
                    "KPs must perform this Yatra at least once in lifetime.\n\n"
                    "Mantra: 'Om Namah Shivaya' | Mrityunjaya Japa at the cave\n"
                    "Official: Shri Amarnathji Shrine Board (shriamarnathjishrine.com)"
                ),
                "links": [
                    ("Wikipedia · Amarnath", "https://en.wikipedia.org/wiki/Amarnath_temple"),
                    ("Official Shrine Board", "https://shriamarnathjishrine.com/"),
                    ("Google Maps · Amarnath Cave", "https://www.google.com/maps/search/Amarnath+Cave+shrine+Pahalgam"),
                ],
            },
            {
                "name": "Bijbehara Shiva Temple (Vijeshvara) · विजेश्वर, बिजबेहाड़ा",
                "icon": "",
                "timing": "Year-round; Shivratri and Herath",
                "desc": (
                    "SHIVA TEMPLE · One of the most ancient Shiva temples in Kashmir.\n"
                    "Location: Bijbehara, Anantnag district · 33.9137°N 75.0120°E\n"
                    "Google Maps: https://www.google.com/maps/search/Vijeshvara+temple+Bijbehara+Anantnag\n\n"
                    "Vijeshvara (= Shiva as the Lord of Heroes) is one of the principal Shiva shrines "
                    "of Anantnag district. The temple is mentioned in early medieval Kashmir texts. "
                    "The town Bijbehara is an ancient KP settlement with a history dating back over 2000 years. "
                    "The Vitasta (Jhelum) flows near the temple.\n\n"
                    "Mantra: 'Om Vijeshvaraya Namah'\n"
                    "Reference: Nilamata Purana, Rajatarangini"
                ),
                "links": [
                    ("Wikipedia · Bijbehara", "https://en.wikipedia.org/wiki/Bijbehara"),
                    ("Google Maps · Bijbehara temple", "https://www.google.com/maps/search/ancient+temple+Bijbehara+Anantnag"),
                ],
            },
            {
                "name": "Shiva Temple — Baramulla (Varahamula) · वराहमूल शिव मन्दिर",
                "icon": "",
                "timing": "Year-round",
                "desc": (
                    "SHIVA TEMPLE · Ancient Shiva shrine at Baramulla, north Kashmir.\n"
                    "Location: Baramulla town · 34.2099°N 74.3450°E\n"
                    "Google Maps: https://www.google.com/maps/search/Shiva+Temple+Baramulla+Kashmir\n\n"
                    "Baramulla = Varahamula (Varaha's snout) — where Varaha (Vishnu's boar avatar) "
                    "struck the Himalayan range to release the waters of Satisar lake, "
                    "creating the Kashmir Valley (Nilamata Purana mythology). "
                    "The Vitasta (Jhelum) exits the valley through Baramulla. "
                    "Multiple ancient Shiva and Vishnu temples historically dotted this town.\n\n"
                    "Reference: Nilamata Purana (Varahamula section), Rajatarangini"
                ),
                "links": [
                    ("Wikipedia · Baramulla", "https://en.wikipedia.org/wiki/Baramulla"),
                    ("Google Maps · Baramulla temples", "https://www.google.com/maps/search/ancient+temple+Baramulla+Kashmir"),
                ],
            },
            # ── SURYA / VISHNU TEMPLES ────────────────────────────
            {
                "name": "Martand Sun Temple · मार्तण्ड सूर्य मन्दिर, मट्टन (अनन्तनाग)",
                "icon": "",
                "timing": "Sunrise visits; Ratha Saptami (Magha Shukla 7) most sacred",
                "desc": (
                    "SURYA TEMPLE · Greatest Surya temple of ancient India.\n"
                    "Location: Mattan, Anantnag district · 33.7583°N 75.2145°E\n"
                    "Google Maps: https://www.google.com/maps/search/Martand+Sun+Temple+Mattan+Anantnag\n\n"
                    "Built by King Lalitaditya Muktapida (c. 724–760 CE) of the Karkota dynasty. "
                    "Main sanctum flanked by 84 smaller shrines. "
                    "Temple faces east — equinox sunrise illuminates the inner sanctum precisely. "
                    "Destroyed by Sultan Sikandar (Butshikan) c. 1400 CE. "
                    "Ruins are among the finest examples of Kashmiri temple architecture. "
                    "ASI protected monument.\n\n"
                    "Deity: Martanda Surya (the immortal sun)\n"
                    "Puja: Arghya to the rising sun, Aditya Hridayam recitation\n"
                    "Mantra: 'Om Suryaya Namah' | 'Om Mitraya Namah'\n"
                    "Reference: Rajatarangini (Book 4, Lalitaditya's reign)"
                ),
                "links": [
                    ("Wikipedia · Martand Sun Temple", "https://en.wikipedia.org/wiki/Martand_Sun_Temple"),
                    ("Google Maps · Martand Temple", "https://www.google.com/maps/search/Martand+Sun+Temple+Kashmir"),
                    ("ASI Kashmir", "https://asi.nic.in/"),
                ],
            },
            {
                "name": "Awantiswara & Awantishwamin · अवन्तिस्वर और अवन्तिस्वामिन (अवन्तिपोर)",
                "icon": "",
                "timing": "Year-round; Shivratri (Awantiswara) and Ekadashi (Awantishwamin)",
                "desc": (
                    "SHIVA + VISHNU TEMPLES · Twin 9th century temples — finest pre-Islamic Kashmir architecture.\n"
                    "Location: Awantipora, Pulwama district · 33.9225°N 75.0140°E\n"
                    "Google Maps: https://www.google.com/maps/search/Avantiswara+temple+Awantipora\n\n"
                    "Built by King Awantivarman (855–883 CE) of the Utpala dynasty. "
                    "Awantiswara: Shiva temple (south side of road). "
                    "Awantishwamin: Vishnu temple (north side of road). "
                    "Both temples display the mature Kashmiri temple style — "
                    "trefoil arched niches, carved friezes, peristyle colonnades. "
                    "Now in ruins but magnificent; ASI protected.\n\n"
                    "Mantra (Awantiswara): 'Om Awanteshwaraya Namah'\n"
                    "Mantra (Awantishwamin): 'Om Awantishwamine Namah' (Vishnu)\n"
                    "Reference: Rajatarangini Book 5 (Awantivarman's reign), ASI documentation"
                ),
                "links": [
                    ("Wikipedia · Avantiswara", "https://en.wikipedia.org/wiki/Avantiswara_temple"),
                    ("Google Maps · Avantiswara Awantipora", "https://www.google.com/maps/search/Avantiswara+Awantipora+Pulwama"),
                    ("ASI Kashmir circles", "https://asi.nic.in/"),
                ],
            },
            # ── NAG TEMPLES (SACRED SPRINGS) ─────────────────────
            {
                "name": "Nag Temples — Nagbal · नागबल (गंदेरबल)",
                "icon": "",
                "timing": "Nag Panchami (Shravana Shukla 5) most sacred; year-round",
                "desc": (
                    "NAG TIRTHA · Sacred Naga (serpent deity) spring — one of the most important in Kashmir.\n"
                    "Location: Nagbal area, Ganderbal district · Near Srinagar-Leh highway\n"
                    "Google Maps: https://www.google.com/maps/search/Nagbal+spring+Ganderbal+Kashmir\n\n"
                    "Kashmir has dozens of sacred Naga springs (Nagas are water deities in Nilamata Purana). "
                    "The Nilamata Purana lists 527 Naga tirthas in Kashmir! "
                    "Major Naga tirthas: Nagbal, Anantanag (the spring that gave Anantnag its name), "
                    "Nandikund, Vasukikund, Takshakakund. "
                    "KPs perform Nag Puja on Nag Panchami — offer milk to the Naga spring, "
                    "tie sacred thread, offer flowers.\n\n"
                    "Anantnag = 'Ananta-nag' = the spring of Ananta (the infinite serpent/Shiva).\n\n"
                    "Mantra: 'Om Namo Bhagavate Anantaya' | 'Om Nagaya Namah'\n"
                    "Nag Puja items: Milk, flowers, durva grass, silver Naga image\n"
                    "Reference: Nilamata Purana (Naga section — over 300 verses on Naga worship)"
                ),
                "links": [
                    ("Wikipedia · Nag Panchami", "https://en.wikipedia.org/wiki/Nag_Panchami"),
                    ("Google Maps · Nagbal", "https://www.google.com/maps/search/Nagbal+Ganderbal+Kashmir"),
                    ("Nilamata Purana · Naga tirthas", "https://www.wisdomlib.org/hinduism/book/nilamata-purana"),
                ],
            },
            {
                "name": "Anantnag Spring (Nagin / Nag Tirtha) · अनन्तनाग नाग तीर्थ",
                "icon": "",
                "timing": "Nag Panchami; year-round pilgrimage",
                "desc": (
                    "NAG TIRTHA · The ancient spring that gave Anantnag city its name.\n"
                    "Location: Anantnag town centre · 33.7311°N 75.1487°E\n"
                    "Google Maps: https://www.google.com/maps/search/Anantanag+spring+Anantnag\n\n"
                    "Anantnag = Ananta (the infinite Naga/Shiva) + Nag (spring/serpent deity). "
                    "The original spring (natural bubbling spring) was one of the most sacred "
                    "Naga tirthas in the Nilamata Purana. Multiple ancient temples surrounded the spring. "
                    "The Vitasta (Jhelum) flows nearby. "
                    "South Kashmir KP families from Anantnag consider this their ancestral sacred spring. "
                    "Nag Panchami puja: milk, flowers, silver Naga idol offered at the spring.\n\n"
                    "Reference: Nilamata Purana · Rajatarangini"
                ),
                "links": [
                    ("Wikipedia · Anantnag", "https://en.wikipedia.org/wiki/Anantnag"),
                    ("Google Maps · Anantnag city", "https://www.google.com/maps/search/Anantnag+spring+Kashmir"),
                ],
            },
            {
                "name": "Verinag Spring (Vitasta source) · वेरीनाग, वितस्ता उद्गम",
                "icon": "",
                "timing": "Vitasta Jayanti; year-round pilgrimage",
                "desc": (
                    "NAG / RIVER TIRTHA · Source spring of the river Vitasta (Jhelum) — most sacred spring in Kashmir.\n"
                    "Location: Verinag, Anantnag district · 33.5345°N 75.2590°E\n"
                    "Google Maps: https://www.google.com/maps/search/Verinag+Spring+Anantnag+Kashmir\n\n"
                    "The source spring of the Vitasta (Jhelum) — a natural octagonal spring of "
                    "crystal-clear blue water. Visible fish at the bottom. "
                    "Emperor Jahangir built a beautiful Mughal garden and octagonal masonry spring here (1620). "
                    "KPs come here to collect sacred Vitasta water for ceremonies. "
                    "Vitasta Jayanti is observed annually — puja at the spring source. "
                    "The Nilamata Purana dedicates major sections to Vitasta worship — "
                    "she is the 'mother' of Kashmir.\n\n"
                    "Mantra: 'Om Vitastayai Namah' | Vitasta Stotra (Nilamata Purana)\n"
                    "Significance: Vitasta water is used in all major KP rituals — Herath, Shraddha, Vivaha"
                ),
                "links": [
                    ("Wikipedia · Verinag", "https://en.wikipedia.org/wiki/Verinag"),
                    ("Google Maps · Verinag Spring", "https://www.google.com/maps/search/Verinag+spring+source+Jhelum"),
                    ("Nilamata Purana", "https://www.wisdomlib.org/hinduism/book/nilamata-purana"),
                ],
            },
            # ── SACRED SPRINGS & GARDENS ─────────────────────────
            {
                "name": "Achabal Spring & Gardens · अचाबल (अनन्तनाग)",
                "icon": "",
                "timing": "Year-round; spring (Vasanta) most beautiful",
                "desc": (
                    "SACRED SPRING & GARDEN · Ancient Naga tirtha and Mughal garden.\n"
                    "Location: Achabal, Anantnag district · 33.6310°N 75.2040°E\n"
                    "Google Maps: https://www.google.com/maps/search/Achabal+Spring+Garden+Anantnag\n\n"
                    "Achabal (= Achibal = Akshivahal = 'the eye of the valley') — "
                    "an ancient sacred spring mentioned in the Rajatarangini. "
                    "The spring gushes from beneath a cliff at extraordinary volume. "
                    "Mughal Empress Nur Jahan developed it into a terraced garden (early 17th century). "
                    "The spring is considered a Naga tirtha by KP tradition — "
                    "Nag Panchami puja observed here. "
                    "Natural setting: plane trees (chinar), willows, water channels (nalas).\n\n"
                    "Reference: Rajatarangini, Ain-i-Akbari (Abul Fazl's record of Mughal Kashmir)"
                ),
                "links": [
                    ("Wikipedia · Achabal", "https://en.wikipedia.org/wiki/Achabal"),
                    ("Google Maps · Achabal", "https://www.google.com/maps/search/Achabal+garden+spring+Anantnag"),
                ],
            },
            {
                "name": "Kokernag Springs · कोकरनाग (अनन्तनाग)",
                "icon": "",
                "timing": "Year-round; spring most sacred",
                "desc": (
                    "SACRED SPRINGS · Ancient Naga tirthas and most prolific spring complex in Kashmir.\n"
                    "Location: Kokernag, Anantnag district · 33.5736°N 75.2650°E\n"
                    "Google Maps: https://www.google.com/maps/search/Kokernag+Springs+Anantnag+Kashmir\n\n"
                    "Kokernag = Kakanaag = the snake of Kaka (an ancient Naga deity). "
                    "The largest natural spring complex in Kashmir Valley — 70+ springs in one area. "
                    "The water is exceptionally pure and cold — a sacred bathing tirtha. "
                    "Ancient KP tradition: ritual bath at Kokernag on auspicious occasions. "
                    "Multiple Shiva and Naga shrines surround the springs.\n\n"
                    "Reference: Rajatarangini (Kalhana mentions multiple springs), Nilamata Purana"
                ),
                "links": [
                    ("Wikipedia · Kokernag", "https://en.wikipedia.org/wiki/Kokernag"),
                    ("Google Maps · Kokernag", "https://www.google.com/maps/search/Kokernag+springs+Kashmir"),
                ],
            },
            # ── BHAIRAVA TEMPLES ─────────────────────────────────
            {
                "name": "Anandeshwara Bhairava · आनन्देश्वर भैरव (श्रीनगर — अमीरा कदल / सत्थू बर्बर शाह)",
                "icon": "",
                "timing": "Year-round; Herath night most sacred",
                "desc": (
                    "BHAIRAVA TEMPLE · Guardian of central Srinagar — Amira Kadal, Ganpatyar, Maisuma area.\n"
                    "Location: Central Srinagar (Sathu Barbar Shah / Amira Kadal area) · 34.0800°N 74.8050°E\n"
                    "Google Maps: https://www.google.com/maps/search/Anandeshwara+Bhairava+temple+Srinagar\n\n"
                    "One of the 8 Ashta Bhairavas of Kashmir — guards the North-East direction. "
                    "Anandeshwara = Lord of Bliss (Ananda = bliss + Ishwara = Lord = Shiva as Bhairava). "
                    "Patron Bhairava of central Srinagar KP families from Amira Kadal and Ganpatyar mohallas. "
                    "Worshipped on Herath night: special Vatuk (child Bhairava) puja alongside Vatak Puja. "
                    "Puja: bilva leaves, blue flowers, til, sesame, blood-red sindoor\n\n"
                    "Mantra: 'Om Hreem Anandeshwaraya Bhairavaya Namah'\n"
                    "Reference: Nilamata Purana (Ashta Bhairava section)"
                ),
                "links": [
                    ("Wikipedia · Bhairava Kashmir", "https://en.wikipedia.org/wiki/Bhairava"),
                    ("Google Maps · Srinagar Bhairava temples", "https://www.google.com/maps/search/Bhairava+temple+Srinagar+Kashmir"),
                    ("iKashmir · Bhairava temples", "https://www.ikashmir.net/temples/bhairav.html"),
                ],
            },
            {
                "name": "Tushkaraja Bhairava · तुष्करराज भैरव (हब्बा कदल / दूध गंगा)",
                "icon": "",
                "timing": "Year-round; Herath night",
                "desc": (
                    "BHAIRAVA TEMPLE · Guardian of Habba Kadal and Doodh Ganga confluence.\n"
                    "Location: Habba Kadal area, Srinagar · 34.0900°N 74.8100°E\n"
                    "Google Maps: https://www.google.com/maps/search/Habba+Kadal+Bhairava+temple+Srinagar\n\n"
                    "Also called Turushkaraja Bhairava. Guards the East direction — "
                    "one of the 8 Ashta Bhairavas. Patron of Habba Kadal mohalla KP families, "
                    "one of the most densely KP-populated areas of old Srinagar. "
                    "The Doodh Ganga (Milk Ganga) stream flows nearby — sacred to KPs.\n\n"
                    "Mantra: 'Om Hreem Tushkarajaya Bhairavaya Namah'\n"
                    "Reference: Nilamata Purana, iKashmir Bhairava documentation"
                ),
                "links": [
                    ("iKashmir · Bhairavas", "https://www.ikashmir.net/temples/bhairav.html"),
                    ("Google Maps · Habba Kadal", "https://www.google.com/maps/search/Habba+Kadal+bridge+Srinagar"),
                ],
            },
            {
                "name": "Mangalaraja Bhairava · मंगलराज भैरव (फ़तेह कदल / ज़ैन कदल / बोहरी कदल)",
                "icon": "",
                "timing": "Year-round; Herath night",
                "desc": (
                    "BHAIRAVA TEMPLE · Guardian of the old-city kadal (bridge) belt.\n"
                    "Location: Fateh Kadal / Zaina Kadal / Bohri Kadal area, Srinagar\n"
                    "Google Maps: https://www.google.com/maps/search/Fateh+Kadal+Srinagar+temple\n\n"
                    "Also Mangaleshwara Bhairava. Guards the South-West direction. "
                    "Patron of the Fateh Kadal, Zaina Kadal and Bohri Kadal KP families — "
                    "historically among the most prestigious KP mohallas of Srinagar. "
                    "Rupa Bhawani's shrine is at Fateh Kadal — Mangalaraja Bhairava "
                    "is the protector deity of the same area.\n\n"
                    "Mantra: 'Om Hreem Mangalarajaya Bhairavaya Namah'"
                ),
                "links": [
                    ("iKashmir · Bhairava temples", "https://www.ikashmir.net/temples/bhairav.html"),
                    ("Google Maps · Zaina Kadal Srinagar", "https://www.google.com/maps/search/Zaina+Kadal+Srinagar+Kashmir"),
                ],
            },
            {
                "name": "Nandikeshwara Bhairava · नन्दिकेश्वर भैरव, सुम्बल (बांदीपोर)",
                "icon": "",
                "timing": "Year-round; Shivratri and Herath",
                "desc": (
                    "BHAIRAVA / SHIVA TEMPLE · Guardian Bhairava of Bandipora and Sumbal area.\n"
                    "Location: Sumbal, Bandipora district · 34.1500°N 74.6500°E\n"
                    "Google Maps: https://www.google.com/maps/search/Nandikeshwar+temple+Sumbal+Bandipora\n\n"
                    "Nandikeshwara = Nandi (Shiva's bull) + Ishwara (Lord) — Shiva as the Lord of Nandi. "
                    "Also known as Nandkishor / Nandkeshwar Bhairava. "
                    "Principal guardian deity (Kshetrapala) of Bandipora and Sumbal KP families. "
                    "The temple is at a scenic location near the Wular Lake shore.\n\n"
                    "Mantra: 'Om Nandikeshwaraya Namah' | 'Om Nandikeshwaraya Bhairavaya Namah'\n"
                    "Reference: iKashmir local Bhairava documentation"
                ),
                "links": [
                    ("iKashmir · Bhairava temples", "https://www.ikashmir.net/temples/bhairav.html"),
                    ("Google Maps · Sumbal Bandipora", "https://www.google.com/maps/search/Sumbal+Bandipora+Kashmir"),
                ],
            },
            {
                "name": "Bhuteshwara Bhairava · भूतेश्वर भैरव, तुलमुल (गंदेरबल)",
                "icon": "",
                "timing": "Year-round; especially at Zyeth Ashtami mela",
                "desc": (
                    "BHAIRAVA TEMPLE · Guardian Bhairava of Tulmul and Kheer Bhawani area.\n"
                    "Location: Tullamulla, Ganderbal district · near Kheer Bhawani temple\n"
                    "Google Maps: https://www.google.com/maps/search/Bhuteshwara+Bhairava+Tulmul+Ganderbal\n\n"
                    "Bhuteshwara = Lord of Spirits (Bhuta = spirit/element + Ishwara = Lord). "
                    "Guards the Tulmul-Kheer Bhawani sacred complex. "
                    "Worshipped alongside Ragnya Devi (Kheer Bhawani) on Zyeth Ashtami. "
                    "His puja is performed before entering the Kheer Bhawani sanctum "
                    "in traditional KP practice.\n\n"
                    "Mantra: 'Om Bhuteshwaraya Namah' | 'Om Bhuteshwaraya Bhairavaya Namah'"
                ),
                "links": [
                    ("iKashmir · Bhairava documentation", "https://www.ikashmir.net/temples/bhairav.html"),
                    ("Google Maps · Tulmul Ganderbal", "https://www.google.com/maps/search/Tullamulla+Ganderbal+Kashmir"),
                ],
            },
            {
                "name": "Batuka Bhairava · बटुक भैरव (सर्वत्र — सभी KP घरों में)",
                "icon": "",
                "timing": "Herath (principal); all Bhairava pujas; daily worship in many KP homes",
                "desc": (
                    "BHAIRAVA DEITY · Universal child-form of Bhairava — worshipped in every KP home.\n"
                    "Not a fixed temple — present in every KP household shrine and all Herath rituals.\n"
                    "Google Maps: N/A — universal household deity\n\n"
                    "Batuka = child/boy. Batuka Bhairava is the most approachable, most beloved "
                    "form of Bhairava — a child-god who protects like a fierce guardian but is "
                    "worshipped with the tenderness given to a child. "
                    "Central to the Herath (Kashmiri Shivratri) ritual: "
                    "a small clay pot (separate from the 12 Vatak pots) is installed as Batuka Bhairava "
                    "and receives first puja. The all-night Herath vigil is dedicated to Batuka.\n\n"
                    "Puja: Small clay pot + sacred water + walnut twig + tilak of sindoor\n"
                    "Mantra: 'Om Hreem Batukaya Apadudharanaya Kuru Kuru Batukaya Hreem'\n"
                    "Reference: Svacchanda Tantra (Batuka Bhairava section), Herath ritual manuals"
                ),
                "links": [
                    ("Wikipedia · Bhairava", "https://en.wikipedia.org/wiki/Bhairava"),
                    ("Wisdomlib · Batuka", "https://www.wisdomlib.org/definition/batuka"),
                ],
            },
            # ── PANDAVA SITES ─────────────────────────────────────
            {
                "name": "Pandava Temples — Pahalgam area · पाण्डव मन्दिर (पहलगाम / लिद्दर घाटी)",
                "icon": "",
                "timing": "Year-round; Amarnath Yatra season",
                "desc": (
                    "PANDAVA PILGRIMAGE SITES · Multiple sites associated with the Pandavas in Pahalgam area.\n"
                    "Location: Pahalgam, Anantnag district · 34.0158°N 75.3128°E\n"
                    "Google Maps: https://www.google.com/maps/search/Pandava+temple+Pahalgam+Kashmir\n\n"
                    "According to local tradition and the Mahabharata's Tirthayatra Parva, "
                    "the Pandavas passed through Kashmir during their pilgrimage. "
                    "Sites associated with Pandavas in the Lidder Valley (Pahalgam area):\n"
                    "· Mamleshwar temple at Pahalgam — Shiva temple said to have been "
                    "established by Bhima\n"
                    "· Sheshnag Lake (3,590m) — on Amarnath route; sacred serpent lake "
                    "believed to be the abode of Sheshnaga seen by Pandavas\n"
                    "· Panchtarni ('five rivers') — where the Pandavas are said to have camped\n"
                    "· Tulian Lake — associated with Yudhishthira's meditation\n\n"
                    "Reference: Mahabharata Tirthayatra Parva, local Rajatarangini annotations"
                ),
                "links": [
                    ("Wikipedia · Pahalgam", "https://en.wikipedia.org/wiki/Pahalgam"),
                    ("Google Maps · Pahalgam temples", "https://www.google.com/maps/search/ancient+temples+Pahalgam+Kashmir"),
                    ("Wikipedia · Sheshnag Lake", "https://en.wikipedia.org/wiki/Sheshnag_Lake"),
                ],
            },
            {
                "name": "Pandava Temples — Kishtwar · पाण्डव मन्दिर, किश्तवाड़",
                "icon": "",
                "timing": "Year-round",
                "desc": (
                    "PANDAVA PILGRIMAGE SITES · Kishtwar district sites associated with Pandavas.\n"
                    "Location: Kishtwar district · 33.3130°N 75.7660°E\n"
                    "Google Maps: https://www.google.com/maps/search/Pandava+temple+Kishtwar+Jammu+Kashmir\n\n"
                    "Kishtwar (ancient Kashyapapur) has multiple sites associated with Pandava passage: "
                    "· Sarthal Devi temple — goddess temple of great antiquity; "
                    "associated with local Pandava legends\n"
                    "· Natural rock formations identified locally as 'Pandava footprints'\n"
                    "· Machail Mata temple — Chandi Mata temple in remote mountains; "
                    "annual Yatra in August draws thousands\n"
                    "KP families from Kishtwar have strong Pandava-site veneration traditions.\n\n"
                    "Reference: Local oral histories, J&K Archaeological Survey records"
                ),
                "links": [
                    ("Wikipedia · Kishtwar", "https://en.wikipedia.org/wiki/Kishtwar"),
                    ("Google Maps · Kishtwar temples", "https://www.google.com/maps/search/ancient+temple+Kishtwar+Kashmir"),
                    ("Wikipedia · Machail Mata", "https://en.wikipedia.org/wiki/Chandi_Mata_Temple,_Machail"),
                ],
            },
            # ── SAINT SHRINES ─────────────────────────────────────
            {
                "name": "Bhagwan Gopinath Shrine · भगवान गोपीनाथ समाधि, रैनावारी (श्रीनगर)",
                "icon": "",
                "timing": "Year-round; Gopinath Jayanti (annual)",
                "desc": (
                    "SAINT SHRINE · Shrine of the most beloved modern KP saint (1898–1968).\n"
                    "Location: Rainawari, Srinagar · 34.1002°N 74.8141°E\n"
                    "Google Maps: https://www.google.com/maps/search/Bhagwan+Gopinath+Shrine+Rainawari+Srinagar\n\n"
                    "Bhagwan Gopinath Ji — modern Kashmiri Shaiva saint who embodied Pratyabhijña "
                    "(recognition of Shiva in oneself). His samadhi (resting place) at Rainawari "
                    "is an active pilgrimage site visited by KPs from across the diaspora. "
                    "Devotees experience peace and blessings at the shrine. "
                    "Annual Gopinath Jayanti observed by KP community worldwide. "
                    "His teachings: silent transmission of Shiva-consciousness through darshan.\n\n"
                    "Reference: 'Bhagwan Gopinath: The Divine Flame' (KP community publications)\n"
                    "Website: gopinathji.com"
                ),
                "links": [
                    ("Wikipedia · Bhagwan Gopinath", "https://en.wikipedia.org/wiki/Bhagwan_Gopinath"),
                    ("Google Maps · Rainawari Srinagar", "https://www.google.com/maps/search/Bhagwan+Gopinath+mandir+Rainawari+Srinagar"),
                ],
            },
            {
                "name": "Rupa Bhawani Shrine · रूपा भवानी मन्दिर, फ़तेह कदल (श्रीनगर)",
                "icon": "",
                "timing": "Year-round; Rupa Bhawani Jayanti (annual)",
                "desc": (
                    "SAINT SHRINE · Shrine of Devi Rupa Bhawani (1625–1721 CE).\n"
                    "Location: Fateh Kadal, Srinagar · 34.0830°N 74.8040°E\n"
                    "Google Maps: https://www.google.com/maps/search/Rupa+Bhawani+temple+Fateh+Kadal+Srinagar\n\n"
                    "Rupa Bhawani — Kashmiri Shakti saint and mystic poetess. "
                    "Her shrine at Fateh Kadal is one of the most revered KP sites in Srinagar. "
                    "Devotees come for blessings, especially women seeking guidance and spiritual protection. "
                    "Her Vakhs are recited at the shrine. "
                    "A second shrine is at Rainawari, Srinagar. "
                    "Rupa Bhawani Jayanti draws large gatherings of KP devotees.\n\n"
                    "Mantra: 'Om Rupa Bhawanyai Namah'"
                ),
                "links": [
                    ("Wikipedia · Rupa Bhawani", "https://en.wikipedia.org/wiki/Rupa_Bhawani"),
                    ("Google Maps · Fateh Kadal Srinagar", "https://www.google.com/maps/search/Fateh+Kadal+Srinagar+temple"),
                ],
            },
            {
                "name": "Swami Lakshmanjoo Ashram · स्वामी लक्ष्मण जू आश्रम, इशबर (श्रीनगर)",
                "icon": "",
                "timing": "Year-round; Guru Purnima most significant",
                "desc": (
                    "SAINT ASHRAM · Ashram of the last great master of Kashmir Shaivism (1907–1991).\n"
                    "Location: Ishber, Nishat, Srinagar · 34.1240°N 74.8810°E\n"
                    "Google Maps: https://www.google.com/maps/search/Swami+Lakshmanjoo+Ashram+Ishber+Srinagar\n\n"
                    "Swami Lakshmanjoo spent his entire life in Srinagar — never leaving Kashmir. "
                    "His ashram at Ishber (near Nishat, Dal Lake shore) is still active. "
                    "The Universal Shaiva Fellowship maintains the ashram and Swamiji's memory. "
                    "200+ hours of his recorded lectures are available online. "
                    "Serious students of Kashmir Shaivism make pilgrimage to this ashram. "
                    "His library and manuscripts are preserved here.\n\n"
                    "Website: lakshmanjoo.com | universalshaivafelllowship.org"
                ),
                "links": [
                    ("Wikipedia · Swami Lakshmanjoo", "https://en.wikipedia.org/wiki/Swami_Lakshmanjoo"),
                    ("Universal Shaiva Fellowship", "https://www.universalshaivafelllowship.org/"),
                    ("Google Maps · Nishat Srinagar", "https://www.google.com/maps/search/Ishber+Nishat+Srinagar+Kashmir"),
                ],
            },
            # ── OTHER MAJOR ANCIENT TEMPLES ──────────────────────
            {
                "name": "Ganesh Temple — Ganpatyar · गणपत्यार (श्रीनगर)",
                "icon": "",
                "timing": "Year-round; Ganesh Chaturthi and all new beginnings",
                "desc": (
                    "GANESHA TEMPLE · Principal Ganesha temple of Srinagar.\n"
                    "Location: Ganpatyar (Ganpatiyar), Srinagar · 34.0824°N 74.7993°E\n"
                    "Google Maps: https://www.google.com/maps/search/Ganpatyar+temple+Srinagar\n\n"
                    "The mohalla of Ganpatyar is named after this Ganesha temple — "
                    "one of the principal KP residential areas of old Srinagar. "
                    "KPs visit here before all auspicious events: marriages, new businesses, "
                    "Navreh, examinations. 'Om Gam Ganapataye Namah' is the primary mantra. "
                    "Ganesha is invoked first in every KP puja.\n\n"
                    "Mantra: 'Om Gam Ganapataye Namah' | 'Vakratunda Mahakaya Suryakoti Samaprabha...'"
                ),
                "links": [
                    ("Google Maps · Ganpatyar Srinagar", "https://www.google.com/maps/search/Ganpatyar+Srinagar+Kashmir"),
                    ("Wikipedia · Ganesha", "https://en.wikipedia.org/wiki/Ganesha"),
                ],
            },
            {
                "name": "Vitasta (Jhelum) Ghats — Srinagar · वितस्ता घाट",
                "icon": "",
                "timing": "Herath, Shraddha, Navreh, Nag Panchami",
                "desc": (
                    "RIVER GHATS · Sacred ghats of the Vitasta (Jhelum) in Srinagar.\n"
                    "Location: Multiple ghats along Jhelum in Srinagar · 34.0836°N 74.7973°E\n"
                    "Google Maps: https://www.google.com/maps/search/Jhelum+river+ghats+Srinagar\n\n"
                    "The Vitasta (Jhelum) is the sacred river-goddess of Kashmir. "
                    "KPs perform all major river rituals at the Jhelum ghats: "
                    "· Shraddha tarpan (water offerings to ancestors)\n"
                    "· Herath: Vatak pots are immersed at the ghat after puja\n"
                    "· Nag Panchami: milk offerings at the river\n"
                    "· Navreh morning: ritual bath in the Vitasta\n"
                    "· Vivaha: groom's procession traditionally included a visit to the ghat\n\n"
                    "Main ghats: Zaina Kadal ghat, Habba Kadal ghat, Fateh Kadal ghat, "
                    "Rainawari ghat (near Gopinath shrine)."
                ),
                "links": [
                    ("Wikipedia · Jhelum river", "https://en.wikipedia.org/wiki/Jhelum_River"),
                    ("Google Maps · Jhelum Srinagar ghats", "https://www.google.com/maps/search/Jhelum+river+Srinagar+ghat"),
                ],
            },
            {
                "name": "Parihas Pora (Awantivarman palace ruins) · परिहासपोर (बारामुला)",
                "icon": "",
                "timing": "Year-round; historical pilgrimage",
                "desc": (
                    "ANCIENT SITE · 9th century royal city ruins with temples.\n"
                    "Location: Parihaspora, Baramulla district · 34.0934°N 74.5891°E\n"
                    "Google Maps: https://www.google.com/maps/search/Parihaspora+temple+ruins+Baramulla\n\n"
                    "Parihaspora = City of Jest/Play — built by King Lalitaditya Muktapida (8th century CE). "
                    "Once had massive temples including Muktakeshava (Vishnu) and Parihaskesvara (Shiva). "
                    "Now ruins — but among the most important archaeological sites in Kashmir. "
                    "The scale of construction rivals Martand. ASI protected.\n\n"
                    "Reference: Rajatarangini (Books 4–5), ASI Kashmir Survey"
                ),
                "links": [
                    ("Wikipedia · Parihaspora", "https://en.wikipedia.org/wiki/Parihaspora"),
                    ("Google Maps · Parihaspora", "https://www.google.com/maps/search/Parihaspora+Kashmir"),
                ],
            },
            {
                "name": "Buniyar Temples · बुनियार मन्दिर (बारामुला)",
                "icon": "",
                "timing": "Year-round",
                "desc": (
                    "ANCIENT TEMPLES · Medieval temple complex, north Kashmir.\n"
                    "Location: Buniyar, Baramulla district · 34.3100°N 73.9400°E\n"
                    "Google Maps: https://www.google.com/maps/search/Buniyar+temple+Baramulla+Kashmir\n\n"
                    "Buniyar has ruins of ancient temples from the early medieval period. "
                    "The area was an important pilgrimage route to the Lolab Valley. "
                    "Stone temple remains show the characteristic Kashmiri trefoil arch style. "
                    "KP families from Baramulla and Sopore include this in regional pilgrimage.\n\n"
                    "Reference: J&K Archaeological Survey, ASI reports"
                ),
                "links": [
                    ("Google Maps · Buniyar Baramulla", "https://www.google.com/maps/search/Buniyar+village+Baramulla+Kashmir"),
                ],
            },
            {
                "name": "Tulmul — Naga tirtha & Ragnya Devi complex · तुलमुल नाग तीर्थ",
                "icon": "",
                "timing": "Nag Panchami; Zyeth Ashtami",
                "desc": (
                    "NAG TIRTHA · The Naga spring complex at Tulmul — separate from but adjacent to the Kheer Bhawani temple.\n"
                    "Location: Tullamulla, Ganderbal · 34.2285°N 74.8090°E\n"
                    "Google Maps: https://www.google.com/maps/search/Tullamulla+Naga+spring+Ganderbal\n\n"
                    "The Tulmul area has multiple sacred springs — the Kheer Bhawani is the most "
                    "famous but the surrounding springs are also Naga tirthas. "
                    "The Naga of Tulmul is Takshaka (one of the principal Nagas of the Nilamata Purana). "
                    "Nag Panchami: milk offered at all springs in the complex. "
                    "The combination of Ragnya Devi (Shakti) and Naga (Shiva's serpent) makes "
                    "this one of the most complete sacred sites in Kashmir.\n\n"
                    "Reference: Nilamata Purana (Naga tirthas section)"
                ),
                "links": [
                    ("Google Maps · Tullamulla", "https://www.google.com/maps/search/Tullamulla+Ganderbal+Kashmir+temple"),
                    ("iKashmir · Tulmul", "https://www.ikashmir.net/tulamula/"),
                ],
            },
            {
                "name": "All Major Kashmiri Pandit Temples — iKashmir Directory",
                "icon": "",
                "timing": "Reference for all KP temples across the valley",
                "desc": (
                    "COMPLETE TEMPLE REFERENCE · The iKashmir temple directory lists all major KP temples:\n\n"
                    "Srinagar area temples:\n"
                    "· Zaina Devi temple · Sharika (Hari Parbat) · Ganpatyar · Bhairon temple "
                    "(old city) · Pandrethaan temple (Pandrethan) — ancient temple near Srinagar "
                    "where Lal Ded was born\n\n"
                    "Anantnag / South Kashmir:\n"
                    "· Martand · Bijbehara Vijeshvara · Bhadrakali · Kokernag temples "
                    "· Achabal · Verinag · Mattan · Daksum Shiva temple\n\n"
                    "Pulwama / Awantipora:\n"
                    "· Jwala Devi (Khrew) · Awantiswara · Awantishwamin · "
                    "Pampore area Naga springs\n\n"
                    "Baramulla / North Kashmir:\n"
                    "· Buniyar · Parihaspora · Sopore area temples\n\n"
                    "Ganderbal:\n"
                    "· Kheer Bhawani (Tulmul) · Nagbal · Kangan area Shiva temples\n\n"
                    "Kupwara / Remote:\n"
                    "· Sharada Peeth vicinity (PoK) · Lolab Valley temples · Gurez temples\n\n"
                    "Google Maps: Search 'ancient Hindu temples Kashmir' for comprehensive map view."
                ),
                "links": [
                    ("iKashmir · Complete temple list", "https://www.ikashmir.net/temples/index.html"),
                    ("iKashmir · All Bhairavas", "https://www.ikashmir.net/temples/bhairav.html"),
                    ("iKashmir · Peethas", "https://www.ikashmir.net/temples/peetham.html"),
                    ("Google Maps · All Kashmir temples", "https://www.google.com/maps/search/ancient+temples+Kashmir+Valley"),
                    ("Wikipedia · Temples of Jammu and Kashmir", "https://en.wikipedia.org/wiki/Category:Hindu_temples_in_Jammu_and_Kashmir"),
                    ("ASI Kashmir Circle", "https://asi.nic.in/"),
                ],
            },
        ],
        "Music & Performing Arts · संगीत": [
            {
                "name": "Sufiana Kalam · सूफियाना कलाम",
                "icon": "",
                "timing": "Classical — mehfils, weddings, spiritual gatherings",
                "desc": (
                    "The classical Sufi music of Kashmir — one of the most refined musical traditions "
                    "in the Indian subcontinent. Evolved over 500+ years blending Persian, Central Asian "
                    "and Kashmiri melodic traditions.\n\n"
                    "Instruments: Santoor (100-string hammered dulcimer), Saz-i-Kashmir (long-necked lute), "
                    "Wasul (dilruba-type bowed instrument), Tumbaknari (clay pot drum), "
                    "Harmonium, Tabla.\n\n"
                    "Language & texts: Persian ghazals, Kashmiri mystic poetry (vakhs), "
                    "Sanskrit shlokas. Most performed ragas: Yaman, Bhairav, Bhairavi, Desh, Todi.\n\n"
                    "Famous compositions & songs:\n"
                    "· 'Mast Qalandar' — devotional to Lal Shahbaz Qalandar; widely performed in Kashmir\n"
                    "· 'Allah Hoo' — deep meditation chant in Sufi gatherings\n"
                    "· 'Shamas-i-Tabrizi' — Rumi's poem set in Sufiana style\n"
                    "· 'Gulzar Hain Hum' — classical Persian ghazal\n"
                    "· Kafi compositions of Shah Qattal and Shamas Faqir\n\n"
                    "Notable artists: Ustad Ghulam Mohammad Zaz, Ustad Ghulam Nabi Shiekh, "
                    "Ustad Mohammad Yaqoob Sheikh, Ustad Nasir Fatehpuri.\n\n"
                    "Status: Recognised by Sangeet Natak Akademi, India. "
                    "Documented by Sahitya Akademi as intangible heritage."
                ),
                "links": [
                    ("Wikipedia · Sufiana Kalam", "https://en.wikipedia.org/wiki/Sufiana_Kalam"),
                    ("YouTube · Sufiana Kalam collection", "https://www.youtube.com/results?search_query=sufiana+kalam+kashmir+classical"),
                    ("YouTube · Ustad Ghulam Mohammad Zaz", "https://www.youtube.com/results?search_query=ghulam+mohammad+zaz+sufiana+kalam"),
                ],
            },
            {
                "name": "Vakhs of Lal Ded · लल देद वाख",
                "icon": "",
                "timing": "Devotional — recited at Herath, Navreh, spiritual gatherings, daily puja",
                "desc": (
                    "The mystical verses (Vakhs) of Lalleshwari are the heart of Kashmiri spiritual music. "
                    "Sung, chanted and meditated upon for 700 years.\n\n"
                    "Form: Unrhymed quatrains in Old Kashmiri. Sung in a slow, meditative style. "
                    "No fixed raga — the melody varies by region and family tradition.\n\n"
                    "Most celebrated Vakhs with Kashmiri text:\n\n"
                    "1. 'Shiv chuy thali thali rozaan\n"
                    "   Moz nay Hindav na Musalmaan\n"
                    "   Trukh pan panun parzanaan\n"
                    "   Sayi chu Shaiv agam nishan'\n"
                    "   — Shiva pervades everywhere; do not distinguish Hindu from Muslim.\n\n"
                    "2. 'Lale ous yeli gurus vachas razi\n"
                    "   Teli mye panun panas disum nazar\n"
                    "   Teli mye zanaan gay bahi nay bazi\n"
                    "   Teli mye poz panun korum shumaar'\n"
                    "   — When I, Lalla, became attentive to the Guru's word, "
                    "I saw my own Self; then I recognised what is real and unreal.\n\n"
                    "3. 'Pranas apanas milawath karim\n"
                    "   Shiv Shakti akh chu beyi nay beyi\n"
                    "   Parzanawith panas karim nisharam\n"
                    "   Panas panas mye aayi suyii'\n"
                    "   — When prana and apana unite, Shiva and Shakti are one; "
                    "recognising the Self, I became still — that alone came to me.\n\n"
                    "4. 'Wopadum wuchum naav taru tari\n"
                    "   Bramh wuchum bramh wuchinam Hari\n"
                    "   Aakis aakis panas aaki\n"
                    "   Kus mye darshyov kus me dith nari'\n"
                    "   — I crossed the water; I found the raft. I saw Brahma; I saw Hari. "
                    "One and one and one — who showed me, and who showed the fire?\n\n"
                    "5. 'Yus panas nish panas maaniy\n"
                    "   Suy chu Shivas peth baaraniy'\n"
                    "   — One who recognises the Self within the Self — "
                    "that one alone is the door to Shiva.\n\n"
                    "Sung by: Pandit Bhajan Sopori (santoor + vakh), "
                    "Kailash Mehra, Vijay Dhar, numerous KP community musicians."
                ),
                "links": [
                    ("Wikipedia · Lalleshwari", "https://en.wikipedia.org/wiki/Lalleshwari"),
                    ("YouTube · Lal Ded Vakhs sung", "https://www.youtube.com/results?search_query=lal+ded+vakhs+sung+kashmiri"),
                    ("YouTube · Lalleshwari Vakhs recitation", "https://www.youtube.com/results?search_query=lalleshwari+vakhs+kashmiri+pandit"),
                    ("Archive.org · Lal Ded texts", "https://archive.org/search?query=lal+ded+vakhs"),
                ],
            },
            {
                "name": "Bhajans & Shiva Stotras · भजन और शिव स्तोत्र",
                "icon": "",
                "timing": "Daily puja, Herath night, Navreh, Ashtami — all devotional occasions",
                "desc": (
                    "Kashmiri Pandit devotional singing tradition — combining Sanskrit stotras "
                    "with Kashmiri bhajans sung at home and temple.\n\n"
                    "── SHIVA STOTRAS (Sanskrit) ──\n\n"
                    "1. Shiva Panchakshara Stotra (by Adi Shankaracharya)\n"
                    "   Full text:\n"
                    "   'Nagendra-hārāya trilochanāya\n"
                    "   Bhasmānga-rāgāya maheshvarāya\n"
                    "   Nityāya shuddhaaya digambharāya\n"
                    "   Tasmai na-kārāya namaḥ Śivāya'\n"
                    "   (Om Namah Shivaya — each of 5 verses meditates on one syllable Na Ma Shi Va Ya)\n"
                    "   Sung at: start and end of all Shiva pujas, Herath night vigil.\n\n"
                    "2. Mrityunjaya Mantra (Rigveda 7.59.12)\n"
                    "   'Om Tryambakam yajamahe\n"
                    "   Sugandhim pushtivardhanam\n"
                    "   Urvaarukamiva bandhanan\n"
                    "   Mrityor mukshiya maamritat'\n"
                    "   — We worship the three-eyed one (Shiva) who nourishes all; "
                    "may he liberate us from death as a ripe cucumber from the vine.\n"
                    "   KP practice: 108 repetitions on Herath; 11 times daily in Nityakarma.\n\n"
                    "3. Shiva Tandava Stotra (by Ravana)\n"
                    "   Opening verse:\n"
                    "   'Jatatavigalajjala-pravahapavitasthale\n"
                    "   Gale avalambya lambitaam bhujangatungamalikaam\n"
                    "   Damad-damad-damaddama-ninnadavadamarvayam\n"
                    "   Chakara chandtandavam tanotu nah shivah shivam'\n"
                    "   — Sung/chanted on Herath; powerful rhythmic recitation.\n\n"
                    "4. Sharada Stotram (KP-specific — invocation of Mata Sharada)\n"
                    "   'Ya Sharada nilotpala-dala-shyama\n"
                    "   Ya vai susukshma-paramanu-ruupaa\n"
                    "   Ya vai para brahma-svaruupa-nityaa\n"
                    "   Namas tasmai brahmane brahma-vidyaayai'\n"
                    "   — She who is dark as the blue lotus petal; recited at Navreh and Saraswati Puja.\n\n"
                    "── KASHMIRI BHAJANS ──\n\n"
                    "5. 'Shivji Bole Nandi Se' — popular Hindi Shiva bhajan sung in KP homes on Herath\n\n"
                    "6. 'Hey Shambhu Baba Mere Bhole Nath' — widely sung at Herath night vigil\n\n"
                    "7. 'Bum Bum Bhole' — festive Shiva song for Herath processions\n\n"
                    "8. 'Kashmiri Mata Sharika Bhawani' — KP-composed devotional to Sharika Devi; "
                    "sung on Vaishakha Ashtami\n\n"
                    "9. 'Jai Kheer Bhawani Mata' — devotional sung at Zyeth Ashtami mela at Tulmul\n\n"
                    "10. 'Ragnya Devi Bhawani' — Kheer Bhawani aarti in Kashmiri; "
                    "sung by KP families before Zyeth Ashtami pilgrimage\n\n"
                    "11. 'Herathas Tsalar Shivji' — Kashmiri song specifically for Herath evening; "
                    "describes the Vatak pots and the night of Shiva\n\n"
                    "12. 'Batuk Bhairav Stotra' — recited at Vatak Puja during Herath:\n"
                    "    'Om Hreem Batukaya Apadudharanaya Kuru Kuru Batukaya Hreem'\n\n"
                    "Notable KP bhajan singers: Pandit Bhajan Sopori, Vijay Dhar, "
                    "Sharda Koul, Kailash Mehra, Pushkar Bhan."
                ),
                "links": [
                    ("YouTube · Shiva Panchakshara Stotra", "https://www.youtube.com/results?search_query=shiva+panchakshara+stotra+kashmiri"),
                    ("YouTube · Mrityunjaya Mantra 108 times", "https://www.youtube.com/results?search_query=mrityunjaya+mantra+108+times"),
                    ("YouTube · Kashmiri Herath Bhajans", "https://www.youtube.com/results?search_query=kashmiri+herath+bhajan+shiva"),
                    ("YouTube · Sharika Devi Bhajan", "https://www.youtube.com/results?search_query=sharika+devi+bhajan+kashmiri"),
                    ("YouTube · Kheer Bhawani Aarti", "https://www.youtube.com/results?search_query=kheer+bhawani+aarti+kashmiri+pandit"),
                    ("Shiva Tandava text", "https://www.wisdomlib.org/definition/shiva-tandava-stotra"),
                ],
            },
            {
                "name": "Chakri · चकरी — Kashmiri Folk Music",
                "icon": "",
                "timing": "Weddings, Navreh, festivals, community gatherings",
                "desc": (
                    "Chakri is the most vibrant and popular Kashmiri folk music genre — "
                    "upbeat, joyful, celebratory. The word 'Chakri' comes from 'chakkar' (spin/circle) "
                    "— the music makes you want to move.\n\n"
                    "Instruments: Rubab (lute — Kashmir's national instrument), "
                    "Tumbaknari (clay barrel drum), Noot (metal pot struck with rings), "
                    "Tche-tche (small cymbals), Harmonium, Sarangi.\n\n"
                    "Famous Chakri songs:\n"
                    "· 'Ded Chum Bramaan' (I am wandering) — classic Chakri about spiritual seeking\n"
                    "· 'Roshan Dalaa Chum Nazaaran' — about Dal Lake beauty; performed at Navreh\n"
                    "· 'Volo Volo Kalaamas' — wedding Chakri for the groom's procession\n"
                    "· 'Pumbe Sur' — spring Chakri about blooming flowers\n"
                    "· 'Boul Boul Gindun' — light celebratory Chakri about nature\n"
                    "· 'Mye Naav Chum Bramaan' — devotional Chakri\n"
                    "· 'Chah Naar Hasa' — festive Chakri sung at homecomings\n\n"
                    "Notable artists: Mohammed Shafi Shauq, Raj Begum (first woman Chakri singer), "
                    "Ghulam Ahmed Sufi, Shamim Dev Azad, Waheed Jeelani, "
                    "Naseem Akhter, Kailash Mehra (KP Chakri tradition).\n\n"
                    "KP Chakri: Kashmiri Pandits have their own Chakri repertoire — "
                    "songs about Herath, Navreh, Kul Devi, and the Valley sung at family gatherings."
                ),
                "links": [
                    ("Wikipedia · Kashmiri Music", "https://en.wikipedia.org/wiki/Music_of_Jammu_and_Kashmir"),
                    ("YouTube · Kashmiri Chakri songs", "https://www.youtube.com/results?search_query=kashmiri+chakri+folk+songs"),
                    ("YouTube · Raj Begum Kashmiri songs", "https://www.youtube.com/results?search_query=raj+begum+kashmiri+folk+songs"),
                    ("YouTube · KP Chakri Navreh", "https://www.youtube.com/results?search_query=kashmiri+pandit+chakri+navreh+songs"),
                ],
            },
            {
                "name": "Wanwun · वान्वुन — KP Wedding Songs",
                "icon": "",
                "timing": "Kashmiri Pandit weddings — specific songs for each ritual stage",
                "desc": (
                    "Wanwun (from Sanskrit: Vandan = salutation/praise) are the traditional "
                    "women's ritual songs of Kashmiri Pandits — sung exclusively by women "
                    "at each stage of the wedding. One of the most endangered elements of KP culture.\n\n"
                    "Song categories by wedding stage:\n\n"
                    "1. DEVGUN WANWUN (invoking family deities):\n"
                    "   · 'Ganesha Puja Wanwun' — women invoke Ganesha before the wedding begins\n"
                    "   · 'Kul Devi Vandana' — invoking Sharika/Ragnya/Jwala Devi\n\n"
                    "2. LAGAN WANWUN (auspicious thread ceremony):\n"
                    "   · 'Lagan Khasaan' — song for the tying of the Lagan thread\n"
                    "   · 'Shubh Lagan Aayo' — welcoming the auspicious moment\n\n"
                    "3. MEHNDI WANWUN (henna night):\n"
                    "   · 'Mehndi Rachao' — in Kashmiri; sung while applying henna to the bride\n"
                    "   · 'Batuk Puja Wanwun' — invoking Bhairava/Batuk for protection\n\n"
                    "4. BARAT WANWUN (groom's procession arrival):\n"
                    "   · 'Volo Volo Dulho' — 'Come, come, O groom' — welcoming song\n"
                    "   · 'Aayo Dulha' — celebratory arrival song\n\n"
                    "5. PHERAN CEREMONY WANWUN:\n"
                    "   · 'Pheran Pahenan Dulhan Ko' — as the bride is dressed in the Pheran\n\n"
                    "6. SAPTAPADI WANWUN (seven steps around the fire):\n"
                    "   · 'Saat Phere' — singing the 7 vows in Kashmiri\n"
                    "   · 'Agni Devta' — invoking the sacred fire\n\n"
                    "7. VIDAI WANWUN (bride's departure — most emotional):\n"
                    "   · 'Wuchum Wuchum Ghar Myon' — 'I looked and looked at my home'\n"
                    "   · 'Maajan Maajan Rozum' — 'I will remain as a daughter'\n"
                    "   · 'Chu Ded Myon' — most moving farewell song\n\n"
                    "8. KHON BATTA WANWUN (bride's welcome at groom's home):\n"
                    "   · 'Aayi Nai Dulhan' — welcoming the bride into the new home\n\n"
                    "Status: Critically endangered — only older KP women (70+) know the complete "
                    "repertoire. Preservation efforts by KP cultural organisations worldwide."
                ),
                "links": [
                    ("Wikipedia · Wanwun", "https://en.wikipedia.org/wiki/Wanwun"),
                    ("YouTube · Kashmiri Pandit Wanwun wedding songs", "https://www.youtube.com/results?search_query=kashmiri+pandit+wanwun+wedding+songs"),
                    ("YouTube · KP wedding Wanwun traditional", "https://www.youtube.com/results?search_query=wanwun+kashmiri+pandit+traditional+wedding"),
                    ("iKashmir · Music", "https://www.ikashmir.net/music/"),
                ],
            },
            {
                "name": "Rouf · रौफ — Women's Dance",
                "icon": "",
                "timing": "Navreh (KP New Year), Eid, spring festivals, weddings",
                "desc": (
                    "Rouf is the most graceful traditional dance of Kashmir — performed exclusively "
                    "by women. A group dance of great elegance and cultural pride.\n\n"
                    "Form: Women stand in two rows facing each other (or in a semi-circle). "
                    "Steps are synchronised — a gentle forward-backward footwork pattern. "
                    "Arms move gracefully at waist level. Performers wear traditional Pheran.\n\n"
                    "Songs sung during Rouf:\n"
                    "· 'Phul Vari Gashe' — 'The garden is in full bloom' — spring Rouf song\n"
                    "· 'Roshan Dalaa' — about Dal Lake in spring\n"
                    "· 'Laali Laali Dodiyaas Laali' — celebratory spring song\n"
                    "· 'Volo Maelis Gulshan Manz' — 'Come to the garden of flowers'\n"
                    "· 'Chu Myon Yaar Sonuy' — 'My beloved is like gold'\n"
                    "· 'Navreh Mubarak' songs — KP-specific Rouf songs for New Year\n\n"
                    "KP context: Rouf is performed by KP women at Navreh celebrations — "
                    "it is one of the most visible signs of Kashmiri cultural identity at "
                    "KP gatherings worldwide (Jammu, Delhi, Mumbai, diaspora cities).\n\n"
                    "UNESCO: Listed as intangible cultural heritage of J&K. "
                    "Sahitya Akademi has documented Rouf as a living tradition."
                ),
                "links": [
                    ("Wikipedia · Rouf", "https://en.wikipedia.org/wiki/Rouf"),
                    ("YouTube · Rouf dance Kashmiri", "https://www.youtube.com/results?search_query=rouf+dance+kashmiri+women+traditional"),
                    ("YouTube · Rouf Navreh songs Kashmir", "https://www.youtube.com/results?search_query=rouf+navreh+kashmiri+pandit+dance"),
                ],
            },
            {
                "name": "Santoor · सन्तूर — Kashmir's Soul Instrument",
                "icon": "",
                "timing": "Classical concerts, Sufiana Kalam, devotional music",
                "desc": (
                    "The Santoor is Kashmir's most iconic instrument and India's most celebrated "
                    "hammered dulcimer. 100 strings stretched over a walnut-wood trapezoidal box, "
                    "struck with light curved mallets (mezrab/mesrab).\n\n"
                    "History: Brought to Kashmir from Persia (Santur) via the Silk Route ~500 years ago. "
                    "Kashmiri Santoor is larger and deeper than the Persian santur. "
                    "Traditional use: Sufiana Kalam ensembles.\n\n"
                    "Pandit Shivkumar Sharma (1938–2022): The greatest Santoor maestro. "
                    "He single-handedly elevated the Santoor from a folk/Sufi instrument "
                    "to a full Hindustani classical concert instrument. "
                    "His recordings are essential listening.\n\n"
                    "Essential recordings & YouTube:\n"
                    "· 'Raga Bhairavi' — Pt. Shivkumar Sharma (morning raga, deeply meditative)\n"
                    "· 'Raga Yaman' — Pt. Shivkumar Sharma (evening raga, quintessential Santoor)\n"
                    "· 'Raga Desh' — Pt. Shivkumar Sharma (monsoon raga)\n"
                    "· 'Raga Bairagi' — deeply devotional Shiva raga\n"
                    "· 'Shiv-Hari' film music collaborations with Hari Prasad Chaurasia\n"
                    "· 'Call of the Valley' (1967) — Shivkumar Sharma + Hariprasad Chaurasia + "
                    "Brij Bhushan Kabra — landmark album of Indian music\n\n"
                    "Second generation: Rahul Sharma (son of Pt. Shivkumar Sharma) continues the legacy."
                ),
                "links": [
                    ("Wikipedia · Santoor", "https://en.wikipedia.org/wiki/Santoor"),
                    ("Wikipedia · Shiv Kumar Sharma", "https://en.wikipedia.org/wiki/Shiv_Kumar_Sharma"),
                    ("YouTube · Pt. Shivkumar Sharma Raga Bhairavi", "https://www.youtube.com/results?search_query=shivkumar+sharma+santoor+raga+bhairavi"),
                    ("YouTube · Call of the Valley full album", "https://www.youtube.com/results?search_query=call+of+the+valley+shivkumar+sharma+hariprasad"),
                    ("YouTube · Santoor Raga Yaman", "https://www.youtube.com/results?search_query=shivkumar+sharma+santoor+raga+yaman"),
                    ("YouTube · Rahul Sharma Santoor", "https://www.youtube.com/results?search_query=rahul+sharma+santoor+kashmiri"),
                ],
            },
            {
                "name": "Kashmiri Bhajan & Kul Devi Aarti · कुल देवी आरती",
                "icon": "",
                "timing": "Ashtami puja, Navratri, Herath, Navreh, daily evening puja",
                "desc": (
                    "Kashmiri Pandit devotional songs specific to each Kul Devi and Shiva — "
                    "sung at home pujas, temples and community gatherings.\n\n"
                    "── SHARIKA DEVI BHAJANS (Hari Parbat, Srinagar) ──\n"
                    "· 'Sharika Mata Aarti': 'Jai Sharika Mata, Jai Chakreshwari / "
                    "Hari Parbat Nivaasi, Kashmeer Kalyan Kari' — main aarti\n"
                    "· 'Hey Sharike Bhawani' — devotional in Kashmiri to Sharika Devi\n"
                    "· 'Shresti Ki Mata' — Sanskrit stotra to Chakreshwari\n\n"
                    "── KHEER BHAWANI / RAGNYA DEVI BHAJANS (Tulmul) ──\n"
                    "· 'Jai Kheer Bhawani Mata Jai' — main aarti at Tulmul temple\n"
                    "· 'Ragnya Devi Bhawani' — Kashmiri devotional; sung by KP women at Zyeth Ashtami\n"
                    "· 'Tulmul Wali Mata' — popular KP bhajan for Kheer Bhawani\n"
                    "· 'Ksheer Bhawani Stotra' in Sanskrit — recited by purohit at spring\n\n"
                    "── JWALA DEVI BHAJANS (Khrew, Pulwama) ──\n"
                    "· 'Jai Jwala Devi Mata' — Navratri aarti\n"
                    "· 'Khrew Wali Jwala Mata' — regional bhajan for south Kashmir KPs\n\n"
                    "── HERATH BHAJANS (Shiva songs for the all-night vigil) ──\n"
                    "· 'Herathas Tsalar Shivji' — KP Kashmiri song for Herath night\n"
                    "· 'Shiv Vandana Herath' — Sanskrit-Kashmiri mix sung at Vatak Puja\n"
                    "· 'Om Namah Shivaya' — sung continuously through the Herath vigil\n"
                    "· 'Har Har Mahadev' call-and-response through the night\n\n"
                    "── NAVREH SONGS ──\n"
                    "· 'Navreh Mubarak Aayi' — celebratory Kashmiri song for New Year\n"
                    "· 'Sharada Vandana' — sung at the Navreh Thali puja to Mata Sharada\n"
                    "· 'Nava Varsha Aayo' — welcome song for the Kashmiri new year\n\n"
                    "── VITASTA / NAGA BHAJANS ──\n"
                    "· 'Vitasta Stotra' (from Nilamata Purana) — recited on Vitasta Jayanti\n"
                    "· 'Nag Panchami Bhajan' — sung at Naga puja on Shravana Panchami\n"
                    "· 'Vasuki Nagaraja Stotra' — Sanskrit; sung at Nag temples"
                ),
                "links": [
                    ("YouTube · Sharika Devi Aarti", "https://www.youtube.com/results?search_query=sharika+devi+aarti+kashmiri+pandit"),
                    ("YouTube · Kheer Bhawani Aarti", "https://www.youtube.com/results?search_query=kheer+bhawani+aarti+tulmul"),
                    ("YouTube · Kashmiri Pandit Herath bhajan", "https://www.youtube.com/results?search_query=kashmiri+pandit+herath+shiva+bhajan"),
                    ("YouTube · Navreh songs KP", "https://www.youtube.com/results?search_query=navreh+kashmiri+pandit+song"),
                    ("YouTube · Jwala Devi bhajan", "https://www.youtube.com/results?search_query=jwala+devi+khrew+aarti+kashmiri"),
                    ("YouTube · Vitasta Jayanti songs", "https://www.youtube.com/results?search_query=vitasta+jayanti+kashmiri+pandit"),
                ],
            },
            {
                "name": "Hafiz Nagma & Kashmiri Gazal · हाफ़िज़ नग्मा",
                "icon": "",
                "timing": "Literary gatherings, weddings, cultural evenings",
                "desc": (
                    "Kashmiri classical poetry set to music — the refined literary-musical tradition "
                    "of the valley.\n\n"
                    "Hafiz Nagma: named after Hafiz (the Persian poet) — Persian and Kashmiri "
                    "poems from classical masters set to classical ragas. "
                    "Slower and more meditative than Chakri.\n\n"
                    "Famous Kashmiri Gazal/Nagma songs:\n"
                    "· Habba Khatoon's Lol (lyric songs) — set to traditional Kashmiri melodies:\n"
                    "  'Rozis na biyus dilbar myon' — 'My beloved does not return' (most famous)\n"
                    "  'Aakh bael' — 'One moment' — love song\n\n"
                    "· Arnimal's Vakhs set to music:\n"
                    "  'Suy myon yaar suy myon dilbar' — devotional love\n\n"
                    "· Mahmood Gami's Kashmiri poetry — 19th century master of Kashmiri poetry:\n"
                    "  'Yimav Gayi Yimav Gayi' — elegy\n\n"
                    "· Maqbool Shah Kralawari — modern Kashmiri poet:\n"
                    "  'Sahibaa' — most performed modern Kashmiri song\n\n"
                    "Notable artists: Raj Begum (greatest Kashmiri female vocalist, "
                    "'Nightingale of Kashmir' in modern era), Shamim Dev Azad, "
                    "Gulzar Ganai, Rashid Hafiz."
                ),
                "links": [
                    ("Wikipedia · Kashmiri literature", "https://en.wikipedia.org/wiki/Kashmiri_literature"),
                    ("YouTube · Habba Khatoon songs", "https://www.youtube.com/results?search_query=habba+khatoon+kashmiri+songs"),
                    ("YouTube · Raj Begum Kashmiri songs", "https://www.youtube.com/results?search_query=raj+begum+kashmiri+classic+songs"),
                    ("YouTube · Kashmiri gazal poetry", "https://www.youtube.com/results?search_query=kashmiri+gazal+nagma+classical"),
                ],
            },
            {
                "name": "Bhand Pather · भाण्ड पाथेर — Folk Theatre",
                "icon": "",
                "timing": "Festivals, fairs, village gatherings — dying tradition",
                "desc": (
                    "Ancient Kashmiri folk theatre — satirical performances by the Bhand "
                    "(jester-actor) community. One of India's oldest living theatre traditions, "
                    "tracing roots to Sanskrit Natya Shastra.\n\n"
                    "Form: Combines music, dance, mime, spoken dialogue and sharp social satire. "
                    "Performances mock royalty, corrupt officials, greedy priests — "
                    "speaking truth to power through comedy.\n\n"
                    "Instruments used in Bhand Pather: Dhol, Nagara (kettle drum), "
                    "Surnai (oboe-like wind instrument), Thalij (cymbals).\n\n"
                    "Famous Bhand Pather pieces:\n"
                    "· 'Darzi Pather' — satire on the tailor's vanity\n"
                    "· 'Watal Pather' — about the washerman; classical piece\n"
                    "· 'Bahman Pather' — about a Brahmin; socially sharp\n"
                    "· 'Gosain Pather' — about a Hindu mendicant\n"
                    "· 'Dokur Pather' — satire on a doctor\n"
                    "· 'Shikargah' — about royal hunting; political allegory\n\n"
                    "Notable family: The Bhand Pather tradition is maintained by the "
                    "Bhand community of Akingam village, Anantnag. "
                    "Master practitioners: Mohammed Shafi Bhand, Gulzar Ahmed Bhand.\n\n"
                    "Status: UNESCO Intangible Cultural Heritage candidate. "
                    "Sangeet Natak Akademi awardees include Bhand Pather performers."
                ),
                "links": [
                    ("Wikipedia · Bhand Pather", "https://en.wikipedia.org/wiki/Bhand_Pather"),
                    ("YouTube · Bhand Pather Kashmir", "https://www.youtube.com/results?search_query=bhand+pather+kashmiri+folk+theatre"),
                    ("Sangeet Natak Akademi", "https://en.wikipedia.org/wiki/Sangeet_Natak_Akademi"),
                ],
            },
            {
                "name": "Lehar & Dumhal · लहर और दुमहल — Traditional Dances",
                "icon": "",
                "timing": "Festivals, Urs (Sufi celebrations), seasonal gatherings",
                "desc": (
                    "Two distinct Kashmiri ceremonial dances:\n\n"
                    "── DUMHAL ──\n"
                    "A ceremonial dance of the Wattal community (Lolab Valley, Kupwara). "
                    "Performed at Urs of saints and special occasions. "
                    "Men carry a tall decorated banner (Dumhal pole) and dance in a circle "
                    "to the beat of drums. "
                    "One of the most visually striking and ancient dance traditions of Kashmir. "
                    "Listed in UNESCO Intangible Cultural Heritage documentation.\n\n"
                    "── LEHAR ──\n"
                    "Men's group dance accompanied by dhol and nagara drums. "
                    "Performed at spring festivals, especially in the Gurez Valley (Bandipora). "
                    "Vigorous footwork and arm movements — a warrior-folk dance tradition.\n\n"
                    "── BAND-I-PATHER (puppet theatre) ──\n"
                    "Traditional string puppet shows (marionettes) with Kashmiri folk stories. "
                    "Now extremely rare — fewer than 5 practicing families in the valley.\n\n"
                    "Songs accompanying Dumhal:\n"
                    "· Drum-based compositions (no lyrics) — pure rhythmic recitation\n"
                    "· 'Allah Hoo' Sufi chant as the banner is raised\n\n"
                    "Reference: Documented by J&K Academy of Art Culture and Languages (JKAACL)."
                ),
                "links": [
                    ("Wikipedia · Dumhal", "https://en.wikipedia.org/wiki/Dumhal"),
                    ("YouTube · Dumhal dance Kashmir", "https://www.youtube.com/results?search_query=dumhal+dance+kashmir+traditional"),
                    ("JKAACL", "https://jkaacl.net/"),
                ],
            },
            {
                "name": "Kashmiri Classical Instruments · संगीत वाद्य",
                "icon": "",
                "timing": "All musical contexts",
                "desc": (
                    "Complete guide to traditional Kashmiri musical instruments:\n\n"
                    "── STRING INSTRUMENTS ──\n"
                    "· Santoor: 100-string hammered dulcimer — Kashmir's signature instrument. "
                    "Made from walnut wood. Maestro: Pt. Shivkumar Sharma.\n"
                    "· Rubab (Robab): Long-necked plucked lute — 'father of guitar'. "
                    "The national instrument of Afghanistan and Kashmir. "
                    "Primary instrument of Chakri. Made from mulberry wood.\n"
                    "· Saz-i-Kashmir: Long-necked lute similar to Sitar but deeper. "
                    "Used in Sufiana Kalam ensembles.\n"
                    "· Sarangi: Short-necked bowed instrument — used in classical and folk music.\n"
                    "· Tanpura: Drone instrument for classical vocal music.\n\n"
                    "── PERCUSSION ──\n"
                    "· Tumbaknari: Clay barrel-shaped drum — essential Chakri instrument. "
                    "Unique to Kashmir — played with fingers.\n"
                    "· Dhol: Large two-headed drum — festivals, processions.\n"
                    "· Nagara: Kettle drum pair — Bhand Pather, royal music.\n"
                    "· Noot: Metal cooking pot struck with rings on fingers — Chakri accompaniment.\n"
                    "· Tabla: Adopted from Hindustani classical tradition.\n\n"
                    "── WIND ──\n"
                    "· Surnai (Shehnai variant): Double-reed wind instrument — "
                    "played at festivals, processions, Bhand Pather.\n"
                    "· Bansuri (flute): Used in devotional music and folk songs.\n"
                    "· Nay (reed flute): Sufi music — associated with Rumi's 'Listen to the Nay'.\n\n"
                    "── RHYTHMIC ──\n"
                    "· Tche-tche: Small cymbals struck together — Chakri, Wanwun.\n"
                    "· Thalij: Large cymbals — Bhand Pather, Dumhal.\n"
                    "· Ghanta (temple bell): Used in all puja and aarti."
                ),
                "links": [
                    ("Wikipedia · Rubab instrument", "https://en.wikipedia.org/wiki/Rubab_(instrument)"),
                    ("Wikipedia · Santoor", "https://en.wikipedia.org/wiki/Santoor"),
                    ("YouTube · Tumbaknari Kashmiri drum", "https://www.youtube.com/results?search_query=tumbaknari+kashmiri+drum+folk"),
                    ("YouTube · Rubab Kashmir music", "https://www.youtube.com/results?search_query=rubab+kashmiri+music+traditional"),
                    ("YouTube · Kashmiri instruments demonstration", "https://www.youtube.com/results?search_query=kashmiri+traditional+instruments+music"),
                ],
            },
        ],
        "Cuisine · व्यंजन": [
            {
                "name": "Wazwan · वाज़वान",
                "icon": "",
                "timing": "Weddings and major celebrations",
                "desc": (
                    "The grand Kashmiri feast — a 36-course ritual meal at weddings. "
                    "Must-have dishes: Rogan Josh, Yakhni, Tabak Maaz (fried ribs), Seekh Kabab, "
                    "Gushtaba (minced meat balls in yogurt gravy — the final 'king dish'), "
                    "Methi Maaz, Dhaniwal Korma. Waza (master chef) cooks on wood fire. "
                    "Served on a large copper plate (traem) shared between 4 people."
                ),
                "links": [
                    ("Wikipedia · Wazwan", "https://en.wikipedia.org/wiki/Wazwan"),
                ],
            },
            {
                "name": "Kashmiri Pandit Cuisine · कश्मीरी पण्डित रसोई",
                "icon": "",
                "timing": "Daily and festive",
                "desc": (
                    "KP cuisine uses no onion or garlic — flavoured with asafoetida (heeng), "
                    "dry ginger (sounth), fennel (saunf), and kashmiri red chilli. "
                    "Key dishes: Haakh (collard greens in mustard oil), Dum Aloo (potatoes in spiced yogurt), "
                    "Chaman (paneer), Nadru (lotus stem), Rajma, Modur Pulav (sweet rice), "
                    "Shab Deg (turnip & meat slow-cooked overnight). "
                    "Festival sweet: Shufta (dry fruits in sugar syrup)."
                ),
                "links": [
                    ("Wikipedia · Kashmiri Cuisine", "https://en.wikipedia.org/wiki/Kashmiri_cuisine"),
                ],
            },
            {
                "name": "Kehwa · केहवा",
                "icon": "",
                "timing": "Daily — offered to every guest",
                "desc": (
                    "Kashmir's iconic green tea — brewed in a Samovar (brass urn) with "
                    "saffron, cardamom, cinnamon, cloves and crushed almonds/walnuts. "
                    "No milk. Served in small cups. Symbol of Kashmiri hospitality — "
                    "refusing Kehwa is considered impolite. Drunk throughout the day."
                ),
                "links": [
                    ("Wikipedia · Kahwah", "https://en.wikipedia.org/wiki/Kahwah"),
                ],
            },
            {
                "name": "Noon Chai (Sheer Chai) · नून चाय",
                "icon": "",
                "timing": "Morning — with bread",
                "desc": (
                    "Pink/magenta salted tea unique to Kashmir — made with special tea leaves, "
                    "baking soda (makes it pink), milk and salt. Served with Kulcha, Lavasa "
                    "(thin bread), or Tchot (ring bread). A breakfast staple in Kashmir. "
                    "The colour comes from oxidation of the tea with baking soda."
                ),
                "links": [
                    ("Wikipedia · Noon Chai", "https://en.wikipedia.org/wiki/Noon_chai"),
                ],
            },
            {
                "name": "Kashmiri Breads · रोटियाँ",
                "icon": "",
                "timing": "Daily",
                "desc": (
                    "Breadmaking is an art in Kashmir — baked in traditional clay ovens (kaan). "
                    "Types: Kulcha (soft round bread), Lavasa (thin crispy flatbread), "
                    "Tchot (ring-shaped sesame bread), Girda (round tandoor bread), "
                    "Sheermal (sweet saffron bread for festivals), Bakarkhani (flaky layered bread)."
                ),
                "links": [
                    ("Wikipedia · Kashmiri Cuisine", "https://en.wikipedia.org/wiki/Kashmiri_cuisine"),
                ],
            },
        ],
        "Dress & Crafts · वेशभूषा और शिल्प": [
            {
                "name": "Pheran · फेरन",
                "icon": "",
                "timing": "Traditional — especially winter",
                "desc": (
                    "The iconic long loose robe of Kashmir — worn by both men and women. "
                    "Women's Pheran is longer with intricate embroidery; men's is plainer. "
                    "Under the Pheran, a Kangri (clay firepot in a wicker basket) is held "
                    "close to the body for warmth in winter. Symbol of Kashmiri identity."
                ),
                "links": [
                    ("Wikipedia · Pheran", "https://en.wikipedia.org/wiki/Pheran"),
                ],
            },
            {
                "name": "Kashmiri Shawls (Pashmina & Kani) · शाल",
                "icon": "",
                "timing": "Traditional craft — centuries old",
                "desc": (
                    "Kashmir's most famous craft. Pashmina: woven from the ultra-fine undercoat "
                    "of Changthangi goat. Kani shawl: woven on a special loom with wooden bobbins "
                    "(kani) — one shawl can take 3 years. Shahtoosh (banned): from Tibetan antelope. "
                    "GI-tagged product. Intricate patterns: Buta, Hashia, Jama, Jamawar."
                ),
                "links": [
                    ("Wikipedia · Pashmina", "https://en.wikipedia.org/wiki/Pashmina"),
                    ("Wikipedia · Kani Shawl", "https://en.wikipedia.org/wiki/Kani_shawl"),
                ],
            },
            {
                "name": "Kashmiri Carpet Weaving · कालीन",
                "icon": "",
                "timing": "Traditional craft",
                "desc": (
                    "Hand-knotted woollen and silk carpets — among the finest in the world. "
                    "Designs: floral medallion (herati), garden (bagh), prayer (namazluq), "
                    "tree of life. Up to 2,400 knots per square inch in fine silk pieces. "
                    "GI-tagged. Villages like Kanihama specialize in specific patterns."
                ),
                "links": [
                    ("Wikipedia · Kashmiri Carpet", "https://en.wikipedia.org/wiki/Kashmiri_carpet"),
                ],
            },
            {
                "name": "Papier-Mâché · कागज़ की कारीगरी",
                "icon": "",
                "timing": "Traditional craft",
                "desc": (
                    "Intricate hand-painted objects — boxes, trays, vases, ornaments — "
                    "made from layered paper pulp. Motifs: chinar leaves, lotus, Mughal florals. "
                    "Introduced to Kashmir by Shah Mir Swati in the 14th century. "
                    "Painted with natural pigments by master artisans (Naqash)."
                ),
                "links": [
                    ("Wikipedia · Kashmiri Papier-Mâché", "https://en.wikipedia.org/wiki/Papier-m%C3%A2ch%C3%A9#Kashmir"),
                ],
            },
            {
                "name": "Walnut Wood Carving · अखरोट की नक्काशी",
                "icon": "",
                "timing": "Traditional craft",
                "desc": (
                    "Kashmir's walnut wood (Juglans regia) has a distinctive dark grain ideal for "
                    "fine carving. Motifs: chinar, lotus, hunting scenes, geometric patterns. "
                    "Used for furniture, screens (jali work), boxes and decorative panels. "
                    "Traditional carving families are based in Srinagar's old city."
                ),
                "links": [
                    ("Wikipedia · Kashmiri Crafts", "https://en.wikipedia.org/wiki/Kashmiri_handicraft"),
                ],
            },
            {
                "name": "Sozni & Tilla Embroidery · सोज़नी / तिल्ला",
                "icon": "",
                "timing": "Traditional craft",
                "desc": (
                    "Sozni: needle embroidery on Pashmina shawls — fine floral patterns worked "
                    "from both sides so the reverse mirrors the front. "
                    "Tilla: gold/silver thread embroidery (zari) on velvet — used for Pherans, "
                    "caps, accessories. Both are GI-tagged crafts of Jammu & Kashmir."
                ),
                "links": [
                    ("Wikipedia · Kashmiri Embroidery", "https://en.wikipedia.org/wiki/Kashmiri_embroidery"),
                ],
            },
        ],
        "Language & Script · भाषा": [
            {
                "name": "Kashmiri Language (Koshur) · कोशुर",
                "icon": "",
                "timing": "Living language",
                "desc": (
                    "Kashmiri (Koshur) is a Dardic Indo-Aryan language spoken by ~7 million people. "
                    "Written in three scripts: Sharada (traditional KP script), "
                    "Nastaliq/Perso-Arabic (official in J&K), and Devanagari. "
                    "Recognized as a Scheduled Language of India (8th Schedule). "
                    "UNESCO classifies it as 'Vulnerable'. Rich in Persian, Sanskrit and Apabhramsha loanwords."
                ),
                "links": [
                    ("Wikipedia · Kashmiri Language", "https://en.wikipedia.org/wiki/Kashmiri_language"),
                    ("Ethnologue · Kashmiri", "https://www.ethnologue.com/language/kas/"),
                ],
            },
            {
                "name": "Sharada Script · शारदा लिपि",
                "icon": "",
                "timing": "c. 8th century CE — now endangered",
                "desc": (
                    "The ancient script of Kashmir — ancestor of Gurmukhi and Takri. "
                    "Used for KP religious manuscripts, horoscopes, letters and temple inscriptions. "
                    "Named after Sharada Devi (Saraswati). ~10,000 manuscripts survive in "
                    "libraries across India and abroad. Now taught only in a few KP families. "
                    "Unicode block U+11180–U+111DF."
                ),
                "links": [
                    ("Wikipedia · Sharada Script", "https://en.wikipedia.org/wiki/Sharada_script"),
                    ("Sharada Script Unicode", "https://www.unicode.org/charts/PDF/U11180.pdf"),
                ],
            },
            {
                "name": "Kashmiri Proverbs (Maqol) · मक़ोल",
                "icon": "",
                "timing": "Living oral tradition",
                "desc": (
                    "Kashmiri has a rich proverbial tradition — Maqol (proverbs) and "
                    "Zaban-i-Khas (idiomatic expressions). Examples: "
                    "'Pyov tse panan khyon, pyov tse maraan' (One who feeds you may also harm you). "
                    "Proverbs encoded in the Vakhs of Lal Ded and Nund Rishi remain in daily speech."
                ),
                "links": [
                    ("Kashmiri Proverbs Archive", "https://archive.org/search?query=kashmiri+proverbs"),
                ],
            },
        ],
        "Nature & Geography · प्रकृति": [
            {
                "name": "Dal Lake · डल झील",
                "icon": "",
                "timing": "Year-round — Lotus blooms summer",
                "desc": (
                    "The heart of Srinagar — 18 sq km freshwater lake. "
                    "Famous for houseboats (Dunga), Shikara rides, floating gardens (Rad), "
                    "floating markets (Sabzi market at dawn). "
                    "Mentioned in Nilamata Purana as sacred. Dal's islands include "
                    "Char Chinar (four chenar trees on an island) — iconic image of Kashmir."
                ),
                "links": [
                    ("Wikipedia · Dal Lake", "https://en.wikipedia.org/wiki/Dal_Lake"),
                ],
            },
            {
                "name": "Chinar Tree (Platanus orientalis) · चिनार",
                "icon": "",
                "timing": "Autumn foliage — Oct–Nov",
                "desc": (
                    "The Chinar (Oriental Plane) is the defining tree of Kashmir — "
                    "planted extensively by Mughal emperors in their gardens. "
                    "Autumn colours (gold, red, amber) are central to Kashmiri aesthetic. "
                    "The chinar leaf is the motif in Kashmiri crafts, carpets and embroidery. "
                    "Some individual trees are 600+ years old."
                ),
                "links": [
                    ("Wikipedia · Chinar Kashmir", "https://en.wikipedia.org/wiki/Chinar"),
                ],
            },
            {
                "name": "Kashmir Saffron (Kesar) · केसर",
                "icon": "",
                "timing": "Harvest: Oct–Nov; Pampore region",
                "desc": (
                    "The world's finest saffron — GI-tagged Kashmiri Kesar from Pampore (Pulwama). "
                    "Only region in the Indian subcontinent where saffron grows. "
                    "Harvested by hand before sunrise. Used in Kehwa, Wazwan, Modur Pulav, "
                    "and as a sacred offering. Cultivation dates back over 2,000 years."
                ),
                "links": [
                    ("Wikipedia · Kashmiri Saffron", "https://en.wikipedia.org/wiki/Kashmiri_saffron"),
                ],
            },
            {
                "name": "Mughal Gardens · मुग़ल बाग़",
                "icon": "",
                "timing": "Spring–Summer",
                "desc": (
                    "Three great Mughal gardens on Dal Lake shore — Shalimar Bagh (1619, Jahangir), "
                    "Nishat Bagh (1633, Asaf Khan) and Chashme Shahi (1632, Shah Jahan). "
                    "Designed on the Char-bagh (4-garden) Persian model with terraces, fountains, "
                    "chinar avenues and floral beds. UNESCO World Heritage tentative list."
                ),
                "links": [
                    ("Wikipedia · Mughal Gardens Kashmir", "https://en.wikipedia.org/wiki/Mughal_gardens_of_Kashmir"),
                ],
            },
        ],
    }

    # ── Category dropdown + search ─────────────────────────────────
    culture_cats = ["All Categories · सभी"] + list(KP_CULTURE.keys())
    cult_col1, cult_col2 = st.columns([2, 3])
    with cult_col1:
        cult_cat = st.selectbox("Category · श्रेणी", culture_cats, key="cult_cat")
    with cult_col2:
        cult_search = st.text_input("Search · खोजें", key="cult_search",
                                     placeholder="e.g. Herath, Wazwan, Santoor, Lal Ded, Pashmina…")

    # Only show content when user has picked a specific category or typed a search term
    _cult_active = cult_cat != "All Categories · सभी" or bool(cult_search)

    if not _cult_active:
        st.markdown("""
        <div style="text-align:center;padding:48px 20px;color:var(--muted)">
          <div style="font-size:36px;margin-bottom:16px;opacity:.4"></div>
          <div style="font-family:'Cinzel',serif;font-size:12px;letter-spacing:2.5px;
               color:var(--walnut-mid);margin-bottom:10px">SELECT A CATEGORY · श्रेणी चुनें</div>
          <div style="font-size:13.5px;line-height:1.8;max-width:420px;margin:0 auto">
            Choose a category from the dropdown — or type a keyword to search —
            to explore Kashmiri culture, festivals, sacred sites, music, cuisine and more.
          </div>
          <div style="font-family:'Noto Serif Devanagari',serif;font-size:12px;
               color:var(--muted);margin-top:10px;opacity:.6">
            ऊपर श्रेणी चुनें या खोज करें
          </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        if cult_search:
            term = cult_search.lower()
            cats_to_show = {}
            for cat, items in KP_CULTURE.items():
                filtered = [it for it in items
                            if term in it["name"].lower() or term in it["desc"].lower()]
                if filtered:
                    cats_to_show[cat] = filtered
        else:
            cats_to_show = {cult_cat: KP_CULTURE[cult_cat]}

        total_cult = sum(len(v) for v in cats_to_show.values())
        if total_cult == 0:
            st.info("No results found. Try a different search term.")
        else:
            st.markdown(f'<div style="font-size:12px;color:var(--muted);margin:6px 0 14px;font-style:italic">'
                        f'Showing {total_cult} entries in {len(cats_to_show)} category/categories</div>',
                        unsafe_allow_html=True)
            for cat_name, items in cats_to_show.items():
                st.markdown(f'<div class="subsec">{cat_name}</div>', unsafe_allow_html=True)
                for item in items:
                    links_html = " &nbsp;".join(
                        f'<a href="{url}" target="_blank" style="font-size:11px;color:var(--teal);'
                        f'text-decoration:none;padding:2px 8px;border:1px solid rgba(42,122,106,.3);'
                        f'border-radius:10px;white-space:nowrap"> {label}</a>'
                        for label, url in item.get("links", [])
                    )
                    st.markdown(f"""
                    <div style="background:white;border:1px solid var(--border);border-radius:10px;
                         padding:15px 20px;margin-bottom:10px;box-shadow:0 1px 6px var(--shadow)">
                      <div style="display:flex;align-items:center;gap:10px;margin-bottom:6px;flex-wrap:wrap">
                        <span style="font-size:20px">{item['icon']}</span>
                        <span style="font-family:Cinzel,serif;font-size:13px;font-weight:500;
                              color:var(--walnut)">{item['name']}</span>
                        <span style="font-size:10px;color:var(--muted);margin-left:auto;
                              font-style:italic">{item['timing']}</span>
                      </div>
                      <div style="font-size:13.5px;color:var(--ink);line-height:1.8;margin-bottom:10px">
                        {item['desc']}
                      </div>
                      <div style="display:flex;flex-wrap:wrap;gap:6px">{links_html}</div>
                    </div>
                    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# TAB 8 — KOSHURPEDIA
# ══════════════════════════════════════════════════════════════════════════════
with tabs[8]:
    st.markdown("""
    <div class="sec-head"> Koshurpedia · कोशुरपीडिया</div>
    <div class="sec-sub">
      Your wise Kashmiri Pandit — rituals, panchang, muhurats, mantras, traditions
      <span class="deva">पंचांग · अनुष्ठान · मुहूर्त · मंत्र · परंपरा · कश्मीरी संस्कृति</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="ai-box">
      <div class="ai-lbl">KOSHURPEDIA · कोशुर पण्डित</div>
      <div style="margin-top:22px;text-align:center;padding:22px 0 14px">
        <div style="font-size:36px;margin-bottom:12px"></div>
        <div style="font-family:'Cinzel Decorative',serif;font-size:14px;letter-spacing:3px;
             color:#DEB85A;margin-bottom:12px">COMING IN NEXT UPDATE</div>
        <div style="font-size:14.5px;color:rgba(253,248,240,.7);line-height:2;
             max-width:520px;margin:0 auto">
          Your wise Kashmiri Pandit — deeply versed in Vedic Pañcāṅga, Kashmiri rituals,
          Herath · Navreh · Kheer Bhawani traditions, Kashmir Shaivism, Mantras,
          Kul Devī puja, saints and the Vakhs of Lalleshwari — is being prepared.
          <br><br>
          <span style="color:#DEB85A;font-family:'Cinzel',serif;font-size:12px;
                letter-spacing:1.5px">Rolling out in the next update.</span>
        </div>
        <div style="font-family:'Noto Serif Devanagari',serif;font-size:13px;
             color:rgba(222,184,90,.5);margin-top:14px;line-height:1.8">
          कोशुर ज्योतिषी — पंचांग · अनुष्ठान · मंत्र · परम्परा · काश्मीर शैव दर्शन
          <br>शीघ्र ही उपलब्ध होंगे — अगले अपडेट में
        </div>
        <div style="margin-top:18px;font-size:11px;color:rgba(253,248,240,.25);
             font-family:'Cinzel',serif;letter-spacing:2px">
           &nbsp; OM NAMAH SHIVAYA &nbsp; 
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="styled-div"><span>CULTURAL HIGHLIGHTS</span></div>', unsafe_allow_html=True)
    oh1, oh2, oh3 = st.columns(3)
    oh1.markdown("""<div class="info-card">
      <div class="ic-icon"></div>
      <div class="ic-title">KASHMIR SHAIVISM</div>
      <div class="ic-body">The Trika philosophy of Abhinavagupta — Pratyabhijna (recognition), 
      Spanda (vibration), and Krama. The universe as Shiva's own manifestation 
      through Shakti (Vimarsha).</div>
      <div class="ic-accent">त्रिक दर्शन · अभिनवगुप्त</div>
    </div>""", unsafe_allow_html=True)
    oh2.markdown("""<div class="info-card">
      <div class="ic-icon"></div>
      <div class="ic-title">KASHMIRI RITUALS</div>
      <div class="ic-body">Herath · Navreh · Zyeth Ashtami · Kheer Bhawani Mela · 
      Pann · Shivratri Vatak Puja · Kul Devi Puja — the sacred calendar of 
      Kashmiri Pandits throughout the year.</div>
      <div class="ic-accent">कश्मीरी पण्डित परम्परा</div>
    </div>""", unsafe_allow_html=True)
    oh3.markdown("""<div class="info-card">
      <div class="ic-icon"></div>
      <div class="ic-title">SAINTS & VAKHS</div>
      <div class="ic-body">Lal Ded · Nund Rishi · Habba Khatoon · Rupa Bhawani — 
      the mystic voices of Kashmir who sang of love, liberation, and the 
      ineffable nature of Shiva.</div>
      <div class="ic-accent">वाख · मिस्टिक पोएट्री</div>
    </div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# TAB 7 — FEEDBACK / SUJHAV
# ══════════════════════════════════════════════════════════════════════════════
with tabs[7]:
    st.markdown("""
    <div class="sec-head">Sujhav · सुझाव</div>
    <div class="sec-sub">
      Feedback, suggestions &amp; contributions · प्रतिक्रिया, सुझाव और योगदान
      <span class="deva">आपके सुझाव इस पोर्टल को बेहतर बनाते हैं</span>
    </div>
    """, unsafe_allow_html=True)

    fb_l, fb_r = st.columns([1.6, 1])

    with fb_l:
        st.markdown("""
        <div style="background:linear-gradient(135deg,var(--saffron-pale),var(--gold-pale));
             border:1px solid rgba(212,114,42,.2);border-radius:14px;padding:24px 28px;
             margin-bottom:18px">
          <div style="font-family:'Cinzel',serif;font-size:9px;letter-spacing:2.5px;
               color:var(--saffron);margin-bottom:8px">YOUR VOICE MATTERS · आपकी आवाज़ मायने रखती है</div>
          <div style="font-size:14px;color:var(--walnut);line-height:2;margin-bottom:14px">
            This portal is a living project — built for the Kashmiri Pandit community
            and all those connected to Kashmir's heritage. Your feedback, corrections
            and suggestions are what make it grow.
          </div>
          <div style="font-family:'Noto Serif Devanagari',serif;font-size:13px;
               color:var(--muted);line-height:1.9;margin-bottom:16px">
            यह पोर्टल एक जीवित परियोजना है — जो कश्मीरी पण्डित समुदाय के लिए
            बनाई गई है। आपकी प्रतिक्रिया और सुझाव इसे और बेहतर बनाते हैं।
          </div>
          <div style="font-size:13px;color:var(--ink);line-height:2">
            We welcome:
            <ul style="margin:8px 0 0 16px;color:var(--muted)">
              <li>Corrections to gotra or surname data</li>
              <li>Missing festivals, rituals or cultural information</li>
              <li>Panchang accuracy feedback for your region</li>
              <li>Suggestions for new features or sections</li>
              <li>Photographs, manuscripts or family records to add</li>
              <li>Stories of saints, Bhairava mandirs or Kul Devis</li>
              <li>Any knowledge that should not be lost</li>
            </ul>
          </div>
        </div>

        <div style="background:white;border:1px solid var(--border);border-radius:14px;
             padding:20px 24px;box-shadow:0 2px 10px var(--shadow)">
          <div style="font-family:'Cinzel',serif;font-size:9px;letter-spacing:2px;
               color:var(--walnut-mid);margin-bottom:14px">HOW TO REACH US · कैसे संपर्क करें</div>

          <div style="display:flex;align-items:center;gap:14px;padding:12px 16px;
               background:linear-gradient(135deg,#3A2010,#4E2210);border-radius:10px;
               margin-bottom:14px">
            <div style="font-size:22px">✉</div>
            <div>
              <div style="font-family:'Cinzel',serif;font-size:8.5px;letter-spacing:1.5px;
                   color:rgba(222,184,90,.6);margin-bottom:3px">EMAIL · ईमेल</div>
              <a href="mailto:ancientkashmiri@gmail.com"
                 style="font-family:'Cinzel',serif;font-size:15px;font-weight:500;
                        color:#DEB85A;text-decoration:none;letter-spacing:1px">
                ancientkashmiri@gmail.com
              </a>
            </div>
          </div>

          <div style="font-size:12px;color:var(--muted);line-height:1.8">
            Write to us in English, Hindi or Kashmiri. We read every message.
            <br>
            <span style="font-family:'Noto Serif Devanagari',serif;font-size:12px">
              अंग्रेज़ी, हिंदी या कश्मीरी में लिखें — हम हर संदेश पढ़ते हैं।
            </span>
          </div>
        </div>
        """, unsafe_allow_html=True)

    with fb_r:
        st.markdown(f"""
        <div style="background:white;border:1px solid var(--border);border-radius:14px;
             padding:20px 22px;box-shadow:0 2px 10px var(--shadow);margin-bottom:14px">
          <div style="font-family:'Cinzel',serif;font-size:9px;letter-spacing:2px;
               color:var(--walnut-mid);margin-bottom:14px">ABOUT THIS PROJECT · इस परियोजना के बारे में</div>

          <div class="lin-item">
            <div class="lin-icon">✦</div>
            <div>
              <div class="lin-lbl">PURPOSE · उद्देश्य</div>
              <div class="lin-val" style="font-size:13px">Preserve &amp; revive KP heritage</div>
              <div class="lin-desc">For the young generation</div>
            </div>
          </div>
          <div class="lin-item">
            <div class="lin-icon">✦</div>
            <div>
              <div class="lin-lbl">ENGINE · गणना</div>
              <div class="lin-val" style="font-size:13px">Swiss Ephemeris (pyswisseph)</div>
              <div class="lin-desc">Lahiri ayanamsha · Amāvasyānta</div>
            </div>
          </div>
          <div class="lin-item">
            <div class="lin-icon">✦</div>
            <div>
              <div class="lin-lbl">DATA · डेटा</div>
              <div class="lin-val" style="font-size:13px">Bhannamasis gotra table</div>
              <div class="lin-desc">KP surnames · regional deities</div>
            </div>
          </div>
          <div class="lin-item">
            <div class="lin-icon">✦</div>
            <div>
              <div class="lin-lbl">CONTACT · संपर्क</div>
              <div class="lin-val" style="font-size:13px">ancientkashmiri@gmail.com</div>
              <div class="lin-desc">Open to all contributions</div>
            </div>
          </div>
        </div>

        <div style="background:linear-gradient(135deg,#3A2010,#4E2210);border-radius:12px;
             padding:18px 20px;text-align:center">
          <div style="font-family:'Cinzel',serif;font-size:8.5px;letter-spacing:2px;
               color:rgba(222,184,90,.5);margin-bottom:8px">VIKRAMA SAṂVAT</div>
          <div style="font-family:'Cinzel Decorative',serif;font-size:28px;
               color:rgba(222,184,90,.9);line-height:1">{samvat_now}</div>
          <div style="font-size:10px;color:rgba(253,248,240,.35);margin-top:6px">
            {today.strftime('%A')}, {today.day} {today.strftime('%B %Y')}
          </div>
          <div style="font-family:'Noto Serif Devanagari',serif;font-size:13px;
               color:rgba(222,184,90,.4);margin-top:10px">ॐ नमः शिवाय</div>
        </div>
        """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="site-footer">
  ANCIENT KASHMIRI ; प्राचीन कश्मीर &nbsp;·&nbsp; PRĀCĪNA KASHMĪRA
  &nbsp;·&nbsp; VIKRAMA SAṂVAT {samvat_now} &nbsp;·&nbsp; LAHIRI AYANĀṂŚA · AMĀVASYĀNTA
</div>
""", unsafe_allow_html=True)
  # ॐ नमः शिवाय &nbsp;·&nbsp; प्राचीन कश्मीर &nbsp;·&nbsp; PRĀCĪNA KASHMĪRA
  # &nbsp;·&nbsp; VIKRAMA SAṂVAT {samvat_now} &nbsp;·&nbsp; LAHIRI AYANĀṂŚA · PŪRṆIMĀNTA
